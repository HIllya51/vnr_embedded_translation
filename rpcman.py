# coding: utf8
# rpcman.py
# 2/1/2013 jichi

__all__ = 'RpcServer' 
 
RPC_WAIT_TIME = 3000 # wait time after sending data

from socketsvc import socketpack 
APP_SOCKET_TYPE='local'
APP_SOCKET_NAME='vnr.socket'
ENABLE_TCP_SOCKET = APP_SOCKET_TYPE == 'tcp'
 
def createSocketServer(parent=None, usetcp=ENABLE_TCP_SOCKET): 
    from socketsvc.localsocketsrv import LocalSocketServer
    ret = LocalSocketServer(parent)
    ret.setServerName(APP_SOCKET_NAME)
    dwarn("rpcname",APP_SOCKET_NAME) 
    return ret
# Client
 
# Server

def _unmarshalInteger(s): # str -> int, use hex
  #try: return int(s, 16) #if s.startswith('0x') else int(s)
  try: return int(s)
  except ValueError:
    dwarn("failed to marshal number %s" % s)
    return 0

def _marshalInteger(v): # int -> str, use hex
  return str(v)
  #return hex(i).replace('0x', '').replace('L', '') # remove prefix '+-0x' and trailing 'L'

def _unmarshalBool(s): # str -> bool
  return s == '1'

def _marshalBool(v): # int -> str, use hex
  return '1' if v else '0'

#from ctypes import c_longlong
from functools import partial
import json
from PySide.QtCore import Signal, Qt, QObject 
from sakurakit.skdebug import dwarn, dprint     
  
def manager(): return RpcServer()

class RpcServer(QObject):

  def __init__(self, parent=None):
    super(RpcServer, self).__init__(parent)
    self.__d =_RpcServer(self)
    self.__d.q=self
    dwarn("rpcserver_Created")
  activated = Signal()

  def stop(self):
    self.__d.server.stop()
  def start(self):
    """@return  bool"""
    dwarn("start")
    return self.__d.server.start()
  def isActive(self):
    """@return  bool"""
    return self.__d.server.isActive()

  activated = Signal()

  # Agent

  agentConnected = Signal(long) # pid
  agentDisconnected = Signal(long) # pid
  windowTextsReceived = Signal(dict) # {long hash:unicode text}
  engineReceived = Signal(str) # name
  engineTextReceived = Signal(unicode, str,  int, str) # text, hash, role, needsTranslation

  def isAgentConnected(self): return bool(self.__d.agentSocket)
  def closeAgent(self): self.__d.closeAgentSocket()

  #def enableAgent(self): self.__d.callAgent('enable')
  def disableAgent(self): self.__d.callAgent('disable')

  #def detachAgent(self): self.__d.callAgent('detach')

  def agentProcessId(self): return self.__d.agentPid

  def setAgentSettings(self, data):
    """
    @param  data  {k:v}
    """
    try:
      data = json.dumps(data) #, ensure_ascii=False) # the json parser in vnragent don't enforce ascii
      self.__d.callAgent('settings', data)
    except TypeError, e:
      dwarn("failed to encode json: %s" % e)

  def clearAgentTranslation(self): self.__d.callAgent('clear')

  def sendWindowTranslation(self, data):
    """
    @param  data  {hash:translation}
    """
    try:
      data = json.dumps(data) #, ensure_ascii=False) # the json parser in vnragent don't enforce ascii
      self.__d.callAgent('window.text', data)
    except TypeError, e:
      dwarn("failed to encode json: %s" % e)

  #def sendEngineTranslation(self, text, hash, role):
  #  """
  #  @param  text  unicode
  #  @param  hash  long
  #  @param  role  int
  #  """
  #  if isinstance(hash, (int, long)):
  #    hash = _marshalInteger(hash)
  #  self.__d.callAgent('engine.text',
  #      text, hash, _marshalInteger(role))
 
class _RpcServer(object):
  def __init__(self, q):
    self.server = createSocketServer(parent=q)

    self.server.dataReceived.connect(self._onDataReceived)

    self.server.disconnected.connect(self._onDisconnected)

    self.agentSocket = None # QAbstractSocket
    self.agentPid = 0 # long

  # Send

  def callAgent(self, *args):
    if self.agentSocket:
      data = socketpack.packstrlist(args)
      dwarn("senddata",str(data))
      self.server.sendData(data, self.agentSocket, waitTime=RPC_WAIT_TIME)

  # Receive

  def _onDisconnected(self, socket):
    if socket is self.agentSocket:
      dprint("pass: pid = %s" % self.agentPid)
      self.agentSocket = None
      self.q.agentDisconnected.emit(self.agentPid)
      self.agentPid  = 0

  def _onDataReceived(self, data, socket):
    args = socketpack.unpackstrlist(data)
    dwarn("datareceived",args)
    if not args:
      dwarn("unpack data failed")
      return
    self._onCall(socket, *args)

  def _onCall(self, socket, cmd, *params): # on serverMessageReceived
    """
    @param  socket  QTcpSocket
    @param  cmd  str
    @param  params  [unicode]
    """
    dwarn(cmd)
    if cmd == 'app.activate':
      self.q.activated.emit()
 
    elif cmd == 'agent.ping':
      if params:
        pid = _unmarshalInteger(params[0])
        if pid:
          self._onAgentPing(socket, pid)
    elif cmd == 'agent.window.text':
      if params:
        self._onWindowTexts(params[0])
    elif cmd == 'agent.engine.name':
      if params:
        self.q.engineReceived.emit(params[0])
    elif cmd == 'agent.engine.text':
      if len(params) == 5:
        dwarn("solveenginetext",*params)
        self._onEngineText(*params)
      else:
        dwarn("invalid parameter count:", params)

    else:
      dwarn("unknown command: %s" % cmd)

  def closeAgentSocket(self):
    pid = self.agentPid
    self.agentPid = 0
    if self.agentSocket:
      self.server.closeSocket(self.agentSocket)
      self.agentSocket = None
      self.q.agentDisconnected.emit(pid)

  def _onAgentPing(self, socket, pid):
    """
    @param  socket  QTcpSocket
    @param  pid  long
    """ 
    if self.agentSocket:
      self.server.closeSocket(self.agentSocket)
    self.agentPid = pid
    self.agentSocket = socket
    self.q.agentConnected.emit(pid) # SIGNAL TO BE CHANGED

  def _onWindowTexts(self, data):
    """
    @param  data  json
    """
    try:
      d = json.loads(data)
      if d and type(d) == dict:
        d = {long(k):v for k,v in d.iteritems()}
        self.q.windowTextsReceived.emit(d)
      else:
        dwarn("error: json is not a map: %s" % data)
    except (ValueError, TypeError, AttributeError), e:
      dwarn(e)
      #dwarn("error: malformed json: %s" % data)

  def _onEngineText(self, text, hash, sig, role, trans):
    """
    @param  text  unicode
    @param  hash  qint64
    @param  role  int
    @param  trans  bool   need translation
    """
    try:
      #hash = _unmarshalInteger(hash) # delay convert it to number
      role = _unmarshalInteger(role)
      sig = _unmarshalInteger(sig)
      trans = _unmarshalBool(trans) 
      if trans:
        print(text)

      trans=text+"haha"
      lang='zhs'
      self.q.engineTextReceived.emit(trans, hash,   role,lang)
      #if trans:
      #  print role, len(text)
      #  text = u'简体中文' + text
      #  #text = u'简体中文'
      #  self.callAgent('engine.text',
      #      text, _marshalInteger(hash), _marshalInteger(role))
    except ValueError:
      dwarn("failed to convert text hash or role to integer")
 
 
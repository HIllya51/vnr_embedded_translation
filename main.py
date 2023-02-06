# -*- coding: utf-8 -*- 
import win32file,win32security
import sys
from PySide.QtCore import QCoreApplication  
from rpcman import RpcServer
from gameagent import GameAgent
import threading,json

import win32pipe, win32file,win32con,win32security
PIPE_TEXT_EMBED_agent2host="\\\\.\\Pipe\\PIPE_TEXT_EMBED_agent2host"
PIPE_TEXT_EMBED_host2agent="\\\\.\\Pipe\\PIPE_TEXT_EMBED_host2agent" 
from traceback import print_exc
from PySide.QtCore import Signal, Qt, QObject
class qapp(QCoreApplication):
    end = Signal()
    pipe_agent2host=Signal(str)
    engineTextReceived_tohost=Signal(unicode, str,  int )
    def __init__(self,arg) :
        super(qapp,self).__init__(arg) 
        t1=threading.Thread(target=self._creater1) 
        t2=threading.Thread(target=self._creater2) 
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        threading.Thread(target=self._listener).start() 

        print("namepipe_ok")
        self.end.connect(self.quit)
        self.engineTextReceived_tohost.connect(self.transfer_to_host) 
    def send(self,s):
        try: 
            print("send",s)
            win32file.WriteFile(self.pipe_send,s.encode('utf8'))
        except:
            print_exc()
    def _creater1(self):
                win32pipe.WaitNamedPipe(PIPE_TEXT_EMBED_host2agent,win32con.NMPWAIT_WAIT_FOREVER) 
                self.pipe_get = win32file.CreateFile( PIPE_TEXT_EMBED_host2agent, win32con.GENERIC_READ | win32con.GENERIC_WRITE,0,  None, win32con.OPEN_EXISTING, win32con.FILE_ATTRIBUTE_NORMAL, None); 
    def _creater2(self):
                win32pipe.WaitNamedPipe(PIPE_TEXT_EMBED_agent2host,win32con.NMPWAIT_WAIT_FOREVER) 
                self.pipe_send = win32file.CreateFile( PIPE_TEXT_EMBED_agent2host, win32con.GENERIC_READ | win32con.GENERIC_WRITE,0,  None, win32con.OPEN_EXISTING, win32con.FILE_ATTRIBUTE_NORMAL, None); 
                  
    def transfer_to_host(self,text, hash, role ):
        lang='zhs' 
         
        self.send(json.dumps({
            "command":"trans",
            "text":text,
            "hash":hash,
            "role":role ,
            'lang':lang
        })) 
    def _listener(self):     
        try:
            while True:
                rd=win32file.ReadFile(self.pipe_get, 65535, None)[1]  
                rd=json.loads(rd)
                print("received",rd)
                self._onreceive_callback(rd) 
                
        except:
            print_exc() 
    def _onreceive_callback(self,rd): 
        if rd['command']=='trans': 
            print(rd)
            self.ga.sendEmbeddedTranslation(rd['text'], rd['hash'],rd['role'] ,rd['lang'])
        elif rd['command']=='end':
            self.ga.quit()
            self.rpc.stop()
            self.end.emit()
if __name__=="__main__":
    app =  qapp(sys.argv) 
    app.rpc=RpcServer(app)
    app.rpc.start()   
    app.ga=GameAgent(app.rpc,app)
    app.ga.attachProcess(pid=int(sys.argv[1])) 
    engine=app.ga.guessEngine(pid=int(sys.argv[1]))
    if engine:
        app.send(json.dumps({'command':"engine","name":engine.name},ensure_ascii=False))
    app.rpc.engineTextReceived.connect(app.engineTextReceived_tohost) 
    app.rpc.clearAgentTranslation() 
    sys.exit(app.exec_())

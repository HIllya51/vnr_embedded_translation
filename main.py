
import time
import sys
from PySide.QtCore import QCoreApplication 
from PySide.QtGui import QMainWindow,QApplication
from rpcman import RpcServer
from gameagent import GameAgent
if __name__=="__main__":
    app =  QApplication(sys.argv) 
    rpc=RpcServer()
    rpc.start()   
    ga=GameAgent(rpc)
    ga.attachProcess(pid=int(sys.argv[1]))
    rpc.engineTextReceived.connect(ga.sendEmbeddedTranslation)
    rpc.clearAgentTranslation()
    x=QMainWindow()
    x.show()
    sys.exit(app.exec_())

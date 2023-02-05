
import time
import sys
from PyQt5.QtCore import QCoreApplication 
from PyQt5.QtWidgets import QMainWindow,QApplication
from rpcman import RpcServer
from gameagent import GameAgent
if __name__=="__main__":
    app =  QApplication(sys.argv) 
    rpc=RpcServer(app)
    rpc.start()   
    ga=GameAgent(rpc)
    ga.attachProcess(pid=9348)
    rpc.engineTextReceived.connect(ga.sendEmbeddedTranslation)
    rpc.clearAgentTranslation()
    x=QMainWindow()
    x.show()
    sys.exit(app.exec_())

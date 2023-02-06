
import time
import sys
from PySide.QtCore import QCoreApplication  
from rpcman import RpcServer
from gameagent import GameAgent
from threading import Thread

from PySide.QtCore import Signal, Qt, QObject
class qapp(QCoreApplication):
    end = Signal()
    def __init__(self,arg) :
        super(qapp,self).__init__(arg)
        self.end.connect(self.quit)
        Thread(target=self.th).start()
    def th(self):
        while True:
            a=raw_input()
            if a=='quit':
                self.end.emit()
                break
if __name__=="__main__":
    app =  qapp(sys.argv) 
    rpc=RpcServer()
    rpc.start()   
    ga=GameAgent(rpc)
    ga.attachProcess(pid=int(sys.argv[1]))
    rpc.engineTextReceived.connect(ga.sendEmbeddedTranslation)  
    rpc.clearAgentTranslation() 
    sys.exit(app.exec_())

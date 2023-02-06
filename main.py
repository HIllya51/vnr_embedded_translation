
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
                self.ga.quit()
                self.rpc.stop()
                self.end.emit()
                break
if __name__=="__main__":
    app =  qapp(sys.argv) 
    app.rpc=RpcServer()
    app.rpc.start()   
    app.ga=GameAgent(app.rpc)
    app.ga.attachProcess(pid=int(sys.argv[1]))
    print(app.ga.guessEngine(pid=int(sys.argv[1])))
    app.rpc.engineTextReceived.connect(app.ga.sendEmbeddedTranslation)  
    app.rpc.disableAgent
    app.rpc.clearAgentTranslation() 
    sys.exit(app.exec_())

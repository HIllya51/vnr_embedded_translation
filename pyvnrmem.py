
from  PyQt5.QtCore import QSharedMemory,QObject
from ctypes import Structure,c_int8,c_int64,c_int8,c_char,c_int32,c_wchar,c_char_p,c_wchar_p,POINTER,cast,byref,create_string_buffer,create_unicode_buffer
LanguageCapacity=4
import struct,ctypes 
class Cell(Structure):
        _fields_=[
            ('status',c_int8),
            ('hash',c_int64),
            ('role',c_int8),
            ('language',c_char*LanguageCapacity),
            ('textSize',c_int32),
            ('text',c_wchar_p)
        ]
class VnrSharedMemory(QObject):
     
    def __init__(self,p=None ) :
        super(VnrSharedMemory,self).__init__() 
        self.cellCount_=0
        self.cellSize_=0  #实际上没有jb用。。。只会用第一个cell
        self.memory=QSharedMemory()
    def textCapacity(self):
        return int(max(0,(self.cellSize_-4)/2))
    
    def cellCount(self):
        return self.cellCount_
    
    def cellSize(self):
        return self.cellSize_
    def constData(self,i): 
        self.memory.constData()+(self.cellSize_*i)
    def cell(self,i):  
        return cast(POINTER(self.memory.data().asarray() ),POINTER(Cell)).contents 
        
    def key(self):
        self.memory.key()
    def setKey(self,v):
        self.memory.setKey(v)
    
    def create(self,size,count,readOnly):
        self.cellSize_=size
        self.cellCount_=count
        ok=self.memory.create(size*count,QSharedMemory.ReadOnly if readOnly else QSharedMemory.ReadWrite)
        return ok
    def attach(self,readOnly):
        return self.memory.attach(QSharedMemory.ReadOnly if readOnly else QSharedMemory.ReadWrite)
    def detach(self):
        return self.memory.detach()
    def isAttached(self):
        return self.memory.isAttached()
    def lock(self):
        return self.memory.lock()
    def unlock(self):
        return self.memory.unlock()
    def errorString(self):
        return self.memory.errorString()
    def hasError(self):
        return self.memory.error()!=QSharedMemory.NoError 
    def setDataHash(self,i,v):
        pass
        #self.cell(i).hash=v 
    def setDataStatus(self,i,v):
        pass
        #self.cell(i).status=v 
    def setDataRole(self,i,v):
        pass
        #self.cell(i).role=v 
    def setDataLanguage(self,i,v):
        pass
        # p=self.cell(i)
        # u8=v.encode('utf8')
        # for i in range(min(len(u8),LanguageCapacity)):
        #     p.language[i]=u8[i] 
    def setDataText(self,i,v):
        print("settingtext",i,v)
        print(self.memory.size())
        print(self.memory.data())
        print()
        mv=memoryview(self.memory.data()).cast('i')
        for i in range(100,0,-1):
            if mv[i]!=0:
                print(i)
                break 
        # w=create_unicode_buffer(v)
        # self.cell(i).language=w

    
        

from  PyQt5.QtCore import QSharedMemory,QObject
from ctypes import Structure,c_int8,c_int64,c_int8,c_char,c_int32,c_wchar,c_char_p,c_wchar_p,POINTER,cast,byref,create_string_buffer,create_unicode_buffer
LanguageCapacity=4
import struct,ctypes 
class Cell(Structure):
        # _fields_=[
        #     ('status',c_int8),  
        #     ('hash',c_int64),   
        #     ('role',c_int8),    
        #     ('language',c_char*LanguageCapacity), 
        #     ('textSize',c_int32),
        #     ('text',c_wchar_p)
        # ]
        _fields_=[
            ('status',c_int8),  #8
            ('hash',c_int64),   #8
            ('role',c_int8),    #1
            ('language',c_char*LanguageCapacity), #8
            ('textSize',c_int32),#4
            ('text',c_wchar_p)#textsize*2(不记末尾0)
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
    def setDataHash(self,i,v:int):
        v=v.to_bytes(8,'little',signed=True)
        mv=memoryview(self.memory.data()).cast('B') 
        for i in range(8):
            mv[i+8]=v[i] 
    def setDataStatus(self,i,v:int):
        self.memory.lock()
        v=v.to_bytes(8,'little')
        mv=memoryview(self.memory.data()).cast('B') 
        for i in range(8):
            mv[i]=v[i] 
        self.memory.unlock()
    def setDataRole(self,i,v):
        v=v.to_bytes(1,'little')
        mv=memoryview(self.memory.data()).cast('B') 
        mv[16]=v[0]
    def setDataLanguage(self,i,v):
        v=v.encode('ascii')
        mv=memoryview(self.memory.data()).cast('B') 
        for i in range(min(8,len(v))):
            mv[i+17]=v[i] 
    def setDataText(self,i,v):
        v=v
        uv=v.encode('utf-16-le')
        self.memory.lock()
        size=len(uv).to_bytes(4,'little')
        mv=memoryview(self.memory.data()).cast('B')
          
        for i in range(min(self.memory.size(),100)):
            print(mv[i],end=',')
        print(mv[25])
        cache=[]
        for i in range(mv[25]):
            cache.append(mv[29+i])
        print(bytes(cache).decode('utf-16-le'))
        # w=create_unicode_buffer(v)
        # self.cell(i).language=w

         
        for i in range(4):
            mv[i+25]=size[i]
        for i,b in enumerate(uv):
            mv[i+29]=b
        mv=memoryview(self.memory.data()).cast('B')
        print(mv[25])
        cache=[]
        for i in range(mv[25]):
            cache.append(mv[29+i])
        print(bytes(cache).decode('utf-16-le'))
        #mv[21]=
        self.memory.unlock()
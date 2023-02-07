
from  PyQt4.QtCore import QSharedMemory,QObject
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
            ('text',c_wchar_p) 
        ]
class VnrSharedMemory(QObject):
     
    def __init__(self,p=None ) :
        super(VnrSharedMemory,self).__init__() 
        self.cellCount_=0
        self.cellSize_=0   
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
        return self.memory.key()
    def setKey(self,v):
        self.memory.setKey(v)
    
    def create(self,size,count,readOnly):
        self.cellSize_=size
        self.cellCount_=count
        ok=self.memory.create(size*count,QSharedMemory.ReadOnly if readOnly else QSharedMemory.ReadWrite)
        return ok
    def attach(self,readOnly):
        return self.memory.attach(QSharedMemory.ReadOnly if readOnly else QSharedMemory.ReadWrite)
    def detach_(self):
        return self.memory.detach()
    def isAttached(self):
        return self.memory.isAttached() 
        
    def setDataHash(self,i,v ): 
        v=self.packuint(v,8) 
        mv=memoryview(self.memory.data()) 
        for i in range(8):
            mv[i+8]=v[i]  
    def packuint(self,i, size=0): # int -> str
        """
        @param  i  int
        @param* size  int  total size after padding
        @return  str
        """
        if i<0:
            i=(2**(8*size))+i
        r = ''
        while i:
            r = r+chr(i & 0xff) 
            i = i >> 8
        while len(r) < size:
            r = r+chr(0) 
        return r
    def setDataStatus(self,i,v ):  
        v=self.packuint(v,8)
        mv=memoryview(self.memory.data()) 
        for i in range(8):
            mv[i]=v[i]   
    def setDataRole(self,i,v):
        v=self.packuint(v,1)
        mv=memoryview(self.memory.data()) 
        mv[16]=v[0]
        print("role",v[0]) 
        cache=[]
        for i in range(100):
            cache.append(ord(mv[i]))
        print((cache) )
    def setDataLanguage(self,i,v):
        v=v.encode('ascii')
        mv=memoryview(self.memory.data()) 
        for i in range(min(8,len(v))):
            mv[i+17]=v[i] 
        print("lang")
        cache=[]
        for i in range(100):
            cache.append(ord(mv[i]))
        print((cache) )
    def setDataText(self,i,v): 
        l=len(v)
        uv=v.encode('utf-16-le') 
        v=self.packuint(l,4)
        mv=memoryview(self.memory.data()) 
        for i in range(4):
            mv[i+24]=v[i] 

        for i in range(len(uv)):
            mv[i+28]=uv[i]
            
        cache=[]
        for i in range(100):
            cache.append(ord(mv[i]))
        print((cache) )
        # cache=[]    
        # print(ord(mv[24]))
        # for i in range(ord(mv[24])):
        #     cache.append(ord(mv[i]))

        
        #print((cache) )
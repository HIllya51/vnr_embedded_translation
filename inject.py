# coding: utf8
# inject.py
# 2/3/2013 jichi
# Windows only
import os
def inject_vnragent(pid): 
  ret = True
  for dllpath in ['dlls/msvcr100.dll',
                  'dlls/msvcp100.dll',
                  'dlls/QtCore4.dll',
                  'dlls/QtNetwork4.dll',
                  'dlls/vnragent.dll']:
    
    #dllpath = os.path.abspath(dllpath)
    dllpath = os.path.abspath(dllpath)   
    os.system('dllinject32.exe '+str(pid)+' "'+dllpath+'"') 
  return ret

# coding: utf8
# inject.py
# 2/3/2013 jichi
# Windows only

from sakurakit import skos, skpaths, skwin, skwinsec
if skos.WIN:
  import os 
  from sakurakit.skdebug import dprint,dwarn

  def inject_vnragent(**kwargs):
    """
    @param* pid  ulong
    @param* handle  HANDLE
    @return  bool
    """
    dprint("enter")
    ret = True
    for dllpath in ['dlls/msvcr100.dll',
                    'dlls/msvcp100.dll',
                    'dlls/QtCore4.dll',
                    'dlls/QtNetwork4.dll',
                    'dlls/vnragent.dll']:
      
      #dllpath = os.path.abspath(dllpath)
      dllpath = skpaths.abspath(dllpath)
      dwarn("inject dll",dllpath)
      assert os.path.exists(dllpath), "needed dll does not exist: %s" % dllpath
      ret = skwinsec.injectdll(dllpath, **kwargs) and ret
    dprint("leave: ret = %s" % ret)
    return ret
 
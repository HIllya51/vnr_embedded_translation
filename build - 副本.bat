C:\Python27_32\python.exe -m nuitka --standalone    --output-dir=.\build main.py  
copy vnragent.dll build\main.dist\
copy dllinject32.exe build\main.dist\
copy engines.json build\main.dist\
pause
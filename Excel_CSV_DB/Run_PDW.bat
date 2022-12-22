@echo off
REM C:\Users\luizc\AppData\Local\Programs\Python\Python310\python.exe C:\Users\luizc\PycharmProjects\guppe\Excel_CSV_DB\XL_importer.v6.py 
C:\Users\luizc\AppData\Local\Programs\Python\Python310\python.exe C:\Users\luizc\PycharmProjects\guppe\Excel_CSV_DB\XL_importer.v6.1.py
echo ' '
echo ' '
echo ' '
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo Current time is %mydate%  %mytime%
echo ' '
echo ' '

pause

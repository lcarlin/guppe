@echo off
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo The Start TIME is: %mydate%  %mytime%

cd "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\"
C:\Users\luizc\AppData\Local\Programs\Python\Python311\python.exe C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\PersonalDataWareHouse.py
echo ' '
echo ' '
echo ' '
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo The end Time is  %mydate%  %mytime%
echo ' '
echo ' '

pause

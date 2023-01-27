@Echo off
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo The Start TIME is: %mydate%  %mytime%
echo ' '
G:
cd "G:\Meu Drive\PDW"
sqlite3mysql -f "G:\Meu Drive\PDW\PDW.db" -d PDW -u xcprd01 --mysql-password senha -h localhost -P 3306 -E -l SQLite3ToMySQL.log

echo ' '
echo ' '
echo ' '
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo The end Time is  %mydate%  %mytime%
echo ' '
echo ' '

pause
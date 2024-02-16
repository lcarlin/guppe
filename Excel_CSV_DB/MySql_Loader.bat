REM mysql8-18c25bdd9ba-3d788bcba08f0ebb	root	Senha@123
@Echo off
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo The Start TIME is: %mydate%  %mytime%
echo ' '

cd "C:\Users\luizc\OneDrive\Documentos\PDW"
sqlite3mysql -f "C:\Users\luizc\OneDrive\Documentos\PDW\PDW.db" -d PDW -u pdw --mysql-password senha -h localhost -P 3306 -E -l SQLite3ToMySQL.log

echo ' '
echo ' '
echo ' '
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo The end Time is  %mydate%  %mytime%
echo ' '
echo ' '

pause
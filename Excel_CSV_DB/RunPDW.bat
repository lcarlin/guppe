@echo off
setlocal enabledelayedexpansion

rem Caminho dos diretórios e arquivos
set "dirPDW=C:\Users\luizc\OneDrive\Documentos\PDW"
set "dirScript=C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB"
set "dirDestDropBox=C:\Users\luizc\Dropbox\PDW_DRPBX"
set "dbFile=PDW.db"
set "xlsxFile=PDW.xlsx"
set "pythonExe=C:\Users\luizc\AppData\Local\Programs\Python\Python312\python.exe"
set "pythonScript=PersonalDataWareHouse.py"
rem set "pythonScript=PersonalDataWareHouse.970.py"
set "outLiner=#######################################################################################################################"

rem Caminho completo dos arquivos
set "pdwDB=%dirPDW%\%dbFile%"
set "pdwExcel=%dirPDW%\%xlsxFile%"
set "caminhoOrigem=%pdwExcel%"
set "caminhoDestino=%dirDestDropBox%\%xlsxFile%"

if not exist "%pdwExcel%" ( 
    echo %pdwExcel% ou %pdwDB% Nao localizado
    goto end
)

if not exist "%pdwDB%" ( 
    echo %pdwExcel% ou %pdwDB% Nao localizado
    goto end
)

for %%F in ("%pdwDB%") do set "dataCriacaopdwDB=%%~tF"
for %%F in ("%pdwExcel%") do set "dataCriacaopdwExcel=%%~tF"

echo %outLiner%
echo Banco-de-dados     : %pdwDB%
echo Ultima Atualizacao : %dataCriacaopdwDB%
echo %outLiner%
echo Planilha           : %pdwExcel%
echo Ultima Atualizacao : %dataCriacaopdwExcel%
echo %outLiner%

rem Comparar as datas de modificação (não é exato como no PowerShell, mas aproxima)
if "%dataCriacaopdwExcel%" GTR "%dataCriacaopdwDB%" (
    cd /d "%dirScript%"
    "%pythonExe%" "%pythonScript%"
    if %errorlevel% equ 0 (
        copy /Y "%caminhoOrigem%" "%caminhoDestino%"
        echo Arquivo copiado de %caminhoOrigem% para %caminhoDestino%
    ) else (
        echo A execução do programa falhou. A cópia não foi efetuada.
    )
) else (
    echo A planilha nao foi alterada depois da ultima execucao, logo ...
    echo Nao ha a necessidade de executar o Personal Dataware House nesse momento. Verifique mais tarde.
)

:end
echo.
echo Pressione qualquer tecla para sair...
pause >nul

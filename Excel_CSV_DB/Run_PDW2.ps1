# Caminho para o executável do Python
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\RunPDW.ps1
# powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\F169352\python\guppe\Excel_CSV_DB\RunPDW.ps1
# Caminho dos arquivos A e B

$dirPDW = "C:\Users\luizc\OneDrive\Documentos\PDW\"
$dirScript = "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\"
$pdwDB = $dirPDW + "PDW.db"
$pdwExcel = $dirPDW + "PDW.xlsx"
if ( -not (Test-Path $pdwExcel )) {
    Write-Host $pdwExcel " Não localizado"
}
$dataCriacaopdwDB = (Get-Item $pdwDB).LastWriteTime
$dataCriacaopdwExcel = (Get-Item $pdwExcel).LastWriteTime
Write-Host "========================================================="
Write-Host "Banco-de-dados :-> "
Write-Host $pdwDB
Write-Host $dataCriacaopdwDB 
Write-Host "========================================================="
Write-Host "Planilha"
Write-Host $pdwExcel
Write-Host $dataCriacaopdwExcel
Write-Host "========================================================="
# Comparar as datas de criação
if ($dataCriacaopdwExcel -gt $dataCriacaopdwDB) {
    $pythonExe = "C:\Users\luizc\AppData\Local\Programs\Python\Python311\python.exe"
    # Caminho para o script Python que você deseja executar
    $pythonScript = "PersonalDataWareHouse.py" 
    cd $dirScript
    # Executa o script Python em segundo plano
    Start-Process -FilePath $pythonExe -ArgumentList $pythonScript -NoNewWindow -Wait
} else {
    Write-Host "Não há a necessidade de se exeucutar o Personal Dataware House"
}
# Aguarda até que uma tecla seja pressionada antes de encerrar o script
Write-Host "Pressione qualquer tecla para sair..."
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null
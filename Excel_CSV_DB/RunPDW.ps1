# Caminho para o executável do Python
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\F169352\python\guppe\Excel_CSV_DB\RunPDW.ps1
# powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\F169352\python\guppe\Excel_CSV_DB\RunPDW.ps1
# Caminho dos arquivos A e B

# Atenção: adequar as 03 variaveis abaixo com base em Vosso Ambiente de Execução, talkey ?
$dirPDW = "C:\Users\luizc\OneDrive\Documentos\PDW\"
$dirScript = "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB"

# Caminho para o executável do Python que você deseja executar
$pythonExe = "C:\Users\luizc\AppData\Local\Programs\Python\Python312\python.exe"

$outLiner = ">===================================================================================================================<"

# O nome do .db e do .xlsx tem que ser o mesmo que vem do arquivo "PersonalDataWareHouse.cfg" (ou similar)
$pdwDB = $dirPDW + "PDW.db"
$pdwExcel = $dirPDW + "PDW.xlsx"
$pythonScript = "PersonalDataWareHouse.py" 

if ( ( -not (Test-Path $pdwExcel )) -or ( -not (Test-Path $pdwDB) )) {
    Write-Host $pdwExcel " ou " $pdwDB "Nao localizado"
} else {
    $dataCriacaopdwDB = (Get-Item $pdwDB).LastWriteTime
    $dataCriacaopdwExcel = (Get-Item $pdwExcel).LastWriteTime
    Write-Host $outLiner
    Write-Host "Banco-de-dados    :-> " $pdwDB
    Write-Host "Ultima Atulizacao :-> " $dataCriacaopdwDB 
    Write-Host $outLiner
    Write-Host "Planilha          :-> " $pdwExcel
    Write-Host "Ultima Atulizacao :-> " $dataCriacaopdwExcel
    Write-Host $outLiner
    # Comparar as datas de criação
    if ($dataCriacaopdwExcel -gt $dataCriacaopdwDB) {
        Set-Location $dirScript
        # Executa o script Python em segundo plano
        Start-Process -FilePath $pythonExe -ArgumentList $pythonScript -NoNewWindow -Wait
    } else {
        Write-Host "A planilha nao foi alterada depois da ultima execucao, logo ... "
        Write-Host "Nao ha a necessidade de se exeucutar o Personal Dataware House nesse momento. Verifique mais tarde"
    }
}
# Aguarda até que uma tecla seja pressionada antes de encerrar o script
Write-Host "Pressione qualquer tecla para sair..."
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null
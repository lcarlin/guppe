# Caminho para o executável do Python
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\F169352\python\guppe\Excel_CSV_DB\RunPDW.ps1
# C:\Program Files\PowerShell\7\pwsh.exe -noexit -ExecutionPolicy Bypass -File C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\RunPDW.ps1
# powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\F169352\python\guppe\Excel_CSV_DB\RunPDW.ps1
# Caminho dos arquivos A e B

# Atenção: adequar as 03 variaveis abaixo com base em Vosso Ambiente de Execução, talkey ?
$dirPDW = "X:\Documentos\PDW"
$localUser = $env:HOMEDRIVE + "\" +  $env:HOMEPATH
$dirScript = $localUser + "\PyCharm\guppe\Excel_CSV_DB"
$dirDestDropBox = $localUser + "\Dropbox\PDW_DRPBX"
$dbFile =  "PDW.db"
$xlsxFile = "PDW.xlsx"

# Caminho para o executável do Python que você deseja executar
$pythonExe = $env:LOCALAPPDATA + "\" + "Programs\Python\Python312\python.exe"

$outLiner = ">========================================================================================================================<"

# O nome do .db e do .xlsx tem que ser o mesmo que vem do arquivo "PersonalDataWareHouse.cfg" (ou similar)
$pdwDB = Join-Path -Path $dirPDW -ChildPath $dbFile
$pdwExcel = Join-Path -Path $dirPDW -ChildPath $xlsxFile
$pythonScript = "PersonalDataWareHouse.py" 

# Caminho completo do arquivo de origem e destino
$caminhoOrigem = $pdwExcel
$caminhoDestino = Join-Path -Path $dirDestDropBox -ChildPath $xlsxFile

if ( ( -not (Test-Path $pdwExcel )) -or ( -not (Test-Path $pdwDB) )) {
    Write-Host $pdwExcel " ou " $pdwDB "Nao localizado"
} else {
    $dataCriacaopdwDB = (Get-Item $pdwDB).LastWriteTime
    $dataCriacaopdwExcel = (Get-Item $pdwExcel).LastWriteTime
    Write-Host $outLiner
    Write-Host "Python Interpreter :-> " $pythonExe
    Write-Host "Banco-de-dados     :-> " $pdwDB
    Write-Host "Ultima Atualizacao :-> " $dataCriacaopdwDB 
    Write-Host $outLiner
    Write-Host "Planilha           :-> " $pdwExcel
    Write-Host "Ultima Atualizacao :-> " $dataCriacaopdwExcel
    Write-Host $outLiner
    # Comparar as datas de criação
    if ($dataCriacaopdwExcel -gt $dataCriacaopdwDB) {
        Set-Location $dirScript
        # Executa o script Python em segundo plano
        Start-Process -FilePath $pythonExe -ArgumentList $pythonScript -NoNewWindow -Wait
        $ReturnCode = $?
        #$ReturnCode = $LASTEXITCODE 
        
        if ($ReturnCode) {
            # Copiar arquivo, sobrescrevendo se já existir, em modo verbose
            Copy-Item -Path $caminhoOrigem -Destination $caminhoDestino -Force # -Verbose
            Write-Host "Arquivo copiado de $caminhoOrigem para $caminhoDestino"
        } else {
            Write-Host "A execução do programa falhou. A cópia não foi efetuada."
        }
    } else {
        Write-Host "A planilha nao foi alterada depois da ultima execucao, logo ... "
        Write-Host "Nao ha a necessidade de se exeucutar o Personal Dataware House nesse momento. Verifique mais tarde"
    }
}
# Aguarda até que uma tecla seja pressionada antes de encerrar o script
Write-Host "Pressione qualquer tecla para sair..."
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null

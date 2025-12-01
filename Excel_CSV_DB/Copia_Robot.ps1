# Definindo caminhos de origem e destino
$origem = "X:\Documentos\PDW"
$OrigemPRG = "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB"
$destino = "C:\Users\luizc\Dropbox\PDW_DRPBX"

# Nome do arquivo
$arquivo = "PDW.xlsx"
$pythonPRG = "PersonalDataWareHouse.py"

# Executando o RoboCopy
robocopy $origem $destino $arquivo /COPY:DAT /R:2 /W:2 # /NFL /NDL /NP /NS /NC
robocopy $OrigemPRG $destino $pythonPRG /COPY:DAT /R:2 /W:2 # /NFL /NDL /NP /NS /NC

# Aguarda até que uma tecla seja pressionada antes de encerrar o script
Write-Host "Pressione qualquer tecla para sair..."
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null


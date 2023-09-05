# Caminho para o executável do Python
# C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\RunPDW.ps1
# powershell.exe -noexit -ExecutionPolicy Bypass -File C:\Users\F169352\python\guppe\Excel_CSV_DB\RunPDW.ps1
$pythonExe = "C:\Users\luizc\AppData\Local\Programs\Python\Python311\\python.exe"

# Caminho para o script Python que você deseja executar
$pythonScript = "PersonalDataWareHouse.py" 

cd "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\"

# Executa o script Python em segundo plano
Start-Process -FilePath $pythonExe -ArgumentList $pythonScript -NoNewWindow -Wait

# Aguarda até que uma tecla seja pressionada antes de encerrar o script
Write-Host "Pressione qualquer tecla para sair..."
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null

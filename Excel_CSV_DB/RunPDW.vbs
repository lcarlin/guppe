' Caminho para os arquivos e diretórios
Dim dirPDW, dirScript, lineOut, pdwDB, pdwExcel, dataCriacaopdwDB, dataCriacaopdwExcel, pythonExe, pythonScript, mensagem

dirPDW = "C:\Users\luizc\OneDrive\Documentos\PDW\"
dirScript = "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\"
lineOut = ">===================================================================================================================<"
pdwDB = dirPDW & "PDW.db"
pdwExcel = dirPDW & "PDW.xlsx"
mensagem = ""

' Verifica se o arquivo Excel existe
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

If Not fso.FileExists(pdwExcel) Then
    mensagem = mensagem & pdwExcel & " Não localizado" & vbCrLf
End If

' Obtém as datas de criação dos arquivos
If fso.FileExists(pdwDB) Then
    dataCriacaopdwDB = fso.GetFile(pdwDB).DateLastModified
Else
    dataCriacaopdwDB = "Arquivo não encontrado"
End If

If fso.FileExists(pdwExcel) Then
    dataCriacaopdwExcel = fso.GetFile(pdwExcel).DateLastModified
Else
    dataCriacaopdwExcel = "Arquivo não encontrado"
End If

' Exibe informações dos arquivos
mensagem = mensagem & lineOut & vbCrLf
mensagem = mensagem & "Banco-de-dados :-> " & vbCrLf
mensagem = mensagem & pdwDB & vbCrLf
mensagem = mensagem & dataCriacaopdwDB & vbCrLf
mensagem = mensagem & lineOut & vbCrLf
mensagem = mensagem & "Planilha" & vbCrLf
mensagem = mensagem & pdwExcel & vbCrLf
mensagem = mensagem & dataCriacaopdwExcel & vbCrLf
mensagem = mensagem & lineOut & vbCrLf

' Compara as datas de criação e executa o script Python se necessário
If IsDate(dataCriacaopdwExcel) And IsDate(dataCriacaopdwDB) Then
    If dataCriacaopdwExcel > dataCriacaopdwDB Then
        pythonExe = "C:\Users\luizc\AppData\Local\Programs\Python\Python312\python.exe"
        pythonScript = "C:\Users\luizc\PyCharm\guppe\Excel_CSV_DB\PersonalDataWareHouse.py"

        Dim objShell
        Set objShell = CreateObject("WScript.Shell")
        objShell.CurrentDirectory = dirScript

        ' Executa o script Python em segundo plano e captura a saída
        Dim objExec, strOutput, strError
        Set objExec = objShell.Exec("""" & pythonExe & """ """ & pythonScript & """")

        Do While objExec.Status = 0
            WScript.Sleep 100
        Loop

        strOutput = objExec.StdOut.ReadAll()
        strError = objExec.StdErr.ReadAll()

        mensagem = mensagem & strOutput & vbCrLf
        mensagem = mensagem & strError & vbCrLf

        Set objShell = Nothing
        Set objExec = Nothing

    Else
        mensagem = mensagem & "Não há a necessidade de se exeucutar o Personal Dataware House" & vbCrLf
    End If
Else
    mensagem = mensagem & "Não foi possível comparar as datas dos arquivos." & vbCrLf
End If

' Exibe a mensagem final e aguarda a entrada do usuário
mensagem = mensagem & "Pressione qualquer tecla para sair..." & vbCrLf
WScript.Echo mensagem
WScript.StdIn.Read(1)

Set fso = Nothing
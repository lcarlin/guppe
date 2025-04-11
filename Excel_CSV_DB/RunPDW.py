import os
import shutil
import subprocess
from datetime import datetime

# Configurações de ambiente - ajustar conforme necessário
dir_pdw = r"X:\Documentos\PDW"
local_user = os.path.join(os.environ['HOMEDRIVE'], os.environ['HOMEPATH'])
dir_script = os.path.join(local_user, "PyCharm", "guppe", "Excel_CSV_DB")
dir_dest_dropbox = os.path.join(local_user, "Dropbox", "PDW_DRPBX")
db_file = "PDW.db"
xlsx_file = "PDW.xlsx"

# Caminho para o executável do Python
python_exe = os.path.join(os.environ['LOCALAPPDATA'], "Programs", "Python", "Python312", "python.exe")

outliner = ">========================================================================================================================<"

# Caminhos completos dos arquivos
pdw_db = os.path.join(dir_pdw, db_file)
pdw_excel = os.path.join(dir_pdw, xlsx_file)
python_script = "PersonalDataWareHouse.py"

caminho_origem = pdw_excel
caminho_destino = os.path.join(dir_dest_dropbox, xlsx_file)

# Verificação de existência dos arquivos
if not os.path.exists(pdw_excel) or not os.path.exists(pdw_db):
    print(f"{pdw_excel} ou {pdw_db} não localizado")
else:
    data_criacao_db = datetime.fromtimestamp(os.path.getmtime(pdw_db))
    data_criacao_excel = datetime.fromtimestamp(os.path.getmtime(pdw_excel))

    print(outliner)
    print(f"Banco-de-dados     :-> {pdw_db}")
    print(f"Última Atualização :-> {data_criacao_db}")
    print(outliner)
    print(f"Planilha           :-> {pdw_excel}")
    print(f"Última Atualização :-> {data_criacao_excel}")
    print(outliner)

    # Comparar datas
    if data_criacao_excel > data_criacao_db:
        try:
            # Muda para diretório do script
            os.chdir(dir_script)

            # Executa script Python e espera finalizar
            resultado = subprocess.run([python_exe, python_script], check=True)

            # Se execução deu certo, copia arquivo
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Arquivo copiado de {caminho_origem} para {caminho_destino}")

        except subprocess.CalledProcessError:
            print("A execução do programa falhou. A cópia não foi efetuada.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    else:
        print("A planilha não foi alterada depois da última execução, logo ...")
        print("Não há a necessidade de executar o Personal Dataware House nesse momento. Verifique mais tarde.")

# Aguarda tecla para sair (simulando o comportamento do PowerShell)
input("Pressione ENTER para sair...")

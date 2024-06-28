"""
####################################################################################
# Author  : Carlin, Luiz A. .'.
# e-mail  : luiz.carlin@claro.com.br
# Date    : 29-mai-2024
# purpose : Lê um arquivo texto e gera chamadas a API do Totem para gravar os PNgs
#            dos Boletos 
####################################################################################
# Current Version : 1.0.0
####################################################################################
# Version control
# Date       # Version #    What                            #   Who
#            #         #                                    # 
####################################################################################
"""
import requests
import datetime
import sys
def main(nomeArq):
    time_stamp = datetime.datetime.now().strftime("%Y%m%d.%H%M%S")
    dir_out = "C:\\TEMP\\TOTEN\\"
    try:
        with open(nomeArq,'r+') as entrada:
             for linha in entrada:
                registro =  linha.replace('"', '').split(";")
                BAN = registro[0]
                INVOICE = registro[1]
                VENCIMENTO = registro[2]
                VALOR = registro[3]
                print("==================================================================")
                print(f"BAN        : {BAN}")
                print(f"INVOICE    : {INVOICE}")
                print(f"VENCIMENTO : {VENCIMENTO}")
                print(f"VALOR      : {VALOR}")

                url = f"http://totem/Totem/GeraBoletoCOL?cd_conta={BAN}&invoices={INVOICE}&txtDtVencimento={VENCIMENTO}&txtValor={VALOR}&canal=44&idFinalidade=FAT"

                response = requests.get(url)
                status_code = response.status_code 

                if status_code == 200:
                    arq_saida = dir_out + f"Boleto_Toten_{BAN}.{INVOICE}.{time_stamp}.png"
                    try:
                        with open(arq_saida, "wb") as file:
                            file.write(response.content)
                        print(f"Arquivo de Imagem {arq_saida} salvo om sucesso.")
                    except FileExistsError:
                        print(f"Arquivo {arq_saida} Ja existe")
                    except FileNotFoundError:
                        print(f"Erro: O arquivo {arq_saida} ou diretório não foi encontrado.")
                    except PermissionError:
                        print("Erro: Permissão negada para gravar no arquivo.")
                    except IsADirectoryError:
                        print("Erro: O caminho especificado é um diretório, não um arquivo.")
                    except IOError as e:
                        print(f"Erro de E/S: {e}")
                else:
                    print(f"Falha ao acessar a URL. Código de status: {status_code}")
    except FileNotFoundError:
        print(nomeArq)
        print('Arquivo não Localizado')

if __name__ == '__main__':
    input_param_file = ""
    if len(sys.argv) == 2:
        input_param_file = sys.argv[1]
    else :
        print("ERROR - FATAL - FAIL - WARNING ")
        print("Faltou o nome do arquivo de entrada")
        exit(1)
    main(input_param_file)

# EOP
####################################################################################
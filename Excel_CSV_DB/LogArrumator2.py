import re
import sys

def converter_data(data):
    # Converter data do formato DD/MM/YYYY para YYYY/MM/DD
    dia, mes, ano = data.split('/')
    return f"{ano}/{mes}/{dia}"

def converter_linha(linha):
    # Encontrar todas as datas na linha
    datas = re.findall(r'\d{2}/\d{2}/\d{4}', linha)
    for data in datas:
        linha = linha.replace(data, converter_data(data))
    return linha

def processar_arquivo_entrada_saida(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
        for linha in entrada:
            linha_convertida = converter_linha(linha)
            saida.write(linha_convertida)

def main(old_log_file):
    # Exemplo de uso
    new_log_file = old_log_file + ".new"
    processar_arquivo_entrada_saida(old_log_file, new_log_file)


if __name__ == '__main__':
    input_param_file = ""
    if len(sys.argv) == 2:
        input_param_file = sys.argv[1]
    else :
        print("ERROR - FATAL - FAIL - WARNING ")
        print("Faltou o nome do arquivo de entrada")
        exit(1)

    main(input_param_file)
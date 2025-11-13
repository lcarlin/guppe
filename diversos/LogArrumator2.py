import re

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

def processar_arquivo_e_ordenar(arquivo_entrada, arquivo_saida):
    linhas_convertidas = []

    with open(arquivo_entrada, 'r') as entrada:
        for linha in entrada:
            linha_convertida = converter_linha(linha)
            linhas_convertidas.append(linha_convertida)
    
    # Ordenar as linhas convertidas em ordem alfabética crescente
    linhas_convertidas.sort()

    with open(arquivo_saida, 'w') as saida:
        for linha in linhas_convertidas:
            saida.write(linha)

# Exemplo de uso
arquivo_entrada = 'PDW.log.old'
arquivo_saida = 'PDW.CONVERTIDO.log'
processar_arquivo_e_ordenar(arquivo_entrada, arquivo_saida)

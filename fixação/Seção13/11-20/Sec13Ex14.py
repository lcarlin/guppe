# -*- coding: cp1252 -*-
from datetime import datetime, date

#arquivoEntrada = input(f'Entre com o nome de O Arquivo de entrada:-> ')
arquivoEntrada = 'DatasENomes.txt'
arquivoSaida = arquivoEntrada + '.out'
dataAtual = date.today()
# já que vamos trabalhar com datas, primeiro a gente acha quantos SEGUNDOS tem num ano
# depois que a gente viver a subtração das DATAS, A GENTE DIVIDE POR essa constante baixo pra pegar os anos
yr_ct = 365 * 24 * 60 * 60

try:
    with open(arquivoEntrada, 'r') as arquivo, open(arquivoSaida, 'w') as saida:
        linhasEntrada = arquivo.readlines()
        for linhaAtual in linhasEntrada:
            registro = linhaAtual.split(';')
            nome = registro[0]
            nascimento = registro[1].strip().replace(' ', '/')
            print(nascimento)
            dataNascimento = datetime.strptime(nascimento, '%d/%m/%Y').date()
            idadeFull = dataAtual - dataNascimento
            idade = divmod( idadeFull.total_seconds(), yr_ct )[0]
            strSaida = nome + ';' + str(idade) + '\n'
            print(strSaida)
            saida.write(strSaida)

except FileNotFoundError:
    print('Arquivo não achado')

"""
Modos de abertura de arquivos
r -> Abre um arquivo para leitura - padrão
w -> abre para escrita - sobrescreve caso exista
a -> open for writing, appending to the end of the file if it exists
    Se o arquivo não exitir, o mesmo será criado. caso escrita, o novo conteudo será dicionado ao existente, no final
    Não é possivel controlar o cursos de posicionamento
x -> open for exclusive creation, failing if the file already exists
b -> binary mode
t -> text mode (default)

+ -> open for updating (reading and writing)
====================================================================================================================
# Se o arquivo já existir dá erro :-> FileExistsError: [Errno 17] File exists: 'university.txt'
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Talkey\n')
        arquivo.write('forte abraço\n')
except FileExistsError:
    print('Ja tem ')

====================================================================================================================
# Exemplo A - screvendo NO FINAL
with open('frutas.txt','a') as arquivo:
    while True:
        fruta = input('Informa uma Fruta ou digite Sair :-> ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

====================================================================================================================

https://docs.python.org/3/library/functions.html#open
"""
# exemplo B , escrevendo no INICio
with open('outro.txt','r+') as arquivo:
    dois = arquivo.read()
    arquivo.seek(0)
    while True:
        fruta = input('Informa uma Fruta ou digite Sair :-> ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
    arquivo.write(dois)

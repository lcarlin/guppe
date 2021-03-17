"""
Dicionários
    *   Em algumas linguagens de programação os dicionários de Python são conhecidos como MAPAS
    *   Dicionários são coleções do tipo Chave/Valor
    *   São representados por chaves " { } "
            print(type ({}))
            <class 'dict'>
    *   OS tipos de dados das chaves/Valores podem ser de qualquer tipos
    *   As chaves/valor são separados por " : "
====================================================================================================================
# Forma 1 de criação de Dict - mais comum
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'PAraguay'}
print(paises)
print(type(paises))
print ("**********************")

# Forma 2 - menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='PAraguay')
print(paises)
print(type(paises))
print ("**********************")
====================================================================================================================
# Acessando elementos
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'PAraguay'}
# Forma 1 - via chave como lista/Tuplas
print(paises['py'])
#print(paises['ru'])
# Se usar uma chave que não existe, dá um KeyError
print ("**********************")

# forma 2 acessando via GET - recomendado -
print(paises.get('br'))
print(paises.get('ru'))
# Quando usar o GET e a chave não existir, o retorno é NONE  e não dá erro.
====================================================================================================================
# Caso o GET não encontre o Objeto com a chave informada, será retornado None e não prococará um KeyError
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'PAraguay'}
pais = paises.get('ru')
if pais:
    print(f'Encontrei o pais {pais} ')
else:
    print('Nao encontrado')

# Pode-se definir um valor padrao para caso não se encontre oObjeto com a chave informada
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'PAraguay'}
pais = paises.get('ru', 'Não Localizado')
print(f'Encontrei o pais {pais} ')

#Verificar se a chave se encontra no dicionário
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'PAraguay'}
print ('br' in paises)
print ('ru' in paises)
print ('Estados Unidos'  in paises) # Isso não é chave, é valor. A busca é feita pela chaves

if 'ru' in paises:
    russia = paises['ru']
====================================================================================================================
#Pode-se utilzar qualquer tipo de dados (int, floar, string, boolean ) inclusive lista, tupla dicionário como chaves
# para o dicionário

# Tuplas são interesantes para ser usadas como chaves, pois são imutáveis
localidades = {
    (35.6895, 39.6917) : 'Escritório de Tokyo',
    (40.7128, 74.0060) : 'Escritório de New Yorque',
    (37.7749, 122.4194) : 'Escritório de Sao paulo'
}

print(localidades)
print(type(localidades))
====================================================================================================================
# Adicionar elemnetos ao dicionário
receita = {
    'jan': 100,
    'fev': 120,
    'mar': 300
}

print (receita)
print(type(receita))
print ("**********************")
#forma 1 de adicionar elementos
receita['abr'] = 350
print (receita)
print ("**********************")
# forma2
novoDado = {'maio':500}
receita.update(novoDado)
print (receita)
print ("**********************")
receita.update({'jun':200})
print (receita)
print ("**********************")

# Atualizando dados do dicionário
receita['maio'] = 200
print (receita)
print ("**********************")
receita.update({'maio':600})
print (receita)
print ("**********************")
# concluões
#   1   A forma de adicionar novos elementos ou atualizar dados em um dicionário a mesma.
#   2   Em dicionários NÃO PODEMOS TER CHAVES REPETIDAS.
====================================================================================================================
# Como remover dados de um dicionários.
# forma 01
receita = {
    'jan': 100,
    'fev': 120,
    'mar': 300,
    'abr': 258,
    'maio': 600
}

receita.pop('mar')
print (receita)
print ("**********************")
ret = receita.pop('maio') # forma mais comum de remover itens de um dicionário
print (ret)
print (receita)
# OBS:
#   aqui precisamos sempre informar a chave, caso não encontre o elemento um KeyError é retornado
#

# forma 2 # nesse caso, o valor não é retornado pra lugar nenhum sendo perdifo.
# se a chave não existir é geradoum Key Erro r
del receita['fev']
print (receita)
print ("**********************")
====================================================================================================================
carrinho = []
produto1 = ['Playstation 4 ', 1, 2300]
produto2 = ['God Of War 4', 1, 150]
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print("**********************")
# teriamos que saber qual é p indicie de cada informação
print(carrinho[0][0])

# forma 2 com TUPLAS
carrinho.clear()
produto1 = ('Playsation4', 1, 2300)
produto2 = ('God Of War 4', 1, 150)

carrinho = (produto1, produto2)
print(carrinho)
print("**********************")
print(carrinho[1][0])

# Forma 3 - poderiamos utilizad dicionários?
carrinho = []
produto1 = {'nome': 'Playstation4', 'qtd': 1, 'valor': 2300}
produto2 = {'nome': 'God Of War 4', 'qtd': 1, 'valor': 150}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print("**********************")
====================================================================================================================
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
print("**********************")
# LImpar o dicionário
d.clear()
print(d)
print("**********************")
# copiando
novo = d.copy()  # Deep copy
novo['d'] =  4
print(d)
print(novo)
print("**********************")
novo = d   # Shallow copy
novo['d'] =  4
print(d)
print(novo)
print("**********************")

====================================================================================================================
# forma não usual de criação de dicionários
outro = {}.fromkeys('a','b') # chave/valor
print(outro)
print(type(outro))
print("**********************")

# O metodo fromKeys recebe 2 parametros um interavel e um valor
# Ele vai gerear para cada valor dointeravel uma chave e irá atribuir a esta chave o valor informado
usuario = {}.fromkeys(['nome','pontos','email','profile'],'desconhecido') # Atribuindo valor padrão para as chaves
print(usuario)
print(type(usuario))
print("**********************")

# Nesse caso, para cada letra DISTINTA será criado uma chave com o valor especificado.
veja = {}.fromkeys('teste', 'valor')
print(veja)
print("**********************")

veja = {}.fromkeys(range(1,11),' novo')
print(veja)
print("**********************")
"""

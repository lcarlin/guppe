"""
Default Dict
Collections -> High-Performance container datatypes

Default Dict -> ao criar um dicionário utilizando-o , nós informamos o valor padrão, podendo utilizar um lambda pra isso
esse valor sera utilizado sempre que não houver uma correspondecia
Caso tente acessar uma chave que não existe,essa chave será criada e o valor default será atribuido
 * Lambdas -> função sem nomes que podem ou não receber valor de entradas e retornar valores
====================================================================================================================
review de dicionários
dicionario = {'curso':'programacao em python essencial'}
print (dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # quando a chave não existe gera um KeyErrors
====================================================================================================================
https://docs.python.org/3/library/collections.html#collections.defaultdict
====================================================================================================================

"""
from collections import defaultdict
dicionario = defaultdict(lambda :0)
print(dicionario)
dicionario['curso'] = 'Programacao em python essnecial '
print(dicionario)
print(dicionario['outro']) # KeyError se fosse um dicionário normal, aqui retorna algo
print(dicionario) # e quando se acessa um elemento que não existye, ele é adicoinado como o default Dict
a = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
b = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
c = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem')
d = ('cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos',
     'novecentos', 'mil')
listaZeros = [] #Lista de 1 á 10
listaDezenas = [] #Lista dos números de 10 á 19
listaDezenasM10 = [] #Lista das dezenas EX: 20, 30
listaCentenas = [] #Lista das centenas EX: 100, 200
listaIntermediaria = [] #Consegue todos os números entre 10 e 10 EX: 21 á 29, 31, 39!
listaTotal = []
for x in a:
    listaZeros.append(len(x))
for x in b:
    listaDezenas.append(len(x))
for x in c:
    listaDezenasM10.append(len(x))
for x in d:
    listaCentenas.append(len(x))
for y in listaDezenasM10[:8]:
    for z in listaZeros:
        t = y + z
        listaIntermediaria.append(t + 1)
ate99 = listaZeros + listaDezenas + listaDezenasM10[:8] + listaIntermediaria
for o in listaCentenas[:9]:
    for i in ate99:
        u = o + i
        listaTotal.append(u + 1)
total = sum(listaTotal) + sum(ate99) + sum(listaCentenas)
print(f'O total de letras dos números de 1 a 1000 escrito por extenso são: {total} Letras')
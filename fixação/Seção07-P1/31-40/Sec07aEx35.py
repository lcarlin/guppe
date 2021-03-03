from collections import deque

numeroUm = -1
numeroDois = -1
vetorFinal = []
while numeroUm < 0 or numeroUm > 10000:
    numeroUm = int(input(f"Entre com o 1º Numero :-> "))

while numeroDois < 0 or numeroDois > 10000:
    numeroDois = int(input(f"Entre com o 2º Numero :-> "))

listNumUm = list(str(numeroUm))
listNumUm.sort()
listNumUm = deque(listNumUm)

listNumDois = list(str(numeroDois))
listNumDois.sort()
listNumDois = deque(listNumDois)

tamanhoUm = len(listNumUm)
tamanhoDois = len(listNumDois)
maior = tamanhoDois

if tamanhoUm >= tamanhoDois:
    maior = tamanhoUm

print("=================================================")
print(f"Numero 1 :-> {numeroUm}")
print(f'Lista Numero Um :-> {listNumUm}')
print("**********************")
print(f"Numero 2 :-> {numeroDois}")
print(f'Lista Numero Dois :-> {listNumDois}')

proximo = 0
soma = 0
# print("=================================================")
for i in range(0,maior):
    vlr1 = vlr2 = 0
    # print (f'I :=> {i} ; Tam1 :-> {tamanhoUm}; Tam2 :-> {tamanhoDois}')
    if i <= tamanhoUm - 1 :
        vlr1 = int(listNumUm.popleft())
    if i <= tamanhoDois - 1 :
        vlr2 = int(listNumDois.popleft())

    soma = vlr1 + vlr2 + proximo

    if soma > 9:
        proximo = 1
        soma -= 10
    else:
        proximo = 0

    # print(f'i = {i}, vlr1 = {vlr1} ,vlr2 =  {vlr2} , proximo =  {proximo},soma =  {soma} ')

    vetorFinal.append(str(soma))

if proximo > 0: vetorFinal.append(str(proximo))
print("=================================================")
print(vetorFinal)
valorFinal = ''.join(vetorFinal)
print(f'E o valor final gerado é :-> {valorFinal}')

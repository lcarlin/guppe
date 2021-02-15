somaGeral = 0
contadorGeral = 0
mediaGeral = 0
maiorNumero = 0
menorNumero = 99999999
somaPar = 0
contaPar = 0
digitado = 0
mediaPares = 0
while True:
    digitado = int(input("Entre com o 1 numero  :-> "))
    if digitado == 0 :
        break

    somaGeral += digitado
    contadorGeral += 1
    if digitado > maiorNumero:
        maiorNumero = digitado
        print(f"Olha só! achei um novo numero Maior : {digitado}")
    if digitado < menorNumero:
        menorNumero = digitado
        print(f"Olha só! achei um novo numero MENOR : {digitado}")
    if (digitado%2 == 0 ):
        print(f"Já esse aqui, é PAR : {digitado}")
        contaPar += 1
        somaPar += digitado

mediaGeral = somaGeral/contadorGeral
mediaPares = somaPar / contaPar

print("=================================================")
print(f"A soma dos numeros digitados é      :-> {somaGeral}")
print(f"A quantidade de numeros digitados é :-> {contadorGeral}")
print(f"A media dos numeros digitados é     :-> {mediaGeral} ")
print(f"O Maior numero digitado é           :-> {maiorNumero} ")
print(f"O Menor numero digitado é           :-> {menorNumero} ")
print(f"A média dos numeros pares é         :-> {mediaPares} ")

print("Final de O programa s")

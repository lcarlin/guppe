notaDigitada = media = somatoria = contador= 0
while True:
    notaDigitada = int (input("Digite uma nota (entre 10 e 20) :-> "))
    if notaDigitada < 10 or notaDigitada > 20 :
        break

    somatoria += notaDigitada
    contador += 1

if contador > 0 :
    media = somatoria / contador
    print(f"média : {media}")
    print(f"Quantidade de notas :{contador}")
## w = [ i for i in x if i%2==1]
vetorFinal = []
numElementos = 100
counter = 0
counterSeq = 0
while counter < numElementos:
    if counterSeq%7 != 0 or str(counterSeq)[-1] == 7 :
        vetorFinal.append(counterSeq)
        counter += 1

    counterSeq += 1
    print("**********************")
    print(counterSeq)
    print(counter)

print("=================================================")
print("100 primeiros nº naturais não multipços de 7 \n ou que acabam em 7")
print (vetorFinal)
print(len(vetorFinal))
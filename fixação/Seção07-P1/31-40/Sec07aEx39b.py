n = int(input('Informe um numero: \n'))
lista = [1, 2, 1]
ext = []
plista = []
contador = 0
for linha in range(1, n + 1):
    for coluna in range(linha + 1):
        soma = lista[contador] + lista[contador + 1]
        ext.append(soma)
        if coluna == linha:
            ext.insert(0, 1)
            ext.insert(len(ext), 1)

            # print na tela do triangulo pascal
            for n in ext:
                plista.append(str(n))
            print(' '.join(plista))
            plista.clear()

            lista.extend(ext)
            ext.clear()
            contador += 2
        else:
            contador += 1
from collections import namedtuple

totalAlunos = 5
listaCodigos = []
listaAlturas = []
matrizAlunos = []

for i in range(totalAlunos):
    listaCodigos.append( int(input(f"Entre com o código do  {i} º Aluno :-> ")))
    listaAlturas.append(float(input(f"Entre com a altura do  {i} º Aluno :-> ")))

    matrizAlunos.append( [listaCodigos[i],listaAlturas[i]] )


print("=================================================")
alturaMinima = min(listaAlturas)
indiceMinimo = listaAlturas.index(alturaMinima)
codigoMinimo = listaCodigos[indiceMinimo]

alturaMaxima = max(listaAlturas)
indiceMaxima = listaAlturas.index(alturaMaxima)
codigoMaxima = listaCodigos[indiceMinimo]


print (matrizAlunos)

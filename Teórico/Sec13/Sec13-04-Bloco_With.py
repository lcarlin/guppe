"""
O Block With
Passos para se trabalhar com o arquivo
1)  Abrir o arquivo
2)  Manipular com o arquivo
3)  Fechar o arquivo

O Bloco With ´é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados Após o block
With. O Proprio With abre e fecha O Aruqivo

====================================================================================================================
"""
# O Bloco with - Forma Pythonica de manipular arquivos.
with open('arquivo.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
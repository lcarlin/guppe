"""
Definindo as funções - presta a atençao nisso
    *   Pequenos trechos de códigos que realizam tarefas especificas;
    *   Pode (ou nao) receber entrada de dados retornar uma saida de dados;
    *   Muito uteis pra executar procedimento similares por repetidas vezes;

OBS 01) Se escrevcer uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função
            seja simplificada

    Já foi-se utilizado varias funções desde o inicio desse curso :
        -   print()
        -   len()
        -   max()
        -   min()
        -   count()
        e muitas outras
====================================================================================================================
# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco' ]
# utilizando função nativa integrada built-in de python
print(cores)
curso = 'Programação em Python: Essencial '
print(curso)

cores.append('roxo')
# curso.append('Mais dados....') ## Attribuite error.
cores.clear()
print(cores)

print(help(print))
# Metodogya DRY - Dont Repeat Yourself
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""

""" 
Em python, a forma geral de definir uma função é :
def nome_da_função (parametros de entrada):
    blocos de codigos 

nome da função - smepre em minuscula, separada por "_" (Snake case) 
PArametros de entrada são opcionais onde tendo + de 1 cada um separado por " , " podendo ser opcionais - ou não 
Bloco de código -> ou corpo da função, é onde o processamento ocorre, podendo ou não ter retrono de função 

OBS 02) Veja que para se definir uma função usa=-se a palavra reservada " def " informado ao Python que estamos a definir
        uma função . também abrimos o Bloco de Código como " : " qu eé utilizado no python pra se definir blocos;     

"""
# definindo a 1ª função
def diz_oi ():
    print ('OI !!!')
"""
OBS : 
    1   veja que dentro de uma função, pode-se usar outras funções
    2   Veja que nossa função só relaiza uma unica tarefa  - dizer " oi " 
    3   Não recebe nenhum parametro de entrada 
    4   Essa função também não retorna NADA 

"""
# Utilizando a função / chamada de execução
diz_oi()
"""
Ateção - nunca se esqueça de utilizar o Paratseis ao executar uma função 
diz_oi - errado 
diz_oi() - certo

diz_oi () - errado 

"""

# exemplo 2
def cantar_parabens():
    print('parabéns proce')
    print('É rola é rola é rola')
    print('morre diabo ')

for n in range(5):
    print(n)
    cantar_parabens()
    print("##########")

# Em python , podemos criar inclusive variaves do tipo de uma função e executar essa funçção atraves da variavl
canta = cantar_parabens # não é comum fazer-se isso, não existe isso em Java nem em C - isso cria confusão
canta()
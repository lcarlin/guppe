"""
Erros mais comuns em Pythons
é muito importante prestar a atenção e aprender a ler as saidas de erros geradas pela execução do nosso código
====================================================================================================================
printf('Geek Unifersity')
NameError: name 'printf' is not defined

Process finished with exit code 1

====================================================================================================================
Syntax Error que ocorre quanto o Python encontra um erro de sintaxe, ou seja vc escreveu algo que o Python não reco
nehce como parte da linguaegm
Exemplos
def funcao:
    print("dois")

None = 1
====================================================================================================================
2 - NameError -> ocorre quando uma variavel E;OU função não foi definida
print(geek)
       ^

====================================================================================================================
3 - Type Error -> ocorre quando uma função/operação/ação é aolicada e um tipo errado
Exemplos
print(len(5))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: object of type 'int' has no len()

print('Geek ' + [])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can only concatenate str (not "list") to str
====================================================================================================================
4 - Index error
Ocorre quando tentamos acessar um elemento em uyma lista ou ouytroi tipo de dado indexado unsando um indice invalido
    print(lista[1])
IndexError: list index out of range

Process finished with exit code 1
====================================================================================================================
5 - Value Error - Ocorre qunando uma função /operação Built-in (integrada) recebe um argumento com tipo correto mas
valor inapropriado
    print(int('xcx'))
ValueError: invalid literal for int() with base 10: 'xcx'

Process finished with exit code 1

    print(dic['geek'])
KeyError: 'geek'

Process finished with exit code 1
====================================================================================================================
6 - Attribute Error -> ocorre quando uma variável não tem um attribuito / função

    dupla.sort()
AttributeError: 'tuple' object has no attribute 'sort'

Process finished with exit code 1

====================================================================================================================
8 Identation Error -
====================================================================================================================
Exceptions e rrors são Sinonimpos
É importante loer e prestar atenção na saida de errors
====================================================================================================================
"""
dupla = ( 11,2,31,4)
dupla.sort()
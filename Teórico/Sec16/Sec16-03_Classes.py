"""
Progamação Orientada à Objetas - POO
- Classes: nada mais são do que modelos dos objetos do mundo real sendo representados computacoinalmentes
Imagine que vc queira criar um sistyema automatizado para controle de lampadas de um ambiente
classes podem contar:
    -   Atributos -> representam as caracteristicas do Objeto.OU seja, pelos atributos conseguimos representar
            computacionalmente os estados de um objeto. No caso da lampada, possivelmente iriamos querer saber se a
            lampada é 110 ou 220, a sua cor, qual a luminosidade, , etc ..
    -   Métodos -> representam os comportamentos dos objetos, ou seja as ações que esse Objeto pode realizar
            no seu Sistema. no caso da Lampada por exempo, um cmportamento comum que muito provavelmte iriamos querer
            representar no nosso sistema é o de LIgar/Desligar a mnesma

Em python para definir uma classe utilizamos a palavra reservada  " class "

OBS.: Utilizamos a palavra " pass " em python quando temos um bloco de código que ainda não está implementado.

OBS.: QUando nomeamos nossas classes em Python utilizamos por convençao o nome com inicial em Maiusculo. Se o nome for
    composto, utiliza as Iniciais de ambas as palavras em Maiusculo, todas Juntas

Dica Geek: em Computação não utilzamos Acentuação , caracteres especiais, espaços ou similares para nomes de classes,
    atributos, metodos, arquivos, diretórios, etc ...

OBS: quando estamos planejando um Software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
    que serão mapeeados para classes de " entidades "
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()
print(type(lamp))

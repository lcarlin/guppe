"""
Documentando Funções com DocStrings
====================================================================================================================
OBS: podemos ter acesso à documentacao de uma função em Python utilizando a propriedade especial ' __doc__ '

Podemos fgazer acsso direto À documentação com a função ' help ()  '
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""
def diz_oi():
    """UMA função simples que retorna a String ' Doi !! """
    return 'OI'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrade de numero de um numero à potencia informada
    :param numero: Numero que desejamos gerar a exponenciação
    :param potencia: potenciaa que queremos gerar a exponenciação - padrãoé 2
    :return: retoirna o exponeical de numero por potencia
    """
    return numero ** potencia

print ("*******************************")
print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)
print ("*******************************")
print (help(exponencial))
print (exponencial.__doc__)
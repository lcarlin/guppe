import primeiro
def funcao2() :
    primeiro.funcao1()

if __name__ == '__main__' :
    print('segundo.Py está em execucao direta')
    print(__name__)
else:
    print('segundo.Py foi importado')
    print(__name__)


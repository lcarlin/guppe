"""
Decoradores
O que são Decorators?
    -   São funções
    -   Envolvem outras funções e aprimoram seus comportamentos
    -   Também são Exemplos de Higher Order function
    -   Possuem uma Sintaxe proria, usandoo " @ " (Syntax Sugar )
====================================================================================================================
# Decorator como função - Sintax não recomendada , sem o Syntax Sugar
def seja_educado (funcao):
    def sendo():
        print('Foi um prazer conhercer você! ')
        funcao()
        print('Tenha um otimo dia !')
    return sendo

def saudacao():
    print('Seja Bem-vindo à G. U. ')

def raiva():
    print('EU TE ODEO !!! !! !')

#Testando 01

# saudacao()

teste = seja_educado(saudacao)
teste()

print('============================================')
raiva_educada = seja_educado(raiva)
raiva_educada()
====================================================================================================================
# Decorators com Syntax Sugar (Açucar Sintático)
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer vconhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é pedreiro')

@seja_educado_mesmo
def dormir():
    print('Quero dormir')

#Testando
apresentando()
print('============================================')
dormir()
====================================================================================================================
|----------------------------------------------|
|              Function Decorator              |
------------------------------------------------

----------------------------------------------------
| |----------------------------------------------| |
| |   Função Decorada (embelezada, aprimorada    | |
| -------------------------------------------------
====================================================================================================================
|---------------------------------------------------------|
| HOme    | serviços     | Produtos   | Administrativos   |
----------------------------------------------------------
http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin
# Nãoé um codigo funcional é um exemplo
def checa_login(request)
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')

def home(request):
    return 'Pode acessara home'

def servicos(request):
    return 'Pode acesar a serviços'

def produtos(request):
        return 'Pode acesso a produtos'

@checa_login
def admin(request):
    return 'Pode acessar AdMin'


====================================================================================================================
"""
# Não confinda Decorator com Decorator function !!! !! !
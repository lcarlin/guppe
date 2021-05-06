"""
Progamação Orientada à Objetas - POO
- Atributos representam as caracteristicas do Objeto, oui seja pelos atributos nós conseguimos representar
    computacionalmente oe estados de um objecto.
Em Python dividimos os atributos em 3 grupos :
    -   Atributos de Instancias
    -   Atributos de classes
    -   Atirbutos Dinâmicos
*   Atributos de Instancia: São atributos declarados dentro do metodo construtor

OBS: metodo construtor é um metodo especial utilizado para a construção do Objeto
Em Java uma classe " lampada " incluindo seus atriubudos ficaria +/- assim:
public class Lampada () {
    private int voltagem ;
    private int String cor;
    private Boolean ligada = false ;

    public Lampada (int voltagem, String cor ) {
        this.voltagem = voltagem;
        this.cor = cor;
    }
    public int getVoltagem(){
        return this.voltagem
}

Em python por c0opnvenção ficoiu -se estabelecido que todos os atribuoidops de uma classe é publivo, pode-se acessado
    em todo o projeto.
Caso queiramos demostrar que determinado atriubudi deve ser tratado como privado, ou seja, que deve ser acessado/utilzado
    somemnte dentro da popria classe onde está declarado, utiliza-se o " __ " no inicio no seu nome.

Isso é conhecido como Name Mangling

====================================================================================================================
====================================================================================================================
# OBS lembre-se que isso é apenas uma convernção. ou seja, a linguagenm Python não vai impedir que façamos acesso
# Aos atributos sinalizadds como privados fora da classe.
#exemplo :
user = Acesso('bolseta@piroca.com', 'piroca')
print(user.email)
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
print(user._Acesso__senha) #temos acesso mas não deveriamos faze-lo dessa maneira

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
user.mostra_email()
user.mostra_senha()

print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
#O que significa atributos de instancia:
# siginifa que ao criarmos uma instancia de uma classe, todas as instancias terão esses atributos

user1 = Acesso('user1@email.com', '123456')
user2 = Acesso('user2#email.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de classes:
p1 = Produto('Playstation 5 ', 'Video-Gueime', 8489.00)
p2 = Produto('xBox One X ', 'Otro Video-Gueime', 4199.00)

#Atributos de classe são atributos que são delcarados diretamente na classe, ou seja, fora do constutor.
#   Geralmente já inicializamos um valor e este valor pe compartilhado entre todas as instancias da classe.
#   Ou Seja, ao invés de cada instancia da classe ter seus proprios valores como ´pe o caso dos atributos
#   de instancia, com os atributos de classe todasas as instancias terão o mesmo valor para este atributo

class Produto_nvo:
    #Atributo de classe
    imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = Produto_nvo.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto_nvo.imposto
        Produto_nvo.contador = self.id


p3 = Produto_nvo('Playstation 5 ', 'Video-Gueime', 8489.00)
p4 = Produto_nvo('xBox One X ', 'Otro Video-Gueime', 4199.00)

print(p3.valor) # acesso possivel, mas incorreto à um atributo de classe
print(p4.valor)
# não precisams cirar uma instancia de classe para fazer acesso a um atributo de classe.
print(Produto_nvo.imposto) #Acesso correto à um atributo de classe

print(p3.id)
print(p4.id)

# OBS: em linguamems ocmo java, os atributos conhecidos como de classe aqui em Python são chamados de atrbiutos estáticos

# Atibutos dinâmicos
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')

# Classes com atributos de instancia Publico
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContCorrente():
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limie = limite
        self.saldo = saldo


class Produto():
    imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id


class Usuario():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.senha = senha
        self.email = email

# classes co0m atributos de instacias privados
class Acesso:
    def __init__(self, email, senha ):
        self.email = email
        self.__senha = senha

    def mostra_senha (self):
        print((self.__senha))

    def mostra_email(self):
        print(self.email)

# Atributos dinamios -> um atributo de instancia que pode ser criado em tempo de execução
# OBS: o atributo dinâmico será exclusivo da instancia que o Criou

p1 = Produto('Playstation 5 ', 'Video-Gueime', 8489.00)
p2 = Produto('xBox One X ', 'Otro Video-Gueime', 4199.00)
p2.peso = '5 KGs' # note que na classe produt não existe o atributo peso

print(f'Produto: {p2.nome} , descricao {p2.descricao} , Valor {p2.valor}, Peso {p2.peso}')

# print(f'Produto: {p1.nome} , descricao {p1.descricao} , Valor {p1.valor}, Peso {p1.peso}')
# deletando atributos
print(p1.__dict__)
print(p2.__dict__)

print(Produto.__dict__)

del p2.peso

print(p2.__dict__)
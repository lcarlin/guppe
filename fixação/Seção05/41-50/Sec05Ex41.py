peso  = float(input("Entre com o PESO da pessoa  :-> "))
altura = float(input("Entre com a altura da pessoa :-> "))

imc = peso / (altura**2)
mensagem = ""
if imc <= 18.5:
    mensagem = "Abaixo de O Peso "
elif 18.6 <= imc <= 24.9 :
    mensagem = "Saudável"
elif 25 <= imc <= 29.9:
    mensagem = "Peso em Excesso"
elif 30 <= imc <= 34.9:
    mensagem = "Obesidade Grau I"
elif 35 <= imc <= 39.9:
    mensagem = "Obesidade Grau II (Severa) "
elif imc >= 40:
    mensagem =  "Obesidade Grau III (Mórbida) "

print(f"E o calculo de IMC para os dados informados é de {imc:.1f} e o sujeito é classificado com '{mensagem}'")
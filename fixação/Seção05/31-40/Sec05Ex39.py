salarioAtual = float(input("Entre com o Salario Atual da Pessoal :-> "))
tempoServico = float(input("Entre com o tempo de serviço da pessoa :-> "))

reajustePorcent = 0
bonusTempo = 0
novoSalario = 0
if salarioAtual <= 500:
    reajustePorcent = 1.25
elif 501 <= salarioAtual <= 1000:
    reajustePorcent = 1.20
elif 1001 <= salarioAtual <= 1500:
    reajustePorcent = 1.15
elif 1501 <= salarioAtual <= 2000:
    reajustePorcent = 1.10
elif salarioAtual >= 2001:
    reajustePorcent = 1

if tempoServico < 1:
   bonusTempo = 0
elif 1 <= tempoServico <= 3:
    bonusTempo = 100
elif 4 <= tempoServico <= 6:
    bonusTempo  = 200
elif 7 <= tempoServico <= 10:
    bonusTempo = 300
elif tempoServico > 10 :
    bonusTempo = 500

novoSalario = (salarioAtual * reajustePorcent )  + bonusTempo

print(f"E o salario reajustado é de :-> {novoSalario:.2f}")
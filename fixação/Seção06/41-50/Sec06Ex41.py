resist1 = resist2 = resistencia = 0
while True:
    resist1 = int(input("Entre com o valor do Resistor 1 :-> "))
    resist2 = int(input("Entre com o valor do Resistor 2 :-> "))
    if resist1==0 or resist2 ==0:
        break

    resistencia =(resist1*resist2) / (resist1 + resist2)
    print(f"E o valor da resistencia é de :-> {resistencia:.2f}")
    print("=================================================")

print("Final de O programa s")

base = altura = area = 0
while base <= 0: base = int(input("Entre com a Base do triangulo  :-> "))
while altura <= 0: altura = int(input("Entre com a altura do triangulo:-> "))
area = (base* altura)/2

print (f"E a área do triangulo é de {area:.4f}")
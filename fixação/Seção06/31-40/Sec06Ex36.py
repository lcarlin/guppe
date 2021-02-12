import math

soma1 = 0
soma2 = 0
counter = 1
threshold = 100
while counter <= threshold:
    soma1 += (counter ** 2)
    soma2 += counter

    counter += 1

soma2 = soma2 ** 2
print("===========================================")
print(f"Intervalo : de 0 até {threshold}")
print(f"A soma dos quadrados :-> {soma1}")
print(f"O QUadrado das Somas :-> {soma2}")
print(f"E diferença é        :-> {soma2 - soma1}")

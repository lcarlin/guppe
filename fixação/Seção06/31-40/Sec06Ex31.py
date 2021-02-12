dem = 0
soma = 0
for n in range(1, 100, 2):
    dem += 1
    div = n / dem
    print (f"{n}/{dem}")
    soma += div



print (f"E a Soma S :-> {soma:.4f}")
from math import sqrt

for a in range(1, 501):
    for b in range(1, 501):
        c = sqrt(a ** 2 + b ** 2)
        if a + b + c == 1000:
            print(a, b, c)

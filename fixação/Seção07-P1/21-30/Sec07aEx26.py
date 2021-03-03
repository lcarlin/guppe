# FAÇA UM PROGRAMA QUE CALCULE O DESVIO PADRÃO DE UM VETOR v CONTENDO n = 10 NÚMEROS,
# ONDE m É A MÉDIA DO VETOR

# RECEBENDO OS VALORES
v = []
n = 8
soma = 0
variancia = 0
for i in range(n):
    v.append(int(input(f'Digite o {i + 1}º valor: ')))
    soma += v[i]

# MÉDIA ARITIMÉTICA
m = soma / n

# VARIÂNCIA AMOSTRAL
for j in v:
    variancia += (j - m) ** 2
s = variancia / (n - 1)

# DESVIO PADRÃO AMOSTRAL (n - 1) // POPULACIONAL SERIA (n)
d = s ** 0.5
print(d)
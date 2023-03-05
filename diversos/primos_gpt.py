# Definir a função para verificar se um número é primo
def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True

# Obter o intervalo de números a serem verificados
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Verificar cada número no intervalo e imprimir os números primos encontrados
print("Números primos no intervalo de", inicio, "a", fim, ":")
for num in range(inicio, fim + 1):
    if eh_primo(num):
        print(num)
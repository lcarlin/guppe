def celsiusToFahreinheit (tempCelcius) :
    return tempCelcius * (9/5) + 32

#valor = int(input("entre com a Temperatura em º celcius :-> "))
#convertido = celsiusToFahreinheit(valor)
#print(f'E a temperatura em Fahrenheit -e :-> {convertido}')

print(f'E a temperatura em Fahrenheit -e :-> {celsiusToFahreinheit(int(input("entre com a Temperatura em º celcius :-> ")))}')


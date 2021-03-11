def decompoePrimo (numeroInteiro ):
    fatorPrimo = []
    i = 2
    while i <= numeroInteiro:
        if numeroInteiro%i == 0 :
            fatorPrimo.append(i)
            numeroInteiro /= i
        else:
            i += 1

    return max(fatorPrimo)


print(decompoePrimo(16))
print(decompoePrimo(330))
print(decompoePrimo(47856))
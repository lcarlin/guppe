vetor = [1, 553, 53, 142, 0, 14, 5, 158, 165, 12, 884]
vetor2 = []
vetor3 = []

for i in range(11):

    if i < 5:
        s = vetor[i]
        vetor2.append(s)
        vetor2.sort()

    elif i >= 5:
        s = vetor[i]
        vetor3.append(s)
        vetor3.sort()
        vetor3.reverse()

vetor = vetor2 + vetor3

print(vetor)
print(vetor2)
print(vetor3)
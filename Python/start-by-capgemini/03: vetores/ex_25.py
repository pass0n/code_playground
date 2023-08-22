numeros = [8, 45, 99, 1, 26, 45, 89, 65, 10, 666]


for i in range(10):
    for j in range(10):
        if numeros[j] > numeros[i]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print(numeros)

numeros = []
numeros_reversos = []

i = 0

for i in range(10):
    num = input("Número: ")
    numeros.append(num)

numeros_reversos = numeros[::-1]

print(numeros, numeros_reversos)

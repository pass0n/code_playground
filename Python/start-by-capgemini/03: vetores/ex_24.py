numeros1 = []
numeros2 = []
numeros3 = []

for i in range(5):
    num = i
    numeros1.append(num)

for i in range(5):
    num = i
    numeros2.append(num)


num1 = input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n")

if num1 == "1":
    for i in range(5):
        num = numeros1[i] + numeros2[i]
        numeros3.append(num)
elif num1 == "2":
    for i in range(5):
        num = numeros1[i] - numeros2[i]
        numeros3.append(num)
else:
    for i in range(5):
        num = numeros1[i] * numeros2[i]
        numeros3.append(num)

print(numeros1, numeros2, numeros3)

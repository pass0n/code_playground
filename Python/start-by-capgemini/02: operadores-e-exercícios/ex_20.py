import random

while True:
    aleartorio_maximo = random.randint(1, 100)
    aleartorio_minimo = random.randint(1, 100)

    if aleartorio_maximo >= aleartorio_minimo:
        print("maximo:", aleartorio_maximo)
        print("minimo:", aleartorio_minimo)
        break

incremento = random.randint(1, 5)
print("incremento:", incremento)

for i in range(aleartorio_minimo, aleartorio_maximo, incremento):
    print(i)

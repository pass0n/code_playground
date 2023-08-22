def ler_dados():
    global lado1, lado2, lado3
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))


def verificar_triangulo():
    if (lado1 > lado2 + lado3) or (lado2 > lado1 + lado3) or (lado3 > lado1 + lado2):
        return False
    else:
        return True


def verificar_tipo_triangulo():
    if (lado1 == lado2) and (lado2 == lado3):
        return "Equilátero"
    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        return "Isósceles"
    else:
        return "Escaleno"


ler_dados()
if verificar_triangulo():
    print(verificar_tipo_triangulo())
else:
    print("Não é triangulo!")

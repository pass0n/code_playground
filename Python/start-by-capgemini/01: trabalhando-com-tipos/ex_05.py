nota1 = int(input("Informa a nota 1: "))
nota2 = int(input("Informa a nota 2: "))
nota3 = int(input("Informa a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Você passou, sua média foi {media}")
else:
    print("Você está de recuperação.")

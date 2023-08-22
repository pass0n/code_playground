nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Você passou com a média {media:.2f}.")
elif media < 5:
    print(f"Você reprovou com a média {media:.2f}.")
else:
    print(f"Você está de recuperação com a média {media:.2f}.")

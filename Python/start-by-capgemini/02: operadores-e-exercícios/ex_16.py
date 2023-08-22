import os

senha = input("Informe a senha: ")
i = 0
os.system("clear")

while True:
    resposta = input("Digite a senha para sair do programa. ")
    i += 1
    os.system("clear")

    if senha == resposta:
        print(f"Resposta correta! Tentativa n: {i}")
        break

    print(f"Resposta errada tentativa n: {i}")

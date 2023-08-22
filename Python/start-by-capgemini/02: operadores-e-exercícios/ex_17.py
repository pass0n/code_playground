import os

total_conta = 0

while True:
    print("1 - Troca de oleo")
    print("2 - Balanceamento")
    print("3 - Sair")

    opcao_menu = int(input("O que dejesa? "))

    os.system("clear")

    if opcao_menu == 1:
        total_conta += 100

    if opcao_menu == 2:
        total_conta += 70

    if opcao_menu == 3:
        print(f"Total conta: R$ {total_conta}")
        break

cinema = [["0"] * 10 for _ in range(10)]
print(cinema)
while True:
    escolha = input("1 - Reservar\n2 - Layout do Cinema\n3 - Sair\n")

    if escolha == "1":
        fila = int(input("Fila: "))
        poltrona = int(input("Poltrona: "))

        if cinema[fila][poltrona] == "0":
            cinema[fila][poltrona] = "X"
        else:
            print("Poltrona já ocupada")

    elif escolha == "2":
        for linha in cinema:
            print(linha)

    elif escolha == "3":
        break
    else:
        print("Opção inválida")

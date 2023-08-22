clientes = [""] * 5
opcao_menu = 0


def mostrar_menu():
    print("1- Cadastrar ")
    print("2- Pesquisar ")
    print("3- Excluir ")
    print("4- Sair ")
    global opcao_menu
    opcao_menu = input("Escolha uma opção: ")


def cadastrar():
    for i, cliente in enumerate(clientes):
        if cliente == "":
            nome = input("Informe o nome do cliente: ")
            clientes[i] = nome
        else:
            break


def pesquisar():
    nome = input("Nome do cliente a pesquisar: ")
    sucesso = None
    for i, cliente in enumerate(clientes):
        if cliente == nome:
            sucesso = 1
            if sucesso == 1:
                print(f"Cliente {nome} encontrado na posição {i}.")
                input()
            else:
                print("Cliente não existente!")
            break


def excluir():
    nome = int(input("Informe o índice a exluir: "))
    if nome >= 5:
        print("Cliente inexistente!")
    else:
        clientes[nome] = ""


while True:
    mostrar_menu()
    match opcao_menu:
        case "1":
            cadastrar()
        case "2":
            pesquisar()
        case "3":
            excluir()
        case "4":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida!")

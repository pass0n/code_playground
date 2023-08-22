class Cliente:
    def __init__(self, nome, rg, idade):
        self.nome = nome
        self.rg = rg
        self.idade = idade


clientes = []

while True:
    print("1- Cadastrar")
    print("2- Pesquisar")
    print("3- Sair")

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        nome = input("Digite seu nome: ")
        rg = input("Digite seu RG: ")
        checagem = any(
            cliente.nome.lower() == nome.lower() and cliente.rg == rg
            for cliente in clientes
        )
        if checagem:
            print("Cliente já cadastrado!")
        else:
            idade = int(input("Digite sua idade: "))
            cliente = Cliente(nome, rg, idade)
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")

    elif opcao_menu == "2":
        rg_pesquisa = input("Digite o RG para pesquisar: ")

        for cliente in clientes:
            if cliente.rg.lower() == rg_pesquisa.lower():
                print(f"Cliente {cliente.nome.capitalize()} encontrado!")
            else:
                print("Cliente não encontrado.")

    elif opcao_menu == "3":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Escolha novamente.")

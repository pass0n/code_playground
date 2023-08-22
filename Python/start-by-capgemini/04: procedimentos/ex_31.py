gabarito = [0] * 10


def mostrar_menu():
    print("1- Cadastrar Gabarito")
    print("2- Cadastrar Prova")
    print("3- Sair")
    global opcao_menu
    opcao_menu = input("Escolha uma opção: ")


def cadastrar_gabarito():
    for i in range(len(gabarito)):
        gabarito[i] = int(input("Informe a resposta da questão: "))


def cadastrar_prova():
    nota = 0
    for i in range(len(gabarito)):
        resposta = int(input("Informe a resposta da questão: "))
        if resposta == gabarito[i]:
            nota += 1
    return nota


def verificar_notas(nota):
    if nota >= 7:
        return "Aprovado."
    else:
        return "Reprovado."


while True:
    mostrar_menu()
    match opcao_menu:
        case "1":
            cadastrar_gabarito()
        case "2":
            nota_obtida = cadastrar_prova()
            resultado = verificar_notas(nota_obtida)
            print(f"Você foi {resultado}.")
            input()
        case "3":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida!")

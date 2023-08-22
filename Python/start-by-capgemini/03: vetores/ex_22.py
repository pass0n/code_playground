vetor = []

encontrado = bool(False)

i = 0

for i in range(5):
    nome = input("Digite o nome: ")
    vetor.append(nome)

pesquisa = input("Digite o nome a ser pesquisado: ")

for i in range(5):
    if pesquisa == vetor[i]:
        encontrado = True

if encontrado:
    print("Cliente encontrado")
else:
    print("Cliente não encontrado")

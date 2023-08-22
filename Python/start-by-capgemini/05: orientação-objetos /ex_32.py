class Cliente:
    def __init__(self, nome, rg, idade):
        self.nome = nome
        self.rg = rg
        self.idade = idade


nome = input("Digite seu nome: ")
rg = input("Digite seu RG: ")
idade = input("Digite sua idade: ")

cliente1 = Cliente(nome, rg, idade)

print("Nome:", cliente1.nome)
print("RG:", cliente1.rg)
print("Idade:", cliente1.idade)

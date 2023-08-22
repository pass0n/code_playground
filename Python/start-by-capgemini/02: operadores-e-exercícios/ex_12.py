altura_marcelo = 1.20
altura_joao = 1.05
crescimento_anual_marcelo = 0.05
crescimento_anual_joao = 0.07
idade = 8

while altura_marcelo >= altura_joao:
    altura_marcelo += crescimento_anual_marcelo
    altura_joao += crescimento_anual_joao
    idade += 1

print("Idade: ", idade)
print("Altura João: ", round(altura_joao, 2))
print("Altura Marcelo: ", round(altura_marcelo, 2))

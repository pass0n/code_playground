mais_novo = 9999
mais_velho = 0
qtd_entrevistados = 0
qtd_menores_idade = 0
soma_idades = 0

while qtd_entrevistados < 5:
    idade_informada = int(input("Favor, informe a sua idade: "))

    if idade_informada > mais_velho:
        mais_velho = idade_informada

    if idade_informada < mais_novo:
        mais_novo = idade_informada

    if idade_informada < 18:
        qtd_menores_idade += 1

    soma_idades = soma_idades + idade_informada
    qtd_entrevistados += 1

print(f"Mais novo: {mais_novo}")
print(f"Mais velho: {mais_velho}")
porcentagem_menor_idade = (qtd_menores_idade / 5) * 100
print(f"Porcentagem menor idade:  {porcentagem_menor_idade}%")
media_idade = soma_idades / 5
print(f"Media de idade {media_idade}")

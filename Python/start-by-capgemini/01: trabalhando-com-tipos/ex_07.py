# acréscimo de 10% = 1.1 || 20% = 1.2 // decréscimo = 0.1

velocidade_leve = 50 * 1.1
velocidade_media = 70
velocidade_grave = 90
velocidade_gravissima = 110

velocidade_veiculo = float(input("Escreva a velocidade que o veiculo passou: "))

if velocidade_veiculo <= velocidade_leve:
    print("Isento de multa!")
elif velocidade_veiculo <= velocidade_media:
    print("3 pontas na carteira.")
elif velocidade_veiculo <= velocidade_grave:
    print("4 pontos na carteira.")
elif velocidade_veiculo <= velocidade_gravissima:
    print("5 pontos na carteira.")
else:
    print("7 pontos na carteira.")

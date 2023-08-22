altura = round(float(input("Informe sua altura: ")), 2)
peso = round(float(input("Informe seu peso: ")), 2)

imc = peso / (altura**2)

if imc < 18.5:
    print("Magreza")
elif imc < 24.9:
    print("Normal")
elif imc < 29.9:
    print("Sobrepeso Grau I")
elif imc < 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grave, Grau III")

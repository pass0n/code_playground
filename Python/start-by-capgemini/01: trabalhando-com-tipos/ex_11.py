voto = input("Digite seu voto: ")

"""
if voto == 20 :
    print("Você votou no Pikachu")
elif voto == 30 :
    print("Você votou no Pica-Pau")
elif voto == 40 :
    print("Você votou no Patolino")
else :
    print("Voto nulo.")
"""

match voto:
    case "20":
        print("Você votou no Pikachu")
    case "30":
        print("Você votou no Pica-Pau")
    case "40":
        print("Você votou no Patolino")
    case _:
        print("Voto nulo.")

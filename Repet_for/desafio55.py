# Arquivo: pesos

""" print("Conferir massa corporal (kg)")
quant = int(input("Quantas pessoas vão participar? "))

algo = 0
algo2 = 9999

for i in range (quant):
    peso = float(input(f"Digite o peso da {i+1}° pessoa (kg): "))
    if peso > algo:
        algo = peso
        pesada = i+1
    elif peso < algo2:
        algo2 = peso
        leve = i+1

print(f"\nDas {quant} pessoas, a {pesada}° é a mais pesada e a {leve}° é a mais leve.") """

print("Conferir massa corporal (kg)")
quant = int(input("Quantas pessoas vão participar? "))

pesada = 0
leve = 0
posmaior = 0
posmenor = 0

for i in range(quant):
    peso = float(input(f"Digite o peso da {i+1}° pessoa (kg): "))
    if i == 0:
        pesada = peso
        leve = peso
        posmaior = i + 1
        posmenor = i + 1
    else:
        if peso > pesada:
            pesada = peso
            posmaior = i + 1
        if peso < leve:
            leve = peso
            posmenor = i + 1

print(f"\nDas {quant} pessoas, a {posmaior}° é a mais pesada com {pesada:.2f} kg e a {posmenor}° é a mais leve com {leve:.2f} kg.")

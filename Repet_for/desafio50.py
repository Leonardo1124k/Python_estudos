# Arquivo: soma dos pares de numeros inteiros

print("Digite seis números inteiros a seguir: ")
soma = 0

for i in range (0,6):
    seis = int(input(""))
    if seis % 2 == 0:
        soma += seis

print(f"SOMA DOS PARES = {soma}")
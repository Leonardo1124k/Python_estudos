# Arquivo: desafio85
""" pares = []
impares = []
geral = []

for i in range(0,7):
    num = int(input(f"Digite o {i+1}° valor: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
geral.append(pares[:])
geral.append(impares[:])
#print(f"TUDO -> {geral}")
print(f"Valores pares -> {geral[0]}")
print(f"Valores ímpares -> {geral[1]}") """

""" geral = [[], []]
num = 0

for i in range(0,7):
    num = int(input(f"Digite o {i+1}° valor: "))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)
        
geral[0].sort()
geral[1].sort()
print(f"\nOs valores pares foram -> {geral[0]}")
print(f"Os valores impares foram -> {geral[1]}") """

lista = [[], []]

for i in range(0,7):
    valor = int(input(f"Digite o {i+1}° valor numerico: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f"Valores pares -> {lista[0]}")
print(f"Valores IMpares -> {lista[1]}")
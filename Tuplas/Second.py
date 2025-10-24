# numeros =  (x for x in range(0,5))
numeros =  (1,2,3,4)

print(tuple(numeros))

for n in numeros:
    print(f"Ganhei o numero {n}")

for cont in range (0, len(numeros)):
    print(f"Eu ganharei o {numeros[cont]} na posição {cont}")
    
for pos, n in enumerate(numeros):
    print(f"Eu vou comer {n} na posição {pos}")
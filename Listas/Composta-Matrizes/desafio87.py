# Arquivo: MATRIZ MELHORADA

print("==" * 20)
print(f"{"Montador de MATRIZES":^40}")
print("==" * 20)

""" matriz = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))

print("--" * 20)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()
 """
""" matriz = [[0 for x in range(0,3)] for x in range(0,3)]
pares = []
somapares = 0
soma3c = 0
maior2l = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
        if matriz[i][j] % 2 == 0:
            pares.append(matriz[i][j])
        soma3c += matriz[i][2]

for i in pares:
    somapares += i

for i in range(0,3):
    for j in range(0,3):
        if matriz[1][j] == 0:
            maior2l = matriz[1][j]
        else:
            if matriz[1][j] > maior2l:
                maior2l = matriz[1][j]

print("--" * 20)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()

print(f"\nOs valores pares digitados foram: {pares}. Somados são igual a {somapares}")
print(f"Os valores somados da terceira coluna é {soma3c}")
print(f"O maior valor da segunda linha é {maior2l}")
 """
mat = [[0 for x in range(0,3)] for x in range(0,3)]
somapar = 0
somater = 0
maiorseg = 0

for i in range(len(mat)):
    for j in range (len(mat[i])):
        mat[i][j] = int(input(f"Digite o elemento [{i}, {j}]: "))
        if mat[i][j] % 2 == 0:
            somapar += mat[i][j]
        if j == 2:
            somater += mat[i][j] 
        if i == 1 and j == 0:
            maiorseg = mat[i][j]
        else:
            if mat[1][j] > maiorseg:
                maiorseg = mat[i][j]            

print("Matriz montada: ")

for i in mat:
    for j in i:
        print(f"|{j:^5}|", end=" ")
    print()

print()
print(f"Soma de todos os valores pares digitados: {somapar}")
print(f"Soma dos valores da 3° coluna: {somater}")
print(f"Maior valor da 2° linha: {maiorseg}")

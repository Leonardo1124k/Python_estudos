print("==" * 20)
print(f"{"Montador de MATRIZES":^40}")
print("==" * 20)

"""
GUANABARA
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))

print("--" * 20)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()
 """
#eu

mat = [[0 for x in range(0,3)] for x in range(0,3)]

for i in range(len(mat)):
    for j in range (len(mat[i])):
        mat[i][j] = int(input(f"Digite o elemento [{i}, {j}]: "))

print("Matriz montada: ")

for i in mat:
    for j in i:
        print(f"|{j:^5}|", end=" ")
    print()
        

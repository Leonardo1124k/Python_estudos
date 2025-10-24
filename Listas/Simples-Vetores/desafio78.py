# Arquivo: desafio78
print("==" * 20)
print(f"{"INICIANTE EM LISTAS":^40}")
print("==" * 20)
lista = list()

for i in range(0,5):
    lista.append(int(input(f"Digite um numero para posição {i}: ")))

print(f"\nLista criada -> {lista}\n")

print(f"O maior valor foi o {max(lista)} na posição: ", end="")
for i in range(0,len(lista)):
    if lista[i] == max(lista):
        print(f"{i} ", end="")

print(f"\nO menor valor foi o {min(lista)} na posição: ", end="")
for i in range(0,len(lista)):
    if lista[i] == min(lista):
        print(f"{i} ", end="")
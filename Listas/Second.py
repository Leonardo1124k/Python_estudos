lista = []
for i in range(0,5):
    lista.append(int(input("Digite um valor: ")))    

for i in lista:
    print(f"{i} ; ", end='')

print()    
for i, v in enumerate(lista):
    print(f"Na posição {i} encontrei o valor {v}!")

print("Cheguei ao final da lista...")
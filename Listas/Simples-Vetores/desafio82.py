# Arquivo: desafio82
quant = int(input("Quantos numeros quer digitar? "))
lista = list()
lista1 = list()
lista2 = list()

for i in range (quant):
    num = int(input(f"Digite o {i+1}° numero: "))
    lista.append(num)
    if num % 2 == 0 and num not in lista2:
        lista2.append(num)
    elif num % 2 != 0 and num not in lista1:
            lista1.append(num)

print(f"A lista digitada é {lista}")
print(f"A lista de ímpares é {lista1}")
print(f"A lista de pares é {lista2}")

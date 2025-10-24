# Arquivo: desafio84
""" print("==" * 20)
print("Cadastro de pessoas")
print("==" * 20)

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso (kg): ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()  
    option = input("Quer continuar (s/n)?")
    if option in 'Nn':
        break

print(f"\nOs dados foram -> {princ}")
print(f"Ao todo, foram cadastradas {len(princ)} pessoas")
print(f"O maior peso foi de {maior}kg. Peso de ",end="")
for p in princ:
    if p[1] == maior:
        print(f"{p[0]} ", end="")
print(f"\nO menor peso foi de {menor}kg. Peso de ", end="")
for p in princ:
    if p[1] == menor:
        print(f"{p[0]} ", end="") """
        
lista = []
pessoas = []
pesadas = []
leves = []
quant = 0
while True:
    lista.append(input("What's your name? "))
    lista.append(float(input("What's your height? ")))
    pessoas.append(lista[:])
    lista.clear()
    option = input("Do you wanna continue (Y/N)? ").upper().strip()[0]
    if option in "Nn":
        break
for i in range (len(pessoas)):
    quant += 1
    for j in range (len(pessoas[i])):
        if i == 0:
            maiorpeso = pessoas[i][1]
            menorpeso = pessoas[i][1]
        else:
            if pessoas[i][1] >= maiorpeso:
                 maiorpeso = pessoas[i][1]
            elif pessoas[i][1] <= menorpeso:
                 menorpeso = pessoas[i][1]
for i in range (len(pessoas)):
    for j in range (len(pessoas[i])):
        if pessoas[i][j] == maiorpeso:
            pesadas.append(pessoas[i][0])
        elif pessoas[i][j] == menorpeso:
            leves.append(pessoas[i][0])
print(f"Foram cadastradas {quant} pessoas")
print(f"As pessoas mais pesadas foram {pesadas} pesando {maiorpeso} kg")
print(f"As pessoas mais leves foram {leves} pesando {menorpeso} kg")
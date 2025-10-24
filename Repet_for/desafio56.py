# Arquivo: grupo de pessoas

print("==" * 5)
print("Levantamento de dados do time")
print("==" * 5)

quant = int(input("Quantas pessoas vão digitar os dados? "))

soma = 0
maisvelho = 0
nomevelho = "0"
menor20 = 0

for i in range(quant):
    name = input(f"Digite o nome da {i+1}° pessoa: ").strip()
    age = int(input("Idade: "))
    sex = input("Sexo (M/F): ").upper().strip()
    if sex[0] == "M":
        if age > maisvelho:
            maisvelho = age
            nomevelho = name
    elif sex[0] == "F":
        if age < 20:
            menor20 += 1
    else:
        print("Sexo inválido!")
        break            
    soma += age

media = soma / quant
print(f"\nA média de idade do grupo é {media:.1f} anos")

if nomevelho != "0":        
    print(f"O homem mais velho é o {nomevelho} com {maisvelho} anos")
elif menor20 != "0":
    print(f"Há {menor20} mulher(es) com idade inferior a 20 anos.")
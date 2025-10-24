# Arquivo: CADASTROS
print("-----" * 10)
print("PROGRAMA DE CADASTROS")
print("-----" * 10)
mais18 = homens = menor20 = 0
while True: 
    name = input("Digite o nome: ")
    age = int(input("Digite aqui a idade: "))
    sex = input("Digite o sexo (M/F): ").upper().strip()[0]

    if age >= 18:
        mais18 +=1
    
    if sex == "M":
        homens +=1
    elif sex == "F" and age < 20:
        menor20 += 1
    elif sex not in "MF":
        print("SEXO INVALIDO.")

    option = input("Quer cadastrar mais pessoas (S/N)? ").upper().strip()[0]

    if option == "N":
        print("-----" * 5)
        print("Finalizando...")
        break
    
print(f"No total são {mais18} pessoas maiores de idade, {homens} homens cadastrados e {menor20} mulheres menores de 20 anos.")
# Arquivo: que leia o sexo de uma pessoa, mas
# só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

""" sex = str(input("Digite seu gênero a seguir (M/F): ")).strip().upper()[0]

while sex not in "MF":
    sex = input("ERRO. Só são aceitos gêneros Masculino ou Feminino.\nDigite seu gênero a seguir (M/F): ").upper().strip()[0]

if sex == "M":
    print("Você é homem!")
else:
    print("Você é uma mulher!")
 """
 
sex = str(input("Informe seu gênero (M/F): ")).strip().upper()[0]

while sex not in 'MmFf': #AQUI É TOTALMENTE OBRIGATORIO USAR '' ASPAS SIMPLES
    sex = str(input("Dados inválidos. Por favor, informe seu genero: ")).strip().upper()[0]
    
print(f"Sexo {sex} registrado com sucesso.")

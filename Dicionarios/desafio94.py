# Arquivo: desafio94
"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

lista = []
dici = {}
mulheres = []
acimaMedia = []
soma = quant = 0

while True:
    dici['Nome'] = input("Seu nome: ")
    sex = input("Sexo (M/F): ").upper().strip()[0]
    while sex not in "FM": 
        print("ERRO! Digite apenas M ou F.")
        sex = input("Sexo (M/F): ").upper().strip()[0]
    dici['Sexo'] = sex
    dici["Idade"]= int(input("Idade: "))
    soma += dici['Idade'] # Aqui eu somo as idades para dividir dps
    
    lista.append(dici.copy())
    
    option = input("Quer continuar (S/N)? ").upper().strip()[0]
    if option in "N":
        break
    while option not in "S":
        print("ERRO. Responda apenas sim ou não.")
        option = input("Quer continuar (S/N)? ").upper().strip()[0]

for i in range(len(lista)):
    quant += 1
    if lista[i]["Sexo"] == "F":
        mulheres.append(lista[i]["Nome"]) 

media = soma/quant

print("--" * 20)
print(f"Ao todo temos {quant} pessoas cadastradas.")
print(f"A média de idade é de {media:.2f} anos.")
print(f"As mulheres cadastradas foram -> {mulheres}")
print(f"Lista das pessoas acima da média de idade: ") 
for i in range(len(lista)):
    if lista[i]["Idade"] > media:
        print(f"nome = {lista[i]["Nome"]}; sexo = {lista[i]["Sexo"]}; idade = {lista[i]["Idade"]}")
        quantAcima += 1
print("--" * 20)
print(f"{"ENCERRADO. OBRIGADO!":^40}")
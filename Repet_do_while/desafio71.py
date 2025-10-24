# Arquivo: CAIXA ELETRONICO
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual 
#será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
""" 
print("===" * 10)
print('{:^30}'.format('BANCO DO BRASIL'))
print("===" * 10)

sacar = int(input("Quanto vai sacar? R$"))

div = resto = cinquenta = vinte = dez = um = 0


while True:
    if sacar >= 50:
        cinquenta = sacar // 50
        resto = sacar % 50
        if resto >= 20:
            vinte = resto // 20
            resto = resto % 20
            if resto >= 10:
                dez = resto // 10
                resto = resto % 10
                if resto >= 1:
                    um = resto // 1
                    resto = resto % 1
            else:
                um = resto // 1
                resto = resto % 1
        elif resto >= 10:
            dez = resto // 10
            resto = resto % 10
            if resto >= 1:
                um = resto // 1
                resto = resto % 1
        else:
            um = resto // 1
            resto = resto % 1
    elif sacar >= 20:
        vinte = sacar // 20
        resto = sacar % 20
        if resto >= 10:
            dez = resto // 10
            resto = resto % 10
            if resto >= 1:
                um = resto // 1
                resto = resto % 1
        else:
            um = resto // 1
            resto = resto % 1
        
    elif sacar >= 10:
        dez = sacar // 10
        resto = sacar % 10
        if resto >= 1:
            um = resto // 1
            resto = resto % 1
    else:
        um = sacar // 1
        resto = sacar % 1
    
    if resto == 0:
        break
    
print()
if cinquenta >= 1:
    print(f"Retirar {cinquenta} cédulas de R$50")
if vinte >= 1:
    print(f"Retirar {vinte} cédulas de R$20")
if dez >= 1:
    print(f"Retirar {dez} cédulas de R$10")
if um >= 1:
    print(f"Retirar {um} cédulas de R$1")
print("===" * 10)
print("Volte sempre!") """

print('=' * 30)
print('{:^40}'.format('\033[1;33mBanco do Brasil\033[m'))
print('=' * 30)
sacar = int(input("Que valor sacar? R$"))
total = sacar # atribue o valor para outra variavel
ced = 50 # Faz que começe com a cedual de R$ 50
totalCed = 0 # inicializa com 0 cedulas na historia

while True:
    if total >= ced: # Se o valor...
        total = total - ced
        totalCed = totalCed + 1
    else:
        if totalCed > 0:
            print(f"Retirar {totalCed} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print("=" * 30)
print("Volte sempre!")
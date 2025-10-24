# Arquivo: desafio66
quant = soma = 0
while True:
    num = int(input("Digite um número inteiro a seguir (999 para): "))
    if num == 999:
        break
    soma += num
    quant += 1

print(f"Foram {quant} números digitados.")
print(f"SOMA TOTAL = {soma}")    
 
""" num = int(input("Digite um número inteiro a seguir (999 para): "))
quant = soma = 0
while num != 999:
    soma += num
    quant += 1
    num = int(input("Digite outro (999 para): "))

print(f"Foram {quant} números digitados.")
print(f"SOMA TOTAL = {soma}")    
 """
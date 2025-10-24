# Arquivo: leitura de numeros inteiros e sua soma

num = int(input("Digite um número inteiro a seguir (999 para): "))
quant = soma = 0
while num != 999:
    soma += num
    quant += 1
    num = int(input("Digite outro (999 para): "))

print(f"Foram {quant} números digitados.")
print(f"SOMA TOTAL = {soma}")    

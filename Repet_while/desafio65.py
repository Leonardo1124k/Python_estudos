# Arquivo: desafio65
""" resp = "a"
while resp not in "Nn": """
resp = "a"
soma = 0
quant = 0
while resp not in "N":
    num = int(input("Digite um numero inteiro: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        elif num <= menor:
            menor = num
    resp = input("Quer continuar (S/N)? ").upper().strip()[0]

media = soma/quant

print(f"\nVoce digitou {quant} numeros e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}.")

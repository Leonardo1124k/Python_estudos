# Arquivo: calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
print("SOMA ENTRE MULTIPLOS DE 3 NO INTERVALO DE 1 À 500")

soma = 0
for i in range(1,501):
    if i % 3 == 0:
        soma += i

print(f"O resultado da soma é = {soma}")
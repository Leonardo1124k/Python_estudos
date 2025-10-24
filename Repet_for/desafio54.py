# Arquivo: maioridade
from datetime import date

print("Conferir maioridade")
quant = int(input("Quantas pessoas vão participar? "))

maior = 0
ano_atual = date.today().year

for i in range(quant):
    nasc = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    if ano_atual - nasc >= 18:
        maior += 1

print(f"Das {quant} pessoas, {maior} são maiores de idade e {quant - maior} são menores.")

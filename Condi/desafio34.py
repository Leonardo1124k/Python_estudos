# aumento de salario

sal = float(input("Digite seu salario a seguir: "))
if sal > 1250.00:
    newsal = sal * 1.10
    aum = 10
else:
    newsal = sal * 1.15
    aum = 15

print(f"Seu novo salário será R${newsal:.2f}, com aumento de {aum}%")
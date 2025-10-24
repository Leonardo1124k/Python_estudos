#Emprestimo bancario para compra de uma casa

value = float(input("Digite qual o valor da casa a comprar: R$"))
sal = float(input("Digite seu salário: R$"))
anos = int(input("Em quantos anos vai financiar? "))

mensal = value / (anos * 12)

if mensal > (sal * 0.30):
    print(f"Empréstimo NEGADO. Pois a prestação de R${mensal:0.2f} excede em 30% seu salário")
else:
    print(f"Empréstimo permitido! Prestação mensal de R${mensal:.2f}")
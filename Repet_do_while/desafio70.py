# Arquivo: desafio70
print("===" * 12)
print("COMPRA DE PRODUTOS")
print("===" * 12)
gasto = maisMil = cont = 0
while True:
    name = input("Digite o nome do produto: ")
    price = float(input("Preço: R$"))
    cont += 1
    gasto += price
    if price > 1000:
        maisMil += 1        
    if cont == 1:
        menor = name
        menorPreco = price
    else:
        if price < menorPreco:
            menor = name
            menorPreco = price
    
    option = input("Cadastrar mais produtos (S/N)? ").upper().strip()[0]
    if option == "N":
        break
        
print("===" * 5 + " FIM " +  "===" * 5)
print(f"TOTAL GASTO = R${gasto:.2f}")
print(f"Dentre esses produtos, {maisMil} custam mais de R$1000")
print(f"O produto mais barato é {menor} por R${menorPreco:.2f}")

# Formatação com virgulas e milhar
""" total_format = f"{gasto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
menor_format = f"{menorPreco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(f"TOTAL GASTO = R$ {total_format}")
print(f"Dentre esses produtos, {maisMil} custam mais de R$1.000")
print(f"O produto mais barato é {menor} por R$ {menor_format}")
 """
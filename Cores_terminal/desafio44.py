# Arquivo: QUANTO PAGAR PELO PRODUTO
print("\033[0;35m==\033[m" * 5, end=" ")
print("\033[1;33mLoja Pessoni\033[m", end=" ")
print("\033[0;35m==\033[m" * 5)
preco = float(input("Digite o preço da compra: R$"))
print("Digite qual a condição do \033[0;30;45mpagamento\033[m:\n1 - PIX ou dinheiro físico (\033[0;31m10% desconto\033[m);\n2 - À vista no cartão de débito (\033[0;32m5% desconto\033[m);\n3 - Em 2x no cartão de crédito (preço normal); \n4 - 3x ou mais no cartão de crédito (20% de juros) ")
opcao = int(input("Opção escolhida (1, 2, 3 ou 4): "))
print()

if opcao == 1:
    pay = preco * 0.90
    desc = preco - pay
    print(f"Valor a pagar = R${pay:.2f}")
    print(f"Desconto concedido de R${desc:.2f}")
elif opcao == 2:
    pay = preco * 0.95
    desc = preco - pay
    print(f"Valor a pagar = R${pay:.2f}")
    print(f"Desconto concedido de R${desc:.2f}")
elif opcao == 3:
    pay = preco
    print(f"Valor a pagar = R${pay:.2f}")
    print(f"Dividido em 2x de R${pay/2:.2f}")
elif opcao == 4:
    parcelas = int(input("Serão em quantas parcelas? "))
    pay = preco * 1.20
    print(f"\nValor a pagar = R${pay:.2f}")
    print(f"Dividido em {parcelas}x de R${pay/parcelas:.2f}")
    print(f"Juros de R${pay-preco:.2f} aplicado.")
else:
    print(f"OPÇÃO INVÁLIDA. TRY AGAIN.")
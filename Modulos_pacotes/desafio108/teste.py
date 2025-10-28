import moeda

valor = float(input("Digite um valor a seguir: R$"))

print(f"O valor {moeda.moeda(valor)} aumentado em 10% é {moeda.moeda(moeda.aumentar(valor,10))}")
print(f"O valor {moeda.moeda(valor)} diminuido em 10% é {moeda.moeda(moeda.diminuir(valor,10))}")
print(f"O valor {moeda.moeda(valor)} dobrado é {moeda.moeda(moeda.dobro(valor))}")
print(f"O valor {moeda.moeda(valor)} em sua metade é {moeda.moeda(moeda.metade(valor))}")
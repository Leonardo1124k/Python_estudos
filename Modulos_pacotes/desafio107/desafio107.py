import moeda

valor = float(input("Digite um valor a seguir: R$"))

print(f"O valor aumentado é R${moeda.aumentar(valor,10)}")
print(f"O valor diminuido é R${moeda.diminuir(valor,10)}")
print(f"O valor dobrado é R${moeda.dobro(valor)}")
print(f"O valor em sua metade é R${moeda.metade(valor)}")
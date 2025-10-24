# Arquivo: desafio76

print("=" * 40)
print(f"{"PREÇOS DA PAPELARIA":^40}")
print("=" * 40)
tupla = ('Lápis' , 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.80,
         'Livro', 34.90)

for i in range(0,len(tupla)):
    if i % 2 == 0:
        print(f"{tupla[i]:.<30}", end = "")
    else:
        print(f"R${tupla[i]:>7.2f}")
print("-" * 40)
# Arquivo: TABUADA

num = int(input("Escolha um número para apresentar sua tabuada: "))

print("==" * 4)
for i in range (1, 11):
    print(f"{num} x {i:2} = {num*i:2}")
print("==" * 4)
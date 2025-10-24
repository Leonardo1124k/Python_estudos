# Arquivo: desafio75

num = int(input("Digite um numero inteiro: "))
num2 = int(input("Outro numero: "))
num3 = int(input("Outro numero: "))
num4 = int(input("Outro numero: "))

tupla = (num, num2, num3, num4)

print(tupla)
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if tupla.count(3) > 0:
    print(f"O valor 3 apareceu pela primeira vez na posição {tupla.index(3) + 1}")
else:
    print("O valor 3 não apareceu nenhuma vez.")
    
print("Os valores pares foram: ", end="")
for i in tupla:
    if i % 2 ==0:
        print(f"{i} ", end="")
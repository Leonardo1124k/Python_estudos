# Qual valor e maior dos dois

print("Analise de qual numero inteiro é maior \n")
x = int(input("Primeiro numero: "))
y = int(input("Segundo numero: "))

if x > y:
    print(f"{x} é o maior valor!")
elif y > x:
    print(f"{y} é o maior valor!")
else:
    print(f"OS dois valores são iguais! São igual a {x}")
# Arquivo: fatorial
""" from math import factorial
num = int(input("Digite um numero a seguir: "))
print(f"{num}! = {factorial(num)}") """

num = int(input("Digite um numero a seguir: "))
var = num
fat = 1

print(f"FATORIAL {num}! => ", end="")

while var > 0:
    print(f"{var}", end="")
    print(f" x " if var > 1 else " = ", end="")
    fat = fat * var
    var -= 1

print(f"{fat}")
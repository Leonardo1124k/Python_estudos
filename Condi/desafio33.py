# qual maior e menor dos 3

x = float(input("Digite um numero a seguir: "))
y = float(input("Digite o segundo: "))
z = float(input("Digite o terceiro: "))
print()
if x > y and x > z:
    print(f"{x} é o maior de todos")
elif y > z:
    print(f"{y} é o maior de todos")
else:
    print(f"{z} é o maior de todos")
    
if x < y and x < z:
    print(f"E {x} é o menor de todos")
elif y < z:
    print(f"E {y} é o menor de todos")
else:
    print(f"E {z} é o menor de todos")
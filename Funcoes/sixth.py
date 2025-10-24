def fat(num=1): # Parametro opcional definido
    f = 1
    for c in range(num,0, -1):
        f *= c
    return f

# n = int(input("Digite um numero: "))
# print(f"O valor fatorial de {n} é {fat(n)}")

f1 = fat(int(input("Digite um numero: ")))
f2 = fat(int(input("Digite outro: ")))
f3 = fat(int(input('Digite o ultimo: ')))

print(f"Os resultados fatoriais são {f1}, {f2}, {f3}")

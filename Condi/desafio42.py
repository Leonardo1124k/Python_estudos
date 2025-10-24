# retas podem formar triangulo equilatero ESCALENO E ISOSCELES

print("==" * 50)
print("Analise de condições de existencia para um TRIANGULO")
print("==" * 50)

x = float(input("Primeiro segmento de reta: "))
y = float(input("Segundo segmento de reta: "))
z = float(input("Terceiro segmento de reta: "))

if x < (y + z) and y < (x + z) and z < (x + y):
    print("Condições satisfeitas! Este triângulo pode existir")
    if x == y == z:
        print("O triângulo será equilátero. Todos os lados são iguais")
    elif x == y or y == z or x == z:
        print("O triângulo será isósceles. Dois lados são iguais")
    else:
        print("O triângulo será escaleno. Nenhum lado é igual.")
else:
    print("NÃO é possível existir um triangulo com essas dimensões!")
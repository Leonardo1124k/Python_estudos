# retas podem formar triangulo

print("==" * 50)
print("Analise de condições de existencia para um TRIANGULO")
print("==" * 50)

x = float(input("Primeiro segmento de reta: "))
y = float(input("Segundo segmento de reta: "))
z = float(input("Terceiro segmento de reta: "))

if x < (y + z) and y < (x + z) and z < (x + y):
    print("Condições satisfeitas! Este triângulo pode existir")
else:
    print("NÃO é possível existir um triangulo com essas dimensões!")
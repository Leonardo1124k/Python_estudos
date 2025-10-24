# retas podem formar triangulo equilatero ESCALENO E ISOSCELES

print("\033[1;31m==\033[m" * 50)
print("\033[0;33mAnalise de condições de existencia para um TRIANGULO\033[m")
print("\033[1;31m==\033[m" * 50)

x = float(input("\033[4;35mPrimeiro\033[m segmento de reta: "))
y = float(input("\033[4;36mSegundo\033[m segmento de reta: "))
z = float(input("\033[1;30;41mTerceiro\033[m segmento de reta: "))

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
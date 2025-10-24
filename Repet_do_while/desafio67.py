# Arquivo: desafio67
print("PROGRAMA TABUADA")
#i = 0
while True:
    num = int(input("Digite um numero (negativo para parar): "))
    if num < 0:
        break
    for i in range (1,11):
        print(f"{num} x {i:2} = {num*i}")

print("FIM")
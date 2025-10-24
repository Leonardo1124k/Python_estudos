# Arquivo: pa

print("Especialista em P.A's")

num = int(input("Digite o primeiro número da progressão: "))
raz = int(input("Digite a razão (distância entre numeros): "))
result = 0

print("\nSequência dos 10 primeiros números: ")
for i in range(0,10):
    result = num + raz * i
    print(f"{result:2}") 
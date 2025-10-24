# Arquivo: pa MELHORADA

print("Especialista em P.A's 2.0")

num = int(input("Digite o primeiro número da progressão: "))
raz = int(input("Digite a razão (distância entre numeros): "))
i = 0

print("\nSequência dos 10 primeiros números: ", end="")
while i != 10:
    result = num + raz * i
    i += 1
    print(f"{result} ", end ="")  


# Arquivo: pa
""" 
print("Especialista em P.A's")

num = int(input("Digite o primeiro número da progressão: "))
raz = int(input("Digite a razão (distância entre numeros): "))

print("\nSequência dos 10 primeiros números: ")
for i in range(0,10):
    result = num + raz * i
    print(f"{result:2}")  """
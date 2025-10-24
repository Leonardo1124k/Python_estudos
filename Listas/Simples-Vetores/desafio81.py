# Arquivo: desafio81
# quant = int(input("Quantos numeros vai querer digitar? "))
# lista = []
# cinco = False
# for i in range (quant):
#     num = int(input(f"Digite o {i+1}° numero: "))
#     lista.append(num)
#     if num == 5:
#         cinco = True
#         posi5 = i

# print(f"Foram digitados {quant} numeros")
# lista.sort(reverse=True)
# print(f"Lista em ordem decrescente-> {lista}")
# if cinco == True:
#     print(f"O valor 5 foi digitado na lista.")
# else:
#     print("O valor 5 não foi digitado na lista.")



lista = []
cinco = False
quant = 0
while True:
    quant += 1
    num = int(input(f"Digite o {quant}° numero: "))
    lista.append(num)
    if num == 5:
        cinco = True
        posi5 = quant
        
    option = input("Vai querer continuar (S/N) ? ").upper().strip()[0]    
    if option == "N": 
        break

print(f"Foram digitados {quant} numeros")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente-> {lista}")
if cinco == True:
    print(f"O valor 5 foi digitado na lista.")
else:
    print("O valor 5 não foi digitado na lista.")
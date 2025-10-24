# Conversao de numero para binario octa e hexa
print("=="*30)
print("Conversor de numeros")
print("=="*30)

num = int(input("Digite um numero a seguir: "))
print("Escolha para qual opção quer converter: \n1 - binario; 2 - octal; 3 = hexadecimal")
decisao = int(input("Opção escolhida: "))

if decisao == 1:
    trans = bin(num)
    print(f"{num} convertido para binario é igual a {trans[2:]}") # para nao ficar aparecendo ob...xyz
elif decisao == 2:
    trans = oct(num)
    print(f"{num} convertido para octal é igual a {trans[2:]}") # para nao ficar aparecendo oc...xyz
elif decisao == 3:
    trans = hex(num)
    print(f"{num} convertido para hexadecimal é igual a {trans[2:]}") # para nao ficar aparecendo ox...xyz
else:
    print("Opção invalida. Try again...")
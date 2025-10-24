def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um numero: "))

if par(num):
    print("É um numero par! ")
else:
    print("Não é um numero par!")
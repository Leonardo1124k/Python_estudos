# Arquivo: Sequencia de fibonacci
print("Sequência de Fibonacci")

termos = int(input("Quantos termos voce quer mostrar da sequência? "))
i = 0
num = 0
num2 = 1
result = 0
print("--" * 30)
while i != termos:
    if i == 0:
        print(f"{num} -> ", end="")
    elif i == 1:
        print(f"{num2} -> ", end="")
    else:
        result = num + num2
        num = num2
        num2 = result
        if i == termos - 1:
            print(f"{result}")    
        else: 
            print(f"{result} -> ", end="")
    i += 1
print("--" * 30)
print("FIM")
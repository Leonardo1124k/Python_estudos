# Arquivo: número primo

num = int(input("Digite um número inteiro, para ver se é primo ou não: "))
result = 0

for i in range(1, num+1):
    if num % i == 0:
        result += 1
        print('\033[31m', end ='')
    else:
        print('\033[32m', end ='')
    print(f'{i} ', end='')

print("\n\033[m", end="")
if result > 2: 
    print(f"O número {num} NÃO é primo, pois foi divizível {result} vezes!")
else:
    print(f"O número {num} é PRIMO, pois foi divisível apenas {result} vezes!")
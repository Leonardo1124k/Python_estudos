num = int(input("Digite um numero (0-9999): "))

u = num % 10 # divido o numero por 10 e pego o resto que é a unidade
d = num // 10 % 10 # divido o numero por 10 em parte inteira...
c = num // 100 % 10
m = num // 1000 % 10

print(f"\033[0;31mUnidade: {u}\033[m")
print(f"\033[0;32mDezena: {d}\033[m")
print(f"\033[0;33mCentena: {c}\033[m")
print(f"\033[0;34mMilhar: {m}\033[m")

# num = input("Digite um numero (0-9999): ")

# u = num[-1]
# if int(num) >= 10:
#     d = num[2]
# else:
#     d = 0
# if int(num) >= 100:
#     c = num[1]
# else:
#     c = 0
# if int(num) >= 1000:
#     m = num[0]
# else: 
#     m = 0

# print(f"Unidade: {u}")
# print(f"Dezena: {d}")
# print(f"Centena: {c}")
# print(f"Milhar: {m}")
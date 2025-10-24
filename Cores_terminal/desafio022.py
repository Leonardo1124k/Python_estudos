#Crie um programa que leia o nome completo da pessoa e mostre:
#O nome com todas as letras maiusculas
#minusculas
#Quantas letras tem ao (todo sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ")

print(f"\033[0;30m{nome.upper()}\033[m")
# print(nome.lower())
print(f"\033[0;31m{nome.lower()}\033[m")
nospace = nome.split()
print(f"\033[0;32m{nospace}\033[m")
print(f"\033[0;33m{len(''.join(nospace))}\033[m")
print(f"\033[0;34m{len(nospace[0])}\033[m")

# nospace = 'xx'.join(nospace)
# print(nospace)
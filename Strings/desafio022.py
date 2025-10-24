#Crie um programa que leia o nome completo da pessoa e mostre:
#O nome com todas as letras maiusculas
#minusculas
#Quantas letras tem ao (todo sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ")

print(nome.upper())
print(nome.lower())
nospace = nome.split()
print(nospace)
print(len(''.join(nospace)))
print(len(nospace[0]))

nospace = 'xx'.join(nospace)
print(nospace)
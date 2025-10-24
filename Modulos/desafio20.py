# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia o nome deles e escreva o escolhido.

from random import shuffle

print("Digite o nome dos alunos abaixo: ")

n1 = input("")
n2 = input("")
n3 = input("")
n4 = input("")

lista = [n1,n2,n3,n4]
shuffle(lista)

print("A ordem de apresentação será: ")
print(lista)
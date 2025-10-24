# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia o nome deles e escreva o escolhido.

from random import choice

print("Digite os nomes dos alunos a seguir: ")
n1 = input("")
n2 = input("")
n3 = input("")
n4 = input("")

lista = [n1,n2,n3,n4]

escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")

# from random import choice

# lista = []

# for i in range (0,4):
#     n1 = input(f"Digite o nome do {i+1}° aluno: ")
#     lista.append(n1)

# print(f"O aluno escolhido foi {choice(lista)}")
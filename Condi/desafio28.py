# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

sorte = randint(0,5)

print("=" * 50)
print("Pensei em um numero entre 0 e 5... Tente adivinhar!")
print("=" * 50)

num = int(input("Qual numero que pensei? "))
print("Processando...")
sleep(2)

if num == sorte:
    print(f"Parabéns, voce acertou! O número é {num}")
else:
    print(f"Você errou! O número correto é {sorte} e não {num}")
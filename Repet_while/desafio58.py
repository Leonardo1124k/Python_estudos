# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# PROGRAMA MELHORADO COM WHILE

from random import randint
from time import sleep

print("=" * 55)
print("Pensei em um numero entre 0 e 10... Tente adivinhar!")
print("=" * 55)

num = int(input("Qual numero que pensei? "))
print("Processando...")
sleep(2)

sorte = randint(0,10)
tentativas = 1

while num != sorte:
    tentativas += 1
    if num < sorte:
        num = int(input("ERRADO!\nTente um numero maior: "))
    else:
        num = int(input("ERRADO!\nTente um numero menor: "))
    print("Processando...")
    sleep(2)

print(f"Parabéns, voce acertou em {tentativas} tentativas! O número é {num}")
sleep(2)

""" else:
    print(f"Você perdeu! O número correto é {sorte} e não {num}") """
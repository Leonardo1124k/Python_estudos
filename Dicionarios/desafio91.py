# Arquivo: desafio91
from random import randint
from time import sleep
from operator import itemgetter

#Significa JOGADORES
jog = {'jogador 1': randint(1,6),
       'jogador 2': randint(1,6),
       'jogador 3': randint(1,6),
       'jogador 4': randint(1,6)
       }
ranking = list()

print("Valores sorteados: ")
for k,v in jog.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jog.items(), key = itemgetter(1), reverse = True)
#EXPLICACAO:
#jog.items() -> gera uma lista de tuplas: [(jogador1, numero)...]
#key = itemgetter(1) -> diz para o sorted ordenar usando o elemento 1 da tupla, ou seja, o numero do dado
#reverse = True -> Coloca a ordem decrescente

print('--' * 30)
print("Ranking dos jogadores: ")
for i,j in enumerate(ranking):
    print(f"{i+1}° lugar: {j[0]} com {j[1]} pontos")
    sleep(1)
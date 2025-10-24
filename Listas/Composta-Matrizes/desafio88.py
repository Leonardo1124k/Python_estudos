# Arquivo: desafio88
""" from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
print("==" * 20)
print(f"{"MEGA SENA GAME":^40}")
print("==" * 20)
quant = int(input("Quantos jogos sortear? "))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    
print("--" * 3, f" Sorteio de {quant} jogos ", "--" * 3)
for i, j in enumerate(jogos):
    print(f"Jogo {i+1}: {j}")
    sleep(1)
print("--" * 5, "BOA SORTE", "--" * 5)
     """
from random import randint
from time import sleep
listajogos = []
jogo = []
print("==" * 20)
print(f"{"MEGA SENA DA VIRADA":^40}")
print("==" * 20)
jog = int(input("Quantos jogos devo sortear de 1 a 60? "))
print("--" * 5, f"SORTEIO DE {jog} JOGOS", "--" * 5)
for i in range(jog):
    while len(jogo) < 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    listajogos.append(jogo[:])
    jogo.clear()
for i, jogo in enumerate(listajogos, start=1):
    print(f"Jogo {i}: {jogo}")
    sleep(0.5)
print("--" * 5, f"{"< BOA SORTE >":^18}", "--" * 5)



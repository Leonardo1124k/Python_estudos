# Arquivo: PEDRA PAPEL TESOURA
import random
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")

print("==" * 5, end="")
print(" JOKENPO GAME ", end="")
print("==" * 5)

print("""Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

game = int(input("Qual sua escolha? "))
if game < 0 or game > 2:
    print("OPÇÃO INVÁLIDA! TRY AGAIN.")
else:
    maq = random.randint(0,2)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(1)
    print("PO")
    print("==" * 8)
    print(f"Sua escolha = {itens[game]}")
    print(f"Escolha da máquina = {itens[maq]}")
    print("==" * 8)
            
if game == maq:
    print("EMPATE")
elif (game == 0 and maq == 2) or (game == 1 and maq == 0) or (game == 2 and maq == 1):
    print("VOCÊ VENCEU!")
else:
    print("VOCÊ PERDEU!")
# PODERIA USAR ESSA OPÇAO melhor
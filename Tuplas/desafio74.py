# Arquivo: desafio74
from random import randint

tupla = (randint(0,10),randint(0,10), randint(0,10), randint(0,10), randint(0,10))
# tupla = (randint(0,10) for x in range (0,5))

print("Números gerados: ", end="")
for i in tupla:
    print(f"{i} ", end="")
print(f"\nO maior valor sorteado foi {max(tupla)}")
print(f"O menor valor sorteado foi {min(tupla)}")
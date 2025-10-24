# Arquivo: par ou impar game 
import random
from time import sleep
print("==" * 20)
print("PAR OU IMPAR GAME")
print("==" * 20)
vitoria = derrota = num = num2 = 0
while True:
    option = input("Voce será par ou impar? ").upper().strip()[0]
    num = int(input("Digite seu numero: "))
    num2 = random.randint(0,10)
    sleep(1)
    
    if option == "P":
        if (num + num2)%2==0:
            vitoria += 1
            print(f"Você acertou! Meu numero foi {num2}, então o resultado foi {num + num2} -> PAR")
        else:
            derrota += 1
            print(f"Você errou! Meu numero foi {num2}, então o resultado foi {num + num2} -> IMPAR")
            break
    elif option == "I":
        if (num + num2)%2!=0:
            vitoria += 1
            print(f"Você acertou! Meu numero foi {num2}, então o resultado foi {num + num2} -> IMPAR")
        else:
            derrota += 1
            print(f"Você errou! Meu numero foi {num2}, então o resultado foi {num + num2} -> PAR")
            break
    else:
        print("OPÇÃO INVALIDA. TRY AGAIN.")
print("GAME OVER")
if vitoria > 1:
    print(f"Você teve {vitoria} vitorias consecutivas!")
elif vitoria == 1:
    print(f"Você teve {vitoria} vitoria durante o jogo!")
else:
    print(f"Você não teve vitoria alguma!")
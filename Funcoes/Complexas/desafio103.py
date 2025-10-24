# Arquivo: ficha de jogador FUNÇÃO

def ficha(nome = "<desconhecido>", gols = 0):
    return f"O jogador {nome} fez {gols} gols(s) no campeonato."


#Programa Principal
print("==" * 20)
jog = input("Digite o nome do jogador: ")
golos = input("Digite quantos gols foram feitos: ") 

if golos.isnumeric():
    golos= int(golos)
else:
    golos = 0

if jog.strip() == "":
    print(ficha(gols=0))
else:
    print(ficha(jog,golos))
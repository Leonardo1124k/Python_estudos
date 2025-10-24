# Arquivo: desafio95
#Exercício Python 095: Aprimore o desafio 93 para que ele funcione
#com vários jogadores, incluindo um 
#sistema de visualização de detalhes do aproveitamento de cada jogador.

""" print("==" * 20)
print(f"{'⚽ Aproveitamento em jogos ⚽':^40}")
print("==" * 20)

geral = []
gols = []
player = {}
total = 0
while True:
    player['nome'] = input("\nDigite seu nome: ")
    player['partidas'] = int(input(f"Quantas partidas {player['nome']} jogou? "))
    total = 0
    gols.clear()
    for i in range(0,player['partidas']):
        gol = int(input(f"Quantos gols fez na {i+1}° partida? "))
        total += gol
        gols.append(gol)
    player['gols'] = gols[:]
    player['total'] = total
    geral.append(player.copy())
    
    option = input("Quer continuar (S/N)? ").upper().strip()[0]
    if option == "N":
        break
    while not option == "S":
        option = input("ERRO. DIGITE APENAS S OU N.\nQuer continuar (S/N)? ").upper().strip()[0]

print('==' * 20)
print(f"{"cod":<6}{"nome":<6}{"gols":>10}{"total":>12}")
print("--" * 20)
for i in range(len(geral)):
    print(f"{i:<6} {geral[i]['nome']:<6} {geral[i]['gols']} {geral[i]['total']:>10}")
print("--" * 20)

while True:
    qual = int(input("Mostrar dados de qual jogador? (99 para parar) "))
    if qual == 99:
        break
    while qual > len(geral)-1:
        print('Erro. codigo INVALIDO.')
        qual = int(input("Mostrar dados de qual jogador? (99 para parar) "))
        
    print(f"Levantamento do jogador {geral[qual]['nome']}: ")
    for i in range(0, geral[qual]['partidas']):
        print(f"No jogo {i+1} fez {geral[qual]['gols'][i]} gols ")
    
print("<<< Programa finalizado >>>") """
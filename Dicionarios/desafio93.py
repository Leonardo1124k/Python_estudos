# Arquivo: desafio93
print("==" * 20)
print(f"{'⚽ Aproveitamento em jogos ⚽':^40}")
print("==" * 20)

player = {}
gols = []
total = 0

player['nome'] = input("Digite seu nome: ")
player['partidas'] = int(input(f"Quantas partidas {player['nome']} jogou? "))
for i in range(0,player['partidas']):
    gol = int(input(f"Quantos gols fez na {i+1}° partida? "))
    total += gol
    gols.append(gol)
player['gols'] = gols
player['total'] = total    
print('--' * 20)
print(player)
print('--' * 20)
for k, v in player.items():
    print(f"O campo {k} é igual a {v}")
print('--' * 20)
print(f"O jogador {player['nome']} jogou {player['partidas']} partidas: ")
for i in range(len(player['gols'])):
    print(f"-> Na partida {i+1}, fez {player["gols"][i]} gols")
print(f"Foi um total de {player['total']} gols.")
# Arquivo: desafio73
tabela = ("Palmeiras","Flamengo", "Cruzeiro", "Mirassol", "Botafogo", "Bahia", "Fluminense", "São Paulo", "Bragantino", "Ceará","Vasco da Gama", "Corinthians","Grêmio", "Atlético MG", "Internacional" , "Santos","Vitória","Fortaleza", "Juventude", "Sport")

print(f"Lista de times do Brasileirão: {tabela}")
print("===" * 40)
print(f"Os 5 primeiros: {tabela[:5]}")
print(f"\nOs 4 últimos: {tabela[16:]}")
print(f"\nEm ordem alfabética: {sorted(tabela)}")
time = "Chapecoense"
if tabela.count(time) > 0:
    print(f"\nO {time} está na {tabela.index(time) + 1}° posição da tabela.")
else:
    print(f"\n{time} não está no campeonato!")
galera = list()
dados = list()
totmaior = totmenor = 0

for i in range(0,4):
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:]) # importante detalhe sem isso faz uma ligação com outra lista
    dados.clear()
    
for p in galera:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmenor += 1

print(f"Temos {totmaior} maiores e {totmenor} menores de idade.")
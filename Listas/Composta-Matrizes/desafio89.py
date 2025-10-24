# Arquivo: desafio89
ficha = list()

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media]) # Cria uma estrutura de ficha já delimitada manualmente sua composição
    resp = input("Continuar (S/N)? ")
    if resp in "Nn": # apenas questiona se na string tem N ou n (prático)
        break

print("==" * 30)
print(f"{"N°":<4}{"Nome":<10}{"Média":>8}") # :<4 alinha a esquerda em 4 caracteres :>8 alinha para a direita em 8 caracteres
print("-" * 26)
for i, j in enumerate(ficha):
    print(f"{i:<4}{j[0]:<10}{j[2]:>8.1f}")# :<4 alinha a esquerda em 4 caracteres :>8 alinha para a direita em 8 caracteres
while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno (999 finaliza)? "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(ficha) - 1: # questiona se opc tem valor do tamanho da ficha
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}") #seleciono nome e notas com os indices
    elif opc > len(ficha) - 1: # se opc for maior que o tamanho da ficha já é barrado
        print("Índice inexistente. Tente novamente...")
print("<<< Volte sempre >>>")
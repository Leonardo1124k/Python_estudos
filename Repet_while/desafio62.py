# Arquivo: desafio62 P.A SUPER MELHORADA

print("Especialista em P.A's 3.0")
first = int(input("Primeiro termo: "))
raz = int(input("Razão da P.A: "))
termo = first
cont = 1 
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} ", end="")
        termo += raz
        cont += 1
    mais = int(input("\nQuantos termos mais mostrar? "))
print(f"\nPrograma finalizado. Foram {total} termos mostrados")
        
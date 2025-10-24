# Arquivo: desafio59
opcao = 0
print("==" * 20)
print("Programa calculador")
print("==" * 20)

x = float(input("\nDigite o 1° valor: "))
y = float(input("Digite o 2° valor: "))

while opcao != 5:
    print("""
===== MENU =====
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        print(f"SOMA -> {x} + {y} = {x+y}")
    elif opcao == 2:
        print(f"MULTIPLICACAO -> {x} x {y} = {x*y}")
    elif opcao == 3:
        if x > y:
            print(f"{x} é maior que {y}")
        elif x < y:
            print(f"{y} é maior que {x}")
        else:
            print("Os dois valores são iguais.")
    elif opcao == 4:
        x = float(input("\nDigite novamente o 1° valor: "))
        y = float(input("Digite novamente o 2° valor: "))
    elif opcao == 5:
        print("Finalizando o programa...")
    else:
        print("Opção inválida.")

print("===" * 5)
print("Programa finalizado. Volte sempre!")
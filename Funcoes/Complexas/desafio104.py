# Arquivo: desafio104
#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante 'a função input() do Python, só que fazendo a 
# validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;32mErro! Digite um número inteiro válido.\033[m")
        # try: SOLUÇÃO MELHOR AINDA
        #     valor = int(n)  # tenta converter para inteiro
        #     return valor     # se der certo, retorna o número
        # except ValueError:
        #     print("\033[1;32mErro! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor
n = leiaInt("Digite um numero: ")
print(f"Você acabou de digitar o numero {n}")
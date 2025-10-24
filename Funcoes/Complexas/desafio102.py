# Arquivo: desafio102
def fatorial (n, show = False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta toda.
    :return: o valor do Fatorial do numero n.
    """
    f = 1
    for c in range(n,0,-1):
        if show: # Se meu usuario pedir pra mostrar
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f

#Programa principal
print(fatorial(5,show=True)) # Aqui posso conceceder ou não o dado "show"
help(fatorial) #Interactive help da minha docstring

#fatorial(5,show=True) se eu fizesse isso o resultado não ia aparecer no final
# por isso é necessário o print, para mostrar o "return" f dado
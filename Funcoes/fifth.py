#FUNCOES 2

def contador(i,f,p): # Aqui abaixo estou criando a docstring
    """
Faz uma contagem e mostra na tela.
:param i: inicio da contagem
:param f: fim da contagem
:param p: passo da contagem
:return: sem retorno
Função criada por Leonardo Pessoni
    """
    c=i
    while c<=f:
        print(f"{c} ", end="")
        c += p
    print("FIM!\n")

contador(0,100,10)
help(contador) # Aqui estou chamando a descrição da função -> Interactive Help



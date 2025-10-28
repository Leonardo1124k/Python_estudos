def aumentar(n = 0, quanto = 0, formato = False):
    n = n + (n * quanto/100)
    return n if formato is False else moeda(n)

def diminuir(n=0, quanto=0, formato = False):
    n = n - (n * quanto/100)
    return n if formato is False else moeda(n)

def dobro (n=0, formato = False):
    n = n * 2
    return n if formato is False else moeda(n)
def metade (n=0, formato = False):
    n = n / 2
    return n if formato is False else moeda(n)

def moeda (preco = 0.0, moeda = "R$"):
    return f"{moeda}{preco:>.2f}".replace('.', ',')
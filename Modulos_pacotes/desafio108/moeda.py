def aumentar(n, quanto):
    n = n + (n * quanto/100)
    return n
def diminuir(n, quanto):
    n = n - (n * quanto/100)
    return n
def dobro (n):
    n = n * 2
    return n
def metade (n):
    n = n / 2
    return n

def moeda (preco = 0, moeda = "R$"):
    return f"{moeda}{preco:>.2f}".replace('.', ',')
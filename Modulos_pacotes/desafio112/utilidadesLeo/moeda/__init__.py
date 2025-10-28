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

def resumo (preco = 0, taxaaumento = 10, taxareducao = 5):
    print("-" * 30)
    print("Resumo do valor".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco,True)}")
    print(f"Metade do preço: \t{metade(preco,True)}")
    print(f"{taxaaumento}% de aumento: \t{aumentar(preco,taxaaumento,True)}")
    print(f"{taxareducao}% de redução: \t{diminuir(preco,taxareducao,True)}")
    print("-" * 30)
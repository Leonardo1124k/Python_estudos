# num = (0,1,2,3) 
# num[1] = 5 FAzer isso aqui não dá certo

num = [2,5,6,1]
print(f"Minha lista original -> {num}")
num[1] = 7 # Altera o numero neste index
print(f"Minha lista uma vez alterada-> {num}")
num.append(7) # Acrescenta ao final da lista
print(f"Minha lista acrescentada-> {num}")
num.sort() # Ordena a lista em forma crescente (em reverso neste caso)
print(f"Minha lista 'ordenada'-> {num}")
num.insert(2,0) # No determinado index adiciona um valor e faz os outros valores chegarem mais para a direita, alterando seus índices
print(f"Minha lista 'enxertada'-> {num}")
num.pop(2) # Corta o índice indicado (o último se estiver vazio) e altera os outros índices para menor
print(f"Minha lista com um retiro-> {num}")
if 5 in num:
    num.remove
else:
    print("Não encontrei o 5")
print(f"A lista contém {len(num)} elementos")
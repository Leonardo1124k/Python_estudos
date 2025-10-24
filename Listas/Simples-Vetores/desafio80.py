# Arquivo: desafio80
print("Cadastre 5 valores númericos a seguir: ")
lista = []
for i in range(0,5):
    num = int(input(f"Digite o {i+1}° valor: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print(f"{num} foi adicionado ao final da lista...")
    else:
        # pos = 0
        # while pos < len(lista):
        #     if num <= lista[pos]:
        #         lista.insert(pos,num)
        #         print(f"{num} adicionado na posição {pos} da lista...")
        #         break
        #     pos +=1
        for pos in range(0, len(lista)):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f"{num} adicionado na posição {pos} da lista...")
                break
            pos +=1
    
print("==" * 20)
print(f"Lista elaborada em ordem -> {lista}")
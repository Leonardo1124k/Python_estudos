# Arquivo: desafio79
lista = list()
quant = (int(input('Quantos valores queres digitar? ')))

for i in range(quant):
    num = int(input(f"Digite o {i+1}° valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Valor já digitado... Não posso adicionar na lista.")
        
lista.sort()        
print(f"Lista elaborada com os valores -> {lista}")
# Arquivo: desafio72
tupla = ("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Quatorze","Quinze","Desesseis","Desessete", "Dezoito", "Dezenove", "Vinte")

option = int(input("Digite um numero de 0-20 para visualizá-lo:"))

while option < 0 or option > 20:
    option = int(input("ERRO! TRY AGAIN. Digite um numero de 0-20:"))
    
print(f"O número escolhido é o {tupla[option].lower()}")
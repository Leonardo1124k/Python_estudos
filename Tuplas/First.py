lanche = ("Hamburguer", "Lanche", "Coca", "Zen")

print(sorted(lanche)) #Ordena alfabeticamente
print(lanche)

a = (2,5,4)
b = (5,8,1,2)
c = b + a # é diferente de c = a + b

print(c)
print(len(c)) # tamanho total
print(c.count(5)) # vezes que o "x" aparece
print(c.index(5)) # posição de algum elemento
print(c.index(5,1)) # posição do elemento a partir do index x

pessoa = ('Gustavo', 39, "M", 99.8)
print(pessoa)
del(pessoa)
option = input("Continuar? ")
if option == "s":
    print(pessoa)
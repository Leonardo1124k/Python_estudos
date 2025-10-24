# Arquivo: VOGAIS EM TUPLAS
print("PROCURADOR DE VOGAIS")
print("--" * 15, end='')
tupla = ('beija-flor','mesa','perfume','estojo','manteiga','goaiba','iogurte','riqueza','gelo')
for i in tupla:
    print(f"\nNa palavra {i.upper()} temos ", end="")
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra,end="")
    

""" print(c.index(8)) # posição de algum elemento
print(c.index(5,1)) # posição do elemento a partir do index x """
from random import randint

#Escopo local
def soma(a,b): #AQUI SÃO OS PARAMETROS ACEITOS
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma {a} + {b} = {s}\n")
    print(s)

# Programa principal (Escopo global)
soma(randint(0,10),randint(0,10)) # AQUI SÃO OS ARGUMENTOS PASSADOS
soma(randint(0,10),randint(0,10))
soma(randint(0,10),randint(0,10))

#print(s) ISSO AQUI NÃO FUNCIONA... 
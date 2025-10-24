def dobra(lista): # Aqui são os parâmetros
    pos = 0
    while pos < len(lista): #"valores" passa a se chamar "lista" aqui 
        lista[pos] *= 2
        pos += 1
    # for pos in range(len(lista)):
    #     lista[pos] *= 2
    # ...Outra forma
   
valores = [6,3,9,1,0,2]
dobra(valores) # Aqui passo os argumentos
print(valores)
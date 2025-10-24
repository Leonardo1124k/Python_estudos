a = [1,2,3,4,5]
#b = a # ISSO FAZ UMA CONEXÃO/LIGAÇÃO ENTRE AS LISTAS, O QUE MUDARES EM UMA, É MUDADO NA OUTRA
b = a[:] # Isso sim é uma cópia
b[2]= 99
print(f'Lista A: {a}')
print(f'Lista B: {b}')
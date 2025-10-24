def teste():
    x = 8
    print(f"Na função, n = {n}")
    print(f"Na função, x = {x}") # X é uma variável LOCAL!
    
#Programa Principal

n = 2 # N é uma variável GLOBAL!
teste()
print(f"Fora, n = {n}")
# print(f"Fora, x = {x}") DARIA RUIM
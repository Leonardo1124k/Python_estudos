# Lista com valores repetidos
numeros = [1, 2, 3, 2, 4, 3, 5, 1]

# Convertendo para set remove automaticamente os duplicados
conjunto_numeros = set(numeros)
print("Sem duplicatas:", conjunto_numeros)

# Exemplo de operações com conjuntos
pares = {2, 4, 6, 8}
ímpares = {1, 3, 5, 7, 9}

# União: combina os elementos sem repetir
print("União:", pares | ímpares)

# Interseção: elementos comuns
print("Interseção:", pares & ímpares)

# Diferença: elementos que estão em pares, mas não em ímpares
print("Diferença:", pares - ímpares)

# Verificação rápida de existência
print("O número 4 está em pares?", 4 in pares)
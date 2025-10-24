# Arquivo: PALINDROMO

frase = input("Digite uma frase ou palavra a seguir: ").strip().upper()
frase = frase.split()
frase = ''.join(frase)

print(f"O inverso de {frase} é {frase[::-1]}")

if frase == frase[::-1]:
    print("Se trata de um palindromo!")
else:
    print("NAO é um palindromo.")
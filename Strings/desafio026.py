frase = input("Digite uma frase: ").upper()

print(f"A letra A aparece {frase.count('A')} vezes")
print(f"Ela aparece pela primeira vez na posição {frase.find("A") + 1}")
frase = frase[::-1]
print(f"Ela aparece pela última vez na posição {len(frase) - frase.find("A")}")
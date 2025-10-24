frase = input("\033[0;37mDigite uma frase: \033[m").upper()

print(f"\033[0;40mA letra A aparece {frase.count('A')} vezes\033[m")
print(f"\033[1;41mEla aparece pela primeira vez na posição {frase.find("A") + 1}\033[m")
frase = frase[::-1]
print(f"\033[1;42mEla aparece pela última vez na posição {len(frase) - frase.find("A")}\033[m")
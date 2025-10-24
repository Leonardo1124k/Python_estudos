# Arquivo: ANO DE NASCIMENTO PARA CLASSIFICACAO DO ALUNO NA NATAÇÃO
from datetime import date

print("\033[1;34m==\033[m" * 40)
print(f"{"Classificação para divisão de Natação":^80}")
print("\033[1;34m==\033[m" * 40)

birthyear = int(input("Digite seu ano de nascimento: "))
age = date.today().year - birthyear

if age <= 9:
    print(f"Voce tem {age} anos. Está na divisão MIRIM.")
elif age <= 14:
    print(f"Voce tem {age} anos. Está na divisão INFANTIL.")
elif age <= 19:
    print(f"Voce tem {age} anos. Está na divisão JUNIOR.")
elif age <= 25:
    print(f"Voce tem {age} anos. Está na divisão SENIOR.")
else:
    print(f"Voce tem {age} anos. Está na divisão MASTER.")
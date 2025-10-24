# Arquivo: ANO DE NASCIMENTO PARA CLASSIFICACAO DO ALUNO NA NATAÇÃO

from datetime import date

print("==" * 40)
print("Classificação para divisão de Natação")
print("==" * 40)

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
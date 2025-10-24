# Alistamento militar
from datetime import date

ano = int(input("\033[0;43mDigite seu ano de nascimento:\033[m "))
idade = date.today().year - ano
alist = 18 + ano

if idade < 18:
    print(f"Voce não tem que se alistar por enquanto pois tem {idade} anos.\nTerá que se alistar em {alist}, daqui {18 - idade} ano(s)")
elif idade == 18:
    print(f"Voce tem que se alistar O QUANTO ANTES, pois você tem 18 anos por ter nascido em {ano}.\nBoa sorte, soldado!")
else:
    print(f"Você tem {idade} anos e seu ano de alistamento já passou em {alist}, há {idade - 18} ano(s) atrás.\nCaso não tenha se alistado regularize sua situação em uma junta militar!")
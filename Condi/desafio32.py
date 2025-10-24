# Ano bissexto ou não
import datetime

ano = int(input("Digite um ano da história (0 para o atual): "))

if ano == 0:
    ano = datetime.date.today().year

""" if ano % 4 == 0 and not ano % 100 == 0 or ano % 100 == 0 and ano % 400 == 0 :
    print(f"O ano {ano} é bissexto, com 366 dias") """
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto, com 366 dias")
else:
    print(f"O ano {ano} é normal, com 365 dias")
# Arquivo: desafio101
def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade < 70:
        return f"Com {idade} anos: voto é OBRIGATÓRIO"
    elif idade >= 70:
        return f"Com {idade} anos: voto é OPCIONAL"
    else:
        return f"Com {idade} anos: voto é NEGADO"

#Programa principal
nasc = int(input("Digite seu ano de nascimento a seguir: "))
print(voto(nasc))    
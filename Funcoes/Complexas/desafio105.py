# Arquivo: desafio105
def notas(* notas, sit = False):
    """
    -> funcao para analisar notas e situações de alunos:
    param n: uma ou mais notas do aluno (aceita várias);
    para sit: valor opcional, indicando se deve ou não adicionar a situação;
    return: dicionário com várias informações sobre a situação do aluno
    """
    r = {}
    r["total"] = len(notas)
    r["menor"] = min(notas)
    r["maior"] = max(notas)
    r["media"] = sum(notas)/len(notas)
    
    if sit == True:
        if r['media'] >= 6.0:
            r["situacao"] = "Aprovado"
        else:
            r["situacao"] = "reprovado"
    
    return r

resp = notas(5.5, 9.5, 8, 6, sit = True)
print(resp)
#APRIMORE ESSE EXERCICIO
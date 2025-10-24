# Arquivo: dicionario com aprovação de notas de escola

aluno = dict()

aluno["nome"]= input("Nome: ")
aluno["media"] = float(input(f"Média de {aluno["nome"]}: "))

if aluno["media"] >= 7:
    aluno["situacao"] = "aprovado"
else:
    aluno["situacao"] = "reprovado"

print(f"A situação de {aluno['nome']} é {aluno['situacao']}")
    
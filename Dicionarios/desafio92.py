# Arquivo: desafio92
dados = dict()

dados['nome'] = input("Digite seu nome: ")
dados['idade'] = int(input("Digite sua idade: "))
dados['CTPS'] = int(input("Digite sua CTPS (0 - não tem): "))

if dados['CTPS'] != 0:
    dados['contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Qual é o salário? R$"))
    dados['aposentadoria por tempo de servico'] = dados['idade'] + 35
print("==" * 20)
for k, v in dados.items():
    print(f"{k} é igual a {v}")
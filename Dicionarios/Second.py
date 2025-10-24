pessoas = {"Nome": "Gustavo", "sexo" : "M", "idade" : 22}
print(pessoas)
print(f'O {pessoas['Nome']} tem {pessoas['idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas["sexo"]
#Aqui eu utilizaria enumerate para tuplas e listas...
for k,v in pessoas.items():
    print(f"{k} = {v}")
pessoas["Nome"] = "Leandro"
pessoas["peso"] = 98.5
for k,v in pessoas.items():
    print(f"{k} = {v}")
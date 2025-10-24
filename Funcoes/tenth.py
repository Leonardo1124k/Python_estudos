def teste(b = 0):
    global a # para não criar duas variaveis com mesmo nome no codigo (local,global)
    a = 8
    b += 4
    c = 2
    print(f"A dentro = {a}")
    print(f"B dentro = {b}")
    print(f"C dentro = {c}")

a = 0
teste(a)
a = 5
print(f"A fora vale {a}")

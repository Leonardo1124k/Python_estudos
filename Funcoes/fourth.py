def soma(* val): # Multiplos parametros
    s = 0
    for num in val: 
        s += num
    print(f"Somando os valores {val} temos {s}")

soma(5,2) # Argumentos
soma(5,2,5)
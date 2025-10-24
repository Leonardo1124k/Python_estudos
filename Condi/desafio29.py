vel = int(input("Qual a velocidade do carro (km/h)? "))

if vel <= 80:
    print("Está tudo certo! Mantenha a velocidade.")
else:
    pay = (vel - 80) * 7
    print(f"Voce foi multado! Terás que pagar R${pay:.2f}")
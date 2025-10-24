# Viajem cobrança por passagem

viagem = float(input("Digite a distância da sua viagem (km): "))

if viagem <= 200:
    ticket = viagem * 0.50
    print(f"Sua viagem irá custar R${ticket:.2f}")
else:
    ticket = viagem * 0.45
    print(f"Sua viagem irá custar R${ticket:.2f}")
# Arquivo: Teste IMC

print("==" * 30)
print("CÁLCULO DE IMC (INDICE DE MASSA CORPORAL)")
print("==" * 30)

peso = float(input("Digite seu peso (kg): "))
alt = float(input("Digite sua altura (m): "))

imc = peso / (alt ** 2) 

if imc < 18.5:
    print(f"Voce está abaixo do peso. IMC = {imc:.1f}")
elif imc <= 25:
    print(f"Voce está com o peso ideal. IMC = {imc:.1f}")
elif imc <= 30:
    print(f"Voce está com sobrepeso. IMC = {imc:.1f}")
elif imc <= 40:
    print(f"Voce está obeso. IMC = {imc:.1f}")
else:
    print(f"VOCE ESTÁ COM OBESIDADE MÓRBIDA. IMC = {imc:.1f}")
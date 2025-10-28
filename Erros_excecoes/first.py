try: 
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    c = a/b
except (ValueError, TypeError):
    print("Infelizmente tivemos um problema com os tipos de dados...")
except ZeroDivisionError:
    print("Não é possivel dividir um numero por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {c:.2f}")
finally:
    print("Volte sempre! Obrigado")
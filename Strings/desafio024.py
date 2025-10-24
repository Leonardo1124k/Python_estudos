city = input("Digite o nome de uma cidade: ").strip()

if city[:5].upper() == "SANTO":
    print("A cidade começa com o nome Santo.")
else:
    print("A cidade NÃO começa com Santo.")
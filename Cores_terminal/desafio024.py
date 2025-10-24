city = input("\033[0;35mDigite o nome de uma cidade: \033[m").strip()

if city[:5].upper() == "SANTO":
    print("A cidade começa com o nome Santo.")
else:
    print("A cidade NÃO começa com Santo.")
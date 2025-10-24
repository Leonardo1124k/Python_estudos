filme = {"titulo": "Star Wars",
          "ano": 1977,
          "diretor": "George"
}

print(filme.values())

print(filme.keys())

print(filme.items())

print()
for k, v in filme.items():
    print(f"O {k} é {v}")
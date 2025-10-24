emails_inscritos = [
    "ana@email.com", "bruno@email.com", "ana@email.com",
    "carla@email.com", "davi@email.com"
]

# Remove duplicatas automaticamente
emails_unicos = set(emails_inscritos)

# Novo lote de inscrições
novos_emails = {"carla@email.com", "eduardo@email.com"}

# Verifica quem é realmente novo
novos_cadastros = novos_emails - emails_unicos

print("E-mails únicos antigos:", emails_unicos)
print("Novos cadastros:", novos_cadastros)

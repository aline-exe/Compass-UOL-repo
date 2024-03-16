def conta_vogais(texto: str) -> int:
    vogais = "aeiou"

    vogais_encontradas = filter(lambda caractere: caractere in vogais, texto.lower())
    return len(list(vogais_encontradas))


resultado = conta_vogais("Exemplo")
print(resultado)

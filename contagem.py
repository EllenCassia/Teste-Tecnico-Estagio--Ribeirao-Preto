def contar_letra_a(texto):
    contagem = texto.lower().count('a')
    return contagem

texto = input("Digite uma string para contar a letra 'a': ")
contagem = contar_letra_a(texto)
print(f"A letra 'a' aparece {contagem} vez(es) na string.")

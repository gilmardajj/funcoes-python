# for i in "rafael":
#     print(i)

# for i in "rafael":
#     if i in "aeiou":
#         print(i)

def contar_vogais(texto):
    """Função que recebe um texto e retorna o número de vogais presentes nele."""
    contador = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador += 1
    return contador


if __name__ == "__main__":
    texto = input("Digite um texto: ")
    numero_vogais = contar_vogais(texto)
    print(f"O número de vogais no texto é: {numero_vogais}")
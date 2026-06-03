def par_ou_impar(numero):
    """Função que recebe um número e retorna se ele é par ou ímpar."""
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    

# print(par_ou_impar(5))
# print(par_ou_impar(8))


# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         print("impar")
#     else:
#         print("par")



if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    resultado = par_ou_impar(numero)
    print(f"O número {numero} é {resultado}.")
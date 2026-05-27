def par_ou_impar(numero):
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




numero = int(input("Digite um número: "))
resultado = par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")
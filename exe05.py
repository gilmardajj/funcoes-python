def calculadora(a, b, operacao):
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

# Exemplo de uso da função
resultado = calculadora(4, 2, "soma")
print(f"O resultado da operação é: {resultado}")


# Ou

# def calculadora(a, b, operacao):
#     if operacao == "+":
#         print(f"O resultado da soma é: {a + b}")
#     elif operacao == "-":
#         print(f"O resultado da subtração é: {a - b}")
#     elif operacao == "*":
#         print(f"O resultado da multiplicação é: {a * b}")
#     elif operacao == "/":
#         if b != 0:
#             print(f"O resultado da divisão é: {a / b}")
#         else:
#             print("Erro: Divisão por zero")
#     else:
#         print("Operação inválida")

# # Exemplo de uso da função
# calculadora(4, 2, "+")



# ou

# def calculadora(a, b, operacao):
#     if operacao == "+":
#         result = a + b
#     elif operacao == "-":
#         result = a - b
#     elif operacao == "*":
#         result = a * b
#     else:
#         result = a / b 
#     return result   

# print(calculadora(4, 2, "+"))
# print(calculadora(4, 2, "-"))
# print(calculadora(4, 2, "*"))
# print(calculadora(4, 2, "/"))

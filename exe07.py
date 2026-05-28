def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# print(fatorial(5))

num = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {num} é: {fatorial(num)}")


# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# print(fatorial(4))

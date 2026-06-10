def contador_regressivo(n):
# Caso Base: quando n for menor que 0, a função para de chamar a si mesma
    if n < 0:
        return
    
# Exibe o número atual
    print(n)
    
# Caso Recursivo: chama a função novamente subtraindo 1 de n
    contador_regressivo(n - 1)
    

if __name__ == "__main__":
# Teste do exemplo
    contador_regressivo(5)
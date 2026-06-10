def media_lista(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

if __name__ == "__main__":

# Lista que vai guardar os números inseridos pelo usuário
    numeros_digitados = []

    print("--- Calculadora de Média Interativa ---")
    print("Digite os números um por um. Quando quiser parar, digite 'sair'.\n")

    while True:
# Captura a entrada do usuário, remove espaços e transforma em minúsculo
        entrada = input("Digite um número (ou 'sair'): ").strip().lower()
        
# Condição de saída
        if entrada == 'sair':
            break
        
# Tratamento de erro: tenta converter para número, se não conseguir, avisa o usuário
        try:
            numero = float(entrada)
            numeros_digitados.append(numero)
        except ValueError:
            print("Opção inválida! Digite um número válido ou 'sair'.")

# Fora do laço, calcula a média se a lista não estiver vazia
    if numeros_digitados:
        resultado = media_lista(numeros_digitados)
        print("\n---------------------------------------")
        print(f"Você digitou {len(numeros_digitados)} número(s).")
        print(f"A média final é: {resultado}")
        print("---------------------------------------")
    else:
        print("\nNenhum número foi digitado para calcular a média.")
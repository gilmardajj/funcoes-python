import exe01
import exe02
import exe03
import exe04
import exe05
import exe06
import exe07

while True:
    print("Menu de Exercícios:")
    print("1. Saudação")
    print("2. Soma de dois números")
    print("3. Verificar se um número é par ou ímpar")
    print("4. Encontrar o maior número entre dois números")
    print("5. Calculadora simples")
    print("6. Contar o número de vogais em um texto")
    print("7. Calcular o fatorial de um número")
    print("0. Sair")

    escolha = input("Digite o número do exercício que deseja executar: ")

    if escolha == "1":
        nome=input("Digite seu nome: ")
        print(exe01.saudacao(nome))

    elif escolha == "2":
        a=int(input("Digite o primeiro número: "))
        b=int(input("Digite o segundo número: "))
        print(f"O resultado da soma é: {exe02.somar(a, b)}")

    elif escolha == "3":
        numero = int(input("Digite um número: "))
        resultado = exe03.par_ou_impar(numero)  
        print(f"O número é: {resultado}")

    elif escolha == "4":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print(f"O maior número é: {exe04.maior_numero(a, b)}")

    elif escolha == "5":
        resultado = int(input("Digite o primeiro número: "))
        resultado2 = int(input("Digite o segundo número: "))
        operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
        resultado_final = exe05.calculadora(resultado, resultado2, operacao)
        print(f"O resultado da operação é: {resultado_final}")

    elif escolha == "6":
        texto = input("Digite um texto: ")
        numero_vogais = exe06.contar_vogais(texto)
        print(f"O número de vogais no texto é: {numero_vogais}")

    elif escolha == "7":
        num = int(input("Digite um número para calcular o fatorial: "))
        print(f"O fatorial de {num} é: {exe07.fatorial(num)}")

    elif escolha == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

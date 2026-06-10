def login(usuario, senha):
# Verifica se as duas condições são verdadeiras ao mesmo tempo
    if usuario == "admin" and senha == "1234":
        return "Acesso permitido"
    else:
        return "Acesso negado"

if __name__ == "__main__":
# Exemplos de teste
    print(login("admin", "1234"))      # Saída: Acesso permitido
    print(login("admin", "errada"))    # Saída: Acesso negado
    print(login("usuario", "1234"))    # Saída: Acesso negado
def palindromo(texto):
# Remove espaços em branco e transforma tudo em minúsculo
# Isso garante que "Radar " ou "Amor a Roma" funcionem corretamente
    texto_limpo = texto.replace(" ", "").lower()
    
# Compara o texto limpo com ele mesmo invertido [::-1]
    return texto_limpo == texto_limpo[::-1]

if __name__ == "__main__":
# Exemplos de teste
    print(palindromo("radar"))  # Saída: True
    print(palindromo("Python")) # Saída: False
    print(palindromo("Ovo"))    # Saída: True (O minúsculo/maiúsculo foi tratado)
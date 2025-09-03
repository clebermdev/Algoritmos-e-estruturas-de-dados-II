def cifrar_cesar(frase, deslocamento):
    resultado = ""
    
    for caractere in frase:
        # Verifica se o caractere é uma letra
        if caractere.isalpha():
            # Determina o código ASCII base (a ou A)
            base = ord('a') if caractere.islower() else ord('A')
            # Aplica o deslocamento e calcula a nova letra
            nova_letra = chr((ord(caractere) - base + deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            # Mantém caracteres não alfabéticos inalterados
            resultado += caractere
            
    return resultado

# Perguntar ao usuário pela frase cifrada
frase_cifrada = input("Digite a frase cifrada: ")

# Tentar todas as 26 possibilidades de cifra de César
tentativas = []
for i in range(1, 27):
    frase_tentativa = cifrar_cesar(frase_cifrada, i)
    tentativas.append(frase_tentativa)
    print(f"Tentativa com deslocamento {i}: {frase_tentativa}")

# Perguntar ao usuário qual é a tentativa correta
numero_tentativa = int(input("Digite o número da descifragem correta (1-26): "))

# Verificar se o número está dentro do intervalo válido
if 1 <= numero_tentativa <= 26:
    print(f"\nFrase Decifrada Correta: {tentativas[numero_tentativa - 1]}")
else:
    print("Número inválido! Por favor, escolha um número entre 1 e 26.")
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

# Função principal para decifrar a frase cifrada
def decifrar_frase(frase_cifrada):
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
        return tentativas[numero_tentativa - 1], numero_tentativa  # Retorna também o deslocamento escolhido
    else:
        print("Número inválido! Por favor, escolha um número entre 1 e 26.")
        return None, None

# Loop principal do programa
while True:
    # Perguntar pela frase cifrada
    frase_cifrada = input("Digite a frase cifrada: ")
    
    # Decifrar a frase e obter o resultado correto
    resultado_decifrado, deslocamento_usado = decifrar_frase(frase_cifrada)

    # Verifica se o resultado é válido antes de continuar
    if resultado_decifrado is not None:
        print(f"\nFrase Decifrada Correta: {resultado_decifrado}")
        
        # Perguntar se deseja usar esse resultado em outras frases
        while True:
            continuar = input("Deseja usar esse resultado em outras frases? (sim/não): ").strip().lower()
            
            if continuar != 'sim':
                print("Programa encerrado.")
                break
            
            # Solicitar nova frase cifrada e decifrar novamente usando o mesmo método
            nova_frase_cifrada = input("Digite a nova frase cifrada: ")
            novo_resultado_decifrado = cifrar_cesar(nova_frase_cifrada, deslocamento_usado)  # Usando o mesmo deslocamento
            
            print(f"\nFrase Decifrada Correta: {novo_resultado_decifrado}")
        
        break  # Encerra o programa após sair do loop interno
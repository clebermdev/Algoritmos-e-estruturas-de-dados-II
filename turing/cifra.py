def cifra_de_cesar(frase, chave):
    resultado = ""
    
    for caractere in frase:
        # Verifica se o caractere é uma letra maiúscula
        if caractere.isupper():
            resultado += chr((ord(caractere) + chave - 65) % 26 + 65)
        # Verifica se o caractere é uma letra minúscula
        elif caractere.islower():
            resultado += chr((ord(caractere) + chave - 97) % 26 + 97)
        # Verifica se o caractere é um dígito
        elif caractere.isdigit():
            resultado += chr((ord(caractere) + chave - 48) % 10 + 48)
        else:
            # Mantém os caracteres não alfabéticos e não numéricos inalterados
            resultado += caractere
            
    return resultado

# Função principal
def main():
    # Solicitar ao usuário a frase e a chave
    frase_original = input("Digite a frase que deseja criptografar: ")
    chave = int(input("Digite a chave de deslocamento (número inteiro): "))
    
    # Criptografar a frase
    frase_criptografada = cifra_de_cesar(frase_original, chave)

    # Exibir os resultados
    print("\nFrase Original: ", frase_original)
    print("Frase Criptografada: ", frase_criptografada)

# Executar a função principal
if __name__ == "__main__":
    main()
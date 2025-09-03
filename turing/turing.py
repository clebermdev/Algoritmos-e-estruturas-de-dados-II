def substituir_letra(frase, letra_original, letra_substituta):
    resultado = ""
    
    for caractere in frase:
        # Substitui a letra original pela letra substituta
        if caractere == letra_original:
            resultado += letra_substituta
        else:
            resultado += caractere
            
    return resultado

# Frase original
frase_original = "Ongngvaun dhnaqb anfpr, rfcneenzn cryb punb."

# Imprimir a frase original antes de entrar no loop
print("Frase Original: ", frase_original)

# Inicializa a frase resultante com a frase original
frase_resultante = frase_original

while True:
    # Imprimir a frase resultante atual
    print("\nFrase Atual: ", frase_resultante)
    
    # Solicitar ao usuário a letra a ser substituída e a nova letra
    letra_original = input("Digite a letra que deseja substituir (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja sair
    if letra_original.lower() == 'sair':
        print("Saindo do programa.")
        break
    
    letra_substituta = input("Digite a nova letra: ")

    # Aplicar a substituição
    frase_resultante = substituir_letra(frase_resultante, letra_original, letra_substituta)

# Imprimir o resultado final
print("\nFrase Final: ", frase_resultante)


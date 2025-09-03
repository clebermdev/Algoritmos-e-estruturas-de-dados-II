def substituir_letra(frase, substituicoes):
    resultado = ""
    
    for caractere in frase:
        # Substitui a letra original pela letra substituta se existir no dicionário
        if caractere in substituicoes:
            resultado += substituicoes[caractere]
        else:
            resultado += caractere
            
    return resultado

# Dicionário de substituições fornecido
substituicoes = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm'
}

# Inversão do dicionário para decifrar
substituicoes_invertidas = {v: k for k, v in substituicoes.items()}

# Perguntar ao usuário pela frase cifrada
frase_cifrada = input("Digite a frase cifrada: ")

# Decifrar a frase
frase_decifrada = substituir_letra(frase_cifrada, substituicoes_invertidas)

# Imprimir a frase cifrada e a frase decifrada
print("Frase Cifrada: ", frase_cifrada)
print("Frase Decifrada: ", frase_decifrada)
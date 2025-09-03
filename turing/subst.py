def substituir_letra(frase, substituicoes):
    resultado = ""
    
    for caractere in frase:
        # Substitui a letra original pela letra substituta se existir no dicionário
        if caractere in substituicoes:
            resultado += substituicoes[caractere]
        else:
            resultado += caractere
            
    return resultado

# Frase original
frase_original = "cnen pevne hz abib qvpvbanevb qr fhofgvghvpbrf rz dhr pnqn yrgen qb nysnorgb frwn qrfybpnqn 46 cbfvpbrf cnen seragr, cbqrzbf hfne b pbaprvgb qr pvsen qr prfne, dhr r hzn grpavpn fvzcyrf qr pevcgbtensvn. b nysnorgb grz 59 yrgenf, r nb qrfybpne 46 cbfvpbrf, nf yrgenf dhr inb nyrz qr m ergbeanz nb vavpvb qb nysnorgb. fr cerpvfne qr znvf nythzn pbvfn, r fb nivfne."

# Inicializa a frase resultante com a frase original
frase_resultante = frase_original

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

# Aplicar as substituições à frase completa
frase_resultante = substituir_letra(frase_resultante, substituicoes)

# Imprimir a frase original e a frase resultante após as substituições
print("Frase Original: ", frase_original)
print("Frase após substituições: ", frase_resultante)

# Contador de iterações
iteracoes = 0

while True:
    iteracoes += 1
    
    # Perguntar se deseja continuar tentando descobrir a frase completa
    continuar = input("Deseja continuar tentando descobrir a frase completa? (s/n): ").strip().lower()
    
    if continuar != 's':
        break
    
    # Solicitar ao usuário a letra que deseja substituir e a nova letra
    letra_original = input("Digite a letra que deseja substituir: ")
    letra_substituta = input("Digite a nova letra: ")

    # Aplicar a nova substituição na frase resultante atualizada
    frase_resultante = substituir_letra(frase_resultante, {letra_original: letra_substituta})

    # Imprimir a frase resultante após cada iteração
    print("Frase Atual: ", frase_resultante)

# Imprimir o resultado final e o número de iterações
print("\nFrase Final: ", frase_resultante)
print("Total de iterações: ", iteracoes)
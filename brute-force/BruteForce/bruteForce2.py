import time
import itertools

# Tempo de início
start_time = time.time()

password = 'senhas'  # Senha de exemplo
tentativas = 0

# Gera todas as combinações possíveis de strings de 6 letras minúsculas
combinacoes = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=6)

for tentativa in combinacoes:
    tentativas += 1
    if ''.join(tentativa) == password:
        print(f"Senha encontrada: {password}")
        print(f"Número de tentativas: {tentativas}")
        break

# Tempo de término
end_time = time.time()

# Tempo de execução
tempo_execucao = end_time - start_time
print(f"Tempo de execução: {tempo_execucao:.4f} segundos")

import time

# Tempo de início
start_time = time.time()

password = 22334455
tentativas = 0

for i in range(100000000):
    tentativas += 1
    if i == password:
        print(f"Senha encontrada: {password}")
        print(f"Número de tentativas: {tentativas}")
        break

# Tempo de término
end_time = time.time()

# Tempo de execução
tempo_execucao = end_time - start_time
print(f"Tempo de execução: {tempo_execucao:.4f} segundos")

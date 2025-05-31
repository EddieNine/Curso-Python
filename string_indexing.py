# Exemplo base: Número de cartão de crédito fictício
credit_number = "1234-5678-9012-3456"

# 1. Acessando um único caractere (indexação simples)
print(credit_number[0])  # Saída: '1' (1º caractere, índice 0)
print(credit_number[1])  # Saída: '2' (índice 1)
print(credit_number[4])  # Saída: '-' (índice 4)

# 2. Acessando um intervalo (slice) - primeiros 4 dígitos
print(credit_number[0:4])  # Saída: '1234'
print(credit_number[:4])   # Também funciona sem o índice inicial (começa do início)

# 3. Pegando o segundo grupo de dígitos: '5678'
print(credit_number[5:9])  # Saída: '5678' (índice 5 até 8)

# 4. Pegando os últimos 12 caracteres (omitindo os 4 primeiros)
print(credit_number[5:])   # Saída: '5678-9012-3456' (começa no índice 5 até o fim)

# 5. Indexação negativa - contar de trás para frente
print(credit_number[-1])   # Saída: '6' (último caractere)
print(credit_number[-2])   # Saída: '5'
print(credit_number[-5])   # Saída: '-' (quinto a partir do final)

# 6. Usando passo (step) - pulando caracteres
print(credit_number[::2])  # Saída: '13-68 012356' (a cada 2 caracteres)
print(credit_number[::3])  # Saída: '1461-35' (a cada 3 caracteres)

# 7. Últimos 4 dígitos (usando índices negativos)
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")  # Saída: XXXX-XXXX-XXXX-3456

# 8. Revertendo uma string
credit_number = credit_number[::-1]
print(credit_number)  # Saída: '6543-2109-8765-4321'

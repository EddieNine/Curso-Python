# Inicializamos as variáveis com valores padrão
principle = 0
rate = 0
time = 0

# Laço para garantir que o usuário digite um valor inicial válido
while True:
    principle = float(input("Digite o valor inicial (R$): "))
    if principle < 0:
        print("O valor inicial não pode ser menor que zero.")
    else:
        break  # Sai do loop se o valor for válido

# Laço para garantir que a taxa de juros seja válida
while True:
    rate = float(input("Digite a taxa de juros (%): "))
    if rate < 0:
        print("A taxa de juros não pode ser negativa.")
    else:
        break  # Sai do loop se a taxa for válida

# Laço para garantir que o tempo (em anos) seja válido
while True:
    time = int(input("Digite o tempo em anos: "))
    if time < 0:
        print("O tempo não pode ser negativo.")
    else:
        break  # Sai do loop se o tempo for válido

# Cálculo do montante com juros compostos usando a fórmula:
# A = P * (1 + r/100)^t
total = principle * pow((1 + rate / 100), time)

# Exibição do valor final formatado com duas casas decimais
print(f"Saldo após {time} ano(s): R$ {total:.2f}")

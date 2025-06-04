# Criando três variáveis com valores decimais
price1 = 3.14159
price2 = -987.65
price3 = 12.34

# Exibindo os valores sem formatação
print(f"Preço 1 (sem formatação): {price1}")
print(f"Preço 2 (sem formatação): {price2}")
print(f"Preço 3 (sem formatação): {price3}")

# Formatando os valores com duas casas decimais
# .2f => mostra 2 casas decimais e trata o número como ponto flutuante
print(f"Preço 1 (formatado): {price1:.2f}")
print(f"Preço 2 (formatado): {price2:.2f}")
print(f"Preço 3 (formatado): {price3:.2f}")

# Alocando espaço de 10 caracteres com alinhamento à direita
# 10.2f => total de 10 espaços, 2 decimais
print(f"Preço 1 (10 espaços): {price1:10.2f}")
print(f"Preço 2 (10 espaços): {price2:10.2f}")
print(f"Preço 3 (10 espaços): {price3:10.2f}")

# Alinhando à esquerda usando sinal de menor (<)
print(f"Preço 1 (alinhado à esquerda): {price1:<10.2f}")
print(f"Preço 2 (alinhado à esquerda): {price2:<10.2f}")
print(f"Preço 3 (alinhado à esquerda): {price3:<10.2f}")

# Centralizando o valor no espaço
print(f"Preço 1 (centralizado): {price1:^10.2f}")
print(f"Preço 2 (centralizado): {price2:^10.2f}")
print(f"Preço 3 (centralizado): {price3:^10.2f}")

# Preenchendo com zeros à esquerda
print(f"Preço 1 (zero padding): {price1:010.2f}")
print(f"Preço 2 (zero padding): {price2:010.2f}")
print(f"Preço 3 (zero padding): {price3:010.2f}")

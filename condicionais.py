#  Exemplo 1: Número Positivo ou Negativo
num = 5
print("Positivo" if num > 0 else "Negativo")

# Exemplo 2: Par ou Ímpar
num = 6
resultado = "Par" if num % 2 == 0 else "Ímpar"
print(resultado)

# Exemplo 3: Maior e Menor entre dois números
a = 6
b = 7
maior = a if a > b else b
menor = a if a < b else b

# Exemplo 4: Verificar idade
idade = 25
status = "Adulto" if idade >= 18 else "Criança"
print(status)

# Exemplo 5: Clima com Temperatura
temp = 30
clima = "Quente" if temp > 20 else "Frio"
print(clima)

# Exemplo 6: Acesso de usuário
user = "admin"
acesso = "Acesso total" if user == "admin" else "Acesso limitado"
print(acesso)


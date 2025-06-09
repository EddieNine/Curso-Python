# Exemplo 1: Contador de 1 até 5
contador = 1

while contador <= 5:
    print("Contando:", contador)
    contador += 1  # Atualiza o contador para evitar loop infinito

print("Fim do contador!\n")

# Exemplo 2: Cuidado com loop infinito
# Esse código está comentado porque causaria loop infinito!
# contador = 1
# while contador <= 5:
#     print("Contando:", contador)
#     # contador += 1 ← está faltando isso!

# Exemplo 3: Validando entrada do usuário
resposta = ""

while resposta != "sim" and resposta != "não":
    resposta = input("Você quer continuar? (sim/não): ").lower()

print("Resposta recebida:", resposta, "\n")

# Exemplo 4: Somando números até o usuário digitar 0
soma = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para sair): "))

print("Soma total:", soma)

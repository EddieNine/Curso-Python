# ✅ 1. Contando de 1 a 10 com for e range()
for x in range(1, 11):  # range vai de 1 até 10 (11 é exclusivo)
    print(x)  # imprime o valor atual de x

# ✅ 2. Contando com uma variável nomeada diferente
for contador in range(1, 11):
    print(contador)  # imprime o contador de 1 a 10

# ✅ 3. Contagem Regressiva com reversed()
for x in reversed(range(1, 11)):  # conta de 10 até 1
    print(x)
print("Feliz Ano Novo!")  # mensagem final fora do loop

# ✅ 4. Contando de 2 em 2 com passo (step)
for x in range(1, 11, 2):  # começa em 1, vai até 10, pulando de 2 em 2
    print(x)  # imprime: 1, 3, 5, 7, 9

# ✅ 5. Contando de 3 em 3
for x in range(1, 11, 3):  # começa em 1, vai até 10, pulando de 3 em 3
    print(x)  # imprime: 1, 4, 7, 10

# ✅ 6. Iterando sobre uma string
cartao = "1234-5678"
for x in cartao:
    print(x)  # imprime cada caractere: números e o "-"

# ✅ 7. Usando 'continue' para pular o número 13
for x in range(1, 21):  # de 1 a 20
    if x == 13:
        continue  # pula o número 13
    print(x)  # imprime todos, menos o 13

# ✅ 8. Usando 'break' para parar no número 13
for x in range(1, 21):  # de 1 a 20
    if x == 13:
        break  # encerra o loop ao chegar no 13
    print(x)  # imprime de 1 a 12

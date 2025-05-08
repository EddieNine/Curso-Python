nome = "Edcarlos"
idade = 26
media = 1.9
estudante = True

# saber o tipo de uma variável
print(type(nome))

# Converter idade para float:
idade = float(idade)
print(idade)
print(type(idade))

# Converter media para inteiro:
media = int(media)
print(media)

# Converter booleano estudante para string:
estudante = str(estudante)
print(estudante)
print(type(estudante))

# Converter número em booleano:
idade = bool(idade)
print(idade)

# conversão implícita.
x = 2  # int
y = 2.0  # float
x = x / y  # divisão
print(x)

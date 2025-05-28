# Solicita o nome completo do usuário
name = input("Enter your full name: ")

# Obtém o comprimento da string (número de caracteres)
result = len(name)
print("Length:", result)

# Encontra a primeira ocorrência de um espaço
result = name.find(" ")
print("First space at index:", result)

# Encontra a primeira ocorrência da letra 'B'
result = name.find("B")
print("First 'B' at index:", result)

# Encontra a primeira ocorrência da letra 'o'
result = name.find("o")
print("First 'o' at index:", result)

# Encontra a última ocorrência da letra 'o'
result = name.rfind("o")
print("Last 'o' at index:", result)

# Tenta encontrar um caractere inexistente ('q')
result = name.find("q")
print("First 'q' at index (should be -1):", result)

# Capitaliza a primeira letra da string
name = name.capitalize()
print("Capitalized:", name)

# Transforma todos os caracteres em maiúsculos
name = name.upper()
print("Uppercase:", name)

# Transforma todos os caracteres em minúsculos
name = name.lower()
print("Lowercase:", name)

# Verifica se a string contém apenas dígitos
result = name.isdigit()
print("Is digit only?:", result)

# Verifica se a string contém apenas letras (sem espaços ou números)
result = name.isalpha()
print("Is alphabetic only?:", result)

# Solicita um número de telefone ao usuário
phone_number = input("Enter your phone number: ")

# Conta quantos traços existem no número de telefone
result = phone_number.count("-")
print("Number of dashes:", result)

# Substitui os traços por espaços
phone_number = phone_number.replace("-", " ")
print("Phone number with spaces:", phone_number)

# Remove todos os traços do número de telefone
phone_number = phone_number.replace("-", "")
print("Phone number without dashes:", phone_number)

# Mostra todos os métodos disponíveis para strings
print(help(str))

# Valida um nome de usuário
username = input("Enter a user name: ")

# Regra 1: Nome de usuário não pode ter mais de 12 caracteres
if len(username) > 12:
    print("Your username can't be more than 12 characters.")
# Regra 2: Nome de usuário não pode conter espaços
elif username.find(" ") != -1:
    print("Your username can't contain spaces.")
# Regra 3: Nome de usuário não pode conter números
elif not username.isalpha():
    print("Your username can't contain numbers.")
else:
    print(f"Welcome {username}!")

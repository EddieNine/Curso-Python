# Programa Email Slicer em Python
# Objetivo: separar o nome do usuário e o domínio de um email digitado pelo usuário

# Solicita o email do usuário
email = input("Digite seu email: ")  # Exemplo: bro123@gmail.com

# Encontra o índice do caractere '@' dentro da string email
at_index = email.index("@")

# Separa o nome do usuário (tudo antes do '@')
username = email[:at_index]  # Pega do início da string até o índice do '@' (não incluso)

# Separa o domínio (tudo depois do '@')
domain = email[at_index + 1:]  # Pega a partir do caractere logo após o '@' até o final da string

# Exibe o resultado formatado
print(f"Seu username é: {username}")
print(f"Seu domínio é: {domain}")


print(f"Usuario: {email[:email.index('@')]}")
print(f"Dominio: {email[email.index('@')+1:]}")
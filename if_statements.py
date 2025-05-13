if True:
    print("Isso será executado!")

# Verificação de idade
idade = 18

if idade >= 100:
    print("Você é muito velho para se cadastrar.")
elif idade < 0:
    print("Você ainda nem nasceu!")
elif idade >= 18:
    print("Você está cadastrado!")
else:
    print("Você precisa ter 18 anos ou mais para se cadastrar.")

# Comparando valores com ==
response = input("Você quer comida? (y/n): ")

if response == "y":
    print("Aqui está sua comida!")
else:
    print("Sem comida pra você.")

# Verificando strings vazias
name = input("Digite seu nome: ")

if name == "":
    print("Você não digitou seu nome!")
else:
    print(f"Olá, {name}!")

# Usando variáveis booleanas com if
item = True

if item:
    print("Este item está à venda.")
else:
    print("Este item não está à venda.")

online = False

if online:
    print("Usuário está online.")
else:
    print("Usuário está offline.")


# Exercicio
nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")






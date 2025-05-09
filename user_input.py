# Entrada o usuario
name = input("Qual o seu nome? ")
print(f"Olá, {name}")

age = int(input("Qual a sua idade? "))
print(age + 1)

# Exercício 1 – Mad Libs
adjective1 = input("Digite um adjetivo: ")
noun = input("Digite um substantivo: ")
adjective2 = input("Digite outro adjetivo: ")
verb = input("Digite um verbo: ")
adjective3 = input("Digite mais um adjetivo: ")

print(f"O {adjective1} {noun} é muito {adjective2} quando decide {verb}. Isso deixa todo mundo {adjective3}!")

# Exercício 2 – Área e Volume
length = float(input("Digite o comprimento em cm: "))
width = float(input("Digite a largura em cm: "))

area = length * width
print(f"A área é {area} cm²")

height = float(input("Digite a altura em cm: "))
volume = length * width * height
print(f"O volume é {volume} cm³")

# Exercício 3 – Carrinho de Compras
item = input("Qual item você está comprando? ")
price = float(input("Qual o preço por unidade? "))
quantity = int(input("Quantas unidades? "))
total = price * quantity
print(f"O total para {quantity}x {item} é R${round(total, 2)}")

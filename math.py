import math

# ➕ 1. Adição
amigos = 0
amigos += 1
print(amigos)

# ➖ 2. Subtração
amigos -= 2
print(amigos)

# ✖️ 3. Multiplicação
amigos = 5
amigos *= 3
print(amigos)

# ➗ 4. Divisão
amigos /= 2
print(amigos)

# 5. Exponenciação
amigos = 5
amigos **= 2
print(amigos)

# 6. Módulo (Resto da Divisão)
amigos = 10
resto = amigos % 3  # Resultado: 1

if amigos % 2 == 0:
    print("Número par!")
else:
    print("Número ímpar!")

# 🔄 1. Arredondamento (round)
x = 3.14
result = round(x)
print(result)

# 🧾 2. Valor Absoluto (abs)
y = -4
result = abs(y)
print(result)

# 💪 3. Potência com pow()
result = pow(4, 3)  # 4³ = 64
print(result)

# 📈 4. Máximo e Mínimo
x = 3.14
y = 4
z = 5

print(max(x, y, z))  # 5
print(min(x, y, z))  # 3.14

# 🔢 1. Constantes
print(math.pi)  # 3.14159...
print(math.e)   # 2.71828...

# ✔️ 2. Raiz quadrada
result = math.sqrt(9)
print(result)  # 3.0

# 📈 3. Arredondamento com ceil() e floor()
x = 9.1
print(math.ceil(x))   # 10 → arredonda para cima
print(math.floor(x))  # 9  → arredonda para baixo

# 🟢 1. Circunferência do Círculo
radius = float(input("Digite o raio do círculo: "))
circumference = 2 * math.pi * radius
print(f"A circunferência é {round(circumference, 2)} cm")

# 🟢 2. Área do Círculo
radius = float(input("Digite o raio do círculo: "))
area = math.pi * pow(radius, 2)
print(f"A área do círculo é {round(area, 2)} cm²")

# 🟢 3. Hipotenusa de um Triângulo Retângulo
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"A hipotenusa é {c}")
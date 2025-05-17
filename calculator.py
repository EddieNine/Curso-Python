operador = input("Digite o operador (+, -, * , /): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2
    print(round(resultado, 3))
elif operador == "-":
    resultado = num1 - num2
    print(round(resultado, 3))
elif operador == "*":
    resultado = num1 * num2
    print(round(resultado, 3))
elif operador == "/":
    if num2 == 0:
        print("Erro! Não é possivel dividir por zero.")
    resultado = num1 / num2
    print(round(resultado, 3))
else:
    print(f"{operador} não é um operador valido.")

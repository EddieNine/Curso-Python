unidade = input("Essa temperatura está em Celsius ou em Fahrenheit (C/F): ").upper()
temperatura = float(input("Digite a temperatura: "))

if unidade == "C":
    temperatura = round((9 * temperatura) / 5 + 32, 1)
    print(f"A temperatura em Fahrenheit é: {temperatura}")
elif unidade == "F":
    temperatura = round((temperatura - 32) * 5 / 9, 1)
    print(f"A temperatura em Celsius é: {temperatura}")
else:
    print(f"{unidade} é uma unidade invalida.")
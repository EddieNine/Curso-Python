peso = float(input("Digite seu peso: "))
unidade = input("Esse peso está (K) ou (L): ")

if unidade == 'K':
    peso = round(peso * 2.205, 1)
    unidade = 'lbs'
    print(f"Seu peso em libras é {peso}")
elif unidade == 'L':
    peso = round(peso / 2.205, 1)
    unidade = 'kgs'
    print(f'Seu peso em quilogramas é {peso}')
else:
    print(f"Unidade {unidade} não é valida.")
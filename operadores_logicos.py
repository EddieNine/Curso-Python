# and
temp = 25
if temp > 0 and temp < 30:
    print("A temperatura está boa.")
else:
    print("A temperatura está ruim.")

# or
if temp <= 0 or temp >= 30:
    print("A temperatura está ruim.")
else:
    print("A temperatura está boa.")

# not
ensolarado = False

if not ensolarado:
    print("Está nublado")
else:
    print("Está ensolarado")
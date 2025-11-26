total = 0
while True:
    numero = int(input("Introduisme el numero (0 pera acabar):"))
    if numero == 0:
        break
    elif numero > 0:
        total += 1
print(f"Has introdut {total} numeros positius")

cantidad = int(input("Introdueix un número: "))
total = 0
while cantidad != 0:
    if cantidad > 100:
        break
    total = total + 1
    cantidad = int(input("Introdueix un altre numero sisplau 🙏🏿s: "))
print(f"S'han introduït {total} números positius.")

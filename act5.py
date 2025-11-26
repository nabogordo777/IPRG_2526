cantidad = int(input("Introdueix un número: "))
total = 0
while cantidad != 0:
    if cantidad > 0:
        total = total + 1
    cantidad = int(input("Introdueix un altre número: "))
print(f"S'han introduït {total} números positius.")

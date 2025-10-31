pes = float(input("Introdueix el teu pes en kg: "))
altura = float(input("Introdueix la teva alçada en metres: "))

imc = pes / (altura ** 2)

if imc < 18.5:
    print(f"El teu IMC és {imc:.2f}. Inferior al pes saludable.")
elif 18.5 <= imc <= 24.9:
    print(f"El teu IMC és {imc:.2f}. Pes saludable.")
else:
    print(f"El teu IMC és {imc:.2f}. Sobreeiximent de pes.")

try:
    num1 = int(input("Introdueix el primer numero:"))
    num2 = int(input("Introdueix el segon numero:"))
    resultat = num1 / num2
    print(f"El resultat de la diisio es: {resultat}")

except ZeroDivisionError:
    print("Error:No es posible dividir entre zero")

except ValueError:
    print("Error:Has de introduir números vàlids")
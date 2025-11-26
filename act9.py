elements = ["poma", "taronja", "poma", "fresa"]
seleccio = None

try:
    pos = int(input("Introdueix una posicio (0-3): "))
    seleccio = elements[pos]
    print(f"L'element a la posicio {pos} és: {seleccio}")

except ValueError:
    print("Error: has d'introduir un numero")

except IndexError:
    print("Error: la posici´o no existeix")

finally:
    print("Intent completat.")
    print(f"Longitud de la llista: {len(elements)}")
    print(f"Valor de seleccio: {seleccio}")
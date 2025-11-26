elements = ["poma", "pera", "taronja", "platano"]
seleccio = None

try:
    pos = int(input("Introdueix una posicio (0-3): "))
    assert 0 <= pos <= 3
    
    seleccio = elements[pos]
    print(f"L'element a la posicio {pos} és: {seleccio}")
except ValueError:
    print("Error: has de posar un numero entero primo 🙏🏿")
except AssertionError:
    print("Error: la posici´o ha d'estar entre 0 i 3.")
    print("✅ Comprovacio finalitzada.")
    print(f"Longitud de la llista: {len(elements)}")
    print(f"Seleccio reiniciada a: {seleccio}")
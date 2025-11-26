print("Classificador d'alumnes per edat i assistencia")
cantidad = int(input("Quants alumnes vol processar? "))
contador = 0
while cantidad > contador:
    nombre = input("Nom: ")
    años = int(input("Edat: "))
    presente = input("Assistencia (S/N): ").lower()

    if presente == "s" or presente == "si":
        situacion = "present"
    else:
        situacion = "absent"

    if años >= 65:
        tipo = "juilat"
    elif años >= 18:
        tipo = "adulto"
    elif años >= 12:
        tipo = "adolescent"
    else:
        tipo = "infantil"

    print(nombre, "-", tipo, "-", situacion)
    contador = contador + 1

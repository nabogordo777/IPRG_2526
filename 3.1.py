ruta = "dades_usuari.txt"

try:
    persona_nom = input("Introdueix el teu nom: ")
    persona_edat = input("Introdueix la teua edat: ")

    document = open(ruta, "w")
    document.write("Nom: " + persona_nom + "\n")
    document.write("Edat: " + persona_edat + "\n")
    document.close()
    
    document = open(ruta, "r")
    lectura = document.read()
    print(lectura)
    document.close()

    persona_ciutat = input("Introdueix la teua ciutat: ")

    document = open(ruta, "a")
    document.write("Ciutat: " + persona_ciutat + "\n")
    document.close()

    document = open(ruta, "r")
    resultat = document.read()
    print(resultat)
    document.close()

except FileNotFoundError:
    print("ERROR: No s'ha trobat el fitxer.")
except PermissionError:
    print("ERROR: No tens permisos per a escriure o llegir aquest fitxer.")
except:
    print("Ha ocorregut un error.")
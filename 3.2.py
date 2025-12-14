ficheros = ["dades_usuari.txt", "arxiu_inventat.txt", "altre_fitxer.txt"]
salida = "fitxer_concatenat.txt"

try:
    doc_salida = open(salida, "w")
    
    indice = 0
    mientras = True
    while mientras:
        if indice >= len(ficheros):
            mientras = False
            break
        
        nom = ficheros[indice]
        
        try:
            doc_entrada = open(nom, "r")
            texto = doc_entrada.read()
            doc_entrada.close()
            
            doc_salida.write(texto)
            doc_salida.write("\n\n")
            
        except FileNotFoundError:
            print(f"El fitxer '{nom}' no existeix. S'ha omitit.")
        except PermissionError:
            print(f"No tens permis per a llegir '{nom}'.")
        
        indice = indice + 1
    
    doc_salida.close()

except:
    print("Ha ocorregut un error general.")
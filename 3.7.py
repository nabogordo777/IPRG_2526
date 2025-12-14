import csv

origen = "notes.csv"
destino = "notes_modificat.csv"

registros = [
    ["Nom", "Assignatura", "Nota"],
    ["Pablo", "Programacio", "7"],
    ["Denis", "Seguretat", "0"],
    ["Jeroni", "Sistemes", "1"]
]

f = open(origen, "w", newline="")
escribir = csv.writer(f)
escribir.writerows(registros)
f.close()

print(f"Fitxer '{origen}' creat per a la prova.\n")

resultado = []

try:
    f = open(origen, "r", newline="")
    leer = csv.reader(f)
    
    print("Contingut del fitxer original")
    contador = 0
    for linea in leer:
        print(linea)
        resultado.append(linea)
        contador = contador + 1
    
    f.close()
    
    nombre = input("Nom de l'alumne: ")
    materia = input("Assignatura: ")
    calificacion = input("Nota: ")
    
    fila = [nombre, materia, calificacion]
    resultado.append(fila)
    
    f = open(destino, "w", newline="")
    escribir2 = csv.writer(f)
    escribir2.writerows(resultado)
    f.close()
        
    print(f"\nDades guardades correctament en '{destino}'.")

except FileNotFoundError:
    print(f"El fitxer '{origen}' no existeix.")
except:
    print(f"Error inesperat.")
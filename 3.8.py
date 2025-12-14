import json
import csv
import os
import shutil

json_f = "estudiants.json"
csv_f = "estudiants.csv"
backup_carpeta = "fitxers_antics"

existeix = os.path.exists(json_f)
if existeix == False:
    gent = [
        {"nom": "jeroni", "edat": 91, "nota": 0.5, "assignatures": ["Xarxes", "Sistemes"]},
        {"nom": "pABLo", "edat": 44, "nota": 4.0, "assignatures": ["Seguretat", "Aplicacions Web"]}
    ]
    f = open(json_f, "w")
    json.dump(gent, f, indent=4)
    f.close()
    print("S'ha creat un fitxer JSON inicial de prova.\n")

print("GESTIO D'ESTUDIANTS")

try:
    print("1. Llegint dades del JSON...")
    f = open(json_f, "r")
    estudiants = json.load(f)
    f.close()
    
    print("\nAfegir nou estudiant")
    n = input("Nom: ")
    e = input("Edat: ")
    nota = input("Nota: ")
    entrada = input("Assignatures: ")
    
    llista_mat = entrada.split(",")

    alumne = {
        "nom": n,
        "edat": e,
        "nota": nota,
        "assignatures": llista_mat
    }

    estudiants.append(alumne)

    f = open(json_f, "w")
    json.dump(estudiants, f, indent=4)
    f.close()
    print(f"JSON actualitzat correctament.")

    existeix_csv = os.path.exists(csv_f)
    if existeix_csv:
        print(f"\nEl fitxer CSV ja existeix. Movent a '{backup_carpeta}'...")
        
        existeix_carpeta = os.path.exists(backup_carpeta)
        if existeix_carpeta == False:
            os.mkdir(backup_carpeta)
        
        dest = os.path.join(backup_carpeta, "estudiants_vell.csv")
        shutil.move(csv_f, dest)
        print("Fitxer antic mogut correctament.")

    print("\nGenerant nou CSV...")
    f = open(csv_f, "w", newline="")
    escri = csv.writer(f)
    
    escri.writerow(["Nom", "Edat", "Nota", "Assignatures"])
    
    i = 0
    while i < len(estudiants):
        est = estudiants[i]
        mat_string = "-".join(est["assignatures"])
        escri.writerow([est["nom"], est["edat"], est["nota"], mat_string])
        i = i + 1
            
    f.close()
    print(f"Nou fitxer '{csv_f}' creat amb èxit.")

except FileNotFoundError:
    print("No s'ha trobat algun fitxer necessari.")
except json.JSONDecodeError:
    print("El fitxer JSON està corrupte.")
except PermissionError:
    print("No tens permisos.")
except:
    print(f"Error inesperat.")
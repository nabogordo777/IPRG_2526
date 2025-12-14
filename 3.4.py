import json

arxiu = "estudiant.json"

informacio = {
    "Nom": "Pablo",
    "Edat": 17,
    "Nota": 6.9,
    "Assignatures": ["IAP", "APW", "SGI"]
}

f = open(arxiu, "w")
json.dump(informacio, f, indent=4)
f.close()

print(f"Fitxer '{arxiu}' creat amb dades inicials.\n")

try:
    f = open(arxiu, "r")
    estu = json.load(f)
    f.close()
    
    print(f"Dades actuals: {estu}")
    
    materia_nova = input("\nIntrodueix una nova assignatura per afegir: ")
    
    estu["Assignatures"].append(materia_nova)
    
    f = open(arxiu, "w")
    json.dump(estu, f, indent=4)
    f.close()

    print(f"\nDades guardades correctament en '{arxiu}'.")
    
    print("Contingut final de la llista d'assignatures:", estu["Assignatures"])

except FileNotFoundError:
    print(f"El fitxer '{arxiu}' no existeix.")
except json.JSONDecodeError:
    print(f"El fitxer no té un format JSON vàlid.")
except:
    print(f"Error inesperat.")
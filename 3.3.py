import os

fitxer = "prova.txt"

doc = open(fitxer, "w")
doc.write("Primera línia\n")
doc.close()

doc = open(fitxer, "w")
doc.write("Segona línia\n")
doc.close()

intento = 0
while intento == 0:
    try:
        doc = open(fitxer, "x")
        doc.write("Tercera línia\n")
        doc.close()
        intento = 1
    except FileExistsError:
        print("No es pot gastar 'x' perque el fitxer ja existeix.")
        os.remove(fitxer)
        intento = 1

doc = open(fitxer, "a")
doc.write("Cuarta línia\n")
doc.close()

doc = open(fitxer, "a")
doc.write("Quinta línia\n")
doc.write("Sexta línia\n")
doc.close()

doc = open(fitxer, "r")
contingut = doc.read()
print(contingut)
doc.close()

falso = "no_existo.txt"
try:
    doc = open(falso, "r")
    dades = doc.read()
    doc.close()
except FileNotFoundError:
    print(f"El fitxer '{falso}' no existeix.")
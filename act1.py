grados = float(input("Pasam la temperatura"))
cielo = input("Esta nuvolat? (si/s)")

if cielo.lower() == "si" or cielo.lower() == "s":
    tapado = True
else:
    tapado = False

if grados > 35:
    if tapado:
        print("Calor i humitat... una combinació infernal!")
    else:
        print("Fa una calor que fon les pedres!")
elif grados >= 26:
    print("Fa calor, millor buscar ombra.")
elif grados >= 16:
    if tapado:
        print("Temperatura agradable, però potser ploga.")
    else:
        print("Dia perfecte per eixir a passejar!")
elif grados > 0:
    if tapado:
        print("Fa fred i el dia esta trist.")
    else:
        print("Fa fresquetaperò el sol alegra el dia.")
else:
    print("Fa un fred polar!")

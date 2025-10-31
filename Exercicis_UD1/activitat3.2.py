import math

def area_cercle(radi):
    return math.pi * radi ** 2

radi = float(input("Introdueix el radi del cercle: "))
print(f"L'àrea del cercle és: {area_cercle(radi)}")

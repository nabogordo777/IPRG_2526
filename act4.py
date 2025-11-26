total = 0
pares = 0
numero = 1
while numero < 7:
    if numero % 2 == 0:
        total = total + numero
        pares = pares + 1
    else:
        total = total - 1
    numero = numero + 1
print("Resultat final:")
print("suma =", total)
print("comptador_parells =", pares)

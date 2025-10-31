fruits = ["poma", "plàtan", "taronja", "maduixa"]

fruit = input("Introdueix un fruit: ")

if fruit in fruits:
    print(f"El {fruit} està a la llista.")
else:
    print(f"El {fruit} no està a la llista.")

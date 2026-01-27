def key_value (wb, index, liste):
    return wb(liste[index])


wb_leer = {}
wb_test = {1: "Aepfel", 2: "Birne", 3: "Aepfel", 4: "Banane", 5: "Birne"}

try:
    listenlaenge = int(input("Geben Sie die Laenge der Liste ein: "))
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
    exit()
except TypeError:
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
    exit()

try:
    i_nutzer = int(input("Geben Sie den Index ein: "))
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
    exit()
except TypeError:
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
    exit()
if i_nutzer < -listenlaenge or i_nutzer >= listenlaenge:
    print("Der Index liegt außerhalb der Listenlänge.")
    exit()

L_nutzer = []
for n in range(listenlaenge):
    L_nutzer.append(input(f"Geben Sie das Element nächste Element ({n}) der Liste ein: "))

try:
    print(key_value(wb_test, i_nutzer, L_nutzer))
except KeyError:
    print("Das Listenelement kommt nicht als Schlüssel vor.")
# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

def haeufigkeit(s):
    haeufigkeiten = {}
    ergebnis = []
    for buchstabe in s:
        if buchstabe in haeufigkeiten:
            haeufigkeiten[buchstabe] += 1
        else:
            haeufigkeiten[buchstabe] = 1
    for buchstabe, anzahl in haeufigkeiten.items():
        ergebnis.append((buchstabe, anzahl))
    return ergebnis

def ausgabe(haeufigkeiten):
    gesamt = 0
    for buchstabe, anzahl in haeufigkeiten:
        print(f"{buchstabe}: {'*' * anzahl}")
        gesamt += anzahl
    return gesamt

# Test
"""
s = "Hallo"
haeufigkeiten = haeufigkeit(s)
print(haeufigkeiten)
gesamt = ausgabe(haeufigkeiten)
print(f"Gesamtanzahl der Vorkommnisse: {gesamt}")
"""









"""Hausaufgabe 4 (5+2=7 Punkte):
Schreiben Sie eine Funktion haeufigkeit, die eine Zeichenkette s erwartet und eine Liste
von (Buchstabe,Häufigkeit)-Paaren bzgl. s berechnet. Die Liste muss nicht unbedingt
sortiert sein.
Bspw. kann die Funktion auf
haeufigkeit("Hallo")
die Liste
[("l",2),("a",1),("o",1),("H",1)]
zurückgeben.
Schreiben Sie außerdem eine Funktion ausgabe, die einen Rückgabewert der Funktion
haeufigkeit erwartet und eine Histogramm-Ausgabe, wie im Beispiel unten aufgeführt,
(durch print) ausgibt. Die Funktion soll außerdem die Summe aller Vorkommnisse von
Buchstaben zurückgeben. Auf Eingabe
[("l",2),("a",1),("o",1),("H",1)]
soll ausgabe die folgenden Text ausgeben:
l: **
a: *
o: *
H: *
In diesem Beispiel soll der Rückgabewert 5 sein."""
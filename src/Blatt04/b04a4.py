# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

def haeufigkeit(s):
    haeufigkeiten = {}
    for buchstabe in s:
        if buchstabe in haeufigkeiten:
            haeufigkeiten[buchstabe] += 1
        else:
            haeufigkeiten[buchstabe] = 1
    ergebnis = [(buchstabe, anzahl) for buchstabe, anzahl in haeufigkeiten.items()]
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
von (Buchstabe,H¨ aufigkeit)-Paaren bzgl. s berechnet. Die Liste muss nicht unbedingt
sortiert sein.
Bspw. kann die Funktion auf
haeufigkeit("Hallo")
die Liste
3
[("l",2),("a",1),("o",1),("H",1)]
zur
¨ uckgeben.
Schreiben Sie außerdem eine Funktion ausgabe, die einen R¨ uckgabewert der Funktion
haeufigkeit erwartet und eine Histogramm-Ausgabe, wie im Beispiel unten aufgef¨ uhrt,
(durch print) ausgibt. Die Funktion soll außerdem die Summe aller Vorkommnisse von
Buchstaben zur¨ uckgeben. Auf Eingabe
[("l",2),("a",1),("o",1),("H",1)]
soll ausgabe die folgenden Text ausgeben:
l: **
a: *
o: *
H: *
In diesem Beispiel soll der R¨ uckgabewert 5 sein."""
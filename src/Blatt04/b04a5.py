# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

def anwenden(L, bedingung, f, g):
    ergebnis = []
    for e in L:
        if bedingung(e):
            ergebnis.append(f(e))
        else:
            ergebnis.append(g(e))
    return ergebnis











#Test
"""
def funktion(L):
    def ist_warm(temp):
        return temp >= 25
    def erhoehe(temp):
        return temp + 1
    def verdoppele(temp):
        return temp + temp
    return anwenden(L, ist_warm, erhoehe, verdoppele)
print(funktion([24.0, 25.0, 26.5]))  
"""









"""Hausaufgabe 5 (3 Punkte):
Schreiben Sie eine Funktion anwenden, welche
• als ersten Parameter eine Liste L von Floats erwartet,
• als zweiten Parameter eine Funktion bedingung erwartet, die selbst wiederum einen
Float entgegennimmt und einen Booleschen Wert zur¨ uckgibt,
• als dritten Parameter eine Funktion f erwartet, die selbst wiederum einen Float
entgegennimmt und einen Float zur¨ uckgibt, und
• als vierten Parameter eine Funktion g erwartet, die selbst wiederum einen Float
entgegennimmt und einen Float zur¨ uckgibt.
Zur¨ uckgeben soll die Fuktion anwenden die Liste, die aus L entsteht, wenn jedes (Vorkommen
vom) Element e aus L durch f(e) ersetzt wird, falls bedingung(e) wahr ist und g(e)
andernfalls.
Falls unser Hauptprogramm also die Funktionen
def ist_warm(temp):
return temp >= 25
def erhoehe(temp):
return temp+1
def verdoppele(temp):
return temp+temp
enth¨ alt, so soll die Funktion
anwenden([24.0,25.0,26.5],ist_warm,erhoehe,verdoppele)
die Liste
[48.0,26.0,27.5]
zur
¨ uckgeben."""
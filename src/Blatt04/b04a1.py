# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

def durchschnitt(L):
    result = []
    for name, notenliste in L:
        notendurchschnitt = sum(notenliste) / len(notenliste) if notenliste else 0.0
        result.append((name, notendurchschnitt))
    return result

#L=[("Agathe", [2.3, 1.7, 1.3]), ("Ben", [3.0, 2.7]),
#   ("Clara", [1.0, 1.3, 1.0, 1.3])]
#print(durchschnitt(L))








"""Hausaufgabe 1 (3 Punkte):
Schreiben Sie eine Funktion durchschnitt, die eine Liste von Paaren (d.h. 2-Tupeln) der Art
(name,notenliste) erwartet, wobei notenliste eine Liste von Floats ist. Daraus berechnet
werden soll die entsprechende Liste von Paaren der Art (name,notendurchschnitt), wobei
notendurchschnitt ein Float ist, der den Notendurchschnitt beschreibt.
Bspw. soll die Funktion beim ¨ ubergebenen Parameter
[("Agathe", [2.3, 1.7, 1.3]), ("Ben", [3.0, 2.7]),
("Clara", [1.0, 1.3, 1.0, 1.3])]
die R¨ uckgabe
[("Agathe", 1.7666666666666666), ("Ben", 2.85), ("Clara", 1.15)]
liefern."""

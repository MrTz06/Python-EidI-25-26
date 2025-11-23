# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

def parse_daten(s):
    ergebnis = []
    eintraege = s.split(';')
    for eintrag in eintraege:
        name, note = eintrag.split(',')
        ergebnis.append(tuple((name, float(note))))
    return ergebnis

#Test
#print(parse_daten("Alfons,2.3;Ben,3.0;Carla,1.7"))











"""Hausaufgabe 3 (3 Punkte):
Schreiben Sie eine Funktion parse_daten, die einen String der Form
Name,Note;Name,Note;...;Name,Note
erwartet und eine entsprechende Liste von Name/Noten Tupeln erzeugt, wobei die Note als
Float dargestellt wird. Bspw. soll die Funktion auf
parse_daten("Alfons,2.3;Ben,3.0;Carla,1.7")
die R¨ uckgabe
[(’Alfons’, 2.3), (’Ben’, 3.0), (’Carla’, 1.7)]
liefern.
Hinweis: Sie k¨
onnen tuple(liste) verwenden um eine Liste liste in ein Tupel umzuwan-
deln."""
# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
def alph_dict(i):
    return {s: [chr(96 + n) for n in range(s, 0, -1)] for s in range(1, i + 1)}















"""Hausaufgabe 2 (2 Punkte):
Schreiben Sie eine Funktion alph_dict, welche einen Integer i zwischen 1 und 26 erwartet
und mittels List- und Dictionary-Comprehensions ein W¨ orterbuch der folgenden Form
erstellt und zur¨ uckgibt:
Die Schl¨ ussel des W¨ orterbuches sind die ersten i Ganzzahlen, angefangen bei 1. Der zum
Schl¨ ussel s zugeh¨ orige Wert ist die Liste der ersten s Kleinbuchstaben, in umgekehrter
Reihenfolge.
Der Rumpf der Funktionen darf dabei nur aus einer Zeile bestehen.
Beispiel: alph_dict(6) gibt ein W¨ orterbuch der folgenden Form zur¨ uck:
{1:["a"], 2:["b","a"], 3:["c","b","a"], 4:["d","c","b","a"],
5:["e","d","c","b","a"], 6:["f","e","d","c","b","a"]}"""
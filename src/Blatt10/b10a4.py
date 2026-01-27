# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
def remove_A_a(s):
    return ''.join(map(lambda c: c if c != 'A' else '', s))
def remove_A_b(s):
    return ''.join(filter(lambda c: c != 'A', s))








"""Hausaufgabe 4 (2 + 1 Punkte):
Schreiben Sie eine Funktion, welche einen String s erwartet und den String zur¨ uckgibt den
man erh¨ alt, wenn man alle Vorkommen des Zeichens "A" aus s entfernt. Sie d¨ urfen nicht
replace oder remove verwenden und der Rumpf der Funktionen darf je nur aus einer Zeile
bestehen. L¨ osen Sie die Aufgabe
(a) mittels map (ohne filter zu benutzten). Nennen Sie diese Funktion remove_A_a.
(b) mittels filter (ohne map zu benutzten). Nennen Sie diese Funktion remove_A_b."""
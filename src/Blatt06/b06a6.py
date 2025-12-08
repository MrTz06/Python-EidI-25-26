# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)


def anfang_von(tupel1, tupel2):
    if len(tupel1) == 0 or len(tupel2) == 0:
        return True
    elif tupel1[0] != tupel2[0]:
        return False
    else:
        return anfang_von(tupel1[1:], tupel2[1:])






"""Hausaufgabe 6 (3 Punkte):
Schreiben Sie eine Funktion anfang_von, welche zwei Tupel beliebiger Gr¨ oßen m, n ≥ 0
erwartet und rekursiv berechnet, ob beide Tupel in den ersten min(m, n) Eintr¨
agen
¨ ubereinstimmen. Falls ja soll True ausgegeben werden, sonst False.
Beispiele:
• Gibt man (2,"b",9,100) und (2,"b",9) ein, dann erh¨ alt man die R¨ uckgabe True.
• Gibt man (2,"b",9) und (2,"b",9,100) ein, dann erh¨ alt man die R¨ uckgabe True.
• Gibt man (2,"b",9) und (2,9) ein, dann erh¨ alt man die R¨ uckgabe False."""
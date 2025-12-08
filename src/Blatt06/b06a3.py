# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def zerlegung(w):
    if len(w) == 0:
        return []
    elif len(w) == 1:
        return [w]
    else:
        return [w[0:2]] + zerlegung(w[2:])

"""Hausaufgabe 3 (4 Punkte):
Schreiben Sie eine Funktion zerlegung, welche als Eingabe einen String w erwartet. Die
Funktion soll mittels Rekursion eine Liste von Strings der L¨ ange 2 berechnen, welche die
Eingabe w zerlegt darstellt. Bleibt ein Buchstabe ¨ ubrig, so enth¨ alt die R¨ uckgabeliste als
letzten Eintrag einen String der L¨ ange 1.
Beispiele:
• Die Eingabe "abcdef" f¨ uhrt zur R¨ uckgabe ["ab", "cd", "ef"].
• Die Eingabe "abc" f¨ uhrt zur R¨ uckgabe ["ab", "c"].
• Die Eingabe"" f¨ uhrt zur R¨ uckgabe []."""
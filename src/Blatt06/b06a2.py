# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def zerfall(n, p, t):
    if t == 0:
        return float(n)
    else:
        n_neu = n * (1 - p / 100)
        return zerfall(n_neu, p, t - 1)

"""Hausaufgabe 2 (3 Punkte):
Schreiben Sie eine Funktion zerfall, welche drei Eingaben erwartet:
• eine positive Zahl n (Startwert)
• einen Integer-Wert p zwischen 0 und 100 (Prozentangabe)
• einen nicht-negativen Integer-Wert t (Anzahl der Tage)
Die Funktion soll mittels Rekursion das folgende berechnen und das Ergebnis immer als
Float zur¨ uckgeben:
Angenommen wir haben zu Beginn n Einheiten einer Materie und jeden Tag zerfallen p
Prozent davon. Wie viele Einheiten sind dann nach t Tagen noch vorhanden?
Beispiele:
• zerfall(200, 50, 0) liefert die R¨ uckgabe 200.0
• zerfall(200, 50, 1) liefert die R¨ uckgabe 100.0
• zerfall(200, 50, 4) liefert die R¨ uckgabe 12.5
• zerfall(180.9, 17, 2) liefert die R¨ uckgabe 124.62200999999999
Hinweis: Rundungsfehler, wie im letzten Beispiel angegeben, k¨ onnen bei Ihnen auftreten,
m
¨ ussen es aber nicht."""
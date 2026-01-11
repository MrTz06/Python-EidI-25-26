# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def umkehren(wb):
    neues_wb = {}
    for schluessel, wert in woerterbuch.items():
        if wert in neues_wb:
            neues_wb[wert] = min(neues_wb[wert], schluessel)
        else:
            neues_wb[wert] = schluessel
    return neues_wb







"""Hausaufgabe 1 (2 Punkte):
Schreiben Sie eine Funktion umkehren, welche als Eingabe ein W¨ orterbuch wb erwartet, in
dem die Schl¨ ussel Integer-Werte sind. Zur¨ uckgegeben werden soll ein neues W¨ orterbuch, das
die Schl¨ ussel und Werte von wb vertauscht. Falls es in wb zwei verschiedene Schl¨ ussel gibt,
die auf den gleichen Wert verweisen, so soll der kleinste Schl¨ ussel als neuer Wert benutzt
werden.
Beispiel: umkehren({2:3, 4:"ab", 5:True, 9:"ab"}) liefert als R¨ uckgabe ein W¨ orter-
buch der Form {3:2, "ab":4, True:5}.
Ihre Funktion umkehren darf keine Nebeneffekte auf das eingegebene W¨ orterbuch haben,
d.h. durch die Ausf¨ uhrung Ihrer Funktion, darf das eingegebene W¨ orterbuch nicht ver¨ andert
werden.
"""
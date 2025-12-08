# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)



def filter(liste, bedingung):
    if len(liste) == 0:
        return []
    elif bedingung(liste[0]):
        return [liste[0]] + filter(liste[1:], bedingung)
    else:
        return filter(liste[1:], bedingung)








"""Hausaufgabe 5 (4 Punkte):
Schreiben Sie eine Funktion filter, welche als Eingabe eine Liste und eine Bedingung
bedingung erwartet, d.h. eine Funktion, welche wiederum irgendeine Eingabe erwartet und
einen booleschen Wert zur¨ uckgibt.
Die Funktion filter soll mittels Rekursion die Liste berechnen, die man erh¨ alt, wenn man
aus der Eingabeliste nur diejenigen Eintr¨
age e ausw
¨ ahlt, f¨ ur die bedingung(e) den Wert
True zur
¨ uckgibt.
Sie d¨ urfen davon ausgehen, dass Ihre Funktion nur mit Eingaben aufgerufen wird, bei denen
bedingung auf die Eintr¨ age der eingegebenen Liste anwendbar ist.
Beispiel: Enth¨ alt das Hauptprogramm neben Ihrer Funktion noch den folgenden Code ...
def test_bed (zahl):
return zahl < 10
... dann liefert filter([19,-2,10,9],test_bed) die R¨ uckgabe [-2,9]."""
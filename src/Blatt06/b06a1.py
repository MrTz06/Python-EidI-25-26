# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def gerade_summe(n):
    if n == 1:
        return 2
    else:
        return 2 * n + gerade_summe(n - 1)











"""Hausaufgabe 1 (3 Punkte):
Schreiben Sie eine Funktion gerade_summe, welche als Eingabe einen Integer n ≥ 1 erwartet
und rekursiv die Summe der ersten n geraden nat¨ urlichen Zahlen berechnet und zur¨ uckgibt.
Hierbei z¨ ahlen wir die 2 als die erste gerade Zahl.
Beispiel: Die Eingabe 5 f¨ uhrt zur R¨ uckgabe 30, denn 2 + 4 + 6 + 8 + 10 = 30."""
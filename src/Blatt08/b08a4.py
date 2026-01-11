# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def gitter_wege(m, n, wb):
    # Überprüfen, ob das Ergebnis bereits im Wörterbuch gespeichert ist
    if (m, n) in wb:
        return wb[(m, n)]

    # Basisfall: Wenn m oder n 1 ist, gibt es nur einen Weg
    if m == 1 or n == 1:
        return 1

    # Rekursiver Fall: Anzahl der Wege von oben links nach unten rechts
    wege = gitter_wege(m - 1, n, wb) + gitter_wege(m, n - 1, wb)

    # Ergebnis im Wörterbuch speichern
    wb[(m, n)] = wege

    return wege


if __name__ == '__main__':
   m= int(input("Bitte geben Sie die Höhe m des Gitters ein: "))
   n= int(input("Bitte geben Sie die Breite n des Gitters ein: "))
   ergebnis = gitter_wege(m, n, {})
   print(f"Die Anzahl der möglichen Wege in einem {m}x{n}-Gitter beträgt: {ergebnis}")



"""Hausaufgabe 4 (4 Punkte):
Schreiben Sie eine rekursive Funktion gitter_wege, welche als Eingabe zwei positive
Integer-Werte m und n, sowie ein W¨ orterbuch wb, erwartet. Von der Funktion gitter_wege
berechnet und zur¨ uckgegeben werden soll die Anzahl der m¨ oglichen Wege die es gibt, in
einem Gitter der H¨ ohe m und der Breite n, von oben links nach unten rechts zu laufen.
Dabei darf man in jedem Schritt nur nach unten oder rechts laufen.
Fordern Sie im Hauptprogramm die zwei Werte m und n vom Nutzer an, rufen Sie
gitter_wege mit den Eingaben m, n, {}auf (m und n als Integer) und geben die R¨ uckgabe
auf der Konsole aus.
Das ¨ ubergebene W¨ orterbuch wb soll genutzt werden, um Ihr Programm schneller zu machen.
D.h. setzen Sie das W¨ orterbuch ein, sodass bereits berechnete rekursive Aufrufe nicht erneut
berechnet werden. Die Schl¨ ussel dieses W¨ orterbuchs sollten Tupel der Form (m’,n’) sein,
wobei m’, n’ positive Ganzzahlen sind.
Beispiele: Im Folgenden sind alle zul¨ assigen Wege im 3, 3-Gitter dargestellt:
Die Dimensionen beziehen sich also auf die Anzahl der Gitterpunkte, nicht auf die Anzahl
der K¨ astchen.
3
Die folgenden Wege sind z.B. zul¨ assig auf dem 5, 4-Gitter:
Die R¨ uckgabe von gitter_wege(5,4,{}) lautet 35."""
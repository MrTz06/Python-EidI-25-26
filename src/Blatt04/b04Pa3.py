def anzahl_woerter(worte):
    return len(worte)
def laenge_laengstes_wort(worte):
    max_laenge = 0
    for wort in worte:
        if len(wort) > max_laenge:
            max_laenge = len(wort)
    return max_laenge
def alle_laengsten_woerter(worte, max_laenge):
    laengste_woerter = []
    for wort in worte:
        if len(wort) == max_laenge:
            laengste_woerter.append(wort)
    return laengste_woerter
def woerter_mit_grossbuchstaben(worte):
    grossbuchstaben_woerter = []
    for wort in worte:
        if wort[0].isupper():
            grossbuchstaben_woerter.append(wort)
    return grossbuchstaben_woerter
def woerter_mit_kleinbuchstaben(worte):
    kleinbuchstaben_woerter = []
    for wort in worte:
        if wort[0].islower():
            kleinbuchstaben_woerter.append(wort)
    return kleinbuchstaben_woerter
def main():
    eingabe = input("Bitte geben Sie eine Zeichenkette ein: ")
    worte = eingabe.split(" ")
    anzahl = anzahl_woerter(worte)
    max_laenge = laenge_laengstes_wort(worte)
    laengste_woerter = alle_laengsten_woerter(worte, max_laenge)
    grossbuchstaben_woerter = woerter_mit_grossbuchstaben(worte)
    kleinbuchstaben_woerter = woerter_mit_kleinbuchstaben(worte)
    print(f"Anzahl der Wörter: {anzahl}")
    print(f"Länge des längsten Wortes: {max_laenge}")
    print(f"Alle längsten Wörter: {laengste_woerter}")
    print(f"Wörter mit Großbuchstaben: {grossbuchstaben_woerter}")
    print(f"Wörter mit Kleinbuchstaben: {kleinbuchstaben_woerter}")

if __name__ == "__main__":
    main()

















"""Pr¨ asenzaufgabe 3:
Schreiben Sie ein Programm, welches eine Zeichenkette w, bestehend aus W¨ ortern getrennt
durch Leerzeichen, einliest und folgende Werte bestimmt:
• Die Anzahl der W¨ orter in w.
• Die L¨ ange des l¨ angsten Wortes in w.
• Alle l¨ angsten W¨ orter in w.
• Alle W¨ orter in w, die mit einem Großbuchstaben anfangen.
• Alle W¨ orter in w, die mit einem Kleinbuchstaben anfangen.
Verwenden Sie Funktionen, wo sinnvoll, um Ihren Code effizienter und wartbarer zu machen.
Benutzen Sie geeignete Datentypen, um Ihre Resultate und Zwischenergebnisse zu speichern.
Geben Sie anschließend alle Ergebnisse, sowie alle W¨ orter auf der Konsole aus.
Sie d¨ urfen davon ausgehen, dass W¨ orter keine Leerzeichen enthalten, dass W¨ orter immer
durch genau ein Leerzeichen getrennt sind und dass mindestens ein Wort eingegeben wird."""
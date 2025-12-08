def verdoppeln(string):
    if string == '':
        return ''
    else:
        return string[0] * 2 + verdoppeln(string[1:])

print(verdoppeln("Hallo!"))  # Ausgabe: HHaalllloo!!


"""Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Rekursion: Das Programm demonstriert die Verwendung von Rekursion, um eine Aufgabe zu lösen, indem es eine Funktion definiert, die sich selbst aufruft.
2. String-Manipulation: Es zeigt, wie man Zeichen in einem String verdoppelt indem man das erste Zeichen nimmt und es mit dem Ergebnis eines rekursiven Aufrufs auf den Rest des Strings kombiniert.
3. Basisfall und rekursiver Fall: Das Programm illustriert das Konzept von Basisfällen (leerer String) und rekursiven Fällen (nicht-leerer String) in rekursiven Funktionen.
"""

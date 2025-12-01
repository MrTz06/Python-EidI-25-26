### testet ob n einen
### Teiler d hat mit 2<=d<=m
def hat_teiler_kleinergleich(m,n):
    if m==1:
        return False
    return n%m==0 or\
            hat_teiler_kleinergleich(m-1,n)

def ist_prim(n):
    return n>=2 and \
            not hat_teiler_kleinergleich(n-1,n)

for i in range(100):
    if ist_prim(i):
        print(i)



"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?

1. Rekursive Funktionen: Das Programm demonstriert die Verwendung von Rekursion zur Lösung eines Problems,
   indem die Funktion `hat_teiler_kleinergleich` sich selbst aufruft, um zu überprüfen, ob eine Zahl einen Teiler hat.
2. Primzahlprüfung: Es zeigt eine effiziente Methode zur Bestimmung, ob eine Zahl eine Primzahl ist,
   indem überprüft wird, ob sie durch irgendeine Zahl kleiner oder gleich ihrer Quadratwurzel teilbar ist.
3. Logische Operatoren: Die Verwendung von logischen Operatoren wie `and` und `not` wird gezeigt,
   um komplexe Bedingungen in einer klaren und verständlichen Weise auszudrücken.
4. Bereichsüberprüfung: Das Programm nutzt die `range`-Funktion, um eine Schleife über eine Reihe von Zahlen zu erstellen,
   was eine häufige Praxis in Python ist, um Iterationen durchzuführen.
5. Bedingte Rückgabe: Die Funktionen geben boolesche Werte zurück, die direkt in Bedingungen verwendet werden können,
   was die Lesbarkeit und Wartbarkeit des Codes verbessert.
"""
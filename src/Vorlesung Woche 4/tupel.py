#Dieses Programm aus der Vorlesung definiert eine Funktion, die aus einem Tupel von Tupeln
#die Durchschnittswerte der ersten Elemente und die einzigartigen zweiten Elemente extrahiert.

#Funktion zur Extraktion von Durchschnitt und einzigartigen Wörtern
def hole_daten(einTupel):
    # Initialisierung von leeren Tupeln für Zahlen und Wörter
    zahlen=()
    woerter=()
    # Durchlauf durch jedes Tupel im Eingabetupel
    for t in einTupel:
        # Überprüfung und Hinzufügen der ersten Elemente zu zahlen
        zahlen=zahlen + (t[0],)
    # Überprüfung und Hinzufügen der zweiten Elemente zu woerter, falls einzigartig
        if t[1] not in woerter:
            woerter=woerter + (t[1],)
    # Berechnung des Durchschnitts der Zahlen
    durchschnitt=0.0
    summe=0
    # Schleife zur Summierung der Zahlen
    for z in zahlen:
        summe=summe+z
    # Berechnung des Durchschnitts und Rückgabe des Ergebnisses
    if len(zahlen)>0:
        durchschnitt=summe/len(zahlen)
        return (durchschnitt,woerter)

#Beispielaufruf der Funktion
tupel_von_tupeln = ((10, "apfel"), (20, "banane"), (30, "apfel"), (40, "kirsche"), (50, "banane"), (60, "kirsche"))
ergebnis = hole_daten(tupel_von_tupeln)
print(ergebnis)  # Ausgabe: (35.0, ('apfel', 'banane', 'kirsche'))


#Zusammenfassung/Erklärung/Was kann ich neues durch das Programm lernen/Welche neuen Konzepte sind enthalten:
# 1. Tupel-Verarbeitung: Das Programm zeigt, wie man Tupel von Tupeln durchläuft und deren Elemente extrahiert.
# 2. Durchschnittsberechnung: Es demonstriert die Berechnung des Durchschnitts von numerischen Werten in einem Tupel.
# 3. Einzigartige Elemente: Das Programm illustriert, wie man einzigartige Elemente aus einem Tupel extrahiert und speichert.
# 4. Bedingte Logik: Es verwendet bedingte Anweisungen, um zu überprüfen, ob ein Element bereits in einem Tupel vorhanden ist, bevor es hinzugefügt wird.
# 5. Rückgabe von Tupeln: Die Funktion gibt ein Tupel zurück,
# das sowohl den Durchschnitt als auch die einzigartigen Wörter enthält, was die Rückgabe komplexerer Datenstrukturen zeigt.

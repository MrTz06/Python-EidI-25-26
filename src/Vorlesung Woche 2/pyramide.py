# Dieses Programm aus der Vorlesung erstellt eine Pyramide aus Zahlen basierend auf der eingegebenen Höhe.

# Eingabe der Höhe der Pyramide
h=int(input("Geben Sie die Höhe ein: "))

# Iteration über jede Ebene der Pyramide
for i in range(1,h+1): #i ist die aktuelle Ebene, läuft von 1 bis h+1(weil der obere Grenzwert bei range() ausgeschlossen ist)
    # Ausgabe der führenden Leerzeichen für die Zentrierung
    for bla in range(h-i): #bla ist eine leere Variable (Platzhalter)
        print(" ", end="")
    # Ausgabe der Zahlen in der aktuellen Ebene
    for j in range(1,2*i): #j läuft von 1 bis 2*i(nicht i-1, da der Grenzwert ausgeschlossen ist), um die richtige Anzahl von Zahlen pro Ebene zu erzeugen
        print(str(j%10), end="")
    print()


# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Verschachtelte Schleifen: Das Programm verwendet verschachtelte for-Schleifen, um die Struktur der Pyramide zu erstellen.
# 2. Zentrierung: Die äußere Schleife erzeugt führende Leerzeichen, um die Pyramide zu zentrieren.
# 3. Modulo-Operator: Der Modulo-Operator (%) wird verwendet, um sicherzustellen, dass nur die letzten Ziffern der Zahlen (0-9) angezeigt werden.
#(Einfach erklärt: j%10 gibt den Rest der Division von j durch 10 zurück, wodurch nur die letzte Ziffer von j übrig bleibt.)
# 4. Dynamische Pyramidenhöhe: Die Höhe der Pyramide wird durch Benutzereingabe bestimmt, was Flexibilität im Programm ermöglicht.
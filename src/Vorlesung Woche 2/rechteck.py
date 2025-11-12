# Dieses Programm aus der Vorlesung zeichnet ein Rechteck aus Sternchen (*) in der Konsole.

b=int(input("Geben Sie die Breite ein: "))
h=int(input("Geben Sie die Höhe ein: "))

# Iteration über die Höhe
for i in range(h):
    # Iteration über die Breite
    for j in range(b):
        # Überprüfung, ob wir uns an einem Rand befinden
        if i==0 or i==h-1 or j==0 or j==b-1: # Randbedingungen
            print("*",end="") # Ausgabe eines Sternchens am Rand
        #Ansonsten Ausgabe eines Leerzeichens (innen)
        else:
            print(" ",end="")
    ## Zeilenumbruch
    #print()


    # Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
    # 1. Verschachtelte Schleifen: Das Programm verwendet verschachtelte for-Schleifen, um die Struktur des Rechtecks zu erstellen.
    # 2. Bedingte Anweisungen: Die if-Anweisung wird verwendet, um zu bestimmen, ob ein Sternchen oder ein Leerzeichen ausgegeben werden soll,
    # basierend auf der Position im Rechteck.
    # 3. Dynamische Abmessungen: Die Breite und Höhe des Rechtecks werden durch Benutzereingabe bestimmt, was Flexibilität im Programm ermöglicht.
    # 4. Verwendung von end="": Das Argument end="" in der print()-Funktion wird verwendet, um zu verhindern,
    # dass nach jedem Sternchen ein Zeilenumbruch erfolgt, sodass die Sterne in einer einzigen Zeile ausgegeben werden.
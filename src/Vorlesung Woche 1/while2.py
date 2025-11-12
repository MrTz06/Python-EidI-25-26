#Dieses Programm aus der Vorlesung demonstriert und erklärt die Verwendung von while-Schleifen in Python vertiefend.
# Programm zur Bestimmung, ob eine eingegebene natürliche Zahl eine Primzahl ist

#Abfrage der Zahl
n=int(input("Geben Sie eine natürliche Zahl ein: "))

#Initialisierung der Variablen
t=2
prim=True
#Schleife zur Prüfung der Teilbarkeit
#Während t kleiner als n ist
while t<n:
    #Wenn n durch t teilbar ist, ist n keine Primzahl
    if n%t==0:
        prim=False
    #Ansonsten t um 1 erhöhen
    t=t+1

#Ausgabe des Ergebnisses
if prim:
    print(str(n) + " ist eine Primzahl")
else:
    print(str(n) + " ist keine Primzahl")


#Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
#1. while-Schleifen: Die while-Schleife wird verwendet, um eine Aktion wiederholt auszuführen, solange eine bestimmte Bedingung wahr ist.
#2. Primzahlprüfung: Das Programm zeigt, wie man eine Zahl auf Primzahl-Eigenschaft überprüft, indem man alle möglichen Teiler testet.
#3. Bedingte Anweisungen: Die if-Anweisung wird verwendet, um Entscheidungen zu treffen, basierend auf der Teilbarkeit der Zahl.
#4. Variableninitialisierung: Die Variablen t und prim werden initialisiert, um den aktuellen Teiler und den Primzahlstatus zu verfolgen.
#5. Benutzereingabe: Das Programm zeigt, wie man Benutzereingaben in Python verarbeitet.

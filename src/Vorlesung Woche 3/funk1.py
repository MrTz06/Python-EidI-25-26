#Dieses Programm aus der Vorlesung demonstriert und erklärt die Definition und Verwendung von Funktionen in Python.

#def= Definition einer Funktion
def teilt(i,t):
    """Eingabe: i, ein Integer
    und ein positiver Integer t.
    Gibt True zurueck, falls i durch t teilbar ist
    ansonsten False
    """
    #print("Gerade sind wir in ist_gerade")
    return i%t==0

#Hauptprogramm
#Abfrage des Teilers
teiler=int(input("Geben Sie einen Teiler ein: "))

#Ausgabe der Zahlen von 0 bis 100, die durch den Teiler teilbar sind
print(" Teilbarkeit durch "+ str(teiler))
for n in range(101):
    if teilt(n,teiler):
        print(n)


#Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
#1. Funktionsdefinition: Das Programm zeigt, wie man eine Funktion in Python definiert und dokumentiert.
#2. Parameterübergabe: Es wird demonstriert, wie man Parameter an eine Funktion übergibt.
#3. Rückgabewerte: Die Funktion gibt einen booleschen Wert zurück, der angibt, ob eine Zahl durch einen anderen teilbar ist.
#4. Modularität: Die Verwendung von Funktionen fördert die Modularität und Wiederverwendbarkeit des Codes.
#5. Anwendung: Das Hauptprogramm nutzt die definierte Funktion, um eine spezifische Aufgabe zu erfüllen,
# nämlich die Ausgabe von Zahlen, die durch einen gegebenen Teiler teilbar sind.
# Dieses Programm aus der Vorlesung demonstriert und erklärt die Implementierung des Caesar-Verschlüsselungsalgorithmus in Python.

# Eingabe des zu verschlüsselnden Textes
text=input("Geben Sie einen Text ein: ")

# Eingabe der Verschiebung
verschiebung=int(input("Verschiebung, bspw. 3"))

# Initialisierung des Ergebnisses
ergebnis=""

# Iteration über jedes Zeichen im Text
for zeichen in text:
    # Bestimmung der ASCII-Position des Zeichens
    position=ord(zeichen)
    # Berechnung der neuen Position nach der Verschiebung
    position_neu= position+verschiebung
    # Umwandlung der neuen Position zurück in ein Zeichen
    zeichen_neu=chr(position_neu)
    # Hinzufügen des neuen Zeichens zum Ergebnis
    ergebnis=ergebnis+zeichen_neu

# Ausgabe des verschlüsselten Textes
print("Verschlüsselter Text", ergebnis)


# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Caesar-Verschlüsselung: Das Programm demonstriert die Implementierung des Caesar-Verschlüsselungsalgorithmus.
# 2. Zeichen- und ASCII-Werte: Die Funktionen ord() und chr() werden verwendet, um zwischen Zeichen und ihren ASCII-Werten zu konvertieren.
# 3. String-Konkatenation: Das Programm zeigt, wie man Zeichen zu einem neuen String hinzufügt, um das Ergebnis zu erstellen.
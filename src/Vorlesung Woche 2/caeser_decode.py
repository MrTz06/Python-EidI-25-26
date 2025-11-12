# Dieses Programm aus der Vorlesung demonstriert und erklärt die Implementierung des Caesar-Entschlüsselungsalgorithmus in Python.

# Eingabe des zu entschlüsselnden Textes
text=input("Geben Sie einen verschlüsselten Text ein: ")

# Eingabe der Verschiebung
verschiebung=int(input("Verschiebung, bspw. 3"))

# Initialisierung des Ergebnisses
ergebnis=""

# Iteration über jedes Zeichen im Text
for zeichen in text:
    # Bestimmung der ASCII-Position des Zeichens
    position=ord(zeichen)
    # Berechnung der neuen Position nach der Entschlüsselung
    position_neu= position-verschiebung
    # Umwandlung der neuen Position zurück in ein Zeichen
    zeichen_neu=chr(position_neu)
    # Hinzufügen des neuen Zeichens zum Ergebnis
    ergebnis=ergebnis+zeichen_neu

# Ausgabe des entschlüsselten Textes
print("Entschlüsselter Text", ergebnis)

# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Caesar-Entschlüsselung: Das Programm demonstriert die Implementierung des Caesar-Entschlüsselungsalgorithmus.
# Alles weitere ist identisch mit caeser.py
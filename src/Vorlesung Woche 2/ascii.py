# Dieses Programm aus der Vorlesung erklärt wie man die ASCII-Werte der Zeichen eines eingegebenen Textes ausgibt.

text=input("Geben Sie einen Text ein: ")

# Methode 1: Iteration(Iteration=Durchlaufen) über die Zeichen des Strings (text)
for zeichen in text:
    # Ausgabe des Zeichens und seines ASCII-Werts mittels der Funktion ord()
    print(zeichen,"->",ord(zeichen))

# Methode 2: Iteration über die Indizes(Positionen) des Strings (text)
for i in range(len(text)):
    # Ausgabe des Zeichens an der Position i und seines ASCII-Werts
    print(text[i],"->",ord(text[i]))

# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Iteration über Strings: Zwei Methoden zur Iteration über die Zeichen eines Strings werden demonstriert.
# 2. Einführung in ord(): Die Funktion ord() wird verwendet, um Zeichen in ihre entsprechenden ASCII-Werte umzuwandeln.

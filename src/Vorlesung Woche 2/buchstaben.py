# Dieses Programm aus der Vorlesung gibt die ASCII-ZEICHEN für die Werte von 32 bis 127 aus.

for i in range(32,128):
    # Ausgabe des ASCII-Werts i und seines entsprechenden Zeichens mittels der Funktion chr()(chr() wandelt einen ASCII-Wert in das entsprechende Zeichen um)
    print(i,"->",chr(i))

# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. ASCII-Zeichen: Das Programm zeigt, wie man ASCII-Zeichen für bestimmte Werte erhält.
# 2. Iteration mit range(): Die Funktion range() wird verwendet, um eine Sequenz von Zahlen zu generieren.
# 3. Einführung in chr(): Die Funktion chr() wird verwendet, um ASCII-Werte in Zeichen umzuwandeln.

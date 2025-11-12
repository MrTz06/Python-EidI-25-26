# Dieses Programm aus der Vorlesung demonstriert eine digitale Uhr, die Stunden, Minuten und Sekunden anzeigt.
import time

# Iteration über Stunden, Minuten und Sekunden
for h in range(24):
    for m in range(60):
        for s in range(60):
            # Kurze Pause, um die Anzeige lesbar zu machen
            time.sleep(0.002)
            # Ausgabe der Zeit im Format HH:MM:SS mit führenden Nullen
            print(str(h).zfill(2)+":"+str(m).zfill(2)+ \
                  ":"+ str(s).zfill(2))

# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Zeitverzögerung: Die Funktion time.sleep() wird verwendet, um Pausen im Programmablauf einzufügen.
# 2. Einführung der zfill()-Methode: Die Methode zfill() wird verwendet, um Zahlen mit führenden Nullen zu formatieren.
# 3. Verschachtelte Schleifen: Das Programm demonstriert die Verwendung von verschachtelten for-Schleifen zur Iteration über Stunden, Minuten und Sekunden.
# 4. Formatierung von Zeit: Das Programm zeigt, wie man Zeit im Format HH:MM:SS darstellt.
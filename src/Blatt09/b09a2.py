# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
from datetime import datetime

def check_file(file: str) -> int:
    # Notiz für Interessierte: eigentlich sollte man Dateien, die man öffnet, auch schließen (file.close()). Das machen
    # wir hier nicht um den Code einfach zu halten und weil der Code nicht produktiv eingesetzt wird.
    try:
        file = open(file, 'r')
        datetime.strptime(next(file), "%d.%m.%Y")
        return 0
    #except FileNotFoundError: # Datei nicht gefunden
    except OSError: #Datei konnte nicht geöffnet werden
        return 1
    except StopIteration: # Datei ist leer
        return 2
    except ValueError: # Ungültiges Datum
        return 3
    except Exception: # Anderer Fehler
        return 4



if __name__ == "__main__":
    print(check_file("valid.txt"))    # Soll 0 ausgeben
    print(check_file("missing.txt"))  # Soll 1 ausgeben
    print(check_file("empty.txt"))    # Soll 2 ausgeben
    print(check_file("invalid.txt"))  # Soll 3 ausgeben



"""Hausaufgabe 2 (6 Punkte):
Folgende Funktion soll ¨ uberpr¨ ufen, ob eine gegebene Datei in der ersten Zeile ein valides
Datum (TT.MM.YYYY) enth¨ alt.
def check_file(file: str) -> int:
file = open(file, ’r’)
datetime.strptime(next(file), "%d.%m.%Y")
return 0
Nutzen Sie Exceptions um zu implementieren, dass die Funktion
• 1 zur
¨ uckgibt, wenn die Datei nicht ge¨ offnet werden konnte,
• 2 zur
¨ uckgibt, wenn die Datei leer ist,
• 3, wenn die erste Zeile der Datei kein korrekt formatiertes Datum enth¨ alt und
• 4, falls irgendein anderer Fehler auftritt."""
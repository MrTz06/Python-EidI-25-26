# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

s = input("Geben Sie einen String ein: ")
Zahlenwerte = ""
for zeichen in s:
    Zahlenwerte += str(ord(zeichen)) + ","
    # Entfernen des letzten Kommas
Zahlenwerte = Zahlenwerte[:-1]

print(Zahlenwerte, end="")





#Hausaufgabe 2 (2 Punkte):
#Schreiben Sie ein Programm, welches einen String einliest und, mit Komma getrennt, die
#Zahlenwerte der Zeichen ausgibt.
#Hinweis: Nutzen sie ord(zeichen) um den Zahlenwert eines Zeichens zu ermitteln.
#Beispiel: Fuer die Eingabe ASCII soll "65,83,67,73,73" ausgegeben werden.
# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)
n=int(input("Geben Sie eine natuerliche Zahl n ein: "))
i=1
anzahl_teiler=0
for i in range(2, n):
    if n%i==0:
        anzahl_teiler+=1
if anzahl_teiler==0:
    print("Die natürliche Zahl", n, "hat keine echten Teiler und ist somit eine Primzahl.")
else:
    print("Die natürliche Zahl", n, "hat", anzahl_teiler, "echte Teiler.")




#Hausaufgabe 1 (2 Punkte):
#Schreiben Sie ein Programm, welches eine Ganzzahl n einliest und die Anzahl der ech-
#ten Teiler von n berechnet und ausgibt. Sie duerfen davon ausgehen, dass tats¨ achlich eine
#Ganzzahl eingegeben wird.
#Hinweis: Eine Zahl x ist ein echter Teiler von n, wenn x ̸= 1, x ̸= n, sowie x teilt n gilt.

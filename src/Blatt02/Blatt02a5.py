# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)
w = input("Geben Sie eine Zeichenkette bestehend aus mehreren Wörtern, getrennt durch Leerzeichen ein: ")

woerter = w.split(" ")

vokale = "aeiouAEIOU"
for wort in woerter:
    laengste_kette=0
    aktuelle_kette=0
    for buchstabe in wort:
        if buchstabe not in vokale:
            aktuelle_kette += 1
            if aktuelle_kette > laengste_kette:
                laengste_kette = aktuelle_kette
        else:
            aktuelle_kette = 0
    print(wort, laengste_kette)

"""Hausaufgabe 5 (7 Punkte):
Schreiben Sie ein Programm, welches eine Zeichenkette w bestehend aus mehreren W¨ ortern,
getrennt durch Leerzeichen, einliest.
Bestimmen Sie dann f¨ ur jedes Wort die gr¨ oßte aufeinanderfolgende Anzahl an Konsonanten
und geben Sie diese zusammen mit dem Wort aus. Sie d¨ urfen davon ausgehen, dass nur
das lateinische Alphabet verwendet und die W¨ orter korrekt getrennt wurden.
Hinweis: Konsonanten sind alle Buchstaben außer a,e,i,o,u, wobei Groß- und Kleinschrei-
bung keine Rolle spielt.
F¨ ur den eingegebenen Satz Technik macht Spass w
¨ urde die Ausgabe also wie folgt lauten:
Technik 3
macht 3
Spass 2"""
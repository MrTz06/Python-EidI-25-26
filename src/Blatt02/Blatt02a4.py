# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)
s= input("Geben Sie eine Zeichenkette ein: ")
z = input("Geben Sie ein Zeichen ein: ")
position = -1
for i in range(len(s)):
    if s[i] == z:
        position = i
        break
print(position)


"""Hausaufgabe 4 (2 Punkte):
Schreiben Sie ein Programm, welches vom Nutzer eine Zeichenkette und ein Zeichen ein-
liest und die erste Position des Zeichens in der Zeichenkette ausgibt, falls diese existiert.
Ansonsten soll -1 ausgegeben werden. Hierbei ist, wie gewoehnlich, die Position des ersten
Zeichen die Position 0. Sie duerfen davon ausgehen, dass die zweite Eingabe tatsaechlich ein
einzelnes Zeichen, d.h. eine Zeichenkette der L¨ ange 1, ist."""
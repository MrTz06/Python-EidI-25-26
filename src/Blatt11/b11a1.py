# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)



def det(M):
    a00, a01, a02 = M[0]
    a10, a11, a12 = M[1]
    a20, a21, a22 = M[2]
    return (a00 * a11 * a22
        + a01 * a12 * a20
        + a02 * a10 * a21
        - a02 * a11 * a20
        - a01 * a10 * a22
        - a00 * a12 * a21)

def show(M):
    # Bestimmt die maximale Breite jeder Spalte
    column_widths = [0, 0, 0]
    for row in M:
        for j in range(3):
            column_widths[j] = max(column_widths[j], len(str(row[j])))

    # Gibt die Matrix mit korrekter Ausrichtung aus
    for row in M:
        formatted_row = " ".join(f"{str(row[j]):<{column_widths[j]}}" for j in range(3))
        print(formatted_row)
    print()  # Leerzeile am Ende

def zero_determinant(entries):
    from copy import deepcopy

    def backtrack(matrix, row, column, used):
        if row == 3:
            if det(matrix) == 0:
                show(matrix)
            return

        next_row, next_col = (row, column + 1) if column < 2 else (row + 1, 0)

        for entry in entries:
            if used.get(entry, 0) < entries.count(entry):
                matrix[row][column] = entry
                used[entry] = used.get(entry, 0) + 1
                backtrack(matrix, next_row, next_col, used)
                used[entry] -= 1

    initial_matrix = [[0]*3 for _ in range(3)]
    backtrack(initial_matrix, 0, 0, {})
    return None









"""Hausaufgabe 1 (1 + 2 + 5 = 8 Punkte):
Das Ziel dieser Aufgabe ist es, eine Funktion zero_determinant zu schreiben, welche
eine Liste von Ganzzahlen entries erwartet und alle 3 ×3-Matrizen, deren Eintr¨
age aus
entries stammen und deren Determinante 0 ist berechnet.
In dieser Aufgabe sollen 3 ×3-Matrizen als eine Liste der L¨ ange drei dargestellt werden,
wobei jeder der Eintr¨ age wiederum eine Liste der L¨ ange drei ist, welche f¨ ur eine Zeile der
Matrix steht (angefangen mit der obersten Zeile).
(a) Schreiben Sie eine Hilfsfunktion det, die eine Matrix M, wie oben beschrieben, erwartet
und deren Determinante berechnet.
2
(b) Hinweis: Die Determinante einer 3 ×3-Matrix M=  a0,0 a1,0 a1,1 a1,2
a2,0 a2,1 a2,2
a0,1 a0,2
  kann wie folgt
berechnet werden:
det(M ) = a0,0·a1,1·a2,2 + a0,1·a1,2·a2,0 + a0,2·a1,0·a2,1
−a2,0·a1,1·a0,2−a2,1·a1,2·a0,0−a2,2·a1,0·a0,1
Schreiben Sie eine Hilfsfunktion show, die eine Matrix M, wie oben beschrieben, erwartet
und diese als Rechteck von Zahlen, getrennt durch Leerzeichen, auf der Konsole ausgibt.
Dabei sollen auch Matrizen, die Ganzzahlen unterschiedlicher Stelligkeit beinhalten,
korrekt ausgerichtet sein (linksb¨ undig je Spalte, siehe Beispiel). Außerdem soll im
Anschluss eine Leerzeile auf der Konsole ausgegeben werden.
Beispiel: F¨ uhrt man show([[12,2,3],[4,514,6],[7,85,9]]) aus, so soll man die
folgende Konsolenausgabe erhalten:
12 2 3
4 514 6
7 85 9
<- Leerzeile
(c) Schreiben Sie die Funktion zero_determinant, deren Funktionalit¨ at zu Beginn be-
schrieben wurde. Als Eingabe erwartet die Funktion also die Liste entries. Alle
3 ×3-Matrizen mit den genannten Eigenschaften sollen mittels Backtracking be-
rechnet und mit Hilfe Ihrer Funktion show auf der Konsole ausgegeben werden. Jede
L¨ osung soll genau einmal ausgegeben werden, es darf also keine L¨ osung mehrfach
ausgegeben werden.
Die R¨ uckgabe der Funktion ist None.
Hinweis: Wenn Sie from copy import deepcopy als erste Zeile in Ihr Programm einf¨
ugen
k¨ onnen Sie deepcopy(L) verwenden, um einen Klon der Liste L zu erhalten, bei dem auch
die inneren Listen geklont wurden (gleiche Funktionalit¨ at wie Blatt 7 Hausaufgabe 1 (b))."""
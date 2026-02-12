# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)


def show(B):
    for row in B:
        print(" ".join(row))
    print()
def initialize_board(n):
    return [["O"] * n for _ in range(n)]
def put_queen(B, pos):
    n = len(B)
    i, j = pos
    B[i][j] = "Q"
    # Markiert die bedrohten Felder
    for x in range(n):
        for y in range(n):
            if x == i or y == j or abs(x - i) == abs(y - j):
                if B[x][y] == "O":
                    B[x][y] = "X"
def free_fields(B, row):
    return [j for j in range(len(B)) if B[row][j] == "O"]
def n_queens(n):
    def backtrack(B, row):
        if row == n:
            show(B)
            return
        for col in free_fields(B, row):
            new_board = [r[:] for r in B]  # Klont das Brett
            put_queen(new_board, (row, col))
            backtrack(new_board, row + 1)
    initial_board = initialize_board(n)
    backtrack(initial_board, 0)










"""Hinweis: Wenn Sie from copy import deepcopy als erste Zeile in Ihr Programm einf¨
ugen
k¨ onnen Sie deepcopy(L) verwenden, um einen Klon der Liste L zu erhalten, bei dem auch
die inneren Listen geklont wurden (gleiche Funktionalit¨ at wie Blatt 7 Hausaufgabe 1 (b)).
Hausaufgabe 2 (1 + 1 + 4 + 1 + 5 = 12 Punkte):
Das Ziel dieser Aufgabe ist es, eine Funktion n_queens zu schreiben, welche alle L¨
osungen
des n-Damen Problems findet. Diese lautet wie folgt:
Gegeben eine positive Ganzzahl n, platziere n Damen auf einem n ×n großen
Schachbrett, sodass keine der Damen eine der anderen Damen schlagen kann.
3
F¨ ur die Dame gelten dabei die regul¨ aren Schachregeln, d.h. sie darf eine beliebige Distanz
in eine beliebige Richtung (horizontal / vertikal / diagonal) ziehen, dabei jedoch keine
Figuren ¨ uberspringen.
Im Programm wird das Schachbrett als Liste der L¨
ange n dargestellt, wobei jeder der
Eintr¨ age wiederum eine Liste der L¨
ange n ist, welche eine Zeile des Schachbretts darstellt.
Als Eintr¨ age f¨ ur die Felder des Schachbretts (also Eintr¨ age der inneren Listen) nutzen wir 3
verschiedene Strings:
• "O" f¨ ur ein leeres Feld
• "Q" f¨ ur ein Feld mit Dame (Queen)
• "X" f¨ ur ein Feld das von mindestens einer Dame bedroht wird
Wenn wir zum Beispiel n = 5 betrachten, so sehen das leere Schachbrett, und das Schachbrett
mit einer an Position (2, 2) platzierten Damen, graphisch dargestellt, folgendermaßen aus:
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
X O X O X
O X X X O
X X Q X X
O X X X O
X O X O X
Entsprechen der Darstellung als Liste, befindet sich das Feld an Position (0, 0) oben links.
Wenn wir im Folgenden von einer Position (i, j) sprechen, so bezieht sich i auf die Zeile
und j auf die Spalte, in der sich das Feld befindet.
(a) Schreiben Sie eine Hilfsfunktion show, die ein Schachbrett B, wie oben beschrieben,
erwartet und dieses als Rechteck von Zeichen, getrennt durch Leerzeichen, auf der
Konsole ausgibt (siehe Beispiel in Aufgabenteil (e)). Außerdem soll im Anschluss eine
Leerzeile auf der Konsole ausgegeben werden.
(b) Schreiben Sie eine Hilfsfunktion initialize_board, die die Dimension des Schach-
bretts, also die positive Ganzzahl n, erwartet. Zur¨ uckgegeben werden soll das ”leere
Schachbrett“ der Gr¨ oße n ×n, also das Schachbrett in dem alle Eintr¨
age "O" sind.
Der Rumpf dieser Funktion darf nur aus einer Zeile bestehen.
Beispiel: Die R¨ uckgabe von initialize_board(3) lautet
[["O","O","O"],["O","O","O"],["O","O","O"]].
4
(c) Schreiben Sie eine Hilfsfunktion put_queen, die ein Schachbrett B und eine Position
pos (Tupel der L¨ ange 2, wie oben beschrieben) erwartet. Die Funktion soll den Effekt
haben, dass B eine Dame an Position pos hinzugef¨ ugt wird. Das heißt sowohl das
"Q", als auch alle resultierenden "X" m
¨ ussen eingetragen werden. Die R¨ uckgabe der
Funktion ist None.
Beispiel: Sei B_bsp das Schachbrett mit einer Dame an Position (2, 2), aus dem
Beispiel oben. F¨ uhrt man put_queen(B_bsp, (1,4)) aus, so stellt die im Anschluss
unter B_bsp gespeicherte Liste das folgende Schachbrett dar:
X O X X X
X X X X Q
X X Q X X
O X X X X
X X X O X
(d) Schreiben Sie eine Hilfsfunktion free_fields, die ein Schachbrett B und eine Ganzzahl
row erwartet. Die Funktion ¨ uberpr¨ uft f¨ ur die Zeile row, in welchen der Spalten "O"
eingetragen ist. Eine Liste dieser Ganzzahlen wird zur¨ uckgegeben.
Der Rumpf dieser Funktion darf nur aus einer Zeile bestehen.
Beispiel: Sei B_bsp das Schachbrett mit einer Dame an Position (2, 2), aus dem
Beispiel zu Beginn. Dann liefert free_fields(B_bsp, 3) die R¨ uckgabe [0,4] und
free_fields(B_bsp, 2) liefert die R¨ uckgabe [].
(e) Schreiben Sie die Funktion n_queens, die das n-Damen Problem l¨ ost. Als Eingabe
erwartet die Funktion die positive Ganzzahl n.
Die Funktion soll Backtracking verwenden um alle m
¨ oglichen L¨ osungen zu finden
und mit Hilfe Ihrer Funktion show auf der Konsole auszugeben. Starten Sie dabei mit
dem leeren Schachbrett und versuchen Sie zun¨ achst eine Dame in Zeile 0 zu platzieren,
dann in Zeile 1, dann in Zeile 2 usw. Nutzen Sie dabei Ihre restlichen Hilfsfunktionen.
Jede L¨ osung soll genau einmal ausgegeben werden, es darf also keine L¨ osung mehrfach
ausgegeben werden.
Die R¨ uckgabe der Funktion ist None.
Beispiel: F¨ uhrt man n_queens(5) aus, so werden auf der Konsole die 10 L¨
osungen
des 5-Damen Problems ausgegeben. Diese sehen wie folgt aus:

Q X X X X
X X Q X X X Q X X
X X X X Q
X X X X Q
X Q X X X Q X X X
X X X Q X X X Q X
Q X X X Q X X X X
X X X Q X X X Q X
Q X X X X Q X X X
X X Q X X X X X Q
X X X X Q
X X Q X X
X Q X X X Q X X X
X X X Q X X X Q X
X Q X X Q X X X X
X X X X Q
X X Q X X
X X Q X X X X X Q
Q X X X X Q X X X
X X X X Q
X X X X Q
X Q X X X X Q X X
X X X Q Q X X X X
Q X X X X X X Q X
X X Q X X X Q X X
X X X X Q
Q X X X X
X X Q X X X X Q X
Q X X X X Q X X X
X X X Q X X X X Q
X Q X X X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
Hinweis: Beachten Sie auch hier den Hinweis bez¨ uglich deepcopy aus Hausaufgabe 1."""
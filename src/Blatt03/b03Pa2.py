print("Überlegen sie sich eine Ganzzahl aus {-64, ..., 64}.")

orakel =""
links = -64
rechts = 64
vermutung = 0

while orakel != "=":
    orakel = input("Ist die Zahl größer (>), kleiner (<) oder gleich (=) " + str(vermutung) + "? ")
    if orakel == "<":
        rechts = vermutung - 1
    elif orakel == ">":
        links = vermutung + 1
    vermutung = (links + rechts) // 2

print("Die gesuchte Zahl ist die " + str(vermutung) + ".")




"""Pr¨ asenzaufgabe 2:
Schreiben Sie ein Programm, welche eine vom Nutzer gew¨ ahlte ganze Zahl (von -64 bis
64) mittels bin¨ arer Suche err¨ at. Das Programm soll in jedem Schritt daf¨ ur eine Vermutung
anstellen, welche Zahl der Nutzer gew¨ ahlt hat und der Nutzer muss antworten, ob die
gew
¨ ahlte Zahl gr¨ oßer, kleiner oder gleich der Vermutung ist.
Beispiel:
¨
Uberlegen Sie sich eine Ganzzahl aus {-64,...,64}.
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 0? >
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 32? <
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 16? >
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 24? <
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 20? >
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 22? <
Ist die Zahl gr¨oßer [>], kleiner [<] oder gleich [=] 21? =
Die gesuchte Zahl ist die 21."""
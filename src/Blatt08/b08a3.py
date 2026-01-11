# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def wort_paare(string):

    woerter = string.split(" ")
    paare_wb = {}
    for i in range(len(woerter)-1):
        paar = (woerter[i], woerter[i+1])
        if paar in paare_wb:
            paare_wb[paar] += 1
        else:
            paare_wb[paar] = 1
    return paare_wb












"""Hausaufgabe 3 (2 Punkte):
Schreiben Sie eine Funktion wort_paare, welche als Eingabe einen String erwartet, der
aus mehreren W¨ ortern besteht, die jeweils durch genau ein Leerzeichen getrennt sind.
Zur¨ uckgegeben werden soll ein W¨ orterbuch, welches angibt wie oft W¨ orter aufeinander
folgen, d.h. als Schl¨ ussel sollen alle Tupel (w1,w2) vorkommen, sodass die W¨ orter w1 und
w2 in der Eingabe hintereinander vorkommen. Der zugeordnete Wert soll angeben, wie oft
diese Wortkombination in der Engabe vorkommt.
Beispiel:
wort_paare("der Hund l¨auft und der Hund l¨auft schnell und der Hund bellt")
liefert als R¨ uckgabe ein W¨ orterbuch der Form
{("der","Hund"):3, ("Hund","l¨auft"):2, ("l¨auft","und"):1, ("und","der"):2,
("l¨auft","schnell"):1, ("schnell","und"):1, ("Hund","bellt"):1}"""
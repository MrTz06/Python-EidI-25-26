def schaltjahr (jahr):
    if (jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0):
        return True
    else:
        return False
def tage_im_monat(monat, jahr):
    if monat in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif monat in [2, 4, 6, 9, 11]:
        return 30
    elif monat == 2:
        #if schaltjahr(jahr)==True:
        #return 29
        #else: return 28
        return 28 + schaltjahr(jahr)
    else :
        return 0

def datum_check(tag, monat, jahr):
    if 0 < tag <= tage_im_monat(monat, jahr):  #and 1<=monat<=12
        return True
    else:
        return False


Tag= int(input())
monat= int(input())
jahr= int(input())
print(datum_check(Tag, monat, jahr))










"""Pr¨ asenzaufgabe 3:
Schreiben Sie ein Programm, welches folgende Funktionen definiert. Sie k¨ onnen davon
ausgehen, dass die Funktionen nur mit Ganzzahlen aufgerufen werden:
• Eine Funktion schaltjahr, welche eine Ganzzahl (Jahr) entgegen nimmt und pr¨ uft,
ob es sich um ein Schaltjahr handelt. In diesem Fall soll True zur
¨ uck gegeben werden,
sonst False.
Hinweis 1: Ein Jahr ist ein Schaltjahr, wenn es durch 400 teilbar ist oder wenn es
durch 4 aber nicht durch 100 teilbar ist. Zum Beispiel waren 2000 und 2004 Schalt-
jahre, 1900 aber nicht.
• Eine Funktion tage_im_monat, welche zwei Ganzzahl (Monat, Jahr) entgegen nimmt
und zur¨ uckgibt, wie viele Tage der ¨ ubergebene Monat im ¨ ubergebenen Jahr hat. Wird
als Monat ein Wert eingegeben der nicht im Bereich 1-12 liegt, so soll 0 ausgegeben
werden.
• Eine Funktion datum_check, welche drei Ganzzahlen entgegen nimmt und pr¨ uft, ob
diese einem g¨ ultigen Datum vom Format Tag/Monat/Jahr entsprechen. Die Funktion
soll Truezur
¨ uck geben, wenn es sich um ein g¨ ultiges Datum handelt und Falsesonst.
Hinweis 1: Ein Datum ist g¨ ultig, wenn der Tag eine positive Ganzzahl ist, die zum
Monat passt und der Monat im Bereich 1-12 liegt. Die Jahreszahl wird als vollst¨ andig
angegeben interpretiert, d.h. 23 entspricht dem Jahr 23 und nicht dem Jahr 2023.
Fordern Sie anschließend drei Eingaben (Tag, Monat, Jahr) vom Nutzer an, rufen Sie
datum_check auf diesen auf und geben Sie das Ergebnis aus."""
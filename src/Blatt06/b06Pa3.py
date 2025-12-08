def verknuepfen(t1,t2):
    if t1 == () and t2 == (): #oder if t1 == t2 == (): oder if t1/len(t1) == 0: weil beide tupel gleich lang sind reicht es einen zu prüfen
        return ()
    else:
        return (t1[0], t2[0]) + verknuepfen(t1[1:], t2[1:])
t1 = (1,2,3)
t2 = (4,5,6)
print(verknuepfen(t1,t2))
#Ausgabe: (1, 4, 2, 5, 3, 6)
















"""Pr¨ asenzaufgabe 3:
Schreiben Sie eine Funktion verknuepfen, welche zwei Tupel t1, t2 der selben L¨
ange
erwartet. Die Funktion soll die beiden Tupel mittels Rekursion zu einem Tupel verkn¨ upfen,
indem abwechselnd Zeichen aus t1 und t2 eingef¨ ugt werden. Das resultierende Tupel soll
zur
¨ uckgegeben werden.
Beispiel: Gibt man (1,2,3) und ("a","b","c") ein, dann erh¨ alt man die R¨ uckgabe
(1,"a",2,"b",3,"c").
"""
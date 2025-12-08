def teilmengen(liste):
    if len(liste) == 0:
        return [[]]
    teilmengen_ohne_erstes = teilmengen(liste[1:])
    teilmengen_mit_erstes = teilmengen_ohne_erstes[:]
    for pos in range(len(teilmengen_mit_erstes)):
        teilmengen_mit_erstes[pos].append(liste[0])
    return teilmengen_ohne_erstes + teilmengen_mit_erstes






""" Pr¨ asenzaufgabe 5:
    Schreibe eine Funktion teilmengen, welche als Eingabe eine Liste erwartet, die eine Menge
    repr
    ¨ asentiert, d.h. kein Eintrag kommt doppelt vor. Die Funktion soll mittels Rekursion die
    Menge aller Teilmengen berechnen und diese, repr¨ asentiert als Liste von Listen, zur¨ uckgeben.
    Die Reihenfolge, in der die Teilmengen angegeben werden, ist irrelevant, es darf sich in
    der R¨ uckgabeliste aber kein Element wiederholen, weder in der ¨ außeren, noch in einer der
    inneren Listen.
    Beispiel: Die Eingabe [1,2,3] kann z.B. die R¨ uckgabe
    [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
    liefern."""
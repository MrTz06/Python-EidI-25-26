def listen_mod(funktion, liste):
    ergebnis = []
    for element in liste:
        ergebnis.append(funktion(element))
    return ergebnis
def tupel_mod(funktion, tupel):
    ergebnis = []
    for element in tupel:
        ergebnis.append(funktion(element))
    return tuple(ergebnis)

"""
Diskussion:
Sowohl bei der Funktion listen_mod als auch bei der Funktion tupel_mod wird die ursprüngliche
Liste bzw. das ursprüngliche Tupel nicht verändert. Stattdessen wird eine neue Liste bzw. ein
neues Tupel erstellt, das die modifizierten Elemente enthält. Dies bedeutet, dass es keine
Nebeneffekte gibt, wenn diese Funktionen in einem Programm verwendet werden.
Die Konsequenz eines solchen Nebeneffekts wäre, dass die ursprünglichen Datenstrukturen
unbeabsichtigt verändert werden könnten, was zu unerwartetem Verhalten im Programm führen
kann. Um dies zu umgehen, ist es wichtig, dass Funktionen, die Datenstrukturen
modifizieren, neue Kopien dieser Strukturen zurückgeben, anstatt die Originale zu verändern.
Dies fördert die Unveränderlichkeit und erleichtert das Debuggen und Verstehen des Codes
"""








"""Pr¨ asenzaufgabe 2:
(a) Schreiben Sie eine Funktion listen_mod, welche als Eingabe eine Funktion und
eine Liste erwartet. Die Funktion soll auf jedes Element der Liste angewendet und
die resultierende Liste zur¨ uckgegeben werden. Sie k¨ onnen davon ausgehen, dass die
eingegebene Funktion und die eingegebene Liste zueinander passen, d.h. dass die
Funktion auf Elemente der Liste anwendbar ist.
(b) Schreiben Sie eine Funktion tupel_mod, welche die gleiche Aufgabe hat wie in Teil
(a) beschrieben, jedoch soll statt einer Liste ein Tupel eingegeben, modifiziert und
zur
¨ uckgegeben werden.
Diskutieren Sie außerdem, ob eine eingegebene Liste bzw. ein eingegebenes Tupel durch die
Ausf¨ uhrung Ihrer Funktion ver¨ andert wird. Welche Konsequenz hat ein solcher Nebeneffekt,
wenn man die Funktion in einem Programm verwendet? Wie kann man das umgehen?"""
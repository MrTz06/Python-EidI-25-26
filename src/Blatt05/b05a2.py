# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)


def preimage(funktion, startintervall, zielintervall):
    ergebnis = []
    start_start, start_ende = startintervall
    ziel_start, ziel_ende = zielintervall

    for zielwert in range(ziel_start, ziel_ende + 1):
        passende_werte = []
        for wert in range(start_start, start_ende + 1):
            if funktion(wert) == zielwert:
                passende_werte.append(wert)
        ergebnis.append(passende_werte)

    return ergebnis





"""Hausaufgabe 2 (5 Punkte):
Schreiben Sie eine Funktion preimage, welche drei Eingaben erwartet: funktion,
startintervall und zielintervall. Hierbei ist funktion eine Funktion, welche einen
Integer-Wert erwartet und einen Integer-Wert zur¨ uckgibt. Die Eingaben startintervall
und zielintervall sind Paare von Integer-Werten, also Tupel der L¨ ange zwei. Hierbei steht
das Paar (i, j) f¨ ur das mathematische Ganzzahl-Intervall [i, j], also die Werte i, i + 1, ..., j.
Die Funktion soll eine Liste von Listen zur¨ uckgeben, wobei jede der inneren Listen f¨
ur
einen Funktionswert aus dem Zielintervall steht. Die inneren Listen sollen jeweils die Werte
aus dem Startintervall enthalten, welche unter der eingegebenen Funktion funktion auf
den entsprechenden Zielwert abbilden. Sie d¨ urfen davon ausgehen, dass die Eingaben wie
beschrieben sind.
Hinweis: Wenn f¨ ur die Integer-Werte i > j gilt, dann ist [i, j] das leere Intervall.
Beispiele: Seien die folgenden beiden Funktionen im Programm definiert:
def g (zahl):
return zahl+1
def h (zahl):
return 1
Dann sollen die folgenden Funktionsaufrufe von preimage die angegebenen Listen zur¨ uckgeben:
• preimage(g,(-2,2),(-2,2)) → [[], [-2], [-1], [0], [1]]
• preimage(g,(6,10),(9,13)) → [[8], [9], [10], [], []]
• preimage(h,(12,14),(0,3)) → [[], [12,13,14], [], []]
• preimage(h,(12,14),(3,2)) → []"""
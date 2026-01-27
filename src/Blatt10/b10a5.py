# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
import random

def rand_labyrinth():
    length = random.randint(1,23)
    out = []
    for step in range(length):
        out.append(random.choice(["R","L"]))
    return out

loesung = rand_labyrinth()
def solve_labyrinth(weg=None):
    if weg is None:
        weg = []
    #Basisfall: Lösung gefunden
    if weg == loesung:
        return weg
    #Abbruchbedingung: zu lange Wege
    if len(weg) >= 23:
        return None
    #Rekursiver Fall: versucht "R" und "L" hinzuzufügen
    for richtung in ["R", "L"]:
        neuer_weg = weg + [richtung]
        ergebnis = solve_labyrinth(neuer_weg)
        if ergebnis is not None:
            return ergebnis
    return None







"""In dieser Aufgabe sollen Sie eine Funktion solve_labyrinth schreiben, welche den Weg
aus einem Labyrinth findet. In diesem Labyrinth kann man an jeder Verzweigung w¨ ahlen
entweder nach rechts ("R") oder nach links ("L") zu gehen. Außerdem kann man davon
ausgehen, dass man nach sp¨ atestens 23 Abzweigungen den Ausgang erreicht, wenn man
den richtigen Weg gew¨ ahlt hat. Die L¨ osung soll als Liste von "R" und "L" dargestellt und
zur
¨ uckgegeben werden.
Das Labyrinth selbst ist unbekannt, der korrekte Weg wird zuf¨ allig bestimmt und im
Hauptprogramm unter der Variablen loesung gespeichert (ebenfalls als Liste von "R" und
"L"). Dieser Teil des Programms steht Ihnen in der Datei b10a5.py zur Verf¨ ugung. Auf die
Variable loesung d¨ urfen Sie nur in Anweisungen der Form L==loesung zugreifen, wobei L
irgendeine Liste ist.
Nutzen Sie Backtracking um die Aufgabe zu l¨ osen. Sie d¨ urfen der Funktion solve_-
labyrinth Hilfsparameter ¨ ubergeben, um das Backtracking zu erm¨ oglichen. Sonst erh¨ alt
die Funktion solve_labyrinth keine Eingaben. Geben Sie auch den Funktionsaufruf von
solve_labyrinth an, der bei Ausf¨ uhrung loesung findet und zur¨ uckgibt."""
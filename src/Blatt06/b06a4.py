# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)



def enthaelt(liste, element):
    if len(liste) == 0:
        return False
    elif liste[0] == element:
        return True
    else:
        return enthaelt(liste[1:], element)




"""Hausaufgabe 4 (3 Punkte):
Schreiben Sie eine Funktion enthaelt, welche als Eingabe eine Liste und eine weitere
Eingabe element erwartet. Die Funktion soll mittels Rekursion bestimmen, ob element als
Eintrag in der Liste vorkommt. Falls ja soll True ausgegeben werden, sonst False.
Beispiele:
• Gibt man [2,"b",9] und 2 ein, dann erh¨ alt man die R¨ uckgabe True.
• Gibt man [2,[1],[2]] und [1] ein, dann erh¨ alt man die R¨ uckgabe True.
• Gibt man [2,"ab",9] und "a" ein, dann erh¨ alt man die R¨ uckgabe False.
• Gibt man [1,[[1]],[1,[1]]] und [1] ein, dann erh¨ alt man die R¨ uckgabe False"""
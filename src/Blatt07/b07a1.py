# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)



#a)
def int_superliste(liste):
    #Basisfall 1: liste ist keine Liste
    if type(liste) != list:
        return False
    #Basisfall 2: leere Liste ist eine int-Superliste
    if len(liste) == 0:
        return True

    #Bedinung 1: Alle Elemente sind int
    def alle_elemente_int(liste):
        if liste == []:
            return True
        #Kopf prüfen
        elif type(liste[0]) != int:
            return False
        #Tail prüfen
        else:
            return alle_elemente_int(liste[1:])


    #Bedinung 2: Alle Elemente sind int-Superlisten
    def alle_elemente_superliste(liste):
        if liste == []:
            return True
        #Kopf prüfen
        if type(liste[0]) != list:
            return False
        #Tail prüfen
        else:
            return int_superliste(liste[0]) and alle_elemente_superliste(liste[1:])

    #Überprüfung der beiden Bedingungen
    return alle_elemente_int(liste) or alle_elemente_superliste(liste)


#b)
def klonen(liste):
    #Basisfall: leere Liste klonen
    if liste == []:
        return []
    #Basisfall: int klonen
    elif type(liste[0]) == int:
        return liste[0]
    #rekursiver Fall: Liste klonen
    else:
        return [klonen(liste[0])] + klonen(liste[1:])







"""Hausaufgabe 1 (4 + 3 = 7 Punkte):
Wie in der Vorlesung besprochen, k¨ onnen Sie in Python eine Liste L durch den Befehl L[:]
klonen. Dies klont jedoch nur die ¨ außere Liste L und nicht die Elemente von L, die selbst
auch ver¨ anderlich sind: Folgendes Python-Programm
L=[1,3]
K=[L,[2]]
U=K[:]
print(U)
klont zwar die Liste K und liefert die Ausgabe [[1,3],[2]], falls Sie diesem Programm
jedoch die folgenden beiden Zeilen
L.append(4)
print(U)
anh¨
angen w
¨ urden, erhielten Sie die Ausgaben [[1,3],[2]] und [[1,3,4],[2]]. Die
Unterliste L hat also einen Seiteneffekt (der Tiefe 2) erzeugt, da die Unterliste [1,3] in K
selbst nicht geklont wurde. Genauso k¨ onnen u.U. Seiteneffekte in Tiefe 3 auftreten, indem
Sie eine Liste modifizieren, die in einer Liste vorkommt, die selbst wiederum in einer Liste
vorkommt (und so weiter).
Eine int-Superliste ist rekursiv folgendermaßen definiert:
• Jede Liste, deren Elemente alle vom Typ int sind, ist eine int-Superliste.
• Jede Liste deren Elemente alle int-Superlisten sind, ist eine int-Superliste.
2
(a) Schreiben Sie eine rekursive Funktion int_superliste, die als Eingabe eine Liste
erwartet und ¨ uberpr¨ uft, ob es sich dabei um eine int-Superliste handelt, also True
zur
¨ uckgibt, falls es sich um eine int-Superliste handelt und sonst False.
Hinweis: Z.B. die Liste [1,[1],3] ist keine int-Superliste, denn keine der beiden Be-
dingungen ist erf¨ ullt. Z.B. die Liste [[1,2],[[1],[3,4]],[3]] ist eine int-Superliste.
(b) Schreiben Sie eine rekursive Funktion klonen, die als Eingabe eine int-Superliste
erwartet und einen Klon der int-Superliste zur¨ uckgibt, also eine Kopie bei der die
oben beschriebenen Seiteneffekte ausbleiben, d.h. es gibt keine Seiteneffekte beliebiger
Tiefe.
Achtung: F¨ ur diese Aufgabe d¨ urfen Sie nur Python-Befehle verwenden, welche Sie in der
Vorlesung kennen gelernt haben. Insbesondere ist die Verwendung des Befehls deepcopy
nicht erlaubt!"""
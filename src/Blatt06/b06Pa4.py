def ist_anagramm(w, v):
    #Basisfall: Wenn beide Strings leer sind, sind sie Anagramme
    if w == "" and v == "":
        return True
    #Wenn die Längen unterschiedlich sind, können sie keine Anagramme sein
    if len(w) != len(v):
        return False
    #Wenn das erste Zeichen von w nicht in v ist, sind sie keine Anagramme

    if w[0] not in v:
        return False
    #Rekursiver Fall: Entferne das erste Zeichen von w und das erste Vorkommen dieses Zeichens in v
    return ist_anagramm(w[1:], v.replace(w[0], "", 1))


"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Rekursion: Das Programm demonstriert die Verwendung von Rekursion zur Lösung des Anagramm-Problems,
indem es das Problem in kleinere Teilprobleme zerlegt.
2. String-Manipulation: Es zeigt, wie man Strings in Python manipulieren kann, insbesondere mit der Methode replace(),
um Zeichen zu entfernen.
3. Basis- und Rekursionsfälle: Das Programm illustriert die Bedeutung von Basisfällen und rekursiven Fällen in rekursiven Funktionen,
um sicherzustellen, dass die Funktion korrekt funktioniert und terminiert.
"""

















"""
Pr¨ asenzaufgabe 4:
Schreiben Sie eine Funktion ist_anagramm, welche als Eingabe zwei Strings w, v erwartet.
Die Funktion soll mittels Rekursion berechnen, ob w ein Anagramm von v ist, d.h. ob w
und v aus den gleichen Zeichen bestehen und jedes Zeichen gleich oft vorkommt. Falls ja
soll True ausgegeben werden, sonst False.
Beispiele:
• Gibt man "ABLEGER" und "GELABER" ein, dann erh¨ alt man die R¨ uckgabe True.
• Gibt man "Ableger" und "Gelaber" ein, dann erh¨ alt man die R¨ uckgabe False.
• Gibt man "AFFE" und "AFEE" ein, dann erh¨ alt man die R¨ uckgabe False.
• Gibt man "aaa" und "aa" ein, dann erh¨ alt man die R¨ uckgabe False.
Hinweis: Ist z ein Zeichen (String der L¨ ange 1) und s ein String, dann liefert
s.replace(z, "", 1) einen neuen String, der aus s entsteht, indem das erste Vorkommen
von z entfernt wird. Solange das Zeichen tats¨ achlich enthalten ist bewirkt diese Anweisung
also das gleiche auf Strings, was L.remove(z) auf einer Liste L bewirkt."""
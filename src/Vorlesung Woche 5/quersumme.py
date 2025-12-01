def alternative(n):
    summe=0
    for a in str(n):
        summe+=int(a)
    return summe

def quersumme_str(s):
    if len(s)==1:
        return int(s)
    return quersumme_str(s[:-1]) + int(s[-1])

def quersumme(n):
    return n if n<10 else quersumme(n//10)+n%10
"""
    if n<10:
        return n
    return quersumme(n//10)+n%10
   """ 


while True:
    n=int(input("Geben Sie eine Zahl ein: "))
    print("Quersumme("+str(n)+")=",quersumme(n))


    """
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Quersumme: Das Programm berechnet die Quersumme einer Zahl, also die Summe ihrer Ziffern.
 Dies ist eine grundlegende mathematische Operation, die in verschiedenen Anwendungen nützlich sein kann.
2. Rekursion: Die Funktion quersumme(n) verwendet Rekursion, um die Quersumme zu berechnen. 
 Dies zeigt, wie rekursive Funktionen in Python implementiert werden können.
3. String-Manipulation: Die Funktion quersumme_str(s) demonstriert, wie man Strings in Python manipulieren kann,
    indem man einzelne Zeichen extrahiert und in Ganzzahlen umwandelt.
4. Schleifen: Die Funktion alternative(n) verwendet eine for-Schleife, um über die Ziffern einer Zahl zu iterieren.
 Dies zeigt, wie Schleifen in Python verwendet werden können, um wiederholte Aufgaben zu erledigen.
5. Benutzereingabe: Das Programm zeigt, wie man Benutzereingaben in Python verarbeitet, indem es den Benutzer auffordert, eine Zahl einzugeben.
"""

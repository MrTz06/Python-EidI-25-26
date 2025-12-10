#Dieses Programm aus der Vorlesung löst das Türme-von-Hanoi-Problem mithilfe von Rekursion.

def hanoi(n,start,zwischen,ziel):
    if n==1:
        print(start + " ==> " + ziel)
    else:
        hanoi(n-1,start,ziel,zwischen)
        print(start + " ==> " + ziel)
        hanoi(n-1,zwischen,start,ziel)

n=int(input("Geben ein n an: "))
hanoi(n,"A","B","C")




"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Rekursive Funktionen: Das Programm demonstriert die Verwendung von Rekursion zur Lösung eines Problems, 
indem eine Funktion sich selbst aufruft, um kleinere Teilprobleme zu lösen.
2. Problemzerlegung: Das Türme-von-Hanoi-Problem wird in kleinere Schritte zerlegt, was zeigt, 
wie komplexe Probleme durch die Lösung von einfacheren Teilproblemen angegangen werden können.
3. Parameterübergabe: Die Funktion hanoi verwendet Parameter, um den aktuellen Zustand des Problems zu verfolgen (Anzahl der Scheiben und die Namen der Stäbe),
was die Flexibilität und Wiederverwendbarkeit der Funktion erhöht.
4. Ausgabeformatierung: Das Programm zeigt, wie man Ausgaben formatiert, um die Schritte zur Lösung des Problems klar darzustellen.

Häufig mögliches Vorgehen bei Rekursionsaufgaben: 
1. Basisfall definieren: Identifizieren Sie den einfachsten Fall des Problems, der direkt gelöst werden kann (z.B. n==1).
2. Rekursiven Fall definieren: Bestimmen Sie, wie das Problem in kleinere Teilprobleme zerlegt werden kann (z.B. n-1 Scheiben bewegen).
3. Funktionsaufrufe strukturieren: Implementieren Sie die rekursiven Aufrufe innerhalb der Funktion, um die Teilprobleme zu lösen.
4. Testen und validieren: Überprüfen Sie die Funktion mit verschiedenen Eingabewerten, um sicherzustellen, dass sie korrekt funktioniert.
"""

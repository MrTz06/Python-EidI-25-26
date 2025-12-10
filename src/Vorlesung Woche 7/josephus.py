#Dieses Programm aus der Vorlesung implementiert die Josephus-Funktion J(n) rekursiv.
# Die Josephus-Funktion gibt die Position des Überlebenden in einem speziellen Eliminationsspiel
# mit n Teilnehmern zurück, wobei jeder zweite Teilnehmer eliminiert wird.
import bin

def J(n):
    if n<=1:
        return 1
    if n%2==0: ### n ist gerade
        return 2*J(n//2)-1
    else: ### n ist ungerade
        return 2*J(n//2)+1

def J_neu(n):
    return bin.zahl(bin.bin(n)[1:]+"1")

if __name__=="__main__":
    for n in range(21):
        print("J("+str(n)+")="+str(J(n)))
        print("J_neu("+str(n)+")="+str(J_neu(n)))


"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Was ist die Josephus-Funktion: Das Programm implementiert die Josephus-Funktion, 
die in der Kombinatorik und Spieltheorie verwendet wird, um die Position des Überlebenden in einem Eliminationsspiel zu bestimmen.
2. Rekursive Funktionen: Das Programm zeigt, wie man rekursive Funktionen in Python definiert und verwendet,
um Probleme zu lösen, die sich in kleinere Teilprobleme zerlegen lassen.
3. Bedingte Anweisungen: Die Verwendung von if-else-Anweisungen zur Unterscheidung zwischen geraden und ungeraden Zahlen wird demonstriert,
was in vielen Algorithmen nützlich ist.
4. Binäre Darstellung: Die Funktion J_neu zeigt, wie man die binäre Darstellung von Zahlen verwenden kann,
um die Josephus-Position effizient zu berechnen.
"""
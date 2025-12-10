#Dieses Programm aus der Vorlesung definiert eine rekursive Funktion, die eine Liste umkehrt.
def umdrehen(L):
    if len(L)<=1:
        return L
    return [L[-1]]+umdrehen(L[:-1])


L=[[4,2,[23,3]],5,7,8]
# beim Aufruf umdrehen(L) soll [8,7,5,4] zurückgegenen werden
print(umdrehen(L))



"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig? (Keine Dopplung, nur Neues!)
1. Rekursion: Das Programm demonstriert die Verwendung von Rekursion zur Lösung eines Problems,
   indem die Funktion sich selbst aufruft, um die Liste schrittweise zu verkleinern.
2. Listenmanipulation: Es zeigt, wie man Listen in Python manipulieren kann, indem man das letzte Element extrahiert
   und es mit dem Ergebnis der rekursiven Umkehrung der restlichen Liste kombiniert.
3. Basisfall in Rekursion: Das Programm verdeutlicht die Bedeutung eines Basisfalls (len(L)<=1), 
um die Rekursion zu beenden und eine korrekte Rückgabe zu gewährleisten.
"""
### erwartet eine Liste L, deren Einträg
### selbst Listen sind, die ebenfalls
### kopiert werden sollen
def kopietiefe2(L):
    ergebnis=[]
    for e in L:
        ergebnis.append(e)
    return ergebnis

L=[[1,2],[3,4],[5,6,7]]
#K=L[:]
K=kopietiefe2(L)
K[0][0]=17
print("L=",L)
print("K=",K)

"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?

1. Tiefe Kopie von Listen: Das Programm demonstriert, wie man eine tiefe Kopie einer Liste von Listen in Python erstellt.
   Dies ist wichtig, um sicherzustellen, dass Änderungen an den inneren Listen der kopierten Liste die ursprüngliche Liste nicht beeinflussen.
2. Listenmanipulation: Es zeigt, wie man Listen iteriert und Elemente zu einer neuen Liste hinzufügt.
3. Vermeidung von Seiteneffekten: Durch die Erstellung einer tiefen Kopie wird verhindert, dass Änderungen an der kopierten Liste Auswirkungen auf die ursprüngliche Liste haben,
   was zu unerwarteten Seiteneffekten führen könnte.
   
"""
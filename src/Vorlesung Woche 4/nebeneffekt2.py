K=[4,5,6]
U=[22,K]
V=U[:] ### Kopie von U
U[1]=23980712309812
print("U= ",U)
print("V= ",V)


"""
Zusammenfassung/Was kann ich (auf Python bezogen) NEUES aus diesem Programm lernen/Wozu ist das wichtig?
1. Listen und Verschachtelung: Das Programm zeigt, wie Listen in Python erstellt und verschachtelt werden können, 
indem eine Liste (K) innerhalb einer anderen Liste (U) verwendet wird.
2. Listen-Kopien: Die Verwendung von U[:] demonstriert, wie man eine flache Kopie einer Liste erstellt, 
um Änderungen an der Original-Liste (U) zu vermeiden, die sich auf die Kopie (V) auswirken könnten.
3. Referenzverhalten: Das Programm verdeutlicht das Verhalten von Listen in Python hinsichtlich Referenzen und wie Änderungen an einer Liste 
die Kopie nicht beeinflussen, wenn eine Kopie erstellt wurde.

"""
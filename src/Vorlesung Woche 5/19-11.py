#Liste von Listenkopie
#Kopie von Listen auf Tiefe 2
#erwartet eine Liste L, deren Einträge selber listen sind, die ebenfalls kopiert werden sollen
def kopietiefe2(L):
    ergebnis = []
    for eintrag in L:
        ergebnis.append(eintrag[:])

    return ergebnis

L=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
M=L[:] #flache Kopie
M[0][0]=999
print("L nach flacher Kopie und Änderung von M: ", L)
N=kopietiefe2(L) #tiefe Kopie
N[0][0]=555
print("L nach tiefer Kopie und Änderung von N: ", L)
"""Unterschied zwischen flacher und tiefer Kopie von Listen:
Bei einer flachen Kopie (wie mit L[:]) wird nur die äußere Liste kopiert, während die inneren Listen weiterhin auf die gleichen Objekte verweisen. 
Änderungen an den inneren Listen in der Kopie wirken sich daher auch auf die Original-Liste aus.
Bei einer tiefen Kopie (wie mit der Funktion kopietiefe2) werden sowohl die äußere Liste als auch die inneren Listen kopiert. 
Dadurch sind Änderungen an den inneren Listen in der Kopie unabhängig von der Original-Liste.
Wofür ist das wichtig?
Es ist wichtig, wenn man sicherstellen möchte, dass Änderungen an einer Kopie einer Liste die Original-Liste nicht beeinflussen, 
insbesondere wenn die Liste verschachtelte Strukturen enthält.
"""
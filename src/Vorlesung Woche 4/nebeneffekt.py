L=[22]
K=[1,2,3]
L.append(K)
K[1]=15
print(L)

"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Listen und Referenzen: Das Programm zeigt, dass Listen in Python als Referenzen behandelt werden. 
Wenn eine Liste in eine andere Liste eingefügt wird, wird nicht eine Kopie der Liste erstellt, 
sondern eine Referenz auf die ursprüngliche Liste gespeichert.
2. Seiteneffekte: Änderungen an der ursprünglichen Liste (K) wirken sich auf die eingefügte Liste (L) aus,
da beide auf dasselbe Objekt im Speicher verweisen. Dies verdeutlicht das Konzept der Seiteneffekte in der Programmierung.
3. Listenoperationen: Das Programm demonstriert die Verwendung der append()-Methode, um Elemente zu einer Liste hinzuzufügen.
"""
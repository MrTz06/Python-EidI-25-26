x = input("Bitte geben sie einen String ein: ")

out = ""
for laenge in range(1, len(x)+1):
    for start in range(0, len(x)-laenge+1):
       out += x[start:start+laenge]+ ","
        #oder print(x[start:start+laenge], end=","[:-1])

print(out[:-1])

"""
Pr¨ asenzaufgabe 1:

Schreiben Sie ein Programm, welches einen String x einliest und anschließend alle Teil-
strings von x, durch Kommas getrennt, ausgibt. Dabei sollen die Teilstrings sortiert nach
ihrer L¨ ange und ihrem Startpunkt ausgegeben werden, d.h. zuerst alle Teilstrings der L¨
ange
1, dann alle Teilstrings der L¨ ange 2, usw. Die Teilstrings gleicher L¨ ange sollen nach ihrem
Startpunkt sortiert sein, d.h. der Teilstring beginnend bei Index 0 kommt vor dem begin-
nend bei Index 1, usw.
Beispiele:
> 01234
0,1,2,3,4,01,12,23,34,012,123,234,0123,1234,01234
> abbc
a,b,b,c,ab,bb,bc,abb,bbc,abbc
"""
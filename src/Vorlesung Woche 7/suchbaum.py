#Dieses Programm aus der Vorlesung demonstriert die Implementierung eines optimalen binären Suchbaums
#mittels dynamischer Programmierung und rekursiver Ansätze in Python.
import time


leerbaum=()


def init1():
    begriffec = ["1","2","3","4", "5", "6","7"]
    j=0
    d=7
    begriffe = [begriffec[i] for i in range(j,j+d)]
    haeufigkeitc = [0.18,0.22,0.15,0.1,0.06,0.04,0.25]
    haeufigkeit = [haeufigkeitc[i] for i in range(j,j+d)]
    return (len(begriffe),begriffe,haeufigkeit)

def init3():
    begriffe = ["x","y","z"]
    haeufigkeit = [0.33,0.33,0.34]
    return (len(begriffe),begriffe,haeufigkeit)




def init2():
    begriffe = ["a","an","and", "by", "effects", "for", "from", "high", "in", "of", "on", "the", "to", "with"]
    haeufigkeit = [32,7,69,13,6,15,10,8,64,142,22,79,18,9]
    return (len(begriffe),begriffe,haeufigkeit)

def ausgabe(baum):
    if not baum:
        return ""
    ## Baum ist nicht leer
    return "("+ausgabe2(baum[0])+begriffe[baum[1]]+\
            ausgabe2(baum[2])+")"



def gg(baum):
    def gewichtet(baum,faktor):
        if baum==leerbaum:
            return 0
        else:
            return faktor*haeufigkeit[baum[1]] +\
                    gewichtet(baum[0],faktor+1) +\
                    gewichtet(baum[2],faktor+1)
    return gewichtet(baum,1)


def loeseRekursiv(i,j):
    if i==j:
        return leerbaum
    if j==i+1:
        return (leerbaum,i,leerbaum)
    else:
        baum = (leerbaum,i,loeseRekursiv(i+1,j))
        for k in range(i+1,j):
            links = loeseRekursiv(i,k)
            rechts = loeseRekursiv(k+1,j)
            if gg((links,k,rechts)) < gg(baum):
                baum = (links,k,rechts)
        return baum

def loeseDP():
    ergebnis = {}
    for g in range(0,n+1):
        for i in range(n+1):
            j=i+g
            if j in range(n+1):
                if i == j: 
                    ergebnis[(i,j)]=leerbaum
                elif j==i+1:
                    ergebnis[(i,j)]=(leerbaum,i,leerbaum)
                else:
                    baum = (leerbaum,i,ergebnis[(i+1,j)])
                    for k in range(i+1,j):
                        links=ergebnis[(i,k)]
                        rechts=ergebnis[(k+1,j)]
                        if gg((links,k,rechts)) < gg(baum):
                            baum = (links,k,rechts)
                    ergebnis[(i,j)]=baum
    out=""

    out+=" j=   "
    for j in range(0,n):
        out+=str(j+1)
        out+="     "
    for i in range(0,n):
        out+="\n"
        out+="i=" +str(i+1)
        out+="   "
        for j in range(1,n+1):
            if i<j:
                out+=str(round(gg(ergebnis[(i,j)]),2))
            else:
                out+="    "
            out+="  "
    print(out)
    print(gg(ergebnis[(0,n)]))
    print(ausgabe(ergebnis[(0,n)]))
    return ergebnis[(0,n)]              

(n,begriffe,haeufigkeit)=init2()
print("n="+str(n))
loeseDP()
print(len(begriffe))
print(begriffe)

print("\n\n")
print("Wir haben folgende Begriffe:")
print(begriffe)

print("\n mit folgender Häufigkeit:")
print(haeufigkeit)
print("\n")

t0 = time.process_time()
x=loeseDP()
t1 = time.process_time() - t0
print("Benötigte Zeit mit DP",t1,"Sekunden")

print("\n")
u0 = time.process_time()
y=loeseRekursiv(0,n)
u1 = time.process_time() - u0
print("Benötigte Zeit mit Rekursion: "+str(u1)+ " Sekunden, das ist rund " + str(int(u1/t1)) + " Mal so lang wie das DP-Verfahren" )

print("\n")
print("\n")
print("Berechneter Suchbaum mittels DP")
print(ausgabe(x))
print("Gesamtgewicht dieses Baums:"+str(gg(x)))

quit()

print("\n")
print("Berechneter Suchbaum mittels Rekursion")
#print(y)
print(ausgabe(y))
print("Gesamtgewicht dieses Baums:"+str(gg(y)))


print("\n")
print("Sie die beiden berechneten Suchbäume gleich? " + ("ja " if x==y else "nein :(")) 



"""Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Dynamische Programmierung: Das Programm demonstriert die Technik der dynamischen Programmierung zur Lösung des Problems des optimalen binären Suchbaums,
   was die Effizienz im Vergleich zu einer rein rekursiven Lösung erheblich verbessert.
2. Rekursion: Es zeigt auch, wie rekursive Funktionen definiert und verwendet werden können, um komplexe Probleme zu lösen.
3. Baumstrukturen: Das Programm illustriert die Implementierung und Manipulation von binären Suchbäumen,
   einschließlich der Berechnung von gewichteten Pfadlängen basierend auf Häufigkeiten.
4. Tupel und Datenstrukturen: Die Verwendung von Tupeln zur Darstellung von Baumknoten und die Organisation von Daten in Python wird verdeutlicht.
5. Zeitmessung: Das Programm beinhaltet die Messung der Ausführungszeit von Codeabschnitten, was wichtig für die Leistungsanalyse ist.
"""
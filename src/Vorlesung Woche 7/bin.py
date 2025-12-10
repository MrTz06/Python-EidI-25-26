#Dieses Programm aus der Vorlesung demonstriert die Umwandlung von Dezimalzahlen in Binärdarstellung
# und umgekehrt, sowie die Addition von Binärzahlen mittels Rekursion.
def add_bin(a,b,carry=0):
    if a==b=="":
        return str(carry)
    elif a=="":
        return add_bin("0",b,carry)
    elif b=="":
        return add_bin(a,"0",carry)
    summe=int(a[-1])+int(b[-1])+carry
    return  add_bin(a[:-1],b[:-1],summe//2)+str(summe%2)

def bin(n):
    return str(n) if n<=1 else bin(n//2)+str(n%2)
#if n<=1:
#        return str(n)
#    return bin(n//2)+str(n%2)

## ist die Umkehrfunktion von bin
def zahl(s):
    if len(s)==1:
        return int(s)
    return 2*zahl(s[:-1])+int(s[-1])


if __name__=="__main__":
    while True:
        n=int(input("Geben Sie eine Zahl ein: "))
        s=bin(n)
        print(f"Die Binärdarstellung von n={n} lautet: "+ 
              str(s))
        z=zahl(s)
        print("Zur Sicherheit nochmal zurückgerechnet: "+
              str(z))
        


"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Rekursion: Das Programm verwendet rekursive Funktionen, um Binärzahlen zu addieren und Dezimalzahlen in Binärdarstellung umzuwandeln.
2. Binärdarstellung: Es zeigt, wie man Dezimalzahlen in Binärzahlen umwandelt und umgekehrt.
3. String-Manipulation: Die Funktionen arbeiten mit Strings, um die Binärzahlen zu repräsentieren und zu verarbeiten.
4. Basiswissen über Zahlensysteme: Das Programm vermittelt grundlegende Konzepte der Zahlensysteme,
 insbesondere die Umrechnung zwischen Dezimal- und Binärsystemen.
"""
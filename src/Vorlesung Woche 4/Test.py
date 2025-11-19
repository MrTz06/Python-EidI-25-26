from src.Blatt03.b03a1 import *
#import random
#s="Hans, 343623425364, 1970, M, Ingenieur"
#print(s.split(", "))
""""
def zufallsstring(A, laenge):
    passwort = ""
    ziellaenge = random.choice(range(0, laenge + 1))
    for i in range(ziellaenge):
        passwort += random.choice(A)

    return passwort

A=['a','b','c']
laenge = 5
print(zufallsstring(A, laenge))
"""

"""
def alphpos(a, A):
    pos_a=A.find(a)
    return pos_a

A="abcdefg"
a="d"
print(alphpos(a,A))
"""

"""
def lexpos(s, A):
    position_s = int()
    basis_A = len(A)
    for s_i in s:
        position_s= position_s * basis_A #n = n*len(A)
        position_s= position_s + alphpos(s_i, A) # n = n + alphpos(s_i, A) (alphpos=Wert des Zeichens)

    return position_s
"""
"""
def laengenlexpos(s,A):
    laenge_s = len(s)
    position_s = lexpos(s, A) #lexikalische position s in der Gruppe mit len(s)
    basis_A = len(A)
    woerter_kuerzer_als_s = 0
    for aktuelle_laenge in range(0, laenge_s):
        woerter_kuerzer_als_s+= basis_A ** aktuelle_laenge
    position_s+= woerter_kuerzer_als_s #lexikalische position s in der Gruppe mit len(s) + alle wörter die kürzer sind als s zur basis A
return position_s
"""
"""
def trans(s, A, B):
    return wort(laengenlexpos(s, A), B)
"""

"""
def suche_z_linear(alphabet):
    n=0
    while True:
        kandidat = wort(n, alphabet)
        if gleich(kandidat, alphabet):
            return kandidat
        else :
           n+=1
"""
"""
def suche_z_binaer(alphabet, laenge):
    links = 0
    groesstes_wort = alphabet[-1]*laenge
    rechts= (laengenlexpos(groesstes_wort, alphabet))
    while links <= rechts :
        mitte= (links + rechts)//2
        kandidat = wort(mitte, alphabet)
        if kleiner(kandidat, alphabet):
            links = mitte+1
        elif groesser(kandidat, alphabet):
            rechts = mitte-1
        else :
            return kandidat

    return "Fehler in der Schleife"
"""
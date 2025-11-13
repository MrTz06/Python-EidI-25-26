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
def alphpos(a, A):
    pos_a=A.find(a)
    return pos_a

A="abcdefg"
a="d"
print(alphpos(a,A))

import sys
import time
sys.set_int_max_str_digits(100000)
zaehler=0

def nachfolger(n):
    global zaehler
    zaehler+=1
    return n+1

def vorgaenger(n):
    return nachfolger(n-2)

## funktioniert sogar für beliebige Vorzeichen
def add(m,n):
    if n<0:
        for i in range(-n):
            m=vorgaenger(m)
    else:
        for i in range(n):
            m=nachfolger(m)
    return m

### wir nehmen an, dass m,n>=0
def mult(m,n):
    m_alt=m
    if m==0 or n==0:
        return 0
    for i in range(n-1):
        m=add(m,m_alt)
        return m

### wir nehmen an, dass m,n>=0
def exp(m,n):
    if n==0:
        return 1
    else:
        m_alt=m
        for i in range(n-1):
            m=mult(m,m_alt)
        return m
def tower(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        n_alt=n
        for i in range(n_alt-1):
            #n=exp(2,n)
            n=2**n
        return n

#x=exp(2,25)
for i in range(5):
    time.sleep(1)
    print("tower("+str(i)+")="+ str(tower(i)))

#print("Ingesamt wurde nachfolger " +str(zaehler) + \
 #       "mal aufgerufen")

"""
Zusammenfassung/Was kann ich neues aus diesem Programm lernen/Wozu ist das wichtig?
In diesem Programm werden grundlegende arithmetische Operationen wie Addition, Multiplikation und Exponentiation
durch wiederholte Anwendung der Nachfolger- und Vorgängerfunktionen implementiert.
Die Funktion tower(n) berechnet die sogenannte "Tetration" also eine Potenzierung von 2, die n-mal verschachtelt ist.
Dies verdeutlicht, wie schnell bestimmte mathematische Operationen wachsen können, insbesondere bei exponentiellen und tetrationalen Funktionen.
Welche NEUEN Python-Konzepte werden eingeführt?
1. Globale Variablen: Die Variable zaehler wird global definiert und innerhalb der Funktion nachfolger() verwendet, um die Anzahl der Aufrufe zu zählen.
2. Bedingte Logik: Die Funktionen add() und mult() verwenden bedingte Anweisungen, um unterschiedliche Fälle zu behandeln (z.B. negative Zahlen in add()).
3. Iteration: Schleifen werden verwendet, um wiederholte Addition und Multiplikation zu implementieren.
4. Rekursion und Funktionsaufrufe: Die Funktionen rufen sich gegenseitig auf, um komplexe Operationen zu realisieren.
"""
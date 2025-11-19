def teiler_und_rest(x,y):
    t=x//y
    r=x%y
    return (t,r)
teiler,rest=teiler_und_rest(4,5)

"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Funktionen mit mehreren Rückgabewerten: Das Programm zeigt, wie man in Python Funktionen definiert,
 die mehrere Werte zurückgeben können, indem man ein Tupel verwendet.
2. Ganzzahlige Division und Modulo-Operation: Die Verwendung der Operatoren // und % wird demonstriert,
 um den ganzzahligen Quotienten und den Rest einer Division zu berechnen.
3. Tupelzuweisung: Das Programm illustrirt, wie man mehrere Rückgabewerte einer Funktion direkt in separate Variablen zuweisen kann.
"""




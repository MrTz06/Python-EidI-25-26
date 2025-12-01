#Dieses Programm aus der Vorlesung demonstriert eine rekursive Countdown-Funktion in Python.

import time

def countdown(n):
    print(n)
    if n==0:
        print("BOOOOOM")
    time.sleep(1)
    countdown(n-1)

countdown(5)


#Zusammenfassung/Erklärung/Was kann ich neues durch das Programm lernen/Welche neuen Konzepte sind enthalten:
#1. Rekursion: Das Programm zeigt, wie eine Funktion sich selbst aufrufen kann, um eine Aufgabe zu erfüllen.
#2. Basisfall: Es wird ein Basisfall (n==0) definiert, um die Rekursion zu beenden und eine Endbedingung zu schaffen.
#3. Zeitverzögerung: Die Funktion time.sleep(1) wird verwendet, um eine Pause von einer Sekunde zwischen den Ausgaben einzufügen.
#4. Einfache Ausgabe: Das Programm demonstriert die Ausgabe von Zahlen und Text auf der Konsole.
#5. Funktionsaufruf: Es wird gezeigt, wie man eine Funktion mit einem Argument aufruft (countdown(5)).
#6. Stack Overflow Risiko: Das Programm illustriert das Risiko eines Stack Overflows bei zu tiefen Rekursionen, was ein wichtiges Konzept in der Programmierung ist.
#7. Verständnis von Kontrollfluss: Das Programm hilft, das Verständnis des Kontrollflusses in rekursiven Funktionen zu vertiefen.
# Achtung: Dieses Programm wird einen Fehler verursachen (maximum recursion depth exceeded),
# da es keine Abbruchbedingung für n<0 gibt. In einer realen Anwendung sollte eine solche Bedingung hinzugefügt werden, um unendliche Rekursion zu vermeiden.

#Was ist Rekursion?
#Rekursion ist ein Programmierkonzept, bei dem eine Funktion sich selbst aufruft, um ein Problem zu lösen.
# Eine rekursive Funktion besteht typischerweise aus zwei Hauptkomponenten: dem Basisfall und dem rekursiven Fall.
# Der Basisfall definiert die Bedingung, unter der die Rekursion endet,
# während der rekursive Fall die Funktion dazu bringt, sich selbst mit einem veränderten Argument aufzurufen.
#Rekursion wird oft verwendet, um Probleme zu lösen, die sich in kleinere, ähnliche Teilprobleme zerlegen lassen,
# wie z.B. die Berechnung von Fakultäten, Fibonacci-Zahlen, das Durchlaufen von Datenstrukturen wie Bäumen und vieles mehr.
#Beispiel:
#def factorial(n):
#    if n == 0:  # Basisfall
#        return 1
#    else:  # Rekursiver Fall
#        return n * factorial(n - 1)
#In diesem Beispiel berechnet die Funktion factorial die Fakultät einer Zahl n rekursiv.
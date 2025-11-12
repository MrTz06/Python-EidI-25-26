
#Dieses Pogramm aus der Vorlesung demonstriert und erklärt die Verwendung einer while-Schleife in Python.

#Setze n auf 100
n=100
#Setze x auf 1
x=1
#Solange x kleiner gleich n ist, mache:
while x<=n:
    #Gebe x aus
    print(x)
    #Erhöhe x um 1
    x=x+1

#Wann benutzt man eine while-Schleife?
#Man benutzt eine while-Schleife, wenn man nicht genau weiß, wie oft eine Schleife durchlaufen werden muss.
#Beispiel:
"""
eingabe = ""
while eingabe != "ende":
    eingabe = input("Geben Sie 'ende' ein, um die Schleife zu beenden: ")
    print("Sie haben eingegeben:", eingabe)
print("Schleife beendet.")
"""
#In diesem Beispiel wird die Schleife so lange ausgeführt, bis der Benutzer "ende" eingibt.
#Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
#1. while-Schleifen: Die while-Schleife wird verwendet, um eine Aktion wiederholt auszuführen, solange eine bestimmte Bedingung wahr ist.
#2. Variableninitialisierung: Die Variablen n und x werden initialisiert, um die Obergrenze und den aktuellen Wert zu verfolgen.
#3. Inkrementierung: Die Variable x wird in jedem Schleifendurchlauf um 1 erhöht, um sicherzustellen, dass die Schleife schließlich endet.
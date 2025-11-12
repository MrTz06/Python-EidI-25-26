# Dieses Programm aus der Vorlesung demonstriert die Iteration über die Zeichen eines Strings in Python
# und zeigt zwei verschiedene Methoden, um jedes Zeichen einzeln auszugeben.

s=input("Geben Sie etwas ein: ")
# Bestimmung der Länge des Strings
l=len(s)

# Methode 1: Iteration über die Indizes des Strings
for i in range(l):
    # Ausgabe des Zeichens an der Position i
    print(s[i])

print()
# Methode 2: Direkte Iteration über die Zeichen des Strings
for a in s: #Defintion von a als zeichen in s
    # Ausgabe des Zeichens
    print(a)

# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. String-Länge: Die Funktion len() wird verwendet, um die Länge eines Strings zu bestimmen.
# 2. Iteration über Indizes: Die erste Methode zeigt, wie man über die Indizes eines Strings iteriert, um auf jedes Zeichen zuzugreifen.
# 3. Direkte Iteration: Die zweite Methode demonstriert die direkte Iteration über die Zeichen eines Strings ohne Verwendung von Indizes.
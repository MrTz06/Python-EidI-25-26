# Dieses Programm aus der Vorlesung demonstriert die Verwendung von Funktionen in Python
# und zeigt, wie Parameter an Funktionen übergeben und wie Rückgabewerte verwendet werden.

# Definition der Funktion f, die einen Parameter x entgegennimmt und x um 1 erhöht
def f(x):
    x=x+1
    print("Innerhalb f, x=", x)
    return x
# Definition der Funktion g, die einen Parameter x entgegennimmt und x verdoppelt
def g(x):
    x=x+x
    print("Innerhalb g, x=", x)
    return x

# Hauptprogramm
# Initialisierung von x mit dem Wert 3
x=3
# Aufruf der Funktion f mit x als Argument und Speicherung des Rückgabewerts in z
z=f(x)
print("Im Hauptprogramm, x=",x)
print("Im Hauptprogramm, z=",z)
# Aufruf der Funktion g mit x als Argument und Speicherung des Rückgabewerts in u
u=g(x)
# Initialisierung von x mit dem Wert 18
x=18
print("Im Hauptprogramm, x=",x)
print("Im Hauptprogramm, u=",u)


# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Funktionsdefinition: Das Programm zeigt, wie man Funktionen in Python definiert.
# 2. Parameterübergabe: Es wird demonstriert, wie Parameter an Funktionen übergeben werden.
# 3. Rückgabewerte: Das Programm zeigt, wie Funktionen Werte zurückgeben können.
# 4. Variablenumfang: Es wird verdeutlicht, dass Variablen innerhalb von Funktionen lokal sind und nicht den Wert der Variablen im Hauptprogramm beeinflussen.
# 5. Funktionsaufrufe: Das Programm illustriert, wie Funktionen aufgerufen werden und wie deren Rückgabewerte verwendet werden können.

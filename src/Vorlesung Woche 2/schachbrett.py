# Dieses Programm aus der Vorlesung zeichnet ein Schachbrettmuster in der Konsole.

# Eingabe der Seitenlänge des Schachbretts
n=int(input("Geben Sie eine Seitenlänge an: "))

# Erste Methode: Verwendung einer Zählvariablen
b=0
# Zeichnen des Schachbrettmusters
for i in range(n):
    # Innere Schleife für jede Zeile
    for j in range(n):
        # Ausgabe eines "#" oder " " basierend auf der Zählvariablen
        if b%2==0:
            print("#",end="")
        else:
            print(" ",end="")
        # Erhöhen der Zählvariablen
        b=b+1
    # Erhöhen der Zählvariablen am Ende jeder Zeile, um das Muster zu wechseln
    b+=1
    print()
print()
print()
print()

# Zweite Methode: Verwendung der Indizes i und j
for i in range(n):
    # Innere Schleife für jede Zeile
    for j in range(n):
        # Ausgabe eines "#" oder " " basierend auf der Summe der Indizes
        if not (i+j)%2: #Gleichbedeutend mit if (i+j)%2==0:
            print("#",end="")
        else:
            print(" ",end="")
    print()


# Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
# 1. Schachbrettmuster: Das Programm erstellt ein Schachbrettmuster basierend auf der eingegebenen Seitenlänge.
# 2. Verschachtelte Schleifen: Es verwendet verschachtelte for-Schleifen, um Zeilen und Spalten des Musters zu zeichnen.
# 3. Bedingte Ausgabe: Zwei Methoden zur bedingten Ausgabe von Zeichen werden demonstriert - eine mit einer Zählvariablen und eine mit den Indizes der Schleifen.
# 4. Modulo-Operator: Der Modulo-Operator (%) wird verwendet, um abwechselnde Muster zu erzeugen.
# 5. Konsolenausgabe: Das Programm zeigt, wie man Zeichen in der Konsole ohne Zeilenumbruch ausgibt, indem man das Argument end="" in der print()-Funktion verwendet.
# 6. Logische Negation: Die Verwendung von "not" in der Bedingung zeigt eine alternative Möglichkeit, logische Ausdrücke zu formulieren.
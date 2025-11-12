# Dieses Programm aus der Vorlesung ist ein einfaches Cheerleader-Programm, das einen Benutzer auffordert,
# ein Wort einzugeben und dann für jeden Buchstaben des Wortes anfeuert.
#Es unterscheidet zwischen Vokalen und Konsonanten und wiederholt das gesamte Wort basierend auf dem angegebenen Enthusiasmuslevel.

#importieren des time-Moduls für Verzögerungen
import time
#Definieren der Buchstaben, die mit "an" anstatt "a" angesprochen werden (Vokale und bestimmte Konsonanten)
an_letters="aefhilmnorsxAEFHILMNORSX"

#Benutzereingabe für das Wort und das Enthusiasmuslevel
word=input("I will cheer for you! Enter a word: ")
times=int(input("Enthusiasm level (1-10): "))

#Schleife über jeden Buchstaben im Wort
for char in word:
    #Kurze Pause
    time.sleep(0.5)
    #Unterscheidung zwischen "a" und "an"
    if char in an_letters:
        print("Give me an " + char + " !  " + char)
    else:
        print("Give me a " + char + "!  " + char)
print("What does that spell?")

#Wiederholung des gesamten Wortes basierend auf dem Enthusiasmuslevel
for i in range(times):
    time.sleep(0.2)
    print(word,"!!!")


#Zusammenfassung/Was kann ich neues aus diesem Programm lernen?
#1. Einführung von import: Das Programm zeigt, wie man externe Module in Python importiert, um zusätzliche Funktionen zu nutzen.
#2. Zeitverzögerung mit time.sleep(): Die Funktion time.sleep() wird verwendet, um Pausen im Programmablauf einzufügen.
#3. Bedingte Anweisungen: Das Programm verwendet if-Anweisungen, um zwischen verschiedenen Fällen zu unterscheiden (z.B. "a" vs. "an").
#4. Benutzereingabe: Das Programm zeigt, wie man Benutzereingaben in Python verarbeitet.
#5. Schleifen: Das Programm demonstriert die Verwendung von for-Schleifen zur Iteration über Zeichen in einem String
# und zur Wiederholung von Aktionen basierend auf einer Zahl.

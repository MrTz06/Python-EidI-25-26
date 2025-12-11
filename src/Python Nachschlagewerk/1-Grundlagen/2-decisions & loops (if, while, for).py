#Was für Entscheidungen und Schleifen gibt es in Python und wie funktionieren sie?

#if, elif, else
# Entscheidungen in Python werden hauptsächlich durch if-, elif- und else-Anweisungen getroffen.
# Diese Anweisungen ermöglichen es, verschiedene Codeblöcke basierend auf Bedingungen auszuführen.
# Beispiel anhand eines Türstehers:
#Stell dir vor, du bist ein Türsteher in einem Club. Du entscheidest, wer rein darf und wer nicht, basierend auf bestimmten Kriterien.
person = type('Person', (object,), {'age': 20})()  # Erstelle ein Objekt mit einem Alter von 20
if person.age >= 18:
    print("Du darfst rein!")
else:
    print("Tut mir leid, du bist zu jung.")
# In diesem Beispiel entscheidet der Türsteher (das Programm), ob eine Person in den Club darf oder nicht, basierend auf ihrem Alter.

#Wann nutzt man if, elif und else?
# Man nutzt if, elif und else, um mehrere Bedingungen zu überprüfen und unterschiedliche Aktionen basierend auf diesen Bedingungen auszuführen.
# Beispiel:
note = 85
if note >= 90:
    print("Sehr gut!")
elif note >= 75:
    print("Gut gemacht!")
elif note >= 60:
    print("Du hast bestanden.")
else:
    print("Leider nicht bestanden.")
# In diesem Beispiel überprüft das Programm die Note und gibt eine entsprechende Nachricht aus.
#Man nutzt also elif für zusätzliche Bedingungen, die NUR überprüft werden, wenn die vorherigen if- oder elif-Bedingungen nicht erfüllt sind.
# else wird verwendet, um einen Codeblock auszuführen, wenn keine der vorherigen Bedingungen wahr ist.

#Wenn ich eine Entscheidung/if-Anweisung programmieren will, was muss ich beachten?
# 1. Bedingung: Die Bedingung nach dem if (oder elif) muss einen booleschen Wert (True oder False) zurückgeben.
# 2. Einrückung: Der Codeblock, der ausgeführt werden soll, wenn die Bedingung wahr ist, muss eingerückt sein (normalerweise 4 Leerzeichen oder ein Tab).
# 3. Reihenfolge: Die Reihenfolge der Bedingungen ist wichtig, da das Programm die Bedingungen von oben nach unten überprüft und den ersten wahren Block ausführt.
# 4. Optionalität: elif und else sind optional. Du kannst nur if verwenden, wenn du keine weiteren Bedingungen oder einen Standardfall benötigst.
# 5. Definitionen: Alle in der if-Anweisung verwendeten Variablen müssen vorher definiert sein.


#Schleifen
# Schleifen in Python ermöglichen es, einen Codeblock wiederholt auszuführen, solange eine bestimmte Bedingung erfüllt ist.
# Die beiden Haupttypen von Schleifen in Python sind die while-Schleife und die for-Schleife.
#Diese beiden Schleifenarten funktionieren itterativ, also wiederholen einen Prozess, bis eine bestimmte Bedingung nicht mehr erfüllt ist. Dazu später mehr.


# while-Schleife
# Eine while-Schleife wiederholt einen Codeblock, solange eine bestimmte Bedingung wahr ist.
# Beispiel anhand eines Einkaufs, du musst 5 Äpfel kaufen, aber du hast nur 2 im Korb.
aepfel_im_korb = 2
while aepfel_im_korb < 5:
    print("Ich kaufe einen Apfel.")
    aepfel_im_korb += 1
print("Ich habe genug Äpfel.")
# In diesem Beispiel kauft die Person Äpfel, bis sie 5 Äpfel im Korb hat.
#Was muss ich beachten, wenn ich eine while-Schleife programmiere?
# 1. Bedingung: Die Bedingung nach dem while muss einen booleschen Wert (True oder False) zurückgeben.
#z.B. aepfel_im_korb < 5 überprüft, ob die Anzahl der Äpfel im Korb kleiner als 5 ist. wird dies irgendwann False, hört die Schleife auf.
# 2. Einrückung: Der Codeblock, der wiederholt ausgeführt werden soll, muss eingerückt sein (normalerweise 4 Leerzeichen oder ein Tab).
# 3. Endlosschleifen vermeiden: Stelle sicher, dass die Bedingung irgendwann False wird, um Endlosschleifen zu vermeiden.
# In unserem Beispiel wird aepfel_im_korb bei jedem Durchlauf um 1 erhöht, sodass die Bedingung schließlich False wird.
# 4. Initialisierung: Alle in der while-Schleife verwendeten Variablen müssen vorher definiert sein.


# for-Schleife
# Eine for-Schleife wird verwendet, um über eine Sequenz (wie eine Liste, ein Tupel oder eine Zeichenkette) zu iterieren.
# Beispiel anhand einer Einkaufsliste:
einkaufsliste = ["Äpfel", "Bananen", "Orangen"]
for item in einkaufsliste:
    print("Ich kaufe " + item + ".")
# In diesem Beispiel geht die Person durch ihre Einkaufsliste und kauft jedes Element.
#Was muss ich beachten, wenn ich eine for-Schleife programmiere?
# 1. Sequenz: Die for-Schleife benötigt eine Sequenz (Liste, Tupel, String usw.), über die sie iterieren kann.
#z.B. einkaufsliste ist eine Liste von Strings, und die Schleife geht jedes Element dieser Liste durch.
# 2. Einrückung: Der Codeblock, der für jedes Element in der Sequenz ausgeführt werden soll, muss eingerückt sein (normalerweise 4 Leerzeichen oder ein Tab).
# 3. Variable: Die Variable nach for (in diesem Fall item) repräsentiert das aktuelle Element der Sequenz in jedem Durchlauf der Schleife.
# z.B. im ersten Durchlauf ist item "Äpfel", im zweiten "Bananen" usw.
# 4. Definitionen: Alle in der for-Schleife verwendeten Variablen müssen vorher definiert sein.

#Wann nutze ich welche Schleife?
# Man nutzt eine while-Schleife, wenn man nicht genau weiß, wie oft der Codeblock ausgeführt werden muss,
# und die Ausführung von einer Bedingung abhängt.
# Beispiel: Solange der Akku deines Handys nicht voll ist, lade es weiter auf.
akku_ladung = 50
while akku_ladung < 100:
    print("Lade Akku...")
    akku_ladung += 10
print("Akku ist voll!")
# Man nutzt eine for-Schleife, wenn man über eine bekannte Anzahl von Elementen iterieren möchte.
# Beispiel: Du möchtest alle Bücher in deinem Regal durchgehen.
buecher_regal = ["Buch A", "Buch B", "Buch C"]
for buch in buecher_regal:
    print("Ich lese " + buch + ".")
#Zusammenfassung:
# Entscheidungen (if, elif, else) ermöglichen es, verschiedene Codeblöcke basierend auf Bedingungen auszuführen.
# Schleifen (while, for) ermöglichen es, Codeblöcke wiederholt auszuführen, entweder basierend auf einer Bedingung (while) oder über eine Sequenz (for).
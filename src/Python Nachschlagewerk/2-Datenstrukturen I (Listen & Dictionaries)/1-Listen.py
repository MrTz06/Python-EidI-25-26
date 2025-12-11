#Bisher konnten unsere Variablen immer nur eine Sache speichern (eine Zahl oder einen Text).
# Aber in der Realität haben wir oft Sammlungen: eine Playlist, eine Gruppe von Studenten oder einen Warenkorb.
# Dafür hat Python zwei extrem wichtige Werkzeuge: Listen (Lists) und Wörterbücher (Dictionaries).

#Listen
# Stell dir eine Liste wie ein Regal vor.
# Es ist geordnet: Die Dinge stehen in einer festen Reihenfolge.
# Du greifst über die Position (den Index) darauf zu.
#z.B.
#Du kannst Bücher (Elemente) hineinlegen.
# Die Bücher haben Plätze (Indizes), die bei 0 anfangen.
#Du kannst Bücher hinzufügen, entfernen oder ändern.

# Eine Liste wird mit eckigen Klammern erstellt
studenten = ["Anna", "Ben", "Chris"]

# Zugriff: Wir zählen ab 0!
print(studenten[0])  # Gibt "Anna" aus
print(studenten[1])  # Gibt "Ben" aus


#Listenoperationen:

# Ändern: Wir können Elemente ändern
studenten[1] = "Beatrice"
print(studenten)  # Gibt ["Anna", "Beatrice", "Chris"] aus
# Hinzufügen: Wir können Elemente hinzufügen
studenten.append("Diana")
print(studenten)  # Gibt ["Anna", "Beatrice", "Chris", "Diana"] aus
# Entfernen: Wir können Elemente entfernen
studenten.remove("Chris")
print(studenten)  # Gibt ["Anna", "Beatrice", "Diana"] aus
# Iterieren: Wir können über die Liste laufen
for student in studenten:
    print(student)
# Gibt jeden Namen in der Liste aus
#Weitere Listenbefehle:
# len(): Gibt die Länge der Liste zurück
print(len(studenten))  # Gibt 3 aus
# sort(): Sortiert die Liste (alphabetisch für Strings, numerisch für Zahlen)
studenten.sort()
print(studenten)  # Gibt ["Anna", "Beatrice", "Diana"] aus
# reverse(): Kehrt die Reihenfolge der Liste um
studenten.reverse()
print(studenten)  # Gibt ["Diana", "Beatrice", "Anna"] aus
# pop(): Entfernt und gibt das letzte Element der Liste zurück
letzter_student = studenten.pop()
print(letzter_student)  # Gibt "Anna" aus
print(studenten)  # Gibt ["Diana", "Beatrice"] aus
# extend(): Fügt mehrere Elemente hinzu
studenten.extend(["Eva", "Frank"])
print(studenten)  # Gibt ["Diana", "Beatrice", "Eva", "Frank"] aus
# insert(): Fügt ein Element an einer bestimmten Position ein
studenten.insert(1, "Zoe")
print(studenten)  # Gibt ["Diana", "Zoe", "Beatrice", "Eva", "Frank"] aus
# index(): Gibt den Index eines Elements zurück
index_beatrice = studenten.index("Beatrice")
print(index_beatrice)  # Gibt 2 aus
# count(): Zählt, wie oft ein Element in der Liste vorkommt
anzahl_diana = studenten.count("Diana")
print(anzahl_diana)  # Gibt 1 aus
# clear(): Entfernt alle Elemente aus der Liste
studenten.clear()
print(studenten)  # Gibt [] aus



# Listen können auch verschachtelt sein (Listen in Listen)
#Das folgende Beispiel zeigt eine 2D-Liste (Matrix):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Gibt 6 aus (zweite Liste, drittes Element)
# Listen sind sehr flexibel und können verschiedene Datentypen enthalten
gemischte_liste = [1, "Hallo", 3.14, True, [5, 6, 7]]
print(gemischte_liste)
# Gibt [1, "Hallo", 3.14, True, [5, 6, 7]] aus
# Listen sind ein grundlegendes Werkzeug in Python und werden in vielen Programmen verwendet, um Daten zu organisieren und zu verwalten.



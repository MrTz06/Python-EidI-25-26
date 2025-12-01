# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

#Furby Datenbank

def csv_nach_zeilentupel(datei_pfad):
    result = []
    with open(datei_pfad, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            fields = [field.strip() for field in line.split(',')]
            result.append(tuple(fields))
    return result

def aufraeumen(datenbank):
    modifizierte_datenbank = []
    for datensatz in datenbank:
        name = datensatz[0].strip()
        accessoire = datensatz[3].strip()
        # numerisch nach int sortieren, aber als Strings belassen (wie Beispiel)
        bestandszahlen = sorted(datensatz[4:], key=lambda s: int(s), reverse=True)
        modifizierter_datensatz = (name, accessoire) + tuple(bestandszahlen)
        modifizierte_datenbank.append(modifizierter_datensatz)
    return modifizierte_datenbank

def ident(datenbank):
    sortierte_datenbank = sorted(datenbank, key=lambda x: x[0])
    datenbank_mit_ids = []
    for index, datensatz in enumerate(sortierte_datenbank, start=1):
        modifizierter_datensatz = (str(index),) + datensatz
        datenbank_mit_ids.append(modifizierter_datensatz)
    return datenbank_mit_ids

def arithm_mittel(datenbank):
    modifizierte_datenbank = []
    for datensatz in datenbank:
        # datensatz: (id, name, accessoire, count1, ..., count10)
        prefix = datensatz[:3]
        counts = list(map(int, datensatz[3:]))
        mittelwert = sum(counts) / len(counts) if counts else 0.0
        modifizierter_datensatz = prefix + tuple(counts) + (mittelwert,)
        modifizierte_datenbank.append(modifizierter_datensatz)
    return modifizierte_datenbank

def median(datenbank):
    tail_mittelwerte = []
    mane_mittelwerte = []
    for datensatz in datenbank:
        accessoire = datensatz[2]
        mittel = datensatz[-1]
        if accessoire == 'Tail':
            tail_mittelwerte.append(mittel)
        elif accessoire == 'Mane':
            mane_mittelwerte.append(mittel)
    tail_mittelwerte.sort()
    mane_mittelwerte.sort()

    def berechne_median(liste):
        n = len(liste)
        if n == 0:
            return None
        if n % 2 == 1:
            return liste[n // 2]
        else:
            return (liste[n // 2 - 1] + liste[n // 2]) / 2

    tail_median = berechne_median(tail_mittelwerte)
    mane_median = berechne_median(mane_mittelwerte)

    print("Tail: "+ tail_median)
    print("Mane: " + mane_median)
    return None




"""
Hausaufgabe 1 (15 Punkte):
In dieser Aufgabe geht es um eine kleine Datenbank ¨ uber Furbys. Sie erhalten diese
Datenbank als die ebenfalls bereitgestellte Datei furby_datei.csv, welche im Comma-
separated-values-Format (kurz: CSV) vorliegt. Das bedeutet, dass jede Zeile genau einen
Datensatz enth¨ alt. In unserem Fall ist ein Datensatz der Name eines Furbys, seine prim¨
are
Farbe, seine sekund¨ are Farbe, sein Accessoire (Tail oder Mane) und 10 weitere Eintr¨ age, die
den Bestand in verschiedenen Gesch¨ aften angeben. Diese Werte sind aufsteigend sortiert.
Die Daten innerhalb eines Datensatzes, also innerhalb einer Zeile, werden durch Kommas
getrennt.
Eine der Zeilen ist z.B.
Frog, Olive Green, Light Cream, Mane, 4, 4, 4, 6, 9, 11, 15, 16, 19, 20
Sie sollen die Datenbank bearbeiten und analysieren, indem Sie die folgenden Funktionen
implementieren und sie im Hauptprogramm nacheinander auf die Datenbank anwenden. Ihr
Programm muss auch noch funktionieren, wenn der Datenbank neue Datens¨ atze hinzugef¨ ugt
werden.
(a) (3 Punkte) Eine Funktion csv_nach_zeilentupel, welche als Eingabe einen Dateipfad
(String) zu einer CSV-Datei erwartet und welche die Datenbank aus dieser Datei in
eine Liste von Tupeln umwandelt. D.h. die R¨ uckgabe soll eine Liste von Tupeln sein,
wobei jedes Tupel einen der Datens¨ atze enth¨ alt und die Tupel-Eintr¨ age alle vom Typ
String sind. Achten Sie darauf ¨ uberfl¨ ussige Leerzeichen und \n zu entfernen.
Hinweis: Verwenden Sie x = open(datei_pfad, ’r’).readlines(), wobei
datei_pfad der entgegengenommene Dateipfad ist. Nachdem diese Zeile ausgef¨ uhrt
wurde, enth¨ alt x eine Liste von Strings (einen String pro Zeile in der CSV-Datei).
Sie k¨ onnen außerdem tuple(liste) verwenden um eine Liste liste in ein Tupel
umzuwandeln.
Hinweis: Wenn Sie die Datei furby_datei.csv im gleichen Verzeichnis wie Ihr
Programm abspeichern, dann lautet der Dateipfad "furby_datei.csv". Dann f¨ angt
die R¨ uckgabe von csv_nach_zeilentupel("furby_datei.csv") an mit:
[(’Pink Flamingo’, ’Light Pink’, ’Cerise’, ’Tail’, ’3’, ’6’, ’6’, ’12’, ’13’, ’13’, ’13’, ’14’, ’21’, ’22’),
 (’Wizard’, ’Black’, ’Violet’, ’Tail’, ’1’, ’4’, ’7’, ’9’, ’13’, ’16’, ’17’, ’18’, ’22’, ’22’),...
 (b) (2 Punkte) Eine Funktion aufraeumen, welche als Eingabe die R¨ uckgabe aus (a),
also die Datenbank, dargestellt als Liste von Tupeln, erwartet. Beide Spalten, die die
Farbe angeben, sollen entfernt werden. Außerdem sollen die Bestandsangaben, die
pro Datensatz angegeben sind, so umsortiert werden, dass sie statt in aufsteigender,
in absteigender Reihenfolge angegeben sind. Ausgegeben werden soll die modifizierte
Datenbank im Listen-Tupel-Format.
Hinweis: Wendet man aufraeumen auf die Liste aus dem vorherigen Hinweis an, so
f¨ angt die R¨ uckgabe an mit:
2
[(’Pink Flamingo’, ’Tail’, ’22’, ’21’, ’14’, ’13’, ’13’, ’13’, ’12’, ’6’, ’6’, ’3’),
(’Wizard’, ’Tail’, ’22’, ’22’, ’18’, ’17’, ’16’, ’13’, ’9’, ’7’, ’4’, ’1’),...
(c) (2 Punkte) Eine Funktion ident, welche als Eingabe die R¨ uckgabe aus (b), also die
”aufger¨ aumte“ Datenbank, dargestellt als Liste von Tupeln, erwartet. Ihre Funktion
soll die Datens¨ atze so umordnen, dass Sie entsprechend dem Namen des Furbys
alphabetisch sortiert sind. Anschließend soll jeder Datensatz als ersten Eintrag eine ID
bekommen: die erste Zeile erh¨ alt die ID 1, die zweite Zeile die ID 2 usw. Ausgegeben
werden soll die modifizierte Datenbank im Listen-Tupel-Format.
Hinweis: Wendet man ident auf die Liste aus dem vorherigen Hinweis an, so f¨ angt
die R¨ uckgabe an mit:
[(’1’, ’Banana Peel’, ’Mane’, ’17’, ’15’, ’13’, ’13’, ’10’, ’6’, ’6’, ’6’, ’1’, ’1’),
 (’2’, ’Bandit Elephant’, ’Mane’, ’22’, ’20’, ’16’, ’15’, ’13’, ’13’, ’13’, ’12’, ’5’, ’3’),...
 (d) (3 Punkte) Eine Funktion arithm_mittel, welche als Eingabe die R¨ uckgabe aus (c),
also die ”aufger¨ aumte“, sortierte Datenbank mit IDs, dargestellt als Liste von Tupeln,
erwartet. Ihre Funktion soll die Datensatz-Eintr¨ age, die die Best¨ ande angeben, in
Integer-Werte umwandeln (bislang liegen diese als String vor). Anschließend soll jedem
Datensatz als letzter Eintrag das arithmetische Mittel der Bestandszahlen hinzugef¨ ugt
werden (als Float-Wert). Ausgegeben werden soll die modifizierte Datenbank im
Listen-Tupel-Format.
Hinweis: Wendet man arithm_mittel auf die Liste aus dem vorherigen Hinweis an,
so f¨ angt die R¨ uckgabe an mit:
[(’1’, ’Banana Peel’, ’Mane’, 17, 15, 13, 13, 10, 6, 6, 6, 1, 1, 8.8),
 (’2’, ’Bandit Elephant’, ’Mane’, 22, 20, 16, 15, 13, 13, 13, 12, 5, 3, 13.2),...
 (e) (5 Punkte) Eine Funktion median, welche als Eingabe die R¨ uckgabe aus (d), also
die vollst¨ andig modifizierte Datenbank, dargestellt als Liste von Tupeln, erwartet.
Ihre Funktion soll f¨ ur jedes Accessoire (Tail und Mane) den Median, ¨ uber die zuvor
berechneten arithmetischen Mittel, berechnen und in der Konsole ausgeben. Der
Median beschreibt den Wert der, wenn man die Datenpunkte sortiert aufz¨ ahlt, genau
                                                                              in der Mitte liegt, z.B. von 1, 2, 3, 9, 9 ist der Median 3 und von 1, 1, 2, 3, 9, 9 ist der
Median 2.5. Zur¨ uckgegeben werden soll None.
Hinweis: Wendet man median auf die R¨ uckgabe aus dem vorherigen Hinweis an, so
soll in der Konsole folgendes ausgegeben werden:
Tail: 12.2
Mane: 10.45
"""


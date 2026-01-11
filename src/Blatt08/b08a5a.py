# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

#A


alle_muenzen = [200, 100, 50, 20, 10, 5, 2, 1]
def formatiere_muenze(wert):
    if wert >= 100:
        return f"{wert // 100} Euro"
    else:
        return f"{wert} Cent"

def muenz_wechsel(betrag, min_muenze):

    return hilfsfunktion(betrag, min_muenze, 200)

def hilfsfunktion(rest_betrag, min_muenze, max_muenze):
    #Basisfall A
    if rest_betrag == 0:
        return [[]] # Eine Lösung gefunden: die leere Lösung (gleich Münzen hinzufügen)

    # Basisfall B
    if rest_betrag < min_muenze:
        return [] # Keine Lösungen hier

    alle_loesungen = []

    # 3. Rekursiver Schritt
    for muenze in alle_muenzen:
        #Muenze muss:
        # <= max_muenze sein (damit absteigend)
        # >= min_muenze sein (Vorgabe)
        # <= rest_betrag sein (sonst Minus)
        if muenze <= max_muenze and muenze >= min_muenze and muenze <= rest_betrag:

           #Münze abziehen, münze = neue max_muenze
            rest_loesungen = hilfsfunktion(rest_betrag - muenze, min_muenze, muenze)

            #für ausgabe formatieren
            text_muenze = formatiere_muenze(muenze)

            #Alle Lösungen erweitern
            for loesung in rest_loesungen: #jede Teillösung erweitern
                neue_loesung = [text_muenze] + loesung #aktuelle Münze vorne anfügen
                alle_loesungen.append(neue_loesung) #zu Gesamtlösungen hinzufügen

    return alle_loesungen















# ---Hauptprogramm (nichts ändern) ---
if __name__ == "__main__":
    betrag = int(input("Geben Sie einen Betrag in Cent ein: "))
    min_muenze = int(input("Geben Sie die kleinste M¨unze ein (in Cent): "))
    out = muenz_wechsel(betrag, min_muenze)
    for liste in out:
        print(liste)






"""Hausaufgabe 5 (6 + 3 Punkte):
In dieser Aufgabe sollen Sie die zentrale Funktion muenz_wechsel f¨ ur ein Programm
schreiben, das dem Nutzer anzeigt wie er einen gew¨ unschten Geldbetrag in Euro- und
Cent-M¨ unzen wechseln kann. Hierzu soll die Funktion Rekursion verwenden.
Nutzen Sie dazu in Ihrer Datei das folgende Hauptprogramm:
betrag = int(input("Geben Sie einen Betrag in Cent ein: "))
min_muenze = int(input("Geben Sie die kleinste M¨unze ein (in Cent): "))
out = muenz_wechsel(betrag, min_muenze)
for liste in out:
print(liste)
Der Nutzer wird also zu zwei Eingaben aufgefordert: Zuerst der Betrag der gewechselt
werden soll, angegeben in Cent (also z.B. 511 f¨ ur 5, 11 Euro). Anschließend den Wert
der kleinsten M¨ unze, die verwendet werden soll, ebenfalls in Cent (also z.B. 20 f¨ ur die
20-Cent-M¨ unze)
Die M¨ unzen die im Allgemeinen verwendet werden k¨ onnen sind die Euro-M¨ unzen, also 1, 2,
5, 10, 20, 50 Cent, 1 Euro, 2 Euro.
Ihre Funktion muenz_wechsel soll als R¨ uckgabe eine Liste von Listen liefern, die alle
M¨ oglichkeiten angibt, den gew¨ unschten Betrag, mit den gew¨ unschten M¨ unzen, zu wechseln.
Diese zur¨ uckgegebene Liste von Listen wird durch das Hauptprogramm zeilenweise auf
der Konsole ausgegeben. Gibt der Nutzer z.B. 120 und 20 ein, so soll man die folgende
Konsolenausgabe erhalten:
[’20 Cent’, ’20 Cent’, ’20 Cent’, ’20 Cent’, ’20 Cent’, ’20 Cent’]
[’50 Cent’, ’50 Cent’, ’20 Cent’]
[’1 Euro’, ’20 Cent’]
Wie Sie sehen, soll jede M¨ unzen-Kombination nur genau einmal auftauchen (z.B. soll
[’20 Cent’, ’1 Euro’] nicht auch noch ausgegeben werden). Dies k¨ onnen Sie errei-
chen, indem Sie die Listen absteigend sortiert erstellen, d.h. in den rekursiven Aufrufen
werden jeweils nur M¨ unzen verwendet, die einen Wert kleiner oder gleich der M¨
unze
haben, die gerade verwendet wurde. Nutzen Sie hierf¨ ur eine Hilfsfunktion, die die Rekur-
sion ¨ ubernimmt, als Eingabe zus¨ atzlich einen Integer-Wert max_muenze erh¨ alt und die
M¨ unzwechsel-M¨ oglichkeiten berechnet, die man hat, wenn man nur M¨ unzen mit Wert
zwischen min_muenze und max_muenze verwendet.
Wie im Beispiel zu sehen, sollen in der R¨ uckgabe von muenz_wechsel, die M¨ unzen als
String mit Einheit angegeben sein (also z.B. ’5 Cent’ oder ’1 Euro’).
Wenn der Nutzer seine Eingaben so w¨ ahlt, dass es nicht m¨ oglich ist den eingegebenen
Betrag, mit den gew¨ unschten M¨ unzen, zu wechseln (z.B. bei 21 und 5), darf sich Ihre
Funktion beliebig verhalten.
(a) Schreiben Sie die Funktion muenz_wechsel mit Ihrer beschriebenen Hilfsfunktion.
(b) F¨ ugen Sie Ihrer Hilfsfunktion ein W¨ orterbuch als Eingabe hinzu und nutzen Sie dieses,
um Ihr Programm schneller zu machen. D.h. setzen Sie das W¨ orterbuch ein, sodass
bereits berechnete rekursive Aufrufe nicht erneut berechnet werden. Die Schl¨ ussel
dieses W¨ orterbuchs sollten Tupel der Form (betrag, min_muenze, max_muenze)
sein.
Geben Sie Ihre L¨ osungen f¨ ur (a) und (b) in separaten Dateien mit den Namen b08a5a.py
und b08a5b.py ab. In beiden Dateien soll das Hauptprogramm, exakt wie hier angegeben,
enthalten und Ihre Funktion muenz_wechsel benannt sein."""
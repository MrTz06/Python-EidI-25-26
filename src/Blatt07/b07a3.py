# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)


def pyramide(n):
    ## Hilfsfunktion: fügt der Pyramide links und rechts eins Spalte von Leerzeichen hinzu
    def pyramide_padded(pyramide):
        pyramiden_liste = pyramide.split("\n")
        ergebnis = ""
        for zeilen_nr in range(len(pyramiden_liste)):
            ergebnis += " " + pyramiden_liste[zeilen_nr] + " \n"
        return ergebnis
    if n == 1:
        return "*"
    else:
        return pyramide_padded(pyramide(n-1)) + (2*n-1)*"*"

def pyramide_seq(n, k):
    # 1. Basisfall: Wenn n=1 oder k=0, ist es  eine normale Pyramide
    if n == 1 or k == 0:
        return pyramide(n)

        # 2. Rekursion
        # Mitte: Die große Pyramide (als String)
    mitte_string = pyramide(n)
    #string in Liste zerlegen
    mitte_liste = mitte_string.split("\n")

    # Seiten: Die kleineren Sequenzen (rekursiver Aufruf)
    seite_string = pyramide_seq(n // 2, k - 1)
    # String in Liste umwandeln
    seite_liste = seite_string.split("\n")

    # 3. Maße nehmen für das Padding
    breite_seite = len(seite_liste[-1])
    hoehe_seite = len(seite_liste)

    ergebnis_liste = []

    # 4. Zeilen zusammenbauen
    # Wir gehen durch jede Zeile der großen mittleren Pyramide
    for i in range(n):
        zeile_mitte = mitte_liste[i]
        trennzeichen = " "

        # Startpunkt berechnen
        # (Die Seiten sind unten bündig, also n minus ihre Höhe)
        start_seite = n - hoehe_seite

        if i < start_seite:
            # FALL A:
            # links und rechts mit Leerzeichen auffüllen
            padding = " " * breite_seite
            neue_zeile = padding + trennzeichen + zeile_mitte + trennzeichen + padding
        else:
            # FALL B:
            #passende Zeile aus der seite_liste holen
            index_in_seite = i - start_seite
            zeile_seite = seite_liste[index_in_seite]
            neue_zeile = zeile_seite + trennzeichen + zeile_mitte + trennzeichen + zeile_seite

        ergebnis_liste.append(neue_zeile)

    # 5. Abschluss: Die Liste wieder zu einem einzigen String mit Zeilenumbrüchen machen
    return "\n".join(ergebnis_liste)




#if __name__ == "__main__":
 #   print(pyramide_seq(5, 2))

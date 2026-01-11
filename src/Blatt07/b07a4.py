# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
def update_tree(baum):
    # Starte die Rekursion auf Ebene 1
    return update_rekursiv(baum, 1)

def update_rekursiv(baum, ebene):
    # Basisfall: Wenn es ist nur eine Zahl (Blatt)
    if isinstance(baum, int):
        return baum

    # Rekursiver Schritt: Tupel (Knoten mit Nachfolgern)
    else:
        # 1. Zerlegen
        alt_links = baum[0]
        alt_rechts = baum[2]
        # 2. Rekursiv die Nachfolger updaten
        neu_links = update_rekursiv(alt_links, ebene + 1)
        neu_rechts = update_rekursiv(alt_rechts, ebene + 1)

        # 3. Werte der Nachfolger extrahieren
        if isinstance(neu_links, tuple):
            wert_links = neu_links[1]
        else:
            wert_links = neu_links

        if isinstance(neu_rechts, tuple):
            wert_rechts = neu_rechts[1]
        else:
            wert_rechts = neu_rechts

        # 4. Berechnung durchführen
        #Ebene * (Summe der Nachfolger)
        neue_wurzel = ebene * (wert_links + wert_rechts)

        # 5. Neu zusammensetzen und zurückgeben
        return (neu_links, neue_wurzel, neu_rechts)
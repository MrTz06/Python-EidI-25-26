# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
def zusammenfueren(woerterbuch1, woerterbuch2):
    zusammengefuertes_woerterbuch = {}
    for schluessel in woerterbuch1:
        if schluessel in woerterbuch2:
            zusammengefuertes_woerterbuch[schluessel] = woerterbuch1[schluessel] + woerterbuch2[schluessel]
        else:
            zusammengefuertes_woerterbuch[schluessel] = woerterbuch1[schluessel]
    for schluessel in woerterbuch2:
        if schluessel not in zusammengefuertes_woerterbuch:
            zusammengefuertes_woerterbuch[schluessel] = woerterbuch2[schluessel]
    return zusammengefuertes_woerterbuch
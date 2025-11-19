# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)
def lottoziehung(anzahl,maximum):
    import random
    zahlenbereich = list(range(1, maximum + 1))
    ziehung = []
    while len(ziehung) < anzahl:
        zahl = random.choice(zahlenbereich)
        if zahl not in ziehung:
            ziehung.append(zahl)
    zusatzzahl = random.choice([z for z in zahlenbereich])
    return ziehung, zusatzzahl










"""Hausaufgabe 2 (4 Punkte):
Schreiben Sie eine Funktion lottoziehung, die einen Integer anzahl und einen positiven
Integer maximum erwartet, sodass anzahl < maximmum gilt, und eine zuf¨ allige Ziehung von
Zahlen als Liste liefert (keine Wiederholungen!) und die Zusatzzahl als zweites Element
des R¨ uckgabe-Tupels zur¨ uckgibt. Die kleinstm¨ ogliche gezogene Zahl ist die 1 und die
gr
¨ oßtm¨ ogliche Zahl ist maximum. Bspw. kann
lottoziehung(6,49)
die R¨ uckgabe
([22, 11, 47, 3, 41, 28], 16)
liefern.
2
Hinweis. Durch import random k¨ onnen sie das Paket random einbinden. Um von einer
Liste L ein zuf¨ alliges Element zu w¨ ahlen, nutzen Sie random.choice(L)."""
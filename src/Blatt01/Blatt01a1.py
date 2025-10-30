# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

grundgehalt=100000
bonus=2000

auftritte= int (input("Bitte geben sie Anzahl an Auftritten im vergangenen Jahr an: "))
if auftritte <5 :
    auftritts_honorar= 300*auftritte
else :
    auftritts_honorar= (auftritte*400)-400
bueroarbeit = int (input("Bitte geben sie die Anzahl der Stunden an, die sie im vergangenen Jahr mit Büroarbeit verbracht haben: "))
bueroarbeit_honorar= bueroarbeit*100
gesamtgehalt= grundgehalt + bonus +  auftritts_honorar + bueroarbeit_honorar
print("Ihr Gesamtgehalt im vergangenen Jahr betrug: ", gesamtgehalt, "Euro")
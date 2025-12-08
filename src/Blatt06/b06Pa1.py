def listen_summe(liste):
    if liste == []:
        return 0
    else:
        return liste[0] + listen_summe(liste[1:])

print (listen_summe([1,2,3,4,5]))  # Ausgabe: 15
print (listen_summe([]))           # Ausgabe: 0
print (listen_summe([10,20,30]))   # Ausgabe: 60

# Dieses Programm definiert eine rekursive Funktion zur Berechnung der Summe der Elemente in einer Liste.
# Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
# 1. Rekursion: Das Programm demonstriert das Konzept der Rekursion, bei dem eine Funktion sich selbst aufruft, um ein Problem zu lösen.
# 2. Basisfall: Es zeigt die Bedeutung eines Basisfalls (leere Liste) in rekursiven Funktionen, um unendliche Rekursion zu vermeiden.
# 3. Slicing: Das Programm verwendet Listenslicing (liste[1:]), um die Liste in kleinere Teile zu zerlegen und die Summe der Elemente zu berechnen.
#Wie funktioniert Slicing in Python?
# Slicing in Python ermöglicht es, Teile einer Sequenz (wie Listen, Tupel oder Strings) auszuwählen, indem man Start- und Endindizes angibt.
# Die Syntax lautet: sequenz[start:end], wobei 'start' der Index des ersten Elements ist, das eingeschlossen wird,
# und 'end' der Index des ersten Elements ist, das ausgeschlossen wird.
# Beispiel:
# my_list = [0, 1, 2, 3, 4, 5]
# sliced_list = my_list[1:4]  # Ergebnis: [1, 2, 3]
# Wenn 'start' weggelassen wird, beginnt das Slicing am Anfang der Sequenz.
# Wenn 'end' weggelassen wird, geht das Slicing bis zum Ende der Sequenz.
# Beispiel:
# my_list = [0, 1, 2, 3, 4, 5]
# sliced_list_start = my_list[:3]  # Ergebnis: [0, 1, 2]
# sliced_list_end = my_list[3:]    # Ergebnis: [3, 4, 5]
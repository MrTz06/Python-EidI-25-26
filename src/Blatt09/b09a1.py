# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
#a)
def string_funk(s1,s2):
    assert len(s1) >= 3 #Länge von s1 mindestens 3
    assert len(s1) >= 2*len(s2) #Länge von s1 mindestens doppelt so lang wie s2
    #s1 und s2 stimmen in den ersten drei zeichen überein
    for i in range(3):
        assert s1[i] == s2[i]

    #Konkatenation von s1 und s2 (Bedeutet: s1 und s2 aneinanderhängen)
    return s1 + s2

#b)
def nutzer_aufruf():
    try:
        s1 = input("Geben Sie den ersten String ein: ")
        s2 = input("Geben Sie den zweiten String ein: ")
        ergebnis = string_funk(s1, s2)
        print("Ergebnis:", ergebnis)
    except AssertionError:
        print("Eingaben nicht zulässig.")






"""Hausaufgabe 1 (2 + 2= 4 Punkte):
(a) Schreiben Sie eine Funktion string_funk, welche als Eingabe zwei Strings s1 und s2
erwartet, sodass s1 mindestens die L¨ ange 3 hat, s1 doppelt so lang wie s2 ist und s1
und s2 in den ersten 3 Positionen ¨ ubereinstimmen. Zur¨ uckgegeben werden soll die
Konkatenation von s1 und s2.
Verwenden Sie assert, um in der Funktion sicherzustellen, dass die Eingaben wie
beschrieben sind.
(b) Schreiben Sie eine Funktion nutzer_aufruf, welche keine Eingabe erwartet. Die
Funktion fragt vom Nutzer zwei Strings an, ruft string_funk auf diesen auf und gibt,
wenn m
¨ oglich, das Ergebnis auf der Konsole aus. M¨ ogliche auftretende Assertion-
Errors sollen von der Funktion gefangen und die Fehlermeldung "Eingaben nicht
zul¨assig." auf der Konsole ausgegeben werden."""
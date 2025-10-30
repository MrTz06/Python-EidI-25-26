# Gruppenmitglieder der Abgabegruppe 51: Moritz Glaser, Jordan Bank, Daniel Bosman

ergebnis = int (input("Bitte geben Sie eine Zahl (0-9) ein: "))
while True:
    symbol = input("Bitte geben Sie ein Symbol ( + , - oder *) ein: ")
    if symbol == "stop" :
        print("Das Endergebnis lautet: ", ergebnis)
        break
    else:
        zahl = int (input("Bitte geben Sie eine weitere Zahl (0-9) ein: "))
        if symbol == "+" :
            ergebnis = ergebnis + zahl
        elif symbol == "-" :
            ergebnis = ergebnis - zahl
        elif symbol == "*" :
            ergebnis = ergebnis * zahl









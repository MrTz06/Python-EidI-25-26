# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)
zeilen = int(input("Bitte geben sie eine Zahl ein: "))
spalten = int(input("Bitte geben sie eine Zahl ein: "))

for i in range(zeilen):
    for j in range(spalten):
        if(i==j):
            print("1",end="")
        else :
            print("0",end="")

    print()

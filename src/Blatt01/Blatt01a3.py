# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

streichhoelzer = int(input("Geben sie die Anzahl der Streichhölzer ein mit denen gespielt wird:"))
print(streichhoelzer*"|")

#Alternative:
#for i in range(streichhoelzer) :
 #   print("|", end="") #end="" verhindert Zeilenumbruch
#print("\n")

while streichhoelzer !=0 :
    spieler1 = int(input("Spieler 1, wie viele Streichhölzer nimmst du weg (1-3)? "))
    streichhoelzer = streichhoelzer-spieler1
    if streichhoelzer == 0:
        print("Spieler 2 hat gewonnen!")
        break
    else :
        print(streichhoelzer*"|")

        #for i in range(streichhoelzer) :
        #    print("|", end="") #end="" verhindert Zeilenumbruch
       # print("\n")

    spieler2 = int(input("Spieler 2, wie viele Streichhölzer nimmst du weg (1-3)? "))
    streichhoelzer = streichhoelzer-spieler2
    if streichhoelzer == 0:
        print("Spieler 1 hat gewonnen!")
        break
    else :
        print(streichhoelzer*"|")

       # for i in range(streichhoelzer) :
       #     print("|", end="") #end="" verhindert Zeilenumbruch
       # print("\n")
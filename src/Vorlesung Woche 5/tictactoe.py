def zeige_feld(feld):
    for zeile in feld:
        print("|".join(zeile))
        print("-"*5)

def aendere_spieler(s):
    if s=="X":
        return "O"
    return "X"

def mache_zug(feld,spieler,pos):
    i,j=pos
    if feld[i][j]==" ":
        feld[i][j]=spieler
        return True
    return False

def freie_felder(feld):
    ergebnis=[]
    for i in range(3):
        for j in range(3):
            if feld[i][j]==" ":
                ergebnis.append((i,j))
    return ergebnis

def gewinner(feld):
    for i in range(3):
        ## Zeile i
        if feld[i][0]==feld[i][1]==feld[i][2]!=" ":
            return feld[i][0]
        if feld[0][i]==feld[1][i]==feld[2][i]!=" ":
            return feld[0][i]
        if feld[0][0]==feld[1][1]==feld[2][2]!=" ":
            return feld[0][0]
        if feld[0][2]==feld[1][1]==feld[2][0]!=" ":
            return feld[0][2]

def vorbei(feld):
    g=gewinner(feld)
    if g:
        return g
    return len(freie_felder(feld))==0

feld=[[" ", " ", " "],
      [" ", " ", " "],
      [" ", " ", " "]]

spieler="X"
print("WILLKOMMEN BEI TIC TAC TOE")
zeige_feld(feld)
spiel_vorbei=False
while not spiel_vorbei:
    freiefelder=freie_felder(feld)
    while True:
        i,j=input("Geben Sie einen Zug ein\
                (im Format i,j): ").split(",")
        pos=int(i),int(j)
        if pos in freiefelder:
            mache_zug(feld,spieler,pos)
            zeige_feld(feld)
            spieler=aendere_spieler(spieler)
            break
        else:
            print("Zug nicht legal")
    spiel_vorbei=vorbei(feld)
sieger=gewinner(feld)
print("Gewinner:", "unentschieden" if sieger==None else sieger)





"""
Zusammenfassung/Was kann ich (auf Python bezogen) neues aus diesem Programm lernen/Wozu ist das wichtig?
1. Spiellogik: Das Programm implementiert die grundlegende Logik eines Tic-Tac-Toe-Spiels,
 einschließlich der Verwaltung des Spielfelds, der Spielerwechsel und der Überprüfung auf einen Gewinner oder ein Unentschieden.
2. Funktionen: Das Programm verwendet mehrere Funktionen, um verschiedene Aspekte des Spiels zu handhaben,
wie das Anzeigen des Spielfelds, das Ändern des Spielers, das Machen eines Zugs, das Überprüfen freier Felder und das Bestimmen des Gewinners.
Dies zeigt, wie man Funktionen in Python definiert und verwendet.
3. Benutzereingabe: Das Programm zeigt, wie man Benutzereingaben verarbeitet, indem es den Spieler auffordert, 
seine Züge einzugeben,und diese Eingaben validiert.
4. Schleifen und Bedingungen: Das Programm verwendet while-Schleifen und if-Bedingungen, 
um den Spielfluss zu steuern und sicherzustellen, dass das Spiel korrekt abläuft.
5. Datenstrukturen: Das Spielfeld wird als Liste von Listen dargestellt, was zeigt, 
wie man komplexe Datenstrukturen in Python verwenden kann, um Informationen zu organisieren und zu verwalten.
"""





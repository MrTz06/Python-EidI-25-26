# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)


def pyramide(n):
    ## Hilfsfunktion: fügt der Pyramide links und rechts eins Spalte von Leerzeichen hinzu
    def pyramide_padded(pyramide):
        pyramiden_liste = pyramide.split("\n")
        ergebnis = ""
        for zeilen_nr in range(len(pyramiden_liste)):
            ergebnis += " " + pyramiden_liste[zeilen_nr] + " \n"
        return ergebnis
    if n == 1:
        return "*"
    else:
        return pyramide_padded(pyramide(n-1)) + (2*n-1)*"*"

def pyramide_seq(n, k):
        return

# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)
import random

def zufallsstring(A, laenge):
    rueckgabe = ""
    ziellaenge = random.choice(range(0, laenge + 1))
    for i in range(ziellaenge):
        rueckgabe += random.choice(A)

    return rueckgabe


def wort_bzgl_laenge(n, A, l):
    ergebnis = ""
    for i in range(l - 1, -1, -1):  # i in {l-1,...,0} der Exponent vom MSB zum LSB
        ergebnis += A[n // len(A) ** i]
        n = n % len(A) ** i
    return ergebnis


def wort(n, A):
    l = 0
    b = len(A)
    while n >= b ** l:
        n = n - b ** l
        l += 1
    return wort_bzgl_laenge(n, A, l)


def alphpos(a, A):
    pos_a=A.find(a)
    return pos_a


def lexpos(s, A):
    return 0


def laengenlexpos(s, A):
    return 0


def trans(s, A, B):
    return ""


def kleiner(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) < laengenlexpos(Z, A)


def groesser(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) > laengenlexpos(Z, A)


def gleich(s, A):
    global vergleichszaehler
    vergleichszaehler += 1
    return laengenlexpos(s, A) == laengenlexpos(Z, A)


def suche_z_linear(alphabet):
    return ""


def suche_z_binaer(alphabet, laenge):
    return ""


if __name__ == "__main__":
    ag = int(input("Geben Sie eine Alphabetgröße zwischen 1 und 26 ein: "))
    maxPasswortLaenge = int(input("Geben Sie die maximale Passwortlänge ein: "))
    suchArt = int(input("Soll lineare Suche [0], binäre Suche [1] oder beides [2] angewendet werden? "))
    A = ""
    for i in range(ord("A"), ord("A") + ag):
        A = A + chr(i)
    Z = zufallsstring(A, maxPasswortLaenge)
    print("zufaellig erzeugter String: ", Z)
    if suchArt == 0 or suchArt == 2:
        vergleichszaehler = 0
        g = suche_z_linear(A)
        print(g + " gefunden mit linearer Suche")
        print("Test war" + (" erfolgreich" if g == Z else " erfolglos"))
        print(str(vergleichszaehler) + " Vergleiche wurden verwendet")  # zu hoch? siehe Notizen
    if suchArt == 1 or suchArt == 2:
        vergleichszaehler = 0
        g = suche_z_binaer(A, maxPasswortLaenge)
        print(g + " gefunden mit binärer Suche")
        print("Test war" + (" erfolgreich" if g == Z else " erfolglos"))
        print(str(vergleichszaehler) + " Vergleiche wurden verwendet")
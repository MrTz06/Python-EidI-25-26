# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)
def todigitlist(s):
    return list(map(int, s.split()))

def sum_unique_even_squares(L):
    return sum(x**2 for x in set(L) if x % 2 == 0)

def alt_digit_sum(n):
    return sum(int(digit) * (-1)**i for i, digit in enumerate(str(n)))











"""Hausaufgabe 1 (5=1+2+2 Punkte):
Definieren Sie die folgenden Funktionen. Der Rumpf jeder der Funktionen darf dabei nur
aus einer Zeile bestehen.
(a) Die Funktion todigitlist erwartet einen String, der nur Ziffern enth¨ alt, und soll
diese Ziffern als Liste von Integern zur¨ uckgeben.
Beispiele:"" →[]
"68423" →[6,8,4,2,3]
(b) Die Funktion sum_unique_even_squares erwartet eine Liste von Integern und soll
die Summe der Quadratzahlen der geraden Zahlen zur¨ uckgeben. Wiederholte Zahlen
sollen nur ein Mal zur Summe beitragen.
Beispiele: [] →0
[1,2,3,4] →20 (= 22 + 42)
[1,2,3,4,2] →20 (= 22 + 42)
[1,-2,3,4,2] →24 (= (−2)2 + 42 + 22)
(c) Die Funktion alt_digit_sum erwartet einen nicht-negativen Integer n und gibt die
alternierende Quersumme von n zur
¨ uck.
Beispiele: 12 →-1 (= 1−2)
52876 →10 (= 5−2 + 8−7 + 6)
Hinweis: Die Funktion sum berechnet die Summe der Eintr¨ age einer ¨ ubergebenen Liste. Zum
Beispiel liefert sum([1,2,3]) die R¨ uckgabe 6."""
## Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def all_mod_sum(k, l):
    def words(k, l):
        # Basisfall: Länge 0
        if l == 0:
            return ['']
        result = []
        for word in words(k, l - 1):
            for i in range(k):
                result.append(word + str(i))
        return result

    wortbuch = {}
    for word in words(k, l):
        quersumme = sum(int(char) for char in word) % k
        wortbuch[word] = quersumme
    return wortbuch






















"""Hausaufgabe 3 (5 Punkte):
Schreiben Sie eine Funktion all_mod_sum, die eine Ganzzahl 1 ≤k ≤10 und eine Ganzzahl
l ≥0 erwartet und ein W¨ orterbuch zur¨ uckgibt, welches jeder Zeichenkette der L¨
ange l¨ uber
dem Alphabet {’0’, ’1’, . . ., ’k-1’}die Quersumme seiner Zeichen modulo k zuordnet.
Definieren Sie dazu eine Hilfsfunktion words, welche mittels Backtracking alle ben¨ otigten
W¨ orter der L¨
ange l¨ uber dem Alphabet {’0’, ’1’, . . ., ’k-1’}berechnet und als Liste
zur
¨ uckgibt.
Beispiel: F¨
ur k = 2 lautet das Alphabet {’0’,’1’}. Der Aufruf all_mod_sum(2,5) soll das
W¨ orterbuch mit folgenden Schl¨ ussel-Wert Paaren zur¨ uckgeben:
Key Value Key Value Key Value Key Value
’00000’ 0 ’01000’ 1 ’10000’ 1 ’11000’ 0
’00001’ 1 ’01001’ 0 ’10001’ 0 ’11001’ 1
’00010’ 1 ’01010’ 0 ’10010’ 0 ’11010’ 1
’00011’ 0 ’01011’ 1 ’10011’ 1 ’11011’ 0
’00100’ 1 ’01100’ 0 ’10100’ 0 ’11100’ 1
’00101’ 0 ’01101’ 1 ’10101’ 1 ’11101’ 0
’00110’ 0 ’01110’ 1 ’10110’ 1 ’11110’ 0
’00111’ 1 ’01111’ 0 ’10111’ 0 ’11111’ 1"""
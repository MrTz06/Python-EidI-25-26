def move(Liste, string, int):
    if string in Liste:
        pos = Liste.index(string)
        neue_pos = pos + int % len(Liste)
        Liste.remove(string)
        Liste.insert(neue_pos, string)
        return Liste
    return None


print(move(["a", "b", "c"], "d", 1)) #sollte die gleiche Liste zurückgeben da "d" nicht in der Liste ist
print(move(["a", "b", "c"], "b", 0)) #sollte die gleiche Liste zurückgeben

print(move(["a", "b", "c"], "b", 2)) #sollte "b" 2x im Uhrzeigersinn in der liste verschieben Ergebnis:
print(move(["a", "b", "c"], "b", 5)) #sollte "b" 5x im Uhrzeigersinn in der liste verschieben Ergebnis:
print(move(["a", "b", "c"], "b", 21)) #sollte "b" 21x im Uhrzeigersinn in der liste verschieben Ergebnis:

print(move(["a", "b", "c"], "b", -2)) #sollte "b" 2x gegen den Uhrzeigersinn in der liste verschieben Ergebnis:
print(move(["a", "b", "c"], "b", -5)) #sollte "b" 5x gegen den Uhrzeigersinn in der liste verschieben Ergebnis:
print(move(["a", "b", "c"], "b", -21)) #sollte "b" 21x gegen den Uhrzeigersinn in der liste verschieben Ergebnis:

print(move(["a", "b", "c"], "b", 1))  #sollte ["a", "c", "b"] zurückgeben

print(move([], "b", 1)) #sollte die gleiche Liste zurückgeben
print(move(["a"], "a", 21))  #sollte die gleiche Liste zurückgeben

print(move(["a", "b", "a"], "a", 21)) #soll nur das erste "a" bewegt werden






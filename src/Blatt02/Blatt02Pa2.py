
x = False
s=input("Geben Sie einen String ein: ")

#1. Erste Bedingung: Palindrom
p = False
if s == s[::-1]:
    p = True
#2. Zweite Bedingung: Jedes Zeichen ist gedoppelt
d = False
if len(s) % 2 == 0:
    d = True
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            d = False
            break
#3. Dritte Bedingung: Erste Hälfte lexikografisch echt-kleiner
l = False
mid = len(s) // 2
first_half = s[:mid]
second_half = s[-mid:]
if first_half < second_half:
    l = True

x = p and d and l

print(x)





""" Pr¨ asenzaufgabe 2:
Geben Sie f¨ ur jede der folgenden Bedingungen einen Python-Ausdruck an, der genau dann
True ist, wenn ein String x die Bedingung erf¨ ullt. Finden Sie außerdem einen m¨ oglichst
kurzen String, welcher alle drei Bedingungen erf¨ ullt.
1. Der String x ist ein Palindrom.
Beispiele:
"lagerregal" −→ True 
2. Jedes Zeichen in x ist gedoppelt.
Beispiele:
"lagerhalle" −→ False
"aabbaacc" −→ True "bbaacaca" −→ False
3. Die erste H¨ alfte von x ist lexikographisch echt-kleiner ist als die zweite H¨ alfte. Wenn
x eine ungerade L¨ ange hat, soll das Zeichen in der Mitte ignoriert werden.
Beispiele:
"abermals" −→ "aber" < "mals" −→ True
"aufgabe" −→ "auf" > "abe" −→ False
"""
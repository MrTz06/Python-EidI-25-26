def wort_bzgl_laenge(n, A, l):
    ergebnis = ""
    for i in range(l-1, -1, -1):
        ergebnis += A[n // len(A)**i]
        n = n%len(A)**i

    return ergebnis

#for i in range (60):
#    print(wort_bzgl_laenge(i,"AB",3))

def wort (n, A):
    l = 0
    b = len(A)
    while n >= b**l:
        n = n - b**l
        l += 1
    return wort_bzgl_laenge(n, A, l)


for i in range (60):
    print (wort(i,"ABC"))

print(wort(42,"ABC"))













"""Pr¨ asenzaufgabe 1:
Im Folgenden sprechen wir ¨ uber die W¨ orter¨ uber einem Alphabet (z.B. {A, B, C, D}), d.h.
die Strings die aus Zeichen des Alphabets bestehen. Im Programm werden wir das verwen-
dete Alphabet als Alphabet-String darstellen, d.h. ein String aller Zeichen, in dem keines
der Zeichen wiederholt wird (z.B. "ABCD").
Die lexikographische Ordnung, welche durch den <-Operator auf Strings realisiert wird, ist
nicht geeignet um alle Strings ¨ uber einem Alphabet aufzuz¨ ahlen, da sie folgende Eigenschaft
hat:
Es gibt Strings x und y, sodass zwischen x und y unendlich viele andere Werte liegen, d.h.
es gibt unendlich viele Strings z f¨ ur die gilt x < z < y. Dies gilt zum Beispiel f¨
ur x=="A"
und y=="B", denn es ist "A" < "AA" < "AAA" < "AAAA" < ... < "B". W¨ urde man also
versuchen alle m¨ oglichen Strings nach dieser Ordnung aufzuz¨ ahlen, so w¨ urde man niemals
bei "B" ankommen.
Betrachten Sie nun die sogenannte l¨ angen-lexikographische Ordnung, hier dargestellt durch
<<, welche zwei Strings x und y auf folgende Weise miteinander vergleicht:
• Zuerst wird die L¨ ange der Strings verglichen:
Wenn len(x) < len(y), dann ist x << y.
Wenn len(y) < len(x), dann ist y << x.
• Funktioniert dies nicht, also falls len(x) == len(y), dann werden die W¨ orter lexi-
kographisch verglichen, also:
Wenn x < y, dann ist x << y.
Wenn y < x, dann ist y << x.
Die Aufz¨ ahlung aller W¨ orter ¨ uber einem Alphabet gem¨ aß der l¨ angen-lexikographischen
Ordnung beginnt also mit dem leeren String (einziger String der L¨ ange 0), dann kommen
alle W¨ orter der L¨ ange 1, dann alle W¨ orter der L¨ ange 2, usw. Zum Beispiel f¨ ur die W¨ orter
¨ uber dem Alphabet(-String) "AB" erhalten wir:
"" << "A" << "B" << "AA" << "AB" << "BA" << "BB" << "AAA"
<< "AAB" << "ABA" << "ABB" << "BAA" << ...
Wir gehen davon aus, dass die Zeichen in einem Alphabet-String entsprechend der le-
xikographischen Ordnung sortiert sind, d.h. verwenden wir Buchstaben, so m¨ ussen diese
entsprechend der alphabetischen Reihenfolge sortiert sein.
Schreiben Sie die folgenden Funktionen:
5
(a) Eine Funktion wort_bzgl_laenge mit ...
Eingabe: Ganzzahl n ≥0, Alphabet-String A, Ganzzahl l ≥0
Ausgabe: das n-te Wort aller W¨ orter der L¨
ange l,
¨ uber dem Alphabet A, bzgl.
lexikographischer Ordnung (wir beginnen bei 0 zu z¨ ahlen)
Hinweis: Sie d¨ urfen davon ausgehen, dass n maximal die Position des letzten Wortes
der L¨
ange l,
¨ uber dem Alphabet A, ist.
(b) Eine Funktion wort mit ...
Eingabe: Ganzzahl n ≥0, Alphabet-String A
Ausgabe: das n-te Wort aller W¨ orter ¨ uber dem Alphabet A, bzgl. l¨ angen-lexikographischer
Ordnung"""
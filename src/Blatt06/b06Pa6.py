




















"""Pr¨ asenzaufgabe 6:
Die Collatz-Folge beginnt mit einer positiven ganzen Zahl n und wird durch die folgenden
Regeln erzeugt:
• Wenn n gerade ist, ist die n¨ achste Zahl in der Folge n/2.
• Wenn n ungerade ist, ist die n¨ achste Zahl in der Folge 3 ∗ n + 1.
Schreiben Sie eine Funktion collatz, welche eine positive ganze Zahl erwartet und rekursiv
die Collatz-Folge, bis einschließlich zum ersten Auftreten einer 1, berechnet und auf der
Konsole ausgibt. Der R¨ uckgabewert der Funktion soll None sein.
Hinweis: Es ist bisher nicht bekannt, ob die Collatz-Folge f¨ ur jede nat¨ urliche Zahl n irgend-
wann 1 erreicht. Da dies jedoch zumindest f¨ ur alle n ≤ 268 und somit f¨ ur alle auf einem
64-Bit System darstellbaren Integer bewiesen ist, d¨ urfen Sie annehmen, dass eine, nach
obiger Aufgabenstellung, korrekt programmierte Rekursion terminiert.
Beispiel: F¨ uhrt man collatz(5) aus, so sollten 5, 16, 8, 4, 2, 1 ausgegeben werden. Die
Zahlen m¨ ussen in dieser Reihenfolge auf der Konsole ausgegeben werden, d¨ urfen aber in
verschiedenen Zeilen stehen. Die ausgegebenen Zahlen sollen immer Integer sein, z.B. soll
also 8 nicht als 8.0 ausgegeben werden."""
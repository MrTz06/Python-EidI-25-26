# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(uk109727), Jordan Bank(uk110417), Daniel Bosman(uk107607)

s = input("Geben Sie einen String ein: ")
f= True
if s == "0":
    f= True
elif s.startswith("-"):
    if s[1:] == "0":
        f= True
    elif s[1] == "0" or s[1:] == "" :
        f= False
    else:
        for zeichen in s[1:]:
            if zeichen < "0" or zeichen > "9":
                f= False
                break
else:
    if s.startswith("0") or s == "":
        f= False
    else:
        for zeichen in s:
            if zeichen < "0" or zeichen > "9":
                f= False
                break
print(f)

#Hausaufgabe 3 (4 Punkte):
#Schreiben Sie ein Programm, das ueuberprueft, ob ein eingegebener String eine Ganzzahl
#ohne fuehrende 0en darstellt. Sie duerfen nicht try und except oder sonstige Befehle zum
#Abfangen von Exceptions verwenden.
#Beispiele:
#"0" →True "00" →False "100" →True "-100" →True
#"--100" →False "abc" →False " 10 " →False "1-0" →False
#"01" →False "-01" →False "-0" →True "-00" →False
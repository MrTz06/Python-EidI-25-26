print("Willkommen zum Auswahlmenü!")
auswahl = input("Bitte geben Sie a,b,c oder d ein: ")
#a
if auswahl == "a":
    print("Sie haben Option a gewählt.")
    x=int(input("Bitte geben Sie einen Zahl ein: "))
    print(x*str(x))
#b
elif auswahl == "b":
    print("Sie haben Option b gewählt.")

#c
elif auswahl == "c":
    print("Sie haben Option c gewählt.")
    n=int(input("Bitte geben Sie einen Zahl ein: "))
    b=False
    if n%2==0:
        b=True
    if n%3==0:
        b=True
    if n%2==0 and n%3==0:
        b=False
    else :
        b=False

    print(b)
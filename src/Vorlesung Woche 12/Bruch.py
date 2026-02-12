"""def ggT(a, b):
    #Euklidischer Algorithmus zur Berechnung des ggT
    if a%b==0:
        return b
    else:
        return ggT(b, a%b)"""
def ggT(a, b):
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b>0:
        a, b = b, a % b
    return a

class Bruch:
    def __init__(self, zaehler, nenner):
        # Nenner prüfen (0 und negative Werte sind nicht erlaubt)
        if nenner == 0 or nenner < 0:
            raise ValueError("Nenner darf nicht null oder kleiner sein.")

        # Zähler 0 => Bruch als 0/1 normalisieren
        if zaehler == 0:
            self.zaehler = 0
            self.nenner = 1
            return

        # Attribute setzen und kürzen
        self.zaehler = zaehler
        self.nenner = nenner
        ggt = ggT(zaehler, nenner)
        self.zaehler //= ggt
        self.nenner //= ggt


    def __add__(self, other):
        a=self.zaehler
        b=self.nenner
        c=other.zaehler
        d=other.nenner
        return Bruch (a*d +b*c,b*d)
    def __sub__(self, other):
        a=self.zaehler
        b=self.nenner
        c=other.zaehler
        d=other.nenner
        return Bruch (a*d-b*c,b*d)
    def __str__(self):
        return str(self.zaehler) + "/" + str(self.nenner)




# Testbeispiele
x = Bruch(4, 8)
y = Bruch(10, 15)
print(x)  # Ausgabe: 1/2
print(y)  # Ausgabe: 2/3
print(x+y)# Ausgabe: 7/6
print(x-y)# Ausgabe:-1/6


#Frage: wenn ich Klassew student erstlle mit attributen blabala, ..., adresse,
# würde student von adresse erben, oder wie könnte student die klasse adresse verwenden?

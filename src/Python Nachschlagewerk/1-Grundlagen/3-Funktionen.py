#Funktionen in Python
#Stell dir vor, du hast einen Hund.
# Jedes Mal, wenn du willst, dass er bellt, müsstest du ihm theoretisch erklären:
# "Öffne den Mund, drücke Luft aus der Lunge, mache ein Geräusch, schließe den Mund."
# Das ist anstrengend.
# Viel einfacher ist es, ihm ein Kommando beizubringen: "Gib Laut!"

#In Python ist eine Funktion genau das:
# Du fasst mehrere Befehle unter einem einzigen Namen zusammen (dem "Kommando").

#So baust du eine Funktion:

# 1. Wir benutzen das Schlüsselwort def (für definieren).
# 2. Wir geben ihr einen Namen (z. B. sag_hallo).
# 3. Der Code, der ausgeführt werden soll, wird wieder eingerückt.
#z.B.
def sag_hallo():
    print("Hallo!")
    print("Wie geht es dir?")

#Jetzt passiert erstmal ... nichts.
# Wir haben dem Computer nur beigebracht, was sag_hallo bedeutet.
# Um es auszuführen, müssen wir die Funktion aufrufen:

sag_hallo()  # Jetzt führt er die Befehle oben aus

#Wir können Funktionen auch Daten ("Argumente") mitgeben, damit sie flexibel sind.
# Wie ein Toaster, in den man verschiedene Brotsorten stecken kann.
# z.B. eine Funktion, die jemanden begrüßt:
def begruessung(name):
    print("Hallo, " + name + "!")
    print("Schön, dich zu sehen.")
# Jetzt können wir die Funktion mit verschiedenen Namen aufrufen:
begruessung("Anna")  # Ruft die Funktion mit dem Argument "Anna" auf
begruessung("Ben")   # Ruft die Funktion mit dem Argument "Ben" auf
begruessung("Clara") # Ruft die Funktion mit dem Argument "Clara" auf
# Funktionen können auch Werte zurückgeben, die wir weiterverwenden können. z.B. eine Funktion, die zwei Zahlen addiert:
def addiere(a, b):
    return a + b  # Gibt die Summe von a und b zurück

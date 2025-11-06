text=input("Geben Sie einen Text ein: ")

verschiebung=int(input("Verschiebung, bspw. 3"))

ergebnis=""

for zeichen in text:
    position=ord(zeichen)
    position_neu= position+verschiebung
    zeichen_neu=chr(position_neu)
    ergebnis=ergebnis+zeichen_neu

print("Verschlüsselter Text", ergebnis)
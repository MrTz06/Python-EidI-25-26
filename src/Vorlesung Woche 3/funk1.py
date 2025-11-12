def teilt(i,t): 
    """Eingabe: i, ein Integer
    und ein positiver Integer t.
    Gibt True zurueck, falls i durch t teilbar ist
    ansonsten False
    """
    #print("Gerade sind wir in ist_gerade")
    return i%t==0

teiler=int(input("Geben Sie einen Teiler ein: "))

print(" Teilbarkeit durch "+ str(teiler))
for n in range(101):
    if teilt(n,teiler):
        print(n)

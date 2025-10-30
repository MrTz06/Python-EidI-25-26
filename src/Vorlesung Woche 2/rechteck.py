b=int(input("Geben Sie die Breite ein: "))
h=int(input("Geben Sie die Höhe ein: "))

for i in range(h):
    for j in range(b):
        if i==0 or i==h-1 or j==0 or j==b-1:
            print("*",end="")
        else:
            print(" ",end="")
    ## Zeilenumbruch
    #print()
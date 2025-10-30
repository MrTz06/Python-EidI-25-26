h=int(input("Geben Sie die Höhe ein: "))
for i in range(1,h+1):
    for bla in range(h-i):
        print(" ", end="")
    for j in range(1,2*i):
        print(str(j%10), end="")
    print()
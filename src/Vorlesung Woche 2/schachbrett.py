n=int(input("Geben Sie eine Seitenlänge an: "))

b=0
for i in range(n):
    for j in range(n):
        if b%2==0:
            print("#",end="")
        else:
            print(" ",end="")
        b=b+1
    b+=1
    print()
print()
print()
print()

for i in range(n):
    for j in range(n):
        if not (i+j)%2:
            print("#",end="")
        else:
            print(" ",end="")
    print()
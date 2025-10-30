n=int(input("Geben Sie eine natürliche Zahl ein: "))

t=2
prim=True
while t<n:
    if n%t==0:
        prim=False
    t=t+1

if prim:
    print(str(n) + " ist eine Primzahl")
else:
    print(str(n) + " ist keine Primzahl")

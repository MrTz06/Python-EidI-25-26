x=int(input("Integer:"))
while x!=0:
    if x%2==0:
        x=0
    summe=0
    for i in range(x,100,2):
        summe+=i
    if summe>1131 and not summe==4950:
        x=x+2
    else:
        x=0

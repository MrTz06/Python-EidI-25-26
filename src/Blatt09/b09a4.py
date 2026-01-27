def print_combo(wort):
    count=0
    while wort[0]==" " or wort[-1]==" ":
        if wort[0]==" ":
            wort=wort[1:]
        elif wort[-1]==" ":   
            wort=wort[:-1]
    while wort!="":
        for j in range(1,len(wort)):
            count+=1
            print(wort[0]+wort[j])
        wort=wort[1:]

ein=input("Bitte Eingabe tätigen: ")  
print_combo(ein)
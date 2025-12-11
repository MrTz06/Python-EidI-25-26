def pyramid (n: int):
    #basisfall
    if n == 1:
        return "*"
    #Rekursionsfall
    else:
        return pyramid(n-1) + (2*n -1) * "*" 
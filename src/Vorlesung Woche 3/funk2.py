def f(x):
    x=x+1
    print("Innerhalb f, x=", x)
    return x

def g(x):
    x=x+x
    print("Innerhalb g, x=", x)
    return x

x=3
z=f(x)
print("Im Hauptprogramm, x=",x)
print("Im Hauptprogramm, z=",z)
u=g(x)
x=18
print("Im Hauptprogramm, x=",x)
print("Im Hauptprogramm, u=",u)

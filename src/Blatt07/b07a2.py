# Gruppenmitglieder der Abgabegruppe 51:
# Moritz Glaser(36401905), Jordan Bank(36359741), Daniel Bosman(36360019)

def kleinster_baum(baum):
    hoehe_regel_a = baum-34
    hoehe_regel_b = (baum-11)/2

    #Basisfall: beide Regeln sind nicht möglich, die aktuelle Höhe ist die kleinste mögliche
    if hoehe_regel_a<=0 and hoehe_regel_b<=0:
        return baum
    #Rekursiver Fall: beide Regeln sind möglich, wähle die kleinere Höhe
    if hoehe_regel_a>0 and hoehe_regel_b>0:
        return min(kleinster_baum(hoehe_regel_a), kleinster_baum(hoehe_regel_b))
    #Rekursiver Fall: nur Regel B ist möglich
    if hoehe_regel_b > 0:
        return kleinster_baum(hoehe_regel_b)
    #Rekursiver Fall: nur Regel A ist möglich
    if hoehe_regel_a > 0:
        return kleinster_baum(hoehe_regel_a)

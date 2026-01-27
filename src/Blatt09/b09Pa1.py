def convertible_to_int (s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
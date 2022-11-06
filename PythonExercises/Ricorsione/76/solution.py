
def es76(parola):
    if not parola:
        return []
    else:
        return [parola] + es76(parola[1:])

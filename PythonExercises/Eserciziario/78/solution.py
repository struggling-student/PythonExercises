
def es78(parola):
    if len(parola)==1: return [parola]
    a=parola[0]
    lista= es78(parola[1:])
    lista1=lista[:]
    if a not in lista1: lista1+=[a]
    for y in lista:
        if a<=y[0] and a+y not in lista1: lista1+=[a+y]
    return sorted(lista1)





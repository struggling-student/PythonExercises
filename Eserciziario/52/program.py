def es52(d1,d2):
    '''
    Si definisca la  funzione es52(d1,d2) che, 
    - riceve due dizionari di matrici sparse della stessa dimenzione.
    - restituisce un dizionario con la matrice sparsa somma delle due matrici avute in input.
    Ad ESEMPIO se
    d1={(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 } e d2={(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }
    allora la funzione restituira' il dizionario 
    {(0,2): 4,(1,0): 3, (1,1): 4, (2,1):8, (0,0):5, (2,2):5 }
    I dizionari ricevuti non devono essere modificati
    '''

    risultato = {key: d1[key] for key in d1}
    for key in d2:
        if key in risultato:
            risultato[key] += d2[key]
        else:
            risultato[key] = d2[key]
    return risultato
    

print(es52({(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 }, {(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }))

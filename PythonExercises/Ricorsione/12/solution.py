

import albero

'''
    Es 12: 3 punti
    Un albero si dice binario completo se tutti i suoi nodi interni hanno esattamente 2 
    figli e tutte le foglie si trovano allo stesso livello.
    Si definisca la funzione es12(k ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti  un intero k 
    - costruisce un albero binario completo di altezza k composta da nodi del tipo  
      Nodo definito nella libreria albero.py allegata. Gli identificatore delle foglie, 
      letti da sinistra a destra sono i 2^k-interi che vanno da 1 a 2^k (nota che 
      un albero binario completo di altezza k ha sempre 2^k foglie). Gli identificatori 
      dei nodi interni sono dati dalla somma degli identificatori dei due loro figli. 
    - torna come risultato la radice dell'albero costruito. 
    Esempio: 
    - es12(2)  crea e restituisce l'albero a sinistra 
    - es12(3) crea e restituisce l'albero a destra


                    10                                  36               
             _______|______                      _______|______         
            |              |                    |              |        
            3              7                   10             26        
         ___|___        ___|__               ___|___        ___|__      
        |       |      |      |             |       |      |      |     
        1       2      3      4             3       7     11     15     
                                           _|_     _|_    _|_    _|_    
                                          |   |   |   |  |   |  |   |   
                                          1   2   3   4  5   6  7   8   
                                                                   
    '''

import albero

def es1(k):
    # inserisci qui il tuo codice
    t,_ = crea_albero(k,1)
    return t

def crea_albero(k, n):
    """
    crea l'albero con k livelli a partire dal valore n
    torna l'albero e l'ultimo n usato
    """
    if k:       # se siamo su un nodo interno
        t = albero.Nodo( None )
        sinistro, n1 = crea_albero(k-1, n)
        destro,   n2 = crea_albero(k-1, n1+1)
        t.f = [sinistro, destro]
        t.id = sinistro.id + destro.id
        return t, n2
    else:
        t = albero.Nodo(n)
        return t, n


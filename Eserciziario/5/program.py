    
def es5(insieme,k):
    '''
    Es 11: 6 punti
    Si definisca la funzione es5(insieme, k) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti un insieme di stringhe  ed un intero k>0 
    - trova le diverse stringhe che si possono ottenere concatenando k copie delle stringhe 
    originali (una stessa stringa puo' essere utilizzata  piu' volte nelle concatenazioni). 
    - torna come risultato l'insieme delle stringhe trovate.
    Esempi: sia insieme={'a','bb','c'}
    1)  es5(insieme, 1) restituisce l'insieme {'a','bb','c'}
    2)  es5(insieme, 2) restituisce l'insieme {'aa','abb','ac','bba','bbbb','bbc','ca','cbb','cc' }
    3)  es5(insieme, 3) restituisce l'insieme
    {'bbca', 'bbbbbb', 'ccc', 'cca', 'caa', 'ccbb', 'bbaa', 'abbc', 'aac', 'abbbb', 'acbb', 'cbbc', 
    'bbbba', 'bbabb', 'cbba', 'cac', 'bbac', 'acc', 'aabb', 'aca', 'bbbbc', 'aaa', 'cbbbb', 'abba', 
    'bbcbb', 'cabb', 'bbcc}

    SUGGERIMENTO: potete simulare il ciclo su k con la ricorsione
    '''
    return es5_ric(insieme,k, insieme)
def es5_ric(insieme, k, out):
    if k == 1:
        return out
    else:
        nuovo = set()
        for a in insieme:
            for b in out:
                nuovo.add(a+b)
        return es5_ric(insieme, k-1, nuovo)
        
print(es5({'a','bb','c'},3))
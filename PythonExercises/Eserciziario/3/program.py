def es3(ins1, ins2):
    '''
    progettare la funzione es3(ins1, ins2) che:
    - riceve  in input due insiemi  di numeri naturali
    - trova le terne (a,b,c) con a,b e c in insi1 con la proprieta' che a<b<c e a+b+c e' in insi2
    - restituisce l'insieme di tutte le triple trovate.
    Nella lista restituita le triple devono essere  rappresentate tramite tuple e le
    varie tuple devono comparire nella lista per somma di componenti crescenti e in caso di parita'
    in ordine lessicografico crescente.
    ESEMPIO:
    se ins1={ 2,4,5,6,8,9} e ins2={5,15,19,25} la funzione restituisce la lista
    [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
    ''' 
    ls = list(ins1)
    ls.sort()
    risultato = []
    for i, a in enumerate(ls[:-2]):
        for b in (ls[i+1:-1]):
            for c in (ls[ls.index(b)+1:]):
                if (a+b+c) in ins2:
                    risultato.append(tuple([a,b,c]))
    return sorted(risultato, key=lambda x: x[0]+x[1]+x[2])
#print(es3({ 2,4,5,6,8,9}, {5,15,19,25}))
#print(es3({ 1,2,4,5,6,8,9}, {16,18}))

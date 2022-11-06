

def es56(tabella):
    '''
    la funzione es56(tabella) che presa in input:
    - una tabella  di interi (rappresentata tramite lista di liste in cui ciascuna lista e' 
    una riga della tabella) restituisce la lista con gli interi che occorrono il massimo 
    numero di volte nella tabella e modifica la tabella distruttivamente. 
    La lista restituita deve risultare  ordinata in modo crescente. Al termine della funzione, 
    nella tabella i numeri che occorrevano un numero massimo di volte devono risultare sostituiti dal 
    carattere '*'.
    Ad esempio per tabella= [[3,2,1,3],[2,1,3,5],[1,3,2,1]] al termine della funzione la lista 
    restituita e' [1,3] e la tabella diviene [[*,2,*,*],[2,*,*,5],[*,*,2,*]] 
    '''
    # inserisci qui il tuo codice
    counts = {}
    mc = 0
    for r in tabella:
        for v in r:
            if v in counts:
                counts[v] += 1
            else:
                counts[v] = 1
            mc = max(mc, counts[v])
    maxxes = []
    for k,v in counts.items():
        if v == mc:
            maxxes.append(k)
    for r in tabella:
        for i,v in enumerate(r):
            if v in maxxes:
                r[i] = '*'
    maxxes.sort()
    return maxxes


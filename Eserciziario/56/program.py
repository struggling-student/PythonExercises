

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
    occ = {}
    for r in range(len(tabella)):
        for c in range(len(tabella[0])):
            if tabella[r][c] in occ:
                occ[tabella[r][c]] += 1
            else:
                occ[tabella[r][c]] = 1
    massimo = max(occ.values())
    result = []
    for key in occ:
        if occ[key] == massimo:
            result.append(key)
    result.sort()
    for r in range(len(tabella)):
        for c in range(len(tabella[0])):
            if tabella[r][c] in result:
                tabella[r][c] = '*'
    return result


print(es56([[3,2,1,3],[2,1,3,5],[1,3,2,1]]))


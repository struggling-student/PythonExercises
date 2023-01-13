import json


def es34(fname1, fname2):
    '''  
    Un quadrato latino e' una scacchiera quadrata di lato N con un simbolo (scelto in un insieme di N elementi)
    su ogni casella in modo che ognuno dei simboli compaia una e una sola volta in ogni riga e in ogni colonna.
    Implementate la funzione es34(fname1,fname2) che prende in input l'indirizzo fname1 di un file json in cui e'
    contenuto un quadrato latino privato dell'ultima riga e dell'ultima colonna. 
    La scacchiera e' rappresentata come lista di liste. Bisogna completare il quadrato latino e 
    registrarlo come file json all'indirizzo fname2. 
    La funzione deve poi restituire l'insieme dei simboli che compaiono nel quadrato latino.
    Ad esempio: se la lista di liste in fname1 con il quadrato latino parziale e'
    [['X','1'],['?','X']] allora, l'insieme  con i simboli del quadrato latino sara' 
    {'X','1','?'} e la lista di liste in fname2 con il quadrato latino completo sara' 
    [['X','1','?'],['?','X','1'],['1','?','X']]
    Nota: assumete che sia sempre N>2
    '''
    # inserisci qui il tuo codice
    #[['X','1','?'],
    # ['?','X','1'],
    # ['1','?','X']]

    quadrato = []
    with open(fname1, encoding='utf8') as f:
        quadrato = json.load(f)
    simboli = set(quadrato[0]).union(set(quadrato[1]))
    N = len(simboli)
    for line in quadrato:
        line.append((simboli-set(line)).pop())
    print(quadrato)
    last = []
    for c in range(N):
        col = set(l[c] for l in quadrato)
        last.append((simboli-col).pop())
    quadrato.append(last)
    with open(fname2, mode='w', encoding='utf8') as f:
        json.dump(quadrato, f)
    return simboli

print(es34('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Matrici/34/file3.json','/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Matrici/34/risposta.json'))
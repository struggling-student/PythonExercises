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



def es53(ftesto):
    '''
    Si definisca la  funzione es10(ftesto) che, 
    - riceve l'indirizzo di un file di testo.
    - restituisce un dizionario con chiavi degli interi e attributi delle liste di interi.
    Il dizionario da restituire e' contenuto all'interno del file di testo dove e' presente 
    una sequenza di interi 
    inframmezzata da un numero arbitrario di spazi (' '), andate a capo ('\n') e due punti (':').
    Le chiavi del dizionario sono seguite da sempre dai ':' e poi dagli elementi della lista attributo.
    ESEMPI:
    se il file contiene il testo
    '' 
    3 : 3 6 9
    2: 4 6 10
    ''
    la funzione restituira' il dizionario { 3: [3,6,9], 2: [4,6,10]}
    Se il file contiene 
    ''     4: 5 6: 7        8 
    9 10 11:12 13:14 
    15'' 
    la funzione restituira' il dizionario {4:[5], 6:[7,8,9,10], 11:[12], 13:[14,15]}
    '''
    # inserisci qui il tuo codice



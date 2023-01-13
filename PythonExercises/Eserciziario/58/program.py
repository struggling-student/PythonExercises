

def es58(lista):
    '''
    La funzione es58(lista) che presa
    - una lista di stringhe  i cui caratteri sono nell'insieme { 'N','E','S','O'},
    modifica distruttivamente la lista e restituisce il numero totale di caratteri presente
    nella lista (vale a dire la somma del numero di caratteri delle stringhe presenti nella lista).
    Ogni stringa rappresenta una sequenza di mosse effettuate da un robottino su di una griglia:
    il robottino puo' spostarsi da una cella ad una delle celle adiacenti nelle 4 direzioni.
    Ogni carattere della stringa rappresenta una mossa in una delle 4 direzioni:
    N sta per una mossa verso la cella  alto, E per una mossa verso la cella a destra,
    S per una mossa verso la cella in basso basso e O per una mossa verso la cella a sinistra.
    La stringa rappresenta dunque un cammino che dalla cella di pertanza permette di
    raggiungere una certa cella di destinazione.
    Al termine della funzione ciascuna stringa della lista va sostituita da un numero. Il numero
    rappresenta il numero minimo di mosse necessarie al robottino per andare dalla cella
    iniziale alla cella destinazione individuata dalla stringa.
    Ad esempio per lista=[ 'NS', 'NEESS', 'NNOOO','NNEESSO'],
    al termine la funzione restituisce il numero 19 e la lista risulta essere [0,3,5,1]
    '''
    #inserisci qui il tuo codice
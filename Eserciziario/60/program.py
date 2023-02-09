

def es60(ftesto, ftestoMod):
    '''
    La funzione es60(ftesto, ftestoMod) che modifica il contenuto del file di testo il cui
    percorso e' dato da ftesto, registra il file modificato nel file di testo il cui indirizzo
    e' in ftestoMod e restituisce un intero.
    Il file di testo ftesto contiene una matrice che ha per elementi elementi interi tra 1 e 9.
    Ogni riga del file di testo contiene una riga della matrice ed i vari interi della riga sono
    separati tra loro da uno spazio.
    Una colonna della matrice si dice "dispari" se la maggior parte dei suoi elementi e' dispari.
    (se il numero di elementi dispari è uguale al numero di elementi pari, la riga non è dispari)
    In ftestoMod deve essere registrata la matrice dove tutti gli elementi  che occorrono
    in colonne "dispari" sono stati sostituiti dalla cifra zero.
    La funzione restituisce il numero di colonne della matrice che sono state azzerate.
    Ad esempio se il file in ftesto contiene la matrice:
    1 2 3 4 5 7
    3 4 4 4 4 5
    3 1 4 6 3 1
    2 5 8 1 7 3
    al termine della funzione verra' restituito il numero 3 e il file ftestoMod conterra' la matrice
    0 2 3 4 0 0
    0 4 4 4 0 0
    0 1 4 6 0 0
    0 5 8 1 0 0
    '''
    # inserisci qui il tuo codice 

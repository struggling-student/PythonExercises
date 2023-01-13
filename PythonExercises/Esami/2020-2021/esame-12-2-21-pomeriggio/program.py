################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE SUBITO QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG 
#   per eseguire solo parte dei test commentare parte della lista "tests"
#   alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''
    Es 1: punti 7 
    Due matrici di interi A e B della stessa dimensione
    MxN sono codificate in un file di testo nel seguente modo: gli MxN
    elementi della prima matrice sono presenti nelle prime M x N righe
    del file, ognuna di queste righe contiene tre interi separati da
    spazi i, j e k ad indicare che A[i][j] vale k.  Seguono un po' di
    righe vuote e poi compaiono in sequenza le MxN righe contenenti
    gli MxN elementi della matrice B, ciascuna di queste righe
    contiene tre interi i, j e k ad indicare che il valore di B[i][j]
    e' k. Ad esempio il file f1.txt codifica le due matrici di
    dimensione M=2 x N=3

    A= 1 3 2   B= 7 8 1 
       5 5 6      3 4 6

    Progettare una funzione es1(ftesto) che, prende in input
    l'indirizzo di un file di testo siffatto e restituisce la matrice
    somma di A e B rappresentata come lista di liste.  La matrice
    restituita e' codificata come lista di liste

    Ad esempio, per il file di testo f1.txt  
    la funzione restituisce  la lista di liste:
    [[8,11,3],[8,9,12]]
'''

def es1(fname):
    # Inserisci qui il tuo codice
    pass
        
#####################################################################################


'''    
    Es 2: punti 8
    
    Abbiamo un' immagine dove su sfondo nero sono disegnati in bianco
    rettangoli e quadrati che non si toccano ne si intersecano e i cui
    lati sono segmenti orizzontali o verticali.  Si veda ad esempio
    l'immagine in fig1.png.  I rettangoli presenti hanno aree diverse
    e vogliamo individuare quello di area massima.
   
    Progettare la funzione es2(fname) che prende come parametro
    l'indirizzo di un file .PNG contenente l'immagine e restituisce
    una coppia.  Le due coordinate della coppia contengono l'indice di
    riga e l'indice di colonna del vertice in basso a destra del
    rettangolo di area massima presente nella figura.  Ad esempio per
    l'immagine fig1.png la funzione deve restituire la coppia (90,125).

    Per caricare e salvare i file PNG si possono usare load e save
    della libreria immagini.
    '''

import immagini

def es2(fname1):
    # Inserisci qui il tuo codice
    pass


############################################################################


'''
    Es. 3: punti 8
   
    Si definisca la funzione es3(r1) ricorsiva (o che fa uso di
    funzioni o metodi ricorsive/i) che riceve come parametri la radice
    r1 di un albero binario formato da nodi del tipo AlberoBinario
    definito nella libreria albero.py. La funzione deve restituire una
    lista coi valori dei nodi per cui almeno uno dei figli e' una
    foglia.  La lista non deve contenere duplicati e deve risultare
    ordinata in modo crescente.

    Ad esempio per l'albero :
         0          
        / \         
       5   6        
          /         
         3          
        / \         
       9   7        

   La funzione es3 restituisce la lista [0,3]

   NOTA: definite le vostre sottofunzioni a livello esterno altrimenti
          non passate il test di ricorsione
'''


import albero

def es3(r1):
    # Inserisci qui il tuo codice
    pass


###########################################################################
'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es(dirname) che
    riceve come argomento il nome di una directory (dirname).
    La funzione esplora la directory dirname e le sue sottodirectory alla 
    ricerca di directory vuote e restituisce una lista.  
    La lista contiene i nomi delle directory che non contengono al loro interno altre direcory
    e risulta ordinata lessicograficamente.
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio con dirname='dir1' la funzione es4 deve restituire la lista:
    ['dir1/stanza1/stanza2']
   
    NOTA: è proibito usare la funzione os.walk 
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate il
    test di ricorsione
'''    


import os
def es4(dirname): 
    # inserisci qui il tuo codice
    pass

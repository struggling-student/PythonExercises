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
#   per eseguire solo parte dei test commentare le righe 288-292 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''
Es 2: punti 6.

Si progetti la funzione che es2(fname) che, prende in input 
l'indirizzo di un file di testo  e restituisce una  lista di interi. 
Ciascuna riga del file contiene una espressione aritmetica del tipo somma di prodotti di interi positivi.
NOTA: 
Ad esempio
    3 *8 + 5 * 2 * 4 + 2 * 7
 
Ciascuna riga del file termina con un'andata a capo.
Si veda ad esempio il file espressioni1.txt.
La lista da restituire ha tanti elementi quante sono le righe del file di testo e, 
in posizione i, contiene l'intero risultante dall'esecuzione della
espressione aritmetica presente nella riga i -ma del file.

ATTENZIONE: è proibito usare la funzione eval o similari per valutare la stringa direttamente.

Ad esempio per il file expression10.txt che contiene l'espressione precedente la lista da produrre e'
[78]
mentre per il file di sette righe expressioni1.txt la lista da produrre e' 
[370944104397271266530, 744446970798550722708, 2379237618858967013923674, 682592962108239278, 
 120096990261873938567, 1188935186355062021134908, 2749828376010] 
'''

def es2(fname):
    # inserisci qui il tuo codice
    pass

#####################################################################################


'''    
    Es 4: punti 9
    
    Abbiamo immagini che contengono su sfondo nero cammini di color bianco 
    che non si intrecciano ne' si toccano e sono formati da segmenti orizzontali 
    o verticali consecutivi.
    Si veda ad Esempio l'immagine f4c.png.
    Progettare la  funzione es4(fname1) che prende in input l'indirizzo 
    di un file .png. e restituisce un insieme di quadruple di interi. 
    L'insieme  deve contenere 
    una quadrupla per ogni cammino presente nell'immagine. 
    Se il cammino ha come estremi i due pixel (w1,h1) e (w2,h2), la quadrupla  contiene 
    nell'ordine i quattro interi w1,h1, w2,h2  
    I due pixel devono comparire nella quadrupla ordinati per colonna crescente (vale a dire 
    w1 <= w2) ed a parita' di colonna per riga crescente (vale a dire (h1<=h2).
    
    Ad esempio per l'immagine f4c.png l'insieme restituito  sara' 
    {(20, 20, 99, 20), (20, 40, 20, 50), (30, 60, 70, 70)} 
    
    Per caricare e salvare i file PNG si devono usare load e 
    save della libreria immagini.
    '''
import immagini

def es4(fname1):
    # inserisci qui il tuo codice
    pass

############################################################################

import albero

'''
    Es. 5: punti 6

    Si definisca la funzione es5(r) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice r di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py e 
    restituisce un dizionario.
    Il dizionario contiene come chiave le altezze in cui sono presenti nodi dell'albero
    e associata ad ogni altezza c'e' la lista  coi valori dei nodi che nell'albero
    si trovano a quell'altezza. La lista non contiene duplicati e i suoi valori devono 
    essere ordinati in modo crescente. 

    Ad esempio per l'albero:
                    10                                       
             _______|______                              
            |              |                           
            3              3                           
         ___|___        ___|__                    
        |       |      |      |                
        2       1      8      1                  

   la funzione e5 restituisce il dizionario {0:[10], 1:[3],2:[1,2,8]}


    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''

def es5(r):
    # inserisci qui il tuo codice
    pass

  
###########################################################################

'''
    Es. 7: punti 9
    
    Si vogliono estrarre dei frammenti di testo da file che sono contenuti in una directory.
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es7(dirname, ext) che
    riceve come argomenti il nome di una directory (dirname) e l'estensione (ext) dei file cercati.
    L'estensione del nome di un file è sempre di 3 caratteri.
    La funzione esplora la directory dirname e ritorna un dizionario in cui:
        - le chiavi sono i path completi dei file che hanno estensione 'ext' indipendentemente dalle maiuscole/minuscole
        - i valori sono delle stringhe che contengono i primi 10 caratteri dei file individuati
    Assumete che ciascun file contenga almeno 10 caratteri.    
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os
def es7(dirname, ext): 
    # inserisci qui il tuo codice
    pass

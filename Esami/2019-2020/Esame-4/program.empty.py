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
#   per eseguire solo parte dei test commentare le righe 179-182 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''
Es 1: punti 8.
Un file contiene una sequenza  di uguaglianze tra espressioni aritmetiche del tipo somme 
di prodotti di interi positivi. E' presente un'uguaglianza per ogni 
riga del file e ciascuna riga termina con un'andata a capo.

Si veda ad esempio il file uguaglianze1.txt. 
contenente le 4 uguaglianze:

2+3+12=9+8
2+3+4=9*2
22=3+4+5+2*5
3+5+1=4+44

Si noti che le uguaglianze possono essere sia corrette (la prima e la terza) che 
sbagliate (la seconda e l’ultima).

Si progetti una funzione es1(ftesto) che prende in input   l'indirizzo 
del file contenente la sequenza di uguaglianze e restituisce una lista binaria. 
La lista binaria deve contenenre  un bit per ogni uguaglianza del file. Il bit i-esimo della lista 
vale 1 se l'i-esima uguaglianza del file  e' corretta, 0 altrimenti. 

Per il file uguaglianze1.txt la funzione e1 deve restituire la lista [1,0,1,0]. 

ATTENZIONE: è proibito usare la funzione eval o similari per valutare le stringhe 
di somme di prodotti direttamente.
'''


def es1(fname):
    # inserisci qui il tuo codice
    pass
   

#####################################################################################


'''    
    Es 2: punti 6
    
    Abbiamo immagini che contengono su sfondo nero rettangoli di diversi colori che non 
    si intersecano   e i cui lati sono segmenti orizzontali o verticali. 
    Si consideri ad esempio la figura Rettangoli.png.
    Progettare la  funzione es2(fname,w1,h1) che prende come parametri 
    l'indirizzo di un file .PNG con figure siffatte e le coordinate (w1,h1) 
    di un punto  appartenente ad uno dei rettangoli della figura e restituisce 
    il numero di pixel occupati dal rettangolo
    
    Ad esempio per il file Rettangoli.png e il pixel 20,20 la funzione e2 deve restituire 4200.

    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

import immagini

def es2(fname,w1,h1):
    #inserisci qui il tuo codice
    pass
    

############################################################################



'''
    Es. 3: punti 9
    Dato un intero n, l'albero dei divisori di n e' definito come segue:
    il nodo radice ha valore n e ogni altro nodo dell'albero ha come figli i divisori 
    propri del valore del padre in ordine crescente.
    Si ricorda che i divisori propri di un numero sono tutti i numeri positivi che lo dividono 
    tranne l'uno e il numero stesso. 
    Ad esempio i tre alberi che seguono sono nell'ordine, alberi dei divisori di 8, 12 e 25.
    
    
             8                     12                            25
            _|_                ____|_____                        | 
           |   |               |  |  |   |                       5
           2   4               2  3  4   6                         
               |                     |  _|_
               2                     2 |   |
                                       2   3 
    
    Si definisca la funzione es3(n) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come argomento un intero n e 
    genera l'albero dei divisori di n. I nodi dell'albero sono del tipo  Albero definito 
    nella libreria albero.py allegata.
    La funzione deve ritornare  la radice dell'albero generato.
    
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
    il test di ricorsione
    '''

import albero

def es3(n):
    # inserisci qui il tuo codice
    pass
  
###########################################################################

'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es4(dirname) che
    riceve come argomento il nome di una directory (dirname).
    La funzione esplora la directory dirname  e le sue sottodirectory 
    alla ricerca di file con lo stesso nome ed estensione 'txt' e ritorna un dizionario.
    Le chiavi del dizionario sono i nomi dei file   che appaiono piu' volte (privati dell'estensione 'txt')
    gli attributi  sono insiemi che contengono  il nome per esteso di ciascuno dei file ripetuti.
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio per la cartella dir1 la funzione es4 deve restituire il dizionario:
    d={
    'esercizio1': {'dir1/esercizio1.txt', 'dir1/st1/st3/esercizio1.txt', 'dir1/st1/esercizio1.txt'}
    'esercizio5': {'dir1/st1/st3/esercizio5.txt', 'dir1/st2/esercizio5.txt'}, 
    }
    
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os

def es4(dirname):
    #inserisci qui il tuo codice
    pass





################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################

'''
Es 1: punti ?.

Si progetti la funzione es1(lista) che riceve come argomento una lista di interi e cancella 
da questa tutti gli elementi duplicati lasciando in lista per ogni 
elemento solo la sua prima occorrenza. La funzione restituisce il numero di elementi cancellati.

Attenzione: al termine della funzione la lista deve risultare modificata.


Ad esempio per lista=[5,2,5,5,2,3,5,3,2,5,1,1]
es1(lista) restituisce 8 e la lista risulta modificata in [5,2,3,1]

'''

def es1(lista):
    # inserisci qui il tuo codice
    pass



################################################################################

'''
Es 2: punti ?.

L'orlo di una matrice e' costituito dalle sue righe e dalle sue colonne piu' esterne 
(vale a dire prima riga, prima colonna, ultima riga e  ultima colonna).  

Si definisca la funzione es2(mat) che riceve come argomento una  matrice di interi mat 
(rappresentata tramite lista di liste) e restituisce una coppia.
Il primo elemento della coppia e' la lista di tutti gli interi unici presenti all'interno 
della matrice che non compaiono sul suo orlo. Il secondo elemento della coppia e' 
la lista di tutti gli interi che compaiono sull'orlo della matrice e non al suo interno. 
Entrambe le liste devono risultare ordinate in ordine crescente. 

ad esempio se mat=
[[9,2,3,4,4,3],
 [3,8,4,8,1,5],
 [3,3,4,1,2,6],
 [9,5,7,6,4,6]
 ]
es2(mat) restituisce ([1,8],[5,6,7,9])
'''

def es2(mat):
    # inserisci qui il tuo codice
    pass

#####################################################################################

'''
Es 3: punti ?.

Un robot e' in grado di muoversi nel piano nelle quattro direzioni 
nord, sud, est ed ovest (denotate rispettivamente dai caratteri ‘N’, ‘S’, ‘E’ ed ‘O’). 
In particolare, il robot accetta comandi che consistono in una direzione 
e un intero positivo, che rappresenta la distanza (in metri) da percorrere 
in quella direzione. 
I comandi sono registrati in un file, in cui ogni riga contiene un comando, 
e vengono eseguiti dal robot in sequenza.
Si guardi ad esempio il file di testo f5a.txt contenente le 5 righe.

N10
E5
S4
S9
O3

Si progetti la  funzione es3(ftesto) che riceve  come parametro il nome del file di testo 
contenente i comandi e restituisce  le coordinate in cui si trovera' il robot dopo 
l'esecuzione dei comandi sapendo che all'inizio e' posizionato nel punto di  
coordinate (0,0).
Le coordinate del robot sono rappresentate tramite una coppia in cui la prima 
coordinata rappresenta le ascisse mentre la seconda le ordinate.

Ad esempio se la funzione es3 viene chiamata per il file di comandi  f3a.txt,
eseguendo in sequenza i comandi presenti nel file le  posizioni occupate dal robot saranno:
N10   ---> (0,10)
E5    ---> (5,10)
S4    ---> (5,6)
S9    ---> (5,-3)
O3    ---> (2,-3)

es3(f3a.txt) restituisce la coppia (2,-3)
'''

def es3(ftesto):
    # inserisci qui il tuo codice
    pass



######################################################################################

import albero

'''
    Es 4: ? punti

    Si definisca la funzione es4(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata e 
    torna come risultato una lista.
    nella lista in ordine crescente devono comparire i livelli dell'albero in cui sono presenti
    nodi foglia. 
    
    Esempio:  la funzione es4
    - sull'albero a sinistra restituisce  [1,2,3] 
    - sull'albero a destra restituisce [2].

              5                                    5                    
      ________|_____________               ________|_                   
     |          |           |             |          |                  
     20         4           6             20         4                  
     |     _____|______                   |       ___|___               
     12   |   |  |  |  |                  12     |   |   |              
          10  2  9  8  7                         2   9   7              
            __|__                                                       
           |     |                                                      
           30    22                                                     
                                                                        
    '''

def es4(tree):
    # inserisci qui il tuo codice
    pass

############################################################################

import albero

'''
    Es 5: ? punti

    Si definisca la funzione es5(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata e 
    torna come risultato una lista.
    nella lista sono presenti, uno dopo l'altro, gli identificatori dei nodi che si incontrano 
    nel cammino dell'albero che va dal nodo con l'identificativo minimo alla radice. 
    
    Esempio:  la funzione es5
    - sull'albero a sinistra restituisce  [2,4,5] 
    - sull'albero a destra restituisce [1,20,5].

              5                                    5                    
      ________|_____________               ________|_                   
     |          |           |             |          |                  
     20         4           6             20         4                  
     |     _____|______                   |       ___|___               
     12   |   |  |  |  |                  1      |   |   |              
          10  2  9  8  7                         2   9   7              
            __|__                                                       
           |     |                                                      
           30    22                                                     
                                                                        
    '''

def es5(tree):
    # inserisci qui il tuo codice
    pass


###########################################################################

import immagini

'''    
    Es 6: ? punti
    
    Abbiamo immagini che contengono su sfondo nero cammini di color bianco 
    che non si intrecciano ne' si toccano e sono formati da segmenti orizzontali 
    o verticali consecutivi.
    Si veda ad Esempio l'immagine f6.png di dimensioni 100 x 100
    Progettare la  funzione es2(fimm, w1, h1) che prende come parametro 
    l'indirizzo di un file .PNG siffatto e le coordinate (w1,h1) di un suo pixel che 
    e' estremo di uno dei  cammini e restituisce un intero. L'intero restituito e'
    il numero di pixel di cui e' composto il cammino. 
    
    Ad esempio per il file f6.png e w1=20, h1=20  la funzione es6 restituisce 80
    
    Per caricare il file PNG si puo' usare la funzione load importabile dal file  immagini.
    '''

def es6(fimm, w1, h1):
    # inserisci qui il tuo codice
    pass


###########################################################################


'''
Es 7: punti ?.

Si progetti la funzione es7(stringa1,stringa2, k) che riceve come argomento due stringhe 
di caratteri tra 'a' e 'z' ed un intero positivo k e restituisce una lista contenente 
le sottostringhe lunghe k  comuni 
ad entrambe le stringhe. La lista in output non deve contenenre duplicati e  le sue stringhe 
devono risultare ordinate per numero crescente di vocali distinte e in caso di parita' 
di vocali vale  l'ordine lessicografico.


Ad esempio per 
stringa1='uoccazaodaaaoboccbnzbnznbz' 
stringa2='aaaobnzazaodnbzocc'

es7(stringa1, stringa2, 4) restituisce la lista 
['bnz', 'nbz', 'aaa', 'aza', 'occ', 'aao', 'aob', 'aod', 'zao']

'''

def es7(stringa1,stringa2,k):
    # inserisci qui il tuo codice
    pass

###########################################################################

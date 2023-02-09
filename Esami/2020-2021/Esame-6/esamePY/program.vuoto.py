################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #

'''Es1: 6 punti

   Progettare la funzione ex1 che prende in ingresso due liste di liste che
   rappresentano due matrici, chiamate pts e indexes.  La matrice pts
   è di dimensione Nx3, mentre indexes è una matrice di dimensione
   Mx3, con N diverso da M. La funzione ex1 restituisce
   una terza matrice di dimensione Mx3x3 costruita in questo modo:
   - per ogni riga di indexes è presente una riga nella matrice finale
   - ogni riga di indexes è usata per selezionare tre righe di pts
   - le tre righe selezionate in pts sono inserite come una nuova riga
     della matrice finale.

   Esempio, dati in ingresso

   pts    =  [ [1,2,3],    # 0
               [50,20,30], # 1
               [0,12,13],  # 2
               [3,1,0]     # 3
             ]

   indexes = [ [0,1,3],
               [0,0,0],
               [3,2,1],
             ]

   la deve funzione ex1(pts, indexes) deve ritornare:

   [
     [[1, 2, 3], [50, 20, 30], [3, 1, 0]], 
     [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
     [[3, 1, 0], [0, 12, 13], [50, 20, 30]]
   ]

'''

def ex1(pts, indexes):
    pass
    # insert your code here / inserisci qui le tue istruzioni

# ----------------------------------- EX.2 ----------------------------------- #

'''Es2: 8 punti

Vogliamo disegnare una successione di rettangoli colorati lungo la
diagonale secondaria (da basso-sinistra ad alto-destra) di una
immagine con sfondo nero.

Progettare la funzione ex2(rettangoli, larghezza, altezza, filepng)
che riceve come argomenti:

- rettangoli: una lista di (almeno 2) terne (L, A, colore), che indicano
    per ciascun rettangolo le dimensioni L (larghezza), A (altezza) ed
    il colore (diverso da nero) da usare (come terna RGB)

- larghezza e altezza: dimensioni della immagine da costruire

- filepng: il nome del file PNG in cui salvare l'immagine.

I rettangoli devono essere posizionati lungo la diagonale secondaria
in modo che i loro centri siano equispaziati sia in orizzontale sia in
verticale, ovvero:
- una volta sistemati il primo ed ultimo rettangolo rispettivamente
  sull'angolo inferiore sinistro ed sull'angolo superiore destro,

- si calcola la distanza in orizzontale e in verticale tra i centri
  dei rettangoli considerando la distanza fra il centro del primo e il
  centro dell'ultimo, già sistemati (NOTA: la distanza in verticale e
  quella in orizzontale possono essere diverse)

- nel calcolare la posizione degli altri rettangoli, si deve arrotondare
  il valore risultante all'intero più vicino con la funzione round.

Poiché può succedere che i rettangoli si sovrappongano, vanno
disegnati nell'ordine dato dalla lista.

La funzione deve tornare il numero di pixel neri dell'immagine ottenuta.

Si suggerisce di creare una funzione ausiliaria che disegni un
rettangolo di un certo colore e di certe dimensioni, conoscendone il
centro.

Si ricordi che (0,0) corrisponde al pixel in alto a sinistra, poiché le
coordinate delle immagini hanno la y che cresce dall'alto verso il basso.

Esempio: se l'immagine da creare è grande 500x400 e la lista di rettangoli è 
    [   (316, 260, (171, 155, 135)),     
        (304, 328, (77, 176, 176)),
        (172, 180, (193, 76, 56))]
Si deve costruire e salvare un'immagine uguale a "rectangles/example.png"
restituendo 42336 come numero di pixel neri.

Infatti:

- il primo rettangolo ha il suo centro nel punto (158, 270), ovvero
  0+316/2=158 in orizzontale e 400-260/2=270 in verticale
  e viene disegnato da (0,140) a (315,399)

- l'ultimo rettangolo ha il suo centro nel punto (414, 90), ovvero
  500-172/2=414 in orizzontale e 0+180/2=90 in verticale
  e viene disegnato da (328,0) a (499,179)

- poiché rimane da sistemare un solo rettangolo, le distanze fra i
  centri sono divise per due in orizzontale e in verticale, ottenendo
  (414-158)/2 = 256/2 = 128 e (270-90)/2 = 180/2 = 90,
  rispettivamente: queste sono le distanze (o/v) del centro del rettangolo di
  mezzo rispetto ai centri degli altri due rettangoli, per cui il
  centro del rettangolo di mezzo sarà (286,180), poiché 158+128 =
  414-128 = 286 in orizzontale e 270-90 = 90+90 = 180 in verticale.

- quindi, il rettangolo di mezzo è disegnato a partire dal suo centro
  (286,180), considerando la metà della larghezza (304/2=152) e
  dell'altezza (328/2=164) rispettivamente in orizzontale e in
  verticale, e viene disegnato da (134,16) a (437,343)

NOTA conclusiva:
Per via dell'arrotondamento potrebbe capitare che i rettangoli da disegnare
sbordino dall'immagine generando un IndexError che andrà gestito o evitato.
'''
import images
def ex2(rettangoli, larghezza, altezza, filepng):
    pass
    # insert your code here / inserisci qui le tue istruzioni

# ----------------------------------- EX.3 ----------------------------------- #

'''Es3: 9 punti

Si progetti una funzione ricorsiva o che fa uso di funzioni o metodi
ricorsivi che ricerca in una gerarchia di directory i file con certe
estensioni che contengono almeno una parola di una lista di parole. I
file contenuti nelle directory contengono parole separate da 1 o più
caratteri non alfabetici.

Si implementi in modo ricorsivo la funzione ex3(path, parole, estensioni)
che riceve come argomenti:
    - path: il percorso della directory da esplorare
    - parole: la lista di parole da cercare nei file
    - estensioni: lista di estensioni dei file cercati
La funzione ritorna un dizionario in cui:
    - le chiavi sono i path dei file trovati che contengono almeno una delle parole in parole
    - il valore di una data chiave è la PRIMA parola della lista parole
      incontrata all'interno del file della chiave.

NOTA: i file e le directory che iniziano per '.' devono essere ignorati
NOTA: è proibito usare la funzione os.walk o similari
NOTA: definite la funzione in modo ricorsivo al livello più esterno del modulo 
    in modo che il test di ricorsione funzioni
 
Esempio: se nella directory test/d1 c'è il file check.txt contenente la stringa
         'cielo-cane...casa!!! chiodo' l'invocazione della funzione
         ex3('test',['coniglio','casa','cane'],'txt')
         deve restituire il dizionario
         {'test/d1/check.txt':'casa'}
'''
import os

def ex3(path, parole, estensioni):
    pass
    # insert your code here / inserisci qui le tue istruzioni

# ----------------------------------- EX.4 ----------------------------------- #

'''Es4: 8 punti
   Si progetti la funzione ex4, ricorsiva o che fa uso di funzioni o
   metodi ricorsivi, che riceva in input una stringa (alfabeto) ed un
   numero intero (k) e generi ricorsivamente tutte le parole palindrome di
   lunghezza k, composte dai caratteri della stringa alfabeto.  La
   funzione restituisce il set con tutte le parole generate.

Esempio: ex4('abc', 4) restituisce il set
   {'aaaa', 'abba', 'baab', 'bbbb', 'acca', 'caac', 'cccc', 'bccb', 'cbbc'}

Esempio: ex4('abc', 3) restituisce il set
   {'aaa', 'aba', 'bab', 'bbb', 'aca', 'cac', 'ccc', 'bcb', 'cbc'}

'''
def ex4(alfabeto, k):
    pass
    # insert your code here / inserisci qui le tue istruzioni

################################################################################
if __name__ == '__main__':
    # Insert your own tests here
    pass

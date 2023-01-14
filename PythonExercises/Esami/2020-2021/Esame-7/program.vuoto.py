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
'''Es1: 7 punti

Si vuole calcolare la classifica finale di un campionato di calcio.
  L'input è contenuto in un file di testo nel quale sono presenti su righe
  separate le informazioni di ciaascuna partita con i seguenti campi,
  separati da spazi:
    - il nome della squadra che gioca "in casa"
    - il numero di goal da lei subiti
    - il nome della squadra "ospite"
    - il numero di goal da lei subiti
  La squadra vincente guadagna 3 punti. La squadra perdente riceve 0 punti.
  In caso di pareggio, ambedue le squadre guadagnano 1 punto.

  Si implementi la funzione ex1(file_partite, file_classifica) 
  che riceve come argomenti:
    - file_partite:    il nome del file .txt che contiene i dati delle partite
    - file_classifica: il nome del file .txt in cui scrivere la classifica
  e che restituisce il numero di squadre che hanno partecipato al torneo.

  Il file di output deve contenere la classifica finale:
    - ordinata in ordine decrescente di punti finali
        - in caso di parità vince chi ha fatto più goal in trasferta
        - in caso di ulteriore parità vince chi ha fatto più goal in casa
        - in caso di ulteriore parità vince chi ha subito meno goal in trasferta 
        - in caso di ulteriore parità vince chi ha subito meno goal in casa 
        - in caso di ulteriore parità si usi l'ordine alfabetico crescente dei
          nomi delle squadre
    - ogni riga contiene, separate da tab, i dati di una squadra:
        - nome della squadra
        - numero di punti totali
        - numero di goal fatti
        - numero di goal subiti
        - numero di goal fatti in trasferta
        - numero di goal subiti in trasferta
        - numero di goal fatti in casa
        - numero di goal subiti in casa

Esempio: se il file delle partite contiene le righe (a parte l'indentazione):
    uno 3 due 2
    due 2 uno 0
Vuol dire che le squadre sono solo due ('uno' e 'due') e che nelle due partite:
    uno vs due ha vinto due per 3 a 2 quindi uno prende 0 punti e due ne prende 3
    due vs uno ha vinto uno per 2 a 0 quindi uno prende 3 punti e due ne prende 0
La graduatoria finale da scrivere nel file è:
    due 3 3 4 3 2 0 2   (ha fatto più goal in trasferta)
    uno 3 4 3 2 0 2 3
e la funzione deve tornare il valore 2
'''

def ex1(file_partite, file_classifica):
    pass
    # Inserire qui il proprio codice


# ----------------------------------- EX.4 ----------------------------------- #

'''Es2: 8 punti

Data un'immagine in formato PNG vogliamo calcolare e disegnare l'istogramma 
  dei colori presenti nell'immagine.
  Progettare ed implementare la funzione ex2(input_file, output_file) 
  che riceva come argomenti:

    - input_file: il filename dell'immagine PNG da leggere
    - output_file: il filename dell'immagine in cui dovete salvare
      l'istogramma prodotto

  e restituisca come risultato:
      - il numero di colori diversi dell'immagine in input.

  L'immagine dell'istogramma da produrre deve avere queste caratteristiche:
    - lo sfondo è nero (0,0,0)
    - le barre sono:
        - orizzontali
        - allineate a sinistra lasciando uno spazio di 2 pixel dal
          bordo sinistro
        - separate dal bordo superiore, dalla barra precedente e dal
          bordo inferiore di 2 pixel
        - lunghe quanto il numero di pixel contati di quel colore
        - alte 3 pixel
        - dello stesso colore individuato nel file originale
        - e finiscono con almeno 2 pixel neri dal bordo destro
    - l'ordine dei colori deve essere per conteggio decrescente 
        e in caso di conteggio identico, per tupla di colore decrescente.

Esempio: se il file è 5-5-10.png l'istogramma da produrre contiene 9 barre
(vedi expected_histogram_5-5-10.png) e la funzione deve tornare il valore 9.

Per caricare e salvare le immagini PNG usate le funzioni load e save 
della libreria images.

'''

import images
def ex2(input_file, output_file):
    pass
    # Inserire qui il proprio codice


# ----------------------------------- EX.3 ----------------------------------- #

'''Es3: 9 punti

Progettare e implementare una funzione ex3(root), ricorsiva o che
  fa uso di funzioni/metodi ricorsivi, tale che:
    - riceva come argomenti un albero (root) di tipo tree.BinaryTree
    - restituisca in output una lista di interi.

La lista di interi da restituire deve essere costruita visitando
  l'albero in post-order e deve contenere soltanto i valori di quei
  nodi interni per i quali i figli sono uno multiplo dell'altro.

Si ricorda che la visita in post-order prevede che si visiti prima
  il figlio sinistro, poi il figlio destro e infine la radice.

  Es: dato l'albero root di seguito definito
                      6
                  /       \
               5             1
            /     \       /     \
           2       4     6       8
                  / \           / \
                15   3         2   10

  la funzione deve ritornare la lista [4,5,8,6]
'''

from tree import BinaryTree

def ex3(root):
    pass
    # Inserire qui il proprio codice


# ----------------------------------- EX.4 ----------------------------------- #

'''Es4: 8 punti

Si progetti ed implementi la funzione es4(n) ricorsiva (o che faccia uso di
  funzioni o metodi ricorsive/i) che riceva come parametro un numero
  intero n e restituisca tutti i numeri in base 3 codificabili su n
  posizioni, in ordine crescente.
    
  Nota: L'enumerazione deve avvenire * * * in maniera ricorsiva * * *.
    Non sono ammesse versioni iterative. 
    
La funzione deve restituire l'enumerazione dei numeri come una lista. Ogni
  elemento della lista contiene una tupla. La tupla contiene i seguenti tre
  elementi:
    1) una stringa che indica il numero in base 3;
    2) un intero che corrisponde alla conversione in base 10 della stringa in
       base 3 di cui al punto (1);
    3) il numero minimo di bit su cui è esprimibile il numero in base 2.
  
  Se l'argomento n è minore o uguale a zero la funzione deve restituire
  [('', None, None)] senza entrare in ricorsione.

  Nota: Si può usare la funzione int().
  
  Per facilità, mostriamo l'albero di ricorsione che può essere immaginato come
  segue per n=2, sebbene non sia necessario creare strutture addizionali per
  risolvere questo esercizio:
                                                     
            ______________|_______________              
           |              |              |             
           0              1              2            
        ___|___        ___|___        ___|___
       |   |   |      |   |   |      |   |   |                           
       0   1   2      0   1   2      0   1   2                      
 
Esempio: ex4(n=2) deve resituire:
  [('00', 0, 1),
   ('01', 1, 1),
   ('02', 2, 2),
   ('10', 3, 2),
   ('11', 4, 3),
   ('12', 5, 3),
   ('20', 6, 3),
   ('21', 7, 3),
   ('22', 8, 4)]

  (nell'esempio si può notare anche la mappatura fra sistema decimale e base 3).
'''

def ex4(n):
    pass
    # Inserire qui il proprio codice

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
  separate le informazioni di ciaascuna partita con i seguenti campi separati da spazi:
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
        - in caso di ulteriore parità si usi l'ordine alfabetico crescente dei nomi delle squadre
    - ogni riga contiene, separate da tab, i dati di una squadra:
        - nome della squadra
        - numero di punti totali
        - numero di goal fatti
        - numero di goal subiti
        - numero di goal fatti in trasferta
        - numero di goal subiti in trasferta
        - numero di goal fatti in casa
        - numero di goal subiti in casa
'''

def ex1(file_partite, file_classifica):
    classifica = {}
    with open(file_partite) as F:
        for line in F:
            incasa, presi, ospite, dati = line.split()
            presi = int(presi)
            dati  = int(dati)
            if presi == dati:
                puntiin, puntiout = 1, 1
            elif presi > dati:
                puntiin, puntiout = 0, 3
            else: 
                puntiin, puntiout = 3, 0
            if incasa not in classifica:
                classifica[incasa] = { 'punti':0, 'dati':0, 'presi':0, 'datiin':0, 'presiin': 0, 'datiout':0, 'presiout':0 }
            if ospite not in classifica:
                classifica[ospite] = { 'punti':0, 'dati':0, 'presi':0, 'datiin':0, 'presiin': 0, 'datiout':0, 'presiout':0 }
            classifica[incasa]['punti']    += puntiin
            classifica[incasa]['dati']     += dati
            classifica[incasa]['presi']    += presi
            classifica[incasa]['datiin']   += dati
            classifica[incasa]['presiin']  += presi
            classifica[ospite]['punti']    += puntiout
            classifica[ospite]['dati']     += presi
            classifica[ospite]['presi']    += dati
            classifica[ospite]['datiout']  += presi
            classifica[ospite]['presiout'] += dati
    with open(file_classifica, mode='w', encoding='utf8') as F:
        for k,v in sorted(classifica.items(), key=lambda kv: ( -kv[1]['punti'],     # classifica
                                                           -kv[1]['datiout'],   # goal in trasferta
                                                           -kv[1]['datiin'],    # goal in casa
                                                           -kv[1]['presiout'],  # subiti in trasferta
                                                           -kv[1]['presiin'],   # subiti in casa
                                                            kv[0])):            # nome squadra
            print(k, v['punti'], 
                     v['dati'], 
                     v['presi'], 
                     v['datiout'], 
                     v['presiout'], 
                     v['datiin'], 
                     v['presiin'], 
                     sep='\t',
                     file=F)
    return len(classifica)


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
    - l'ordine dei colori deve essere per conteggio decrescente 
        e in caso di conteggio identico, per tupla di colore decrescente.

'''

import images
def ex2(input_file, output_file):
    def draw_bin(img, x,y,w,h,c):
        for X in range(x, x+w):
            for Y in range(y, y+h):
                img[Y][X] = c
    black = (0,0,0)
    img = images.load(input_file)
    conteggio = {}
    for line in img:
        for color in line:
            if color in conteggio:
                conteggio[color] += 1
            else:
                   conteggio[color]  = 1
    maxW = max(conteggio.values(), default=0)
    maxH = len(conteggio)
    #print(maxW, maxH)
    istogramma = [ [ black ] * (maxW + 4) for _ in range(maxH*5 + 2) ]
    for i,(color, count) in enumerate(sorted(conteggio.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))):
        draw_bin(istogramma, 2, i*5+2, count, 3, color)
    #print( *(line[:5] for line in istogramma[:5]), sep='\n')
    images.save(istogramma, output_file)
    return maxH


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
    if not root.left and not root.right:
        return []
    l = []
    if root.left:
        l += ex3(root.left)
    if root.right:
        l += ex3(root.right)
    if root.left and root.right:
        if root.left.value % root.right.value == 0 or root.right.value % root.left.value == 0:
            l += [root.value]
    return l


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


def enum_tri(n, bits=''):
    alphabet = '012'
    if n <= 0:
        if not bits:
            return [('', None, None)]
        else:
            int_v = int(bits, base=len(alphabet))
            int_bits = int_v.bit_length()
            # to code 0 we still need a bit, right?
            if int_v == 0:
                int_bits += 1
            return [(bits, int_v, int_bits)]
    digits = []
    for c in alphabet:
        digits.extend(enum_tri(n-1, bits=bits+c))
    return  digits


def ex4(n):
    return enum_tri(n)

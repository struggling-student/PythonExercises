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
    Si scriva una funzione ex1(file_rows, file_cols, file_values) che
    prende in ingresso i percorsi di 3 file e restituisca in output
    una matrice, rappresentata come lista di liste.  Scopo
    dell'esercizio è ricostruire una matrice "out" codificata mediante
    tre matrici, "rows", "cols" e "values". A loro volta, le tre
    matrici sono codificate in tre file di testo i cui nomi sono dati
    in ingresso: file_rows, file_cols, file_values.

    I file contengono su diverse righe dei numeri interi separati da
    spazi: ogni riga del file è una riga della matrice, ovvero il
    c-esimo numero su una data riga corrisponde al c-esimo elemento
    (la colonna c) della riga corrispondente.  Ad esempio, se il file
    contiene:

    0    1
    1 0

    la matrice codificata come lista di liste è:

    [[0, 1],
    [1, 0]].

    La matrice "out" da restituire ha nella posizione (r,c) l'elemento
    della matrice "values" individuato dalla riga indicata dal valore
    nella posizione (r,c) della matrice "rows" e dalla colonna
    indicata dal valore nella posizione (r,c) della matrice
    "cols". Nel caso in cui gli indici ricavati da "rows" e "cols" non
    individuino un elemento valido nella matrice "vals" (esempio,
    indice negativo o indice fuori dal numero righe o degli elementi
    di una riga), la matrice "out" deve contenere None nella posizione
    corrispondente.

    Ad esempio: dati i tre file di ingresso che codificano le matrici
          "rows"              "cols"                     "vals"
     0         1        |   1              5    |     3     4      1
     0         1        |   0              2    |     10     -1    5

    si deve restituire:

      "out"
    [[4, None],
     [3, 5]]

    infatti:
    - alla posizione di "out" (1,1) vi è 5 che si trova in "vals" alla
      riga indicata da "rows" alla posizione (1,1) (ossia 1) e colonna
      indicata da "cols" alla posizione (1,1) (ossia 2).
    - alla posizione di "out" (0,1) vi è None perché vals non è
      accessibile con indice (1,5).

    Nota: "out", "rows" e "cols" hanno stesse dimensioni fra loro,
          mentre "vals" può avere dimensioni diverse.

'''

def get_mat(file_in):
    with open(file_in) as fr:
        A = fr.read().split('\n')
    return [ list(map(lambda x: int(x), x.split())) for x in A if x ]

def shape(A):
    return len(A), len(A[0])

def ex1(file_rows, file_cols, file_values):
    # reading mat
    rows = get_mat(file_rows)
    cols = get_mat(file_cols)
    vals = get_mat(file_values)
    R, C = shape(rows)
    R_v, C_v = shape(vals)
    # sanity check
    assert R == len(cols) and C == len(cols[0])
    # mat indexing
    return [ [ vals[rows[r][c]][cols[r][c]] if  rows[r][c] >= 0 and rows[r][c] < R_v and
                                                cols[r][c] >= 0 and cols[r][c] < C_v
                else None for c in range(C) ] for r in range(R) ]

# ----------------------------------- EX.2 ----------------------------------- #

'''Es2: 8 punti

   Data una immagine PNG con dei rettangoli di colore bianco su uno
   sfondo di colore nero, si vuole sommare tra loro i perimetri di
   tutti i rettangoli che hanno i lati orizzontali della stessa
   lunghezza, intesa come numero di pixel. I rettangoli non si
   incontrano né si toccano in nessun punto.

   Si progetti la funzione ex2(input_file) che prende in input un file
   con una immagine PNG come descritto sopra e resituisce un
   dizionario. Il dizionario ha:

   - per chiavi, le diverse lunghezze dei lati orizzontali dei
   rettangoli

   - per valori, le somme dei perimetri dei rettangoli che hanno il
   lato orizzontale della lunghezza pari alla chiave.

   Esempio: poiché l'immagine nel file ex2p1.png contiene due
      rettangoli con base 20 pixel e altezza 10 pixel e un rettangolo
      3x3, la funzione ex('ex2p1.png') deve restituire il dizionario:
      {20: 120, 3:12} '''

import images
def process_rect(im, i, j):
    white = tuple([255]*3)
    black = tuple([0]*3)
    pixel = j
    while pixel < len(im[i]) and im[i][pixel]==white:
        im[i][pixel]=black
        pixel+=1
    l = pixel-j
    row = i+1
    while row < len(im) and im[row][j]==white:
        im[row][j]=black
        im[row][pixel-1]=black
        row+=1
    im[row-1][j:pixel]=[black]*l
    h = row-i
    return l, 2*l+2*h



def ex2(input_file):
    im = images.load(input_file)
    dic = {}
    for i, row in enumerate(im):
        for j, pixel in enumerate(row):
            if im[i][j] == tuple([255]*3):
                base, perim = process_rect(im, i, j)
                if base in dic:
                    dic[base]+=perim
                else:
                    dic[base]=perim
    return dic


# ----------------------------------- EX.3 ----------------------------------- #

'''Es3: 9 punti
    Si progetti la funzione ex3 ricorsiva o che fa uso di funzioni o metodi ricorsivi
    che riceve come argomento una stringa di caratteri e torna le foglie dell'albero
    di gioco ottenuto applicando la seguente mossa:
    - eliminare dalla stringa una coppia di caratteri consecutivi diversi
        ma ignorando la differenza tra maiuscole e minuscole
    Le foglie sono le stringhe alle quali non è più possibile applicare la mossa.
    La funzione deve tornare la lista di foglie, senza ripetizioni ed in ordine decrescente
    di lunghezza, ed a parimerito in ordine alfabetico crescente.

Esempio: se la stringa è 'aBbACc' l'albero di gioco (indentato) sarà:

aBbACc
    bACc            # eliminati 'aB'
        Cc          # eliminati 'bA' (foglia)
        bc          # eliminati 'AC'
           ''       # eliminati 'bc' (foglia)
    aBCc            # eliminati 'bA'
        Cc          # eliminati 'aB' (foglia)
        ac          # eliminati 'BC'
           ''       # eliminati 'ac' (foglia)
    aBbc            # eliminati 'AC'
        bc          # eliminati 'aB'
           ''       # eliminati 'bc' (foglia)
        aB          # eliminati 'bc'
           ''       # eliminati 'aB' (foglia)

Quindi il risultato da tornare sarà la lista [ 'Cc', '' ]

'''

def ex3(stringa):
    pass
    # Inserire qui il proprio codice
    return sorted(trova_foglie(stringa), key=lambda x: (-len(x), x))

def trova_foglie(stringa):
    if stringa == '' or len(set(stringa.lower())) == 1:
        return { stringa }
    else:
        return { foglia
                for i in range(len(stringa)-1)
                if len(set(stringa[i:i+2].lower()))==2
                for foglia in trova_foglie(stringa[:i]+stringa[i+2:])
                }

# ----------------------------------- EX.4 ----------------------------------- #

'''Es4: 8 punti
    Si progetti la funzione ex4 ricorsiva o che fa uso di funzioni
    ricorsive, che prende come parametri di input il path di una
    directory 'dir1' e una stringa 'ext'. La funzione deve
    esplorare l'albero delle directory a partire dalla directory 'dir1'
    e ritornare un dizionario così fatto:

    - le chiavi sono stringhe, una per ogni sotto-directory di 'dir1'
      che contiene almeno un file il cui nome inizia con una lettera
      maiuscola e che ha estensione 'ext';

    - i valori sono liste di stringhe, una stringa per ogni file
      presente nella sotto-directory della chiave, il cui nome inizi
      con una lettera maiuscola e che termini con estenzione
      'ext'. Le liste sono ordinate per numero di caratteri
      componenti le stringhe e, in caso di parità, ordine alfabetico.

    Esempio: la funzione ex4('ex4/a0','.txt') deve tornare il dizionario
      {
       'ex4/a0': ['Roar.txt', 'Miaao.txt', 'Muuuu.txt'],
       'ex4/a0/b1': ['Bau.txt', 'Ciao.txt', 'Miao.txt']
      }

    Si suggerisce di usare la funzione os.listdir e le funzioni del
    modulo os.path. La funzione os.path.join potrebbe non funzionare
    in Windows, si suggerisce di usare la concatenazione con il
    carattere '/'.

    NOTA: è proibito usare la funzione os.walk 
'''
import os
def ex4(dir1, ext):
    d = {}
    for f in os.listdir(dir1):
        if os.path.isfile(dir1+'/'+f):
            if f.endswith(ext) and ord('A') <= ord(f[0]) <= ord('Z'):
                d[dir1] = d.get(dir1, []) + [f]
        elif os.path.isdir(dir1+'/'+f):
            d.update(ex4(dir1+'/'+f, ext))
    for k in d:
        d[k].sort(key=lambda x:(len(x),x))
    return d

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
'''
Es1: 6 punti
   Vengono dati in ingresso alla funzione ex1 due strutture dati contenenti
   matrici come liste di liste.  La prima struttura di nome pts
   contiene una matrice Nx3; il secondo input indexes anche è una
   matrice Mx3, con N diverso da M. La funzione deve restituire una matrice di dimensione
   Mx3x3 in questo modo.  Per ogni riga di indexes, vengono presi i
   suoi 3 valori che corrispondono agli indici da usare per accedere a "pts".
   Per i 3 accessi che vengono fatti verrà indicizzato 3 volte una lista 3D.
   Le tre liste di 3 valori sono inserite in una lista finale.

   Esempio:

   vector = [ [1,2,3],    # 0
              [50,20,30], # 1
              [0,12,13],  # 2
              [3,1,0]     # 3
            ]
   idx  = [  [0,1,3],
             [0,0,0],
             [3,2,1],
          ]

    deve rendere:

   [
     [[1, 2, 3], [50, 20, 30], [3, 1, 0]],
     [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
     [[3, 1, 0], [0, 12, 13], [50, 20, 30]]
   ]

'''

def ex1(pts, indexes):
    return [[pts[indice[0]], pts[indice[1]], pts[indice[2]]]
            for indice in indexes ]


# ----------------------------------- EX.2 ----------------------------------- #

'''Es2: 8 punti

Vogliamo disegnare una successione di rettangoli colorati lungo la diagonale secondaria
(da basso-sinistra ad alto-destra) di una immagine con sfondo nero.

Implementate la funzione ex2(rettangoli, larghezza, altezza, filepng) che riceve come
argomenti:
- rettangoli: una lista di terne (L,A,colore) che indicano per ciascun rettangolo
    le dimensioni L (larghezza), A (altezza) ed il colore da usare (come terna RGB)
- larghezza e altezza: dimensioni della immagine da costruire
- filepng: il nome del file PNG in cui salvare l'immagine

I rettangoli devono essere posizionati lungo la diagonale secondaria in modo che
i loro centri siano equispaziati sia in orizzontale che in verticale, ovvero:
- il primo ed ultimo rettangolo sono appoggiati rispettivamente all'angolo inferiore sinistro
    ed all'angolo superiore destro
- la distanza tra i centri dei rettangoli è la stessa in orizzontale sia in orizzontale
    che in verticale
    NOTA: la distanza in verticale e quella in orizzontale possono essere diverse
- nel calcolare la posizione dei rettangoli arrotondate il valore risultante all'intero più vicino

NOTA: può succedere che i rettangoli si sovrappongano, vanno disegnati nell'ordine dato dalla lista.

La funzione deve tornare il numero di pixel che appartengono a più di un rettangolo.

Potete assumere che la lista contienga sempre almeno 2 rettangoli.

Esempio: se l'immagine da creare è grande 500x400 e la lista di rettangoli è
    [   (316, 260, (171, 155, 135)),
        (304, 328, (77, 176, 176)),
        (172, 180, (193, 76, 56))]
Si deve costruire e salvare un'immagine uguale a "rectangles/example.png"
tornando il 54364 come numero di pixel che appartengono a più rettangoli.
Infatti i centri dei tre rettangoli si trovano alle coordinate:
    158, 270
    286, 180
    414, 90
con una distanza orizzontale di 286-158=414-286=128 e verticale di 270-180=180-90=90
'''
import images
def ex2(rettangoli, width, height, file_png):
    # costruisco l'immagine nera
    img   = [ [(0,0,0)]*width for _ in range(height) ]
    # calcolo la spaziatura orizzontale e verticale
    N = len(rettangoli)
    l0,a0,_ = rettangoli[0]     # dimensioni del primo
    l1,a1,_ = rettangoli[-1]    # e dell'ultimo
    spaziaturaH = (width  - l0/2 - l1/2) / (N-1)
    spaziaturaV = (height - a0/2 - a1/2) / (N-1)
    #print('dimensioni',width, height,'spaziature', spaziaturaH, spaziaturaV)
    for i,(l,a,c) in enumerate(rettangoli):
        X = round(l0/2 + i*spaziaturaH - l/2)
        Y = round(height - (a0/2 + i*spaziaturaV + a/2))
        disegna_rettangolo(img,X, Y, l, a, c)
    images.save(img,file_png)
    return sum([ c==(0,0,0) for riga in img for c in riga  ])

def disegna_rettangolo(img, X, Y, W, H, colore):
    #print('disegno', X, Y, W, H, colore)
    for x in range(X,X+W):
        for y in range(Y,Y+H):
            try:
                img[y][x]=colore
            except IndexError:
                #print(x,y)
                pass


# ----------------------------------- EX.3 ----------------------------------- #
'''
Es3: 9 punti

Si dovono cercare i file che contengono certe parole e che hanno date estensioni
in una gerarchia di directory.
I file contenuti nelle directory contengono parole separate da 1 o più caratteri non alfabetici.

Si implementi in modo ricorsivo la funzione ex3(path, parole, estensioni) che riceve come argomenti:
    - path: percorso della directory base da esplorare
    - parole: lista di parole da cercare nei file
    - estensioni: lista di estensioni dei file cercati
La funzione deve tornare un dizionario in cui:
    - le chiavi sono i path dei file trovati (a partire dalla directory base)
    - i valori sono le parole trovate

NOTA: i file e le directory che iniziano per '.' devono essere ignorati
NOTA: è proibito usare la funzione os.walk o similari
NOTA: definite la funzione in modo ricorsivo al livello più esterno del modulo
    in modo che il test di ricorsione funzioni
'''
import os

def ex3( dirname, searched, extensions ):
    dizio = {}  # dizionario da aggiornare nella chiamata ricorsiva
    ricerca(dirname, searched, extensions, dizio)
    return dizio

def ricerca(dirname, searched, extensions, dizio):
    # cerco i file contenuti in dirname ed aggiorno il dizionario dizio
    for name in os.listdir(dirname):
        if name[0] == '.': continue         # ignoro i file che iniziano per '.'
        fullname = f'{dirname}/{name}'      # costruisco il path completo del file/dir
        if os.path.isdir(fullname):         # se è una directory ci cerco dentro
            ricerca(fullname, searched, extensions, dizio)
        else:                               # altrimenti è un file
            for ext in extensions:          # se una delle estensioni cercate
                if name.endswith(ext):      # è la parte finale del filename
                    estratte = estrai_parole(fullname) # estraggo le parole dal file
                    for p in searched:      # cerco nell'ordine ne parole 
                        if p in estratte:   # alla prima che corrisponde
                            dizio[fullname] = p # aggiorno il dizionario
                            break           # e smetto di cercare

def estrai_parole(filename):
    # estraggo le parole dal file
    with open(filename) as F:
        testo = F.read()                    # ne leggo il contenuto
    for c in set(testo):                    # per tutti i caratteri del testo
        if not c.isalpha():                 # che non sono alfabetici
            testo = testo.replace(c, ' ')   # li sostituisco con spazi
    return testo.split()                    # quindi spezzo il testo in parole

# ----------------------------------- EX.4 ----------------------------------- #

'''Es4: 8 punti
   Si progetti funzione ex4 ricorsiva o che fa uso di funzioni o
   metodi ricorsivi che riceve in input una stringa alfabeto ed un
   numero k e genera ricorsivamente tutte le parole palindrome di
   lunghezza k, composte dai caratteri della stringa alfabeto.  La
   funzione restituisce il set con tutte le parole generate.

Esempio: ex4('abc', 4) restituisce il set
   {'aaaa', 'abba', 'baab', 'bbbb', 'acca', 'caac', 'cccc', 'bccb', 'cbbc'}

Esempio: ex4('abc', 3) restituisce il set
   {'aaa', 'aba', 'bab', 'bbb', 'aca', 'cac', 'ccc', 'bcb', 'cbc'}

'''

def ex4(alfabeto, N):
    if N==0:            # se N=0 torno stringa vuota per permettere le concatenazioni di N=2
        return {''}
    elif N==1:          # se N=1 le stringhe da 1 carattere sono proprio i caratteri dell'alfabeto
        return set(alfabeto)
    else:               # altrimenti aggiungo in cima e in fondo alle soluzioni N-2 ciascuno dei caratteri dell'alfabeto
        return { f'{c}{sol}{c}' for c in alfabeto for sol in ex4(alfabeto, N-2) }

################################################################################
if __name__ == '__main__':
    # Insert your own tests here
    pass
    print('abc', 0, ex4('abc',0))
    print('abc', 1, ex4('abc',1))
    print('abc', 2, ex4('abc',2))
    print('abc', 3, ex4('abc',3))

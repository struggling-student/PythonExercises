#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

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
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################

# ----------------------------------- EX.1 ----------------------------------- #

from math import sqrt
def ex1(points, K):
    pass
    # insert here your code
    """
    per ogni gruppo di K punti calcolo centro e raggio e prendo il minimo
    """
    cerchi = [ cerchio(points[i:i+K]) for i in range(len(points)-K+1) ]
    ordinati = sorted(cerchi, key=lambda centro_raggio: centro_raggio[1])
    assert ordinati[0][1] != ordinati[1][1], "il problema ha più di una soluzione"
    center,r2 = min(cerchi, key=lambda centro_raggio: centro_raggio[1])
    x, y = center
    return (round(x,3), round(y, 3)),round(sqrt(r2),3)

def cerchio(gruppo):
    centro = baricentro(gruppo)
    raggio = max( distanza2(centro, punto) for punto in gruppo )
    return centro,raggio

def baricentro(punti):
    X = Y = 0
    N = len(punti)
    for x,y in punti:
        X += x
        Y += y
    X /= N
    Y /= N
    return X,Y

def distanza2(punto1, punto2):
    x1,y1 = punto1
    x2,y2 = punto2
    return (x2-x1)**2 + (y2-y1)**2

# ----------------------------------- EX.2 ----------------------------------- #

"""
Es 2: 7 punti
Viene fornita un'immagine con sfondo nero al cui interno sono presenti
un numero variabile di croci, che possono avere colori sia diversi
sia uguali fra loro.  Ciascuna croce è composta da due linee, una
orizzontale e una verticale che si incontrano. Le linee hanno
spessore di 1 pixel e possono essere di lunghezza diversa.  Due croci
arbitrarie non possono sovrapporsi e c'è sempre almeno un pixel di sfondo
fra le due. Ciascun lato/braccio della croce è lungo almeno un pixel.

Consiglio: prima di iniziare vedere le immagini nella dir 'crosses/'

Si progetti e implementi la funzione ex2 che prende in ingresso
l'immagine suddetta e individua tutte le croci. Ogni croce deve essere
descritta come una tupla di 4 punti più la tupla del colore.
I 4 punti sono nell'ordine "alto", "basso", "sinistra", "destra", dove:
    - "alto" è il punto più in alto,
    - "basso" è il punto più in basso,
    - "sinistra" è il punto più a sinistra,
    - "destra" è il punto più a destra.
Ogni punto è una tupla di coordinate y, x, dove y è la riga e x la colonna.

Ad esempio, la croce seguente:

     0 1 2 3 4
   0 . . . . .
   1 . . x . .
   2 . x x x x
   3 . . x . .
   4 . . x . .
   5 . . . . .

                    alto   basso   sx     dx       colore
è descritta da:  ((1, 2), (4,2), (2,1), (2, 4), (r, g, b))

La funzione deve ritornare tutte le croci individuate come un dizionario
che ha:
- come chiavi i colori delle croci
- come valore un insieme con tutte le croci del colore indicato
  dalla chiave.
"""

import images
def ex2(path_to_im):
    pass
    # inserisci qui il tuo codice
    img = images.load(path_to_im)
    W,H = len(img[0]), len(img)
    croci = {}
    for x in range(1,W-1):
        for y in range(1, H-1):
            if iscross(img, x, y):
                #print('found cross at', x, y)
                c = img[y][x]
                for xl in range(x,-1,-1):
                    if not img[y][xl] == c:
                        xl = xl+1
                        break
                else:
                    xl = 0
                for xr in range(x,W):
                    if not img[y][xr] == c:
                        xr = xr-1
                        break
                else:
                    xr = W-1
                for yt in range(y,-1,-1):
                    if not img[yt][x] == c:
                        yt = yt+1
                        break
                else:
                    yt = 0
                for yb in range(y,H):
                    if not img[yb][x] == c:
                        yb = yb-1
                        break
                else:
                    yb = H-1
                croci[c] = croci.get(c,set()) | { ( (yt,x), (yb,x), (y,xl), (y,xr) )  }
    return croci

def iscross(img, x, y):
    return (0,0,0) != img[y][x] == img[y-1][x] == img[y+1][x] == img[y][x-1] == img[y][x+1]

# ----------------------------------- EX.3 ----------------------------------- #

def ex3(S):
    # INSERISCI IL TUO CODICE QUI
    pass
    res = genera_foglie(S)
    return list(map(int,sorted(res,key=lambda d: (len(d),-int(d)))))

def genera_foglie(S):
    if len(S) < 3:
        return { S }
    mosse = [ i for i in range(len(S)-2) if not set(S[i:i+3])-{'1','0'} ]
    if mosse:
        return { f for m in mosse for f in genera_foglie(applica_mossa(S,m)) }
    else:
        return { S }

def applica_mossa(S,i):
    prima,tripla,dopo = S[:i],S[i:i+3],S[i+3:]
    num = str(int(tripla,base=2))
    ris = prima+num+dopo
    return ris


# %% ----------------------------------- EX.4 ----------------------------------- #

"""
Es 4: 6+3 punti
    Sia data una lista di parole da cercare ed il path di una directory in cui cercare.
    Vogliamo trovare il file di testo (.txt) che contiene le parole indicate con
    una distribuzione delle frequenze "più variabile" (ovvero con varianza massima).

    Associamo ad un vettore di interi (in questo caso le frequenze delle parole nel file)
    la sua "varianza" ovvero la somma dei quadrati delle differenze dalla media.
        varianza(vettore) = somma(  (f-f_medio)^2 ) per tutti gli f del vettore

    Definite la funzione exB(dirpath, parole) che cerca ricorsivamente,
    o usando funzioni ricorsive, il file in cui la frequenza delle occorrenze
    delle parole cercate (ignorando la differenza tra maiuscole e minuscole)
    ha varianza massima.
    NOTA: nell'analizzare un file di testo considerate come separatori tutti i caratteri non
    alfabetici.

    La funzione deve tornare una coppia contenente:
    - come primo elemento un dizionario che ha come chiavi le parole cercate e come
      valori il numero di occorrenze di ciascuna parola nel file trovato (6 punti)
    - come secondo elemento la varianza calcolata, arrotondata alla 3° cifra decimale (3 punti)

Esempio:
    se dirpath = 'A' e parole = ['commodo', 'nisl', 'libero', 'in', 'gravida', 'lacus']
La funzione deve tornare il dizionario
    {'commodo': 13, 'nisl': 10, 'libero': 5, 'in': 37, 'gravida': 6, 'lacus': 14}
    che corrisponde al file 'A/C/Q/Z/Lorem.txt'
    e che ha la massima varianza (690.833) rispetto agli altri file '.txt'
"""

def varianza(vettore):
    assert len(vettore)
    media = sum(vettore) / len(vettore)
    return sum((x - media) ** 2 for x in vettore)/len(vettore)


def leggiparole(filename):
    with open(filename, encoding='utf8') as F:
        text = F.read().lower()
    chars = set(text)
    non_alpha = filter(lambda c: not c.isalpha(), chars)
    for c in non_alpha:
        text = text.replace(c, ' ')
    return text.split()

import os
def ex4(dirpath, parole):
    pass
    # inserisci qui il tuo codice
    d, v = _exB(dirpath, parole)
    return d, round(v, 3)


def _exB(dirpath, parole):
    best = {p: 0 for p in parole}
    total = 0
    for nome in os.listdir(dirpath):
        fullname = dirpath + '/' + nome
        if os.path.isdir(fullname):
            best2, tot2 = _exB(fullname, parole)
            if tot2 > total:
                total = tot2
                best = best2
        else:
            if nome.endswith('.txt'):
                words = leggiparole(fullname)
                quante = {p: words.count(p) for p in parole}
                tot2 = varianza(quante.values())
                if tot2 > total:
                    total = tot2
                    best = quante
                    #print(total, fullname, best)
    return best, total

###################################################################################

if  __name__ == '__main__':
    # inserisci qui i tuoi test
    # prendiamo una parabola, il raggio minimo l'abbiamo all'inizio
    if False:
        punti = [ (x,x**2+2) for x in range(-1, 15, 2)  ]
        print(punti)
        print(exA(punti, 4))

    if False:
        # parole = "commodo nisl libero in gravida lacus".split()
        # parole = "SCELERISQUE A LACUS AT HENDRERIT SEMPER ERAT".lower().split()
        parole = "lemonade orange pear apple cider watermelon".split()
        print(exB('A', parole))
    import random
    if False:
        N  = 15
        M  = 50
        Xs = sorted(random.choices(range(-M,M), k=N))
        Ys = random.choices(range(-M,M), k=N)
        punti = list(zip(Xs, Ys))
        print(f"{punti}")
        print(exA(punti, 5))





#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - !!!riempire le informazioni personali nelle variabili qui sotto!!!
    - AND risolvere almeno 1 esercizio di tipo ex (problema ricorsivo)
    - AND risolvere almeno 3 esercizi di tipo func
    - AND ottenere un punteggio maggiore o uguale a 18

Il punteggio finale è la somma dei punteggi dei problemi risolti.
"""
nome       = "Andrea"
cognome    = "Sterbini"
matricola  = "42"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 2 punti
Si definisca la funzione func1(diz1, diz2) che riceve come argomenti
due dizionari che hanno chiavi intere e valori liste di stringhe.  La
funzione deve tornare il dizionario che contiene le sole chiavi in
comune ad entrambi i dizionari.  I valori associati a ciascuna chiave
sono quelli che appaiono in una sola delle due liste associate a
quella chiave nei due dizionari.  Questi valori, senza ripetizioni,
vanno ordinati in ordine di lunghezza decrescente ed in caso di parità
in ordine alfabetico crescente.

Esempio:
diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
il risultato sarà  { 1: ['bc', 'cd', 'f'], 3: ['qrt', 'bn', 'st', 'c'] }
'''

def func1(diz1, diz2):
    pass
    def criterio(s):  return -len(s), s
    return {
        k : sorted(set(v1).symmetric_difference(set(diz2[k])), key=criterio)
        for k,v1 in diz1.items()
        if k in diz2
    }

#diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
#diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
#print(func1(diz1,diz2))

# ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 punti

Si definisca la funzione func2(text) che riceve come argomento:
- text: una stringa formata da parole separate da spazi
e che ritorna un dizionario che ha:
  - come chiavi la lettera iniziale delle parole presenti, minuscola
  - come valore il numero di parole che contengono quella lettera
    ignorando la differenza tra minuscole e maiuscole

Esempio:
text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
expected   = { 's':2, 'l':4, 'p':6, 'c':6}
'''

def func2(text):
    pass
    lower = text.lower().split()
    diz = { parola[0]: 0 for parola in lower }
    for parola in lower:
        for carattere in diz:
            if carattere in parola:
                diz[carattere] += 1
    return diz

#text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
#print(func2(text))

# ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 punti
Definite la funzione func3(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

Il file indicato da textfile_in contiene dei numeri
float oppure interi, positivi o negativi, separati da spazi.

La funzione deve leggere i numeri, ordinarli in ordine decrescente di
di caratteri numerici presenti e in caso di parità in ordine crescente di valore.
Quindi deve scrivere questi numeri ordinati nel file textfile_out,
separati da virgola e spazio. Infine la funzione restituisce la
quantità di numeri letti da textfile_in.

Esempio:
se il file textfile_in contiene la riga
-23.5 17 -141 +322.7 -3227
Nel file textfile_out la funzione deve scrivere la riga
-3227, +322.7, -141, -23.5, 17
e tornare il valore 5
'''

def func3(textfile_in, textfile_out):
    pass
    def criterio(elemento):
        cifre = elemento.replace('.','')
        cifre = cifre.replace('-', '')
        cifre = cifre.replace('+', '')
        return -len(cifre), float(elemento)
    with open(textfile_in) as FIN:
        numeri = FIN.read().split()
    numeri.sort(key = criterio)
    with open(textfile_out, mode='w') as FOUT:
        print(*numeri, sep=', ', file=FOUT)
    return len(numeri)


# ---------------------------- FUNC 4 ---------------------------- #

'''
Func 4: 4 punti
Si definisca la funzione func5(filein) che riceve come argomento
- filein: un file di testo contenente una matrice di interi NxM
  separati da spazi

e che ritorna la matrice trasposta rispetto alla diagonale secondaria,
ovvero quella che va dall'elemento in alto a destra a quello in basso
a sinistra. La matrice da restituire e' rappresentata come lista di liste.

Esempio:
se il file filein contiene la matrice
1 2 3 4
5 6 7 8
9 10 11 12
la funzione dovrà tornare la matrice riflessa rispetto alla diagonale 4-9,
come lista di liste
[[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
'''
def func4(input_filename):
    pass
    with open(input_filename) as FIN:
        M = [ list(map(int, riga.split())) for riga in FIN ]
    W = len(M[0])
    H = len(M)
    return [ [  M[H-1-y][W-1-x]
                for y in range(H)]
                for x in range(W)]

# ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 8 punti
Si definisca la funzione func5(txt_input, width, height, png_output) che riceve come argomenti
- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file.

Il file txt_file contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura
Possono essre presenti 2 tipi di figura:
- diagonale discendente di un quadrato (in direzione -45°)
    diagonalDOWN R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in BASSO a destra, ed è lunga L pixel
- diagonale ascendente di un quadrato (in direzione +45°)
    diagonalUP R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in ALTO a destra, ed è lunga L pixel

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di diagonali disegnate dei due tipi
come tupla dei due valori (DIAGUP,DIAGDOWN)

NOTA: va gestito correttamente lo sbordare delle figure dalla
immagine, infatti sono ammesse anche coordinate negative, e dimensioni
o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func5/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

l'esecuzione della funzione func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
produrrà una figura uguale al file 'func5/expected_1.png'
e tornerà la coppia (2, 1)
'''


import images
def func5(txt_input, width, height, png_output):
    pass
    def draw_diagonalDown(img, W, H, x, y, L, color):
        for i in range(L):
            X,Y = x+i, y+i
            if 0 <= X < W and 0 <= Y < H:
                img[Y][X] = color
    def draw_diagonalUp(img, W, H, x, y, L, color):
        for i in range(L):
            X,Y = x+i, y-i
            if 0 <= X < W and 0 <= Y < H:
                img[Y][X] = color
    img = [ [(0,0,0)]*width for _ in range(height) ] # immagine vuota, nera
    diagUP = diagDOWN = 0
    with open(txt_input) as F:
        for line in F:
            tipo, *data= line.split()
            R, G, B, x, y, L = list(map(int, data))
            if tipo == 'diagonalDOWN':
                draw_diagonalDown(img, width, height, x, y, L, (R, G, B))
                diagDOWN += 1
            elif tipo == 'diagonalUP':
                draw_diagonalUp(  img, width, height, x, y, L, (R, G, B))
                diagUP += 1
    images.save(img, png_output)
    return diagUP, diagDOWN

# print(func5('func5/in_1.txt', 50, 100, 'func5/out_1.png'))


# ---------------------------- EX 1 ---------------------------- #

'''
Esercizio 1 ricorsivo (6 punti):

Si definisca la funzione es1(root, valori), ricorsiva o che usa funzioni ricorsive,
che riceve in input:
- la radice 'root' di un albero n-ario definito da nodi nary_tree.NaryTree
- una lista di interi 'valori'
che modifica distruttivamente l'albero 'root' sommando a tutti i nodi
che sono a profondità P il valore che nella lista 'valori' si trova
all'indice P, se esiste, altrimenti restano come sono. Si assuma che
la radice si trovi a profondità 0.

La funzione deve restituire la somma 'total' di tutti i nodi
dell'albero risultante.

Esempio:
    values: [-42, -80, 68, 2, 81, 75, 54, 48, -4, 5]        da sommare
    root:                        -7                         | -42
                    /      |      |      |    \             |
                  -10      -3     -8    -10    -5           | -80
                /   \      |       |     |                  |
               6    -2     9       7     -9                 | +68

    expected:                    -49                         |
                    /      |       |      |     \            |
                  -90     -83     -88    -90    -85          |
                /   \      |       |      |                  |
               74    66   77       75     59                 |
    total = -134

ATTENZIONE: definite la funzione ricorsiva a livello esterno,
ovvero con la parola chiave 'def' appoggiata all'inizio della riga.
'''

from nary_tree import NaryTree

def ex1(root : NaryTree, valori : list[int]):
    pass
    return _ex1(root, valori, 0)

def _ex1(root : NaryTree, valori : list[int], depth : int):
    if depth < len(valori):
        root.value += valori[depth]
    total = root.value
    for son in root.sons:
        total += _ex1(son, valori, depth + 1)
    return total

# ---------------------------- EX 2 ---------------------------- #

'''
Ex2: 3 + 3 points
Definite la funzione ex2(dirin, words), ricorsiva o che usa funzioni o metodi ricorsivi,
che riceve come argomenti:
  - dirin: il path di una directory
  - words: una lista di parole

La funzione esplora dirin e tutte le sue sottodirectory (a tutti i
livelli) e conta il numero di occorrenze delle words nei file di testo
(quelli che hanno '.txt' come estensione) a tutti i livelli.  Una
parola appare in un file se è separata dalla precedente o dalla
seguente da almeno uno spazio, tab, o newline.

(3 points)
La funzione torna una lista di coppie (word, occorrenze) in cui il
primo elemento è la word ed il secondo è il numero di occorrenze
trovate.  Se una word non appare in alcun file il suo numero di
occorrenze è 0.

(+ 3 points)
Ordinate la lista di coppie in ordine decrescente di numero di
occorrenze ed in caso di parità in ordine alfabetico crescente.

NOTA 1: potete usare le funzioni: os.listdir, os.path.join,
os.path.isfile, os.mkdir, os.path.exists ...
NOTA 2: è proibito usare la funzione os.walk
NOTA 3: usate il carattere '/' come separatore dei path
(che funzione sia in Windows che su MacOS o Linux)

Esempio:
se il path dirin è "ex2" e le words = ["cat", "dog"]
la funzione ritorna: [('dog', 10), ('cat', 5)]
'''

import os
def ex2(dirin, words):
    pass
    diz = {w:0 for w in words}
    _ex2(dirin,diz)
    def criterio(pair):
        word,count = pair
        return -count, word
    return sorted(diz.items(), key=criterio)

def _ex2(dirin, diz):
    for name in os.listdir(dirin):
        fullname = dirin + '/' + name
        if os.path.isdir(fullname):
            _ex2(fullname, diz)
        else:
            if name.endswith('.txt'):
                with open(fullname, encoding='utf8') as FIN:
                    parole = FIN.read().split()
                for w in diz:
                    diz[w] += parole.count(w)


######################################################################################

if __name__ == '__main__':
    pass
    from random import randint, choice
    def creadiagonale(maxxy):
        UD = choice(['diagonalUP', 'diagonalDOWN'])
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
        x = randint(-50, maxxy)
        y = randint(-50, maxxy)
        L = randint(100, maxxy)
        return UD, R, G, B, x, y, L
    ID = 4
    N = 55
    FN = f'func5/in_{ID}.txt'
    with open(FN, mode='w') as F:
        for _ in range(N):
           print(*creadiagonale(500), sep=' ', file=F)



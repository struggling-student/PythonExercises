



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
name       = 'NAME'
surname    = 'AA'
student_id = 'STUDENT_ID'    # your Sapienza registration number

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
    diz3 = {}
    for k in diz1.keys():
        if k in diz2:
            diz3[k] = [v for v in diz1[k] if v not in diz2[k]] + [v for v in diz2[k] if v not in diz1[k]]
            diz3[k].sort(key=lambda x: (-len(x), x))
    return diz3

#diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
#diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
#print(func1(diz1,diz2))

#%% ---------------------------- FUNC 2 ---------------------------- #

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
    diz = {}
    words = text.lower().split()
    for w in words:
        c = w[0]
        if c not in diz:
            diz[c] = sum(c in w for w in words)
    return diz

text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
print(func2(text))

#%% ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 punti
Definite la funzione func3(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

I file indicato da textfile_in contiene dei numeri
float oppure interi, positivi o negativi, separati da spazi.

La funzione deve leggere i numeri, ordinarli in ordine decrescente di
numero di cifre significative, e in caso di parità in ordine crescente
di valore. Le cifre significative sono quelle che restano ignorando
punto e segno.

Quindi deve scrivere questi numeri ordinati nel file textfile_out,
separati da virgola e spazio Infine la funzione restituisce la
quantita' dei numeri letti da textfile_in.

Esempio:
se il file textfile_in contiene la riga
-23.5 17 -141 +322.7 -3227
Nel file textfile_out la funzione deve scrivere la riga
-3227, +322.7, -141, -23.5, 17
e tornare il valore 5
'''

def func3(textfile_in, textfile_out):
    def sort_func(x):
        n = x.strip('-+')
        l = len(n)
        if '.' in n:
            # l = n.index('.')
            l -=1
        return -l, float(x)

    with open(textfile_in) as f:
        numbers = f.read().split()
    numbers.sort(key = sort_func)
    with open(textfile_out, 'w', encoding='utf8') as f:
        print(', '.join(numbers), file = f)
    return len(numbers)

print(func3('func3/in_1.txt', 'func3/out_1.txt'))
#%% ---------------------------- FUNC 4 ---------------------------- #

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
la funzione dovrà tornare la matrice riflessa rispetto alla diagonale 4-9, come lista di liste
[[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
'''
def func4(input_filename):

    with open(input_filename) as f:
        lines = f.readlines()
    M = [[] for _ in range(len(lines[0].split()))]
    for line in lines:
        for i, v in enumerate(line.split()[::-1]):
            M[i].insert(0, int(v))
    return M

print(func4('func4/in_1.txt'))
#%% ---------------------------- FUNC 5 ---------------------------- #

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

NOTA: va gestito correttamente lo sbordare delle figure dalla immagine,
infatti sono ammesse anche coordinate negative,
e dimensioni o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func5/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

l'esecuzione della funzione func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
produrrà una figura uguale al file 'func5/expected_1.png'
e tornerà la coppia (2, 1)
'''

import images
def draw(im, diag, color, x, y, L, res):
    i = 1
    if 'UP' in diag:
        i=-1
        res[0]+=1
    else:
        res[1]+=1
    for l in range(L):
        if 0<=x+l<len(im[0]) and 0 <= y+l*i < len(im):
            im[y+l*i][x+l] = color


def func5(txt_input, width, height, png_output):
    im = [[(0,0,0)]*width for _ in range(height)]
    res = [0, 0]
    with open(txt_input) as f:
        figures = f.readlines()
    for fig in figures:
        fig = fig.split()
        r, g, b, x, y, L = map(int, fig[1:])
        # print(fig[0], r,g, b, x, y, L)
        draw(im, fig[0], (r,g,b), x, y, L, res)
    images.save(im, png_output)
    return tuple(res)

print(func5('func5/in_1.txt', 50, 100, 'func5/out_1.png'))


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

def ex1(root : NaryTree, valori : list[int], P=0):
    root.value += valori[P] if len(valori)>P else 0
    tot = root.value
    if len(root.sons) > 0:
        for son in root.sons:
            tot += ex1(son, valori, P+1)
    return tot



#%% ---------------------------- EX 2 ---------------------------- #

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
la funzione ritorna: [('dog', 11), ('cat', 6)]
'''

import os


def ex2(dirin, words):
    diz = ex2_(dirin, words)
    return sorted(diz.items(), key = lambda t: (-t[1], t[0]))

def ex2_(dirin, words):
    def process(file, words):
        with open(file) as f:
            text = f.read().split()
        return {w: text.count(w) for w in words}

    ret = {}
    for f in os.listdir(dirin):
        partial = {}
        f = dirin + '/' + f
        if os.path.isfile(f) and f.endswith('.txt'):
            partial = process(f, words)
        elif os.path.isdir(f):
            partial = ex2_(f, words)
        for w, c in partial.items():
            ret[w] = ret.get(w, 0) + c
    return ret

print(ex2('ex2/A', ['fish', 'cat', 'gnu']))


#%%#####################################################################################

if __name__ == '__main__':
    pass


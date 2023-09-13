



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
nome       = "nome"
cognome    = "cognome"
matricola  = "matricola"

name       = 'name'
surname    = 'surname'
student_id = 'student_id'    # your Sapienza registration number

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
Si definisca la funzione func1(diz1, diz2) che riceve come argomenti due dizionari che hanno
chiavi intere e valori liste di stringhe.
La funzione deve tornare il dizionario che contiene le sole chiavi in comune ad entrambi i dizionari.
I valori associati a ciascuna chiave sono quelli che appaiono in una sola delle due liste
associate a quella chiave nei due dizionari.
Questi valori, senza ripetizioni, vanno ordinati in ordine di lunghezza decrescente 
ed in caso di parità in ordine alfabetico crescente.

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
  - come valore il numero di parole che contengono quella lettera ignorando la differenza tra minuscole e maiuscole

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

I file indicato da textfile_in contiene dei numeri 
float oppure interi, positivi o negativi, separati da spazi.

La funzione deve leggere i numeri, ordinarli in ordine decrescente di numero di cifre significative, 
e in caso di parità in ordine crescente di valore.
(le cifre significative sono quelle che restano ignorando punto e segno)

Quindi deve scrivere questi numeri ordinati nel file textfile_out, separati da virgola e spazio
Infine la funzione restituisce la quantita' dei numeri letti da textfile_in.

Esempio:
se il file textfile_in contiene la riga
-23.5 17 -141 +322.7 -3227
Nel file textfile_out la funzione deve scrivere la riga
-3227, +322.7, -141, -23.5, 17
e tornare il valore 5
'''

def func3(textfile_in, textfile_out):
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
- filein: un file di testo contenente una matrice di interi NxM separati da spazi

e che ritorna la matrice trasposta rispetto alla diagonale secondaria 
(ovvero quella che va dall'elemento in alto a destra a quello in basso a sinistra)
rappresentata come lista di liste.

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

La funzione deve creare una immagine a sfondo nero e disegnarci sopra tutte le figure
indicate nel file 'txt_input', nell'ordine in cui appaiono nel file.

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

from math import dist
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
che riceve in input 
- la radice 'root' di un albero n-ario definito da nodi nary_tree.NaryTree
- una lista di interi 'valori' 
che modifica distruttivamente l'albero 'root' sommando a tutti i nodi che sono a profondità P 
(assumendo che la radice si trovi a profondità 0) il valore che nella lista 'valori'
si trova all'indice P (se esiste, altrimenti restano come sono).

La funzione deve restituire la somma 'total' di tutti i nodi dell'albero risultante.

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
    return _ex1(root, valori, 0)

def _ex1(root : NaryTree, valori : list[int], depth : int):
    if depth < len(valori):
        root.value += valori[depth]
    total = root.value
    for son in root.sons:
        total += _ex1(son, valori, depth + 1)
    return total


# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 4 + 2 points
    Implement the ex2(dirin, words) function, recursive or using recursive
    functions or methods, having the argument:
    - dirin: the path of an existing directory
    - words: a list of words
    The function will go through dirin and all its subfolders (at any level),
    and count the occurrences of the words in the input list in all the
    text files (i.e., files having the .txt extension) found in any folder.
    A word occurs in a file, if and only if it is separated from the preceding
    or following word, if there are, by a space, a tab, or a newline character.

    (5 points) The function returns a list of pairs (word, occ), in which the first
    value of each pair is one of the words in the input list and the second
    value of the pair is the number of occurrences of that word in the text files.
    (+ 3 points) The list is sorted on the number of occurrences of the words
    (in descending order); if two or more words have the same number of occurrences,
    they are sorted alphabetically (in ascending order).
    If a word in the input list never occurs, it still has to be returned
    by the function.

    NOTICE 1: you could find useful the functions: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTICE 2: it is forbidden to use the os.walk function

    For example, given the folder "ex2" and if words = ["cat", "dog"]
    the function returns: [('dog', 11), ('cat', 6)]

'''

import os


def RecScan(dir, words):
    D = {}
    items = os.listdir(dir)
    for item in items:
        if os.path.isfile(dir + "/" + item):
            if item[-4:].lower() == ".txt":
                fileRef = open(dir + "/" + item, "r", encoding="utf-8")
                for line in fileRef:
                    tokens = line.strip().replace("\t", " ").split(" ")
                    for token in tokens:
                        if token in words:
                            if token not in D:
                                D[token] = 1
                            else:
                                D[token] += 1
                fileRef.close()
        else:
            resD = RecScan(dir + "/" + item, words)
            for k in resD:
                if k not in D:
                    D[k] = resD[k]
                else:
                    D[k] += resD[k]
    return D


def ex2(dirin, words):
    D = RecScan(dirin, words)
    result = []
    for k in D:
        result.append((k, D[k]))
    return sorted(result, key=lambda x: x[1], reverse=True)

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



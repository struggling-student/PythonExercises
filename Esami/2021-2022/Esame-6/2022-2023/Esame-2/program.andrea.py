#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
 3) Cambiare la directory examPY con il tuo numero di matricola

Per superare l'esame e' necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.
"""
name       = "NOME"
surname    = "COGNOME"
student_id = "MATRICOLA"

#########################################

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


# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 points
Si definisca la funzione func1(string_list1, string_list2) che prende in
ingresso due liste di stringhe e ritorna una nuova lista di stringhe
contenente le stringhe presenti soltanto in una delle due liste prese in
ingresso. La lista va ordinata in ordine alfabetico inverso.
'''
def func1(string_list1, string_list2):
    # Inserisci qui il tuo codice
    risultato  = [ x for x in string_list1 if x not in string_list2 ]
    risultato += [ x for x in string_list2 if x not in string_list1 ]
    return sorted(risultato, reverse=True)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Si definisca una funzione funct2(path_to_file) che prende in ingresso
una stringa che rappresenta il percorso ad un file testuale. La funzione
deve ritornare il dizionario delle frequenze di tutti i caratteri presenti
nel file di testo.
Esempio:
Contenuto di func2_test_1.txt
 cat rat fat
 art
La funzione func2('func2_test_1.txt') ritorna {'c':1, 'a':4, 't':4, 'r':2, 'f':1, ' ':2, '\n':1}
'''
def func2(pathname):
    # Inserisci qui il tuo codice
    with open(pathname, encoding='utf-8') as f:
        text = f.read()
        return { c: text.count(c) for c in text }

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Si definisca una funzione func3(a_list) che prende in ingresso una lista di
numeri e rimuove dalla lista tutti gli elementi uguali al massimo e al minimo.
La funzione ritorna la differenza fra la lunghezza iniziale e la lunghezza
finale della lista.
Esempio:
    se a_list = [3, 12, -3, 4, 6, 12] dopo la chiamata a func3(a_list)
    a_list = [3, 4, 6]
'''

def func3(a_list):
    # Inserisci qui il tuo codice
    m = min(a_list)
    M = max(a_list)
    N = len(a_list)
    a_list[:] = [ x for x in a_list if x != m and x != M ]
    return N - len(a_list)

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca una funzione func4(input_filename, output_filename) che prende in
ingresso due stringhe che rappresentano due nomi di file.
Il file input_filename contiene una serie di stringhe separate da spazi,
tabulazioni o a capo.
La funzione deve creare un nuovo file di testo con nome output_filename.
Il file in output deve contenere tutte le stringhe trovate presenti in
input_filename, ripetute una sola volta ed organizzate per righe.
Le righe sono in ordine alfabetico.
Le parole di ogni riga:
    - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
      minuscole
    - sono separate da uno spazio
    - sono ordinate in base alla loro lunghezza e, in caso di pari lunghezza,
      in base all'ordine alfabetico, senza distinzione fra maiuscole e
      minuscole. In caso di parole uguali, in ordine alfabetico.

La funzione deve ritornare il numero di righe scritte nel file output_filename.

Esempio
Se nel file 'func4_test1.txt' sono presenti le seguenti due righe
cat bat    rat
Condor baT

la funzione func4('func4_test1.txt', 'func4_out1.txt') dovrà scrivere
nel file 'func4_out1.txt' le seguenti 3 righe:
baT bat
cat Condor
rat

e ritornare il valore 3.

"""


# NOTA: nei test ci sono parole ripetute che invece non dovrebbero apparire

def func4(input_filename, output_filename):
    # Inserisci qui il tuo codice
    with open(input_filename, encoding='utf-8') as  F:
        parole = F.read().split()
    uniche = set(parole)
    iniziali = {}
    for w in parole:
        iniziale = w[0].lower()
        if w not in iniziali.get(iniziale,[]):
            iniziali[iniziale] = iniziali.get(iniziale, []) + [w]
    with open(output_filename, encoding='utf-8',mode='w') as F:
        for i,words in sorted(iniziali.items()):
            print(*sorted(words, key=lambda w: (len(w),w.lower(),w)),file=F)
    return len(iniziali)

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Si scriva una funzione func5(imagefile, output_imagefile, color) che prende
in ingresso due stringhe che rappresentano due nomi di file di immagini PNG.
L'immagine nel file 'imagefile' contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza massima utilizzando il colore color preso in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna il numero di segmenti colorati nell'immagine in output.
"""
import images
def func5(imagefile, output_imagefile, color):
    # Inserisci qui il tuo codice
    white = 255,255,255
    black = 0,0,0
    img = images.load(imagefile)
    segmenti = {}
    for y,riga in enumerate(img):
        minx=maxx=None
        for x,c in enumerate(riga):
            if c == white:
                if minx is None:
                    minx = x
                if maxx is None:
                    maxx = x
                elif x > maxx:
                    maxx = x
        if minx is not None:
            segmenti[y] = minx, maxx
    lunghezze = [ maxx-minx for minx,maxx in segmenti.values() ]
    maxlen    = max(lunghezze)
    N = 0
    for y,[minx,maxx] in segmenti.items():
        if maxx-minx == maxlen:
            N += 1
            for x in range(minx,maxx+1):
                img[y][x] = color
    images.save(img,output_imagefile)
    return N



# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1 (recursive or using recursive functions or methods)
having as input the arguments:
    - 'directory', a string representing the path of an existing directory
    - 'ext', a string representing a file extension.
The function must search recursively within the directory given by directory
and in all subdirectories for
all files with 'ext' as extension. Such files are to be interpreted as
text files. The function has to compute the sum of the sizes of all
the files found in every subirectory. The function has to return a
dictionary where:
    - the keys are all the subdirectories where there is at lease one file
      with extension 'ext'
    - the values are the sum of all the sizes of the files found in such a directory.
The directories have to be reported with the relative path from the input
'directory'. The size of a given file can be computed using the read method
of an open file or using the os.stat function.

We suggest using the functions os.listdir, os.path.isfile and
os.path.isdir and NOT to use the os.join function in Windows (use
concatenation between strings with the '/' character).

It is forbidden to use the os.walk function.
"""

import os


def ex1(directory, ext):
    # Inserisci qui il tuo codice
    result = {}
    _ex1(directory, ext, result)
    return result

def _ex1(directory, ext, result):
    size = 0
    for name in os.listdir(directory):
        fullpath = directory + '/' + name
        if os.path.isdir(fullpath):
            _ex1(fullpath, ext, result)
        elif name.endswith(ext):
            size += os.stat(fullpath).st_size
    if size:
        result[directory] = size


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che prende in ingresso un nodo binario
root del tipo BinaryTree, come definito nel modulo tree.py.
La funzione deve ritornare il numero che si ottiene sommando tutti i valori
dei nodi che sono ad un livello pari e sottraendo tutti i valori dei nodi
che sono ad un livello dispari. La radice si assume a livello 0.

    Esempio:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    Se l'albero è quello di sinistra, la funzione deve ritornare il valore 8.
    Se l'albero è quello di destra, la funzione deve ritornare il valore -22.
"""


def ex2(root):
    # Inserisci qui il tuo codice
    return _ex2(root,0,0)

def _ex2(root, livello, totale):
    if root is None:
        return totale
    if livello % 2 == 0:
        totale += root.value
    else:
        totale -= root.value
    totale = _ex2(root.left,  livello+1, totale)
    totale = _ex2(root.right, livello+1, totale)
    return totale


###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

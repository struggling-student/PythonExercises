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
    return sorted(set(string_list1) ^ set(string_list2), reverse=True)


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
    with open(pathname) as fr:
        out = dict()
        for line in fr:
            for c in line:
                out[c] = out.get(c, 0) + 1
    return out
                

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


def remove(a_list, func):
    if a_list:
        val = func(a_list)
        while val in a_list:
            a_list.remove(val)


def func3(a_list):
    N = len(a_list)
    remove(a_list, min)
    remove(a_list, max)
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
Se nel file 'func4/func4_test1.txt' sono presenti le seguenti due righe
cat bat    rat
Condor baT

la funzione func4('func4/func4_test1.txt', 'func4_out1.txt') dovrà scrivere
nel file 'func4_out1.txt' le seguenti 3 righe:
baT bat
cat Condor
rat

e ritornare il valore 3.

"""


def find_words(filei):
    with open(filei) as fr:
        return set(fr.read().split())

    
def find_rows(words):
    rows = {}
    for word in words:
        i = word[0].upper()
        rows[i] = rows.get(i, []) + [word]
    return rows


def sort_row(row):
    row.sort(key=lambda S: (len(S), S.lower(), S))


def func4(input_filename, output_filename):
    words = find_words(input_filename)
    rows = find_rows(words)
    #ordina key of rows in alpha
    with open(output_filename, mode='wt') as fw:
        for row in sorted(rows.keys()):
            sort_row(rows[row])
            print(*rows[row], sep=' ', file=fw)
    return len(rows.keys())
        
        
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
    white = (255,)*3
    img = images.load(imagefile)
    segms = {}
    for r, row in enumerate(img):
        idx = [] 
        for x, pix in enumerate(row):
            if pix == white:
                idx.append((r, x))
        if idx:
            N = idx[-1][1] - idx[0][1] + 1
            segms[N] = segms.get(N, []) + [idx]
    Nmax = max(segms)
    for segm in segms[Nmax]:
        r, x_min = segm[0]
        _, x_max = segm[-1]
        img[r][x_min:x_max+1] = [color]*Nmax
    images.save(img, output_imagefile)
    return len(segms[Nmax])

    
# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Definire la funzione ex1 (ricorsiva o che utilizza funzioni o metodi
ricorsivi) avendo come input gli argomenti
    - 'directory', una stringa che rappresenta il percorso di una
      directory esistente
    - 'ext', una stringa che rappresenta l'estensione di un file.

La funzione deve cercare ricorsivamente all'interno di 'directory' e
in tutte le sottodirectory per tutti i file con estensione 'ext'. Tali
file devono essere interpretati come file di testo. La funzione deve
calcolare la somma delle dimensioni di tutti i file trovati in ogni
sottodirectory. La funzione deve restituire un dizionario dove:
    - le chiavi sono tutte le sottodirectory in cui è presente almeno
      un file con estensione 'ext'
    - i valori sono la somma di tutte le dimensioni dei file trovati
      in tale directory.

Le directory devono essere specificate con il percorso relativo
dall'input 'directory'. La dimensione di un determinato file può
essere calcolata utilizzando il metodo read di un file aperto o
utilizzando la funzione os.stat e dal risultato di os.stat prendere
l'attributo .st_size

Si consiglia di utilizzare le funzioni os.listdir, os.path.isfile e
os.path.isdir e di NON utilizzare la funzione os.join in Windows
(utilizzare la concatenazione tra stringhe con il carattere '/').

È vietato utilizzare la funzione os.walk.
"""

import os


def ex1(directory, ext):
    dizio = {}
    for item in os.listdir(directory):
        full_path = directory + "/" + item
        if os.path.isdir(full_path):
            dizio.update(ex1(full_path, ext))
        elif os.path.isfile(full_path) and item.endswith(ext):
            size = os.stat(full_path).st_size
            dizio[directory] = dizio.get(directory, 0) + size
    return dizio


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


def sump(v, level):
    return v if level % 2 == 0 else -v


def ex2(root, level=0):
    suml = ex2(root.left, level+1) if root.left else 0
    sumr = ex2(root.right, level+1) if root.right else 0
    return sum((sump(root.value, level), suml, sumr))


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

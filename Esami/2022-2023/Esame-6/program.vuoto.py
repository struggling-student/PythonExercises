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
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

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
Si definisca la funzione func1(int_list, bottom, up) che prende in
ingresso una lista di interi e due interi e modifica la lista rimuovendo
tutti gli interi che non sono compresi nell'intervallo [bottom, up],
estremi inclusi. Attenzione: la lista risulta modificata alla fine
della funzione.
La funzione ritorna il numero di elementi rimossi dalla lista.
Esempio:
    func1([4, 5, 10, 3, -1, 2], 0, 5) deve restituire il valore 2 e modificare
    la lista in input in [4, 5, 3, 2].
'''
def func1(int_list, bottom, up):
    ## Scrivi qui il tuo codice
    pass

# l1 = [4, 5, 10, 3, -1, 2]
# print(func1(l1, 0, 5))
# print (l1)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Si definisca una funzione func2(dict1, dict2) che prende in ingresso
due dizionari che hanno valori di tipo stringa e restituisce un nuovo
dizionario. Nel nuovo dizionario sono presenti soltanto le chiavi comuni
ai due dizionari in input. Ad ogni chiave del nuovo dizionario è associato
il valore minore fra i valori dei dizionari in input associati a quella
chiave. Tutte le stringhe valore del nuovo dizionario sono trasformate
in minuscolo.
Esempio:
    func2({'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}, {'a':'Bad', 'c':'greaT'})
    deve restituire il dizionario {'a':'bad', 'c':'excellent'}
'''
def func2(dict1, dict2):
    ## Scrivi qui il tuo codice
    pass

# print(func2({'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}, {'a':'Bad', 'c':'greaT'}))

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Si definisca una funzione func3(str1, str2) che prende in ingresso due stringhe
e costruisce una nuova stringa str3 ottenuta selezionando soltanto i caratteri
per cui str1 e str2 sono uguali, senza distinzione fra minuscole e maiuscole,
ma selezionando il carattere della stringa più corta.
La funzione restituisce la stringa così costruita.
Esempio:
    func3('abracadabra', 'ABerrant') deve restituire la stringa 'ABa'
'''

def func3(str1, str2):
    ## Scrivi qui il tuo codice
    pass

# print(func3('abracadabra', 'ABerrant'))
# print(func3('delIberAtIVelY', 'ReproductIvE'))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca una funzione func4(input_filename, output_filename, length) che
prende in ingresso due stringhe che rappresentano due nomi di file e un
intero.
Il file input_filename contiene una serie di stringhe separate da spazi,
tabulazioni o a capo.
La funzione deve creare un nuovo file di testo con nome output_filename
contenente tutte le stringhe di lunghezza length presenti nel file
input_filename organizzate per righe.
Le righe sono in ordine alfabetico.
Le parole di ogni riga:
    - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
      minuscole
    - sono separate da uno spazio
    - sono ordinate in base all'ordine alfabetico, senza distinzione fra
      maiuscole e minuscole. In caso di parole uguali, in ordine alfabetico.

La funzione deve ritornare il numero di stringhe della lunghezza
richiesta trovate nel file in input.

Esempio
Se nel file 'func4_test1.txt' sono presenti le seguenti tre righe
cat bat    rat
Condor baT
Cat cAr CAR

la funzione func4('func4_test1.txt', 'func4_out1.txt', 3) dovrà scrivere
nel file 'func4_out1.txt' le seguenti 3 righe:
baT bat
CAR cAr Cat cat
rat

e ritornare il valore 7.

"""

def func4(input_filename, output_filename, length):
    ## Scrivi qui il tuo codice
    pass


# print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 3))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Si scriva una funzione func5(input_filename, output_imagefile) che prende
in ingresso due stringhe che rappresentano due nomi di file.
Il file input_filename in ogni riga contiene una serie di interi separati
da una virgola. Per ogni serie di interi, la funzione deve disegnare il
perimetro di una forma in un'immagine con sfondo nero, rispettando l'ordine
delle righe del file in input.
Ogni serie può essere formata da 6 oppure 7 interi, a seconda che la forma
da disegnare sia un quadrato oppure un rettangolo.
La struttura di ogni serie di valori è la seguente: (r, g, b, x, y, w, h), dove
- r, g, b rappresentano i tre canali del colore con cui disegnare la forma
- x, y rappresentano le coordinate dell'angolo superiore sinistro della forma
- w, h rappresentano rispettivamente la larghezza e l'altezza della forma.
Nel caso di un quadrato, non è presente il valore h.
Le dimensioni dell'immagine sono tali da contenere perfettamente tutte le
forme, per cui:
    - la forma con l'angolo inferiore destro più a destra avrà il lato
      destro sul bordo dell'immagine,
    - la forma con l'angolo inferiore destro più in basso avrà il lato
      inferiore sul bordo dell'immagine.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna il numero di forme disegnate nell'immagine in output.

Per gli esempi si vedano i file nella directory func5.
"""
import images

def func5(input_filename, output_imagefile):
    ## Scrivi qui il tuo codice
    pass


# print(func5('func5/func5_test1.txt', 'func5/func5_test1.png'))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(n, faces), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso due interi, n e faces.

La funzione deve restituire una lista con tutti i possibili esiti del
lancio di 'n' dadi, ognuno con 'faces' facce. Ogni esito è rappresentato
da una tupla con 'n' elementi, un elemento per ogni dado.
La lista restituita deve essere ordinata in ordine crescente.

Esempio:
    ex1(2, 3) deve restituire la lista
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
"""

def ex1(n, faces):
    ## Scrivi qui il tuo codice
    pass

# print(ex1(2,3))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root), ricorsiva o che usa un metodo
ricorsivo, che prende in ingresso il nodo root che è la radice di
un albero binario costituito da nodi del tipo BinaryTree,
come definito nel modulo tree.py.
La funzione deve trasformare l'albero in input in modo che ogni nodo
con due figli abbia il figlio sinistro con un valore minore del
figlio destro, scambiando i valori dei nodi dei due figli se necessario.
La funzione restituisce il numero di scambi effettuati.

Esempio:

        root                   expected root
    ______5______              ______5______
   |             |            |             |
   8__        ___2___         2__        ___8___
      |      |       |           |      |       |
      3      9       1           3      1       9

      expected = 2

    Se l'albero è quello a sinistra, la funzione deve ritornare il
    valore 2 e trasformare l'albero in quello a destra.

Altro esempio:

              root                          expected root
          ______2______                      ______2______
         |             |                    |             |
      __ 7__        ___5___              __ 5__        ___7___
     |      |      |       |            |      |      |       |
    _4_     3_    _0_     _5_          _3_     4_    _0_     _5_
   |   |      |  |   |   |   |        |   |      |  |   |   |   |
   2   -1     1  8   3   2   9       -1   2      1  3   8   2   9

       expected = 4

    Se l'albero è quello a sinistra, la funzione deve ritornare il
    valore 4 e trasformare l'albero in quello a destra.

"""
import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass

# root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
# print(ex2(root))


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

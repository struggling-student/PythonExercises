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

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti
Definire la funzione func1(D1, D2), che riceve come argomenti due dizionari
D1 e D2: D1 ha stringhe come chiavi e interi come valori, mentre D2 ha interi
come chiavi e stringhe come valori.
La funzione deve trovare tutti i valori di D1 che sono chiavi di D2 e
restituire un elenco ottenuto concatenando le chiavi corrispondenti di
D1 con il valore corrispondente di D2. L'elenco deve essere ordinato in
ordine decrescente di lunghezza e, in caso di parità, in ordine
alfabetico crescente.

Esempio: se
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
D2 = {4:'bb', 1:'ff', 2:'ggg'}

func1(D1, D2) deve ritornare la lista ['bbggg', 'aaff', 'ccff', 'ebb']
'''
def func1(D1, D2):
    ## Scrivi qui il tuo codice
    pass
## Tests
# D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
# D2 = {4:'bb', 1:'ff', 2:'ggg'}
# print(func1(D1, D2))  # ['bbggg', 'aaff', 'ccff', 'ebb']

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Definire la funzione func2(l) che prende in input una lista di int l e
modifica la lista in modo che l'elemento in posizione i sia la somma di
tutti gli elementi dalla posizione 0 a i. La funzione restituisce il
valore dell'ultimo elemento della lista modificata.

Esempio: se l = [3, -3, 6, -1, 10]
func2(l) deve ritornare il valore 15 e modificare l in [3, 0, 6, 5, 15].
'''
def func2(l):
    ## Scrivi qui il tuo codice
    pass

## Tests
# l = [3, -3, 6, -1, 10]
# print(func2(l) )
# print(l)
# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Definire la funzione func3(words, l) che prenda in input:
    - un set di stringhe words
    - un int l
e restituisce un nuovo insieme con tutte le stringhe di lunghezza almeno l
nell'insieme words che sono una sottostringa di un'altra stringa in words.

Esempio: se words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
func3(words, 3) deve ritornare il set {'cat', 'bert'}
'''

def func3(words, l):
    ## Scrivi qui il tuo codice
    pass

## Tests
# print(func3({'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}, 3))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 punti
Definire la funzione func4(file_in, file_out, length, chars) che prenda in
input:
    -due stringhe che rappresentano i percorsi di due file di testo
    -un int length,
    -una stringa chars.
La funzione deve restituire l'elenco di tutte le parole trovate nel file
puntato da file_in con una lunghezza almeno pari a length e contenenti almeno 
uno dei caratteri della stringa chars. L'elenco deve essere ordinato per 
lunghezza decrescente e, in caso di parità, in ordine alfabetico.
Inoltre, la funzione deve scrivere le parole dell'elenco in output nel file
indicato da file_out separate da uno spazio bianco.

Esempio: func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd')
     deve ritornare la lista['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
     e scrivere la stringa 'hippopotamus elephant cobra horse panda snake' in func4/out_01.txt.
"""

def func4(file_in, file_out, length, chars):
    ## Scrivi qui il tuo codice
    pass
## Tests
# print(func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd'))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Definire la funzione func5(input_png, output_png, m, M) che prende come input
    - il percorso di un'immagine memorizzata in un file .png denominato input_png,
    - il percorso di un file png di output_png
    - due int m e M.
L'immagine di input contiene diverse linee orizzontali colorate su uno sfondo
nero. 
La funzione deve trovare le linee con una lunghezza compresa nell'intervallo
[m, M] e creare una nuova immagine con solo le linee trovate.

La funzione deve ritornare la differenza tra il numero di linee trovate
nell'immagine di input e quelle nell'immagine di output.
"""
import images

def func5(input_png, output_png, m, M):
    ## Scrivi qui il tuo codice
    pass

## Tests
# print(func5('func5/func5_test1.png', 'func5/func5_out1.png', 1, 20))
# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points
Definire la funzione ex1(chars, l), ricorsiva o che utilizza funzioni o
metodi ricorsivi, che prende in input un insieme di caratteri (ovvero 
stringhe di lunghezza uno) e un int l e restituisce l'insieme di tutte
le possibili stringhe palindrome di lunghezza l composte da caratteri
presi da chars.

Esempio:
    ex1({'a', 'b', 'c'}, 3) deve ritornare il set
    {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}

"""
def ex1(chars, l):
    ## Scrivi qui il tuo codice
    pass

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points
Definire una funzione ex2(root), ricorsiva o che utilizzi funzioni o
metodi ricorsivi, che prende come input root un'istanza di un BinaryTree
(come definito nel modulo tree) che rappresenta la radice di un albero
binario con valori int. La funzione deve restituire una coppia (v, l)
con il valore e il livello del nodo dell'albero con il prodotto massimo v*l.
In caso di più nodi con lo stesso prodotto, la funzione restituisce quello
con il livello minimo.
Si supponga che la radice si trovi al livello 1.

Ad esempio, se l'input è la radice del seguente albero:

               6              livello 1
              / \             
             5   16           livello 2
            /   / \
           4   10  6          livello 3
              /   / \
             7   8  1         livello 4
             
ci sono due nodi con prodotto massimo v*l=32, cioè 8*4 e 16*2, quindi
la funzione dovrebbe restituire la coppia (16, 2).
"""
import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass

# Tests
# T = tree.BinaryTree.fromList([6, [5, [4, None, None], None ], [16, [10, [7, None, None], None],
#                                                                [6, [8, None, None], [1, None, None]]]])
# print(ex2(T))

# %%#################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)

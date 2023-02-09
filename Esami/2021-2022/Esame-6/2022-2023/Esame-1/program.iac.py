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
Si definisca la funzione func1(string_list, word) che prende in ingresso una
lista di stringhe 'string_list' e una parola 'word' e cancella in maniera distruttiva
da string_list tutte le parole che contengono 'word'.
La funzione restituisce il numero di parole rimosse.
'''
def func1(string_list, word):
    # fatto a lezione piu volte in 
    # mille salse diverse.
    N = len(string_list)
    for i in range(N-1, -1, -1):
        if word in string_list[i]:
            del string_list[i]
    return N - len(string_list)


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Si definisca una funzione funct2(path_to_file) che prende in ingresso
una stringa che rappresenta il percorso ad un file testuale. Il file
contiene su ciascuna riga una coppia "numero,matricola" separata da
una virgola. I numeri sono sempre maggiori o uguali a zero.  La
funzione deve restituire il dizionario che si crea inserendo la
'matricola' come chiave sottoforma di stringa e come valore il
'numero' ma come tipo intero.  Inoltre una matricola puo' essere
associata a piu' numeri: nel caso in cui questo accade nel dizionario
va mantenuto il numero massimo.
Esempio:
Contenuto di func2_test_1.txt
 27,123456
 78,121212
 90,111111
 79,121212
 26,123456
 91,111111
La funzione func2('func2_test_1') ritorna {'123456': 27, '121212': 79, '111111': 91}
'''
def func2(pathname):
    # anche questo va fatto senza leggere il testo
    out = {}
    with open(pathname) as fr:
        for row in fr:
            v, k = row.rstrip().split(',')
            out[k] = max(out.get(k, -1), int(v))
    return out


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Si definisca una funzione func3(listaA, pathname) che prende in
ingresso una lista di stringhe 'listaA' e una stringa che punta ad una
file al percorso 'pathname'. La funzione deve scrivere al percorso
'pathname' un file di testo dove su ogni riga e' scritta ciascuna
stringa della listaA. Prima di scrivere le stringhe, e' necessario
ordinare in maniera crescente la listaA in base al numero di caratteri
di ciascuna stringa; in caso di parita' in ordine alfabetico inverso.
La funzione rende il numero di caratteri totali fra tutte le stringhe
in listaA.

I file attesi sono visibili in func3_1_exp.txt, func3_2_exp.txt, func3_3_exp.txt
'''


def func3(listaA, pathname):
    # idem, fatto a lezione tantissime volte
    # ordinamento parziale con due chiavi diverse
    elems = sorted(listaA, key=lambda S: (-len(S), S), reverse=True)
    with open(pathname, mode='wt') as fw:
        print(*elems, file=fw, sep='\n')
    return sum(len(S) for S in listaA)

    
# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si scriva una funzione func4(S) che prende in ingresso una stringa
che indica del testo da cui e' necessario togliere tutti gli elementi non
alfabetici e individuare tutte le parole presenti nella stringa e convertirle
in lower case.

Esempio: 
Da:

S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta
al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era
scordato di chiamare Paperino'

si passa a :

['pippo', 'e', 'topolino', 'sono', 'andati', 'al', 'mare', 'hanno',
'mangiato', 'una', 'bella', 'pasta', 'al', 'pesce', 'pescato', 'in',
'mare', 'il', 'giorno', 'prima', 'ma', 'purtroppo', 'topolino', 'si',
'era', 'scordato', 'di', 'chiamare', 'paperino']

Poi la funzione calcola l'istogramma delle parole che deve essere renderizzato
in una stringa.

L'istogramma sotto forma di stringa e' costruito secondo le seguenti regole:
- ciascuna parola appare nella stringa in ordine alfabetico
- il numero di volte (frequenza) che una parola appare in S e'
rappresentato con un numero di asterischi uguali alla frequenza.
- l'istogramma su ciascuna riga segue il formato: 
parola<spazio>* per quante volte e' presente e infine \n (accapo)"
- AVVISO: quando si stampa una parola vanno aggiunti degli spazi a
  destra in maniera che tutte le parole siano allineato a destra.

La parte iniziale della stringa istogramma sara':
'al        **\nandati    *\nbella     *\n .....
"""


def func4(S):
    # questo era piu complesso.
    # ci sono diversi sotto problemi
    # 1. trovare la parole da un testo (fatto a lezione)
    # 2. calcolarsi istogramma (fatto a lezione)
    # 3. renderizzare l'istogramma (fatto durante l'esercitazione)
    # 3b. la complicanza era allineare gli asterischi
    words = ''.join([c.lower() if c.isalpha() else ' ' for c in S]).split()
    histo = {}
    for word in sorted(words):
        histo[word] = histo.get(word, 0) + 1
    out = ''
    maxL = len(max(histo.keys(), key=len))
    for word, count in histo.items():
        # jword = word + ' '*(maxL-len(word)) ## facendolo a mano
        out += f'{word.ljust(maxL)} {"*"*count}\n'
    return out


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 points
Si definisca una funzione func5(img, output_file_name) che prende in ingresso
un'immagine modellata come lista di liste e effetti una rotazione A DESTRA
dell'immagine di 90 gradi. La nuova immagine ruotata deve essere salvata in
output_file_name tramite il modulo images.
La funzione ritorna una tupla nel formato altezza e poi larghezza
dell'immagine ruotata.
"""

import images


def func5(img, output_file_name):
    # a lezione e' stato fatto rotazione a sinstra.
    # per casa ho dato da fare rotazione a destra.
    H, W = len(img), len(img[0])
    rot = [[img[r][c] for r in reversed(range(H))] for c in range(W)]
    images.save(rot, output_file_name)
    return W, H


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points
Si scriva una funzione ricorsiva ex1(root), o che al suo interno usi
una funzione ricorsiva, che prende in ingresso una directory e
ricorsivamente esplori l'albero delle directory e restituisca un
dizionario. La chiave del dizionario e' il percorso assoluto a partire
dalla 'root', sottoforma di stringa.  Il valore corrisponde ad una
stringa cosi fatta: considerando una directory trovata, si prendano
TUTTI i file in QUELLA directory SOLO con estensione ".txt", ordinati
in maniera alfabetica.  I file .txt sono file testuali dove su ogni
riga vi e' una serie di numeri interi seguiti solo da uno spazio. A
esempio 'ex1_A/MPkzlXmQic.txt' contiene:

75 84 84 73 83
76 74 76

Si legga sequenzialmente ciascun numero interpretandolo come valore
unicode e quindi convertendolo in carattere concatenandolo con il
carattere successivo.

Ad esempio la sequenza suddetta e' convertita nella stringa KTTISLJL.

Il valore della chiave per una directory e' la stringa che si ottiene
concatenando le stringhe generate per ogni file testuale per quella
directory, secondo l'ordine alfabetico dei file.txt.

Se la directory non contiene nessun file .txt allora quella directory
non appare nel dizionario.

Quindi ad esempio la directory 'ex1_A' contiene il solo file 'ex1_A/MPkzlXmQic.txt'
e quindi nel dizionario verra' assegnato 'ex1_A': 'KTTISLJL'.

Se la funzione e' chiamta su 'ex1_A', ritorna:

{'ex1_A/BtYNg': 'NXK', 'ex1_A/aVzZb/fEZcS': 'QMJOJGJDGRCEVUNCOR',
'ex1_A/aVzZb/uVccE': 'WP', 'ex1_A/aVzZb/nPjxD': 'VXFGJNXQ',
'ex1_A/aVzZb': 'TKKQDXHTBXJTQS', 'ex1_A': 'KTTISLJL'}
"""

import os


def convert(files):
    out = ''
    for f in sorted(files):
        with open(f) as fr:
            out += ''.join([chr(int(c))
                            for line in fr
                            for c in line.rstrip().split(' ')
                            ])
    return out


def ex1(root):
    # questo era piu complesso ma non difficile
    # c'e' da spezzare il problema in sotto-problemi
    files, rez = [], {}
    for item in os.listdir(root):
        fullpath = root + '/' + item
        if os.path.isfile(fullpath) and fullpath.endswith('.txt'):
            files.append(fullpath)
        elif os.path.isdir(fullpath):
            rez.update(ex1(fullpath))
        else:
            pass
    if files:
        rez[root] = convert(files)
    return rez


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti
Si scriva una funzione ricorsiva ex2(nums, ops), oppure una che usi
altre funzioni ricorsive, che prende in ingresso un set di numeri
interi positivi 'nums' e una lista di stringhe 'ops' che indicano
delle operazioni sui numeri. La funzione deve generare ricorsivamente
tutte le possibili espressioni aritmetiche, dove ciascuna espressione
e' una stringa. Le espressioni derivano dalla concatenzione di un
numero preso da 'nums' con un'operazione dal set 'ops'. La funzione
deve restituire tutte le espressioni costruite.
Nel costruire l'espressione valgono le seguenti regole:

1. una volta che un numero e' usato nell'espressione, non puo' piu' essere usato

se nums={5,8,0} e ops=['+','*']

'8+5+0' e' un'espressione valida ma '8+5+8' non lo e'.

2. le operazioni possono essere riutilizzate a piacimento quante volte si vuole.

infatti in '8+5+0' il + e' stato usato 2 volte.

La funzione puo' ritornare un set con tutte le espressioni generate.
Esempio: nums={5,8,0} e ops=['+','*'] la funzione deve generare il set:

{'8*5*0', '5+0+8', '5+0*8', '0+5+8', '0+8+5', '8+5*0', '0+5*8',
'0*8*5', '0*8+5', '8+5+0', '5*0*8', '8+0*5', '5*8+0', '5*0+8',
'5+8+0', '8*0+5', '0*5*8', '0+8*5', '8*5+0', '8*0*5', '5*8*0',
'5+8*0', '0*5+8', '8+0+5'}
"""


def gen_exp(nums, ops):
    # questo forse era l'esercizio piu difficile
    # e' un caso di PERMUTAZIONI (si veda lezione) dove ogni volta
    # pero' bisogno concatenare anche l'operazione oltre
    # al numero. Quando si propaga la ricorsione ricordarsi di
    # togliere il numero usato e di non togliere niente dalle 
    # operazioni.
    if not nums:
        return ['']
    if len(nums) == 1:
        return list(map(str, nums))
    return [''.join([str(num), o, gs])
            for num in nums
            for o in ops
            for gs in gen_exp(nums-{num}, ops)]


def ex2(nums, ops):
    return set(gen_exp(nums, ops))
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

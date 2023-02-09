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

## RICAPITOLAZIONE PUNTEGGIO:
# | esercizio       | punteggio |
# | func1           |         2 |
# | func2           |         2 |
# | func3           |         2 |
# | func4           |         6 |
# | func5           |         6 |
# | ex1 (ricorsivo) |         6 |
# | ex2 (ricorsivo) |         8 |
# | --------------- |        -- |
# | Totale          |        32 |
"""

name       = "NOME"
surname    = "COGNOME"
student_id = "MATRICOLA"


################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################


# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(string_list, word) che prende in ingresso una
lista di stringhe 'string_list' e una parola 'word' e cancella in maniera distruttiva
da string_list tutte le stringhe che contengono 'word'.
La funzione restituisce il numero di stringhe rimosse.
'''
def func1(string_list, word):
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca una funzione func2(pathname) che prende in ingresso
una stringa che rappresenta il percorso ad un file testuale. Il file
contiene su ciascuna riga una coppia "numero,matricola" separata da
una virgola. I numeri sono sempre maggiori o uguali a zero.  La
funzione deve restituire il dizionario che si crea inserendo la
'matricola' come chiave sottoforma di stringa e come valore il
'numero' come tipo _intero_.  Una matricola puo' essere
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
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca una funzione func3(listaA, pathname) che prende in
ingresso una lista di stringhe 'listaA' e una stringa che punta ad una
file al percorso 'pathname'. La funzione deve scrivere al percorso
'pathname' un file di testo dove su ogni riga e' scritta ciascuna
stringa della listaA. Prima di scrivere le stringhe, e' necessario
ordinare in maniera crescente la listaA in base al numero di caratteri
di ciascuna stringa; in caso di parita' in ordine alfabetico inverso.
La funzione ritorna il numero di caratteri totali di tutte le stringhe
in listaA.

I file attesi sono visibili in func3_1_exp.txt, func3_2_exp.txt, func3_3_exp.txt
'''


def func3(listaA, pathname):
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si scriva una funzione func4(S) che prende in ingresso una stringa 'S'
che indica del testo da cui e' necessario trasformare in spazi tutti i caratteri
non alfabetici, quindi individuare la lista di tutte le parole presenti nella
stringa, convertite in lower case.

Esempio. Da:
S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta
al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era
scordato di chiamare Paperino'

si passa a :
['pippo', 'e', 'topolino', 'sono', 'andati', 'al', 'mare', 'hanno',
'mangiato', 'una', 'bella', 'pasta', 'al', 'pesce', 'pescato', 'in',
'mare', 'il', 'giorno', 'prima', 'ma', 'purtroppo', 'topolino', 'si',
'era', 'scordato', 'di', 'chiamare', 'paperino']

Poi la funzione calcola l'istogramma delle parole renderizzato in una stringa.

L'istogramma sotto forma di stringa e' costruito secondo le seguenti regole:
- le parole appaiono in ordine alfabetico
- ogni parola appare seguita da uno o più spazi, un numero di asterischi ('*')
  pari alle ripetizioni di quella parola e infine un carattere di accapo ('\n')
- il numero di spazi dopo ogni parola è tale che gli asterischi sono
  tutti allineati a sinistra.

Quindi la parte iniziale della stringa istogramma sarà:
'al        **\nandati    *\nbella     *\n .....'

che visualizzata porta a:

al        **
andati    *
bella     *
chiamare  *
di        *
e         *
era       *
giorno    *
hanno     *
il        *
in        *
ma        *
mangiato  *
mare      **
paperino  *
pasta     *
pescato   *
pesce     *
pippo     *
prima     *
purtroppo *
scordato  *
si        *
sono      *
topolino  **
una       *

NOTA: la parola piu lunga e' 'purtroppo' e dista
un solo spazio dal primo asterisco.

Si vedano test_func4_1, test_func4_2, test_func4_3
in grade.py per piu esempi
"""


def func4(S):
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 punti
Si definisca una funzione func5(img, output_file_name) che prende in ingresso
un'immagine modellata come lista di liste e effetti una rotazione A DESTRA
dell'immagine di 90 gradi. La nuova immagine ruotata deve essere salvata in
output_file_name tramite il modulo images.
La funzione ritorna una tupla nel formato altezza e poi larghezza
dell'immagine ruotata.
"""

import images


def func5(img, output_file_name):
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti
Si scriva una funzione ricorsiva ex1(root), o che al suo interno usi
una funzione ricorsiva, che prende in ingresso una stringa che punta ad una
directory e ricorsivamente esplori l'albero delle directory e restituisca un
dizionario. La chiave del dizionario e' il percorso assoluto a partire
dalla 'root', sottoforma di stringa.  Il valore corrisponde ad una
stringa così fatta: considerando una directory trovata, si prendano
soltanto i file in QUELLA directory con estensione ".txt", ordinati
in maniera alfabetica.  I file .txt sono file testuali dove su ogni
riga vi e' una serie di numeri interi seguiti solo da uno spazio. A
esempio 'ex1_A/XYCwdkCokL.txt' contiene:

75 84 84 73 83
76 74 76

Si legga sequenzialmente all'alto al basso, da sinistra a destra,
ciascun numero, lo si interpreti come valore Unicode, convertendolo
in un carattere e lo si concateni con il carattere successivo.

Ad esempio la sequenza suddetta e' convertita nella stringa "KTTISLJL".

Il valore nel dizionario e' la stringa che si ottiene
concatenando le stringhe generate per ogni file testuale per quella
directory, secondo l'ordine alfabetico dei file.txt.

Se la directory non contiene nessun file .txt allora quella directory
non appare nel dizionario.

Se la funzione e' chiamata su 'ex1_A', ritorna:

{'ex1_A/bkLbD': 'A\x9eŻĂĳŜǖ', 'ex1_A': 'KTTISLJL'}

NOTA: e' proibito usare la funzione os.walk. Si possono usare:
os.listdir, os.path.isfile, os.path.exists, etc.
Per concatenare i path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
"""

import os


def ex1(root):
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 8 punti
Si scriva una funzione ricorsiva ex2(nums, ops), oppure una che usi
altre funzioni ricorsive, che prende in ingresso un set di numeri
interi positivi 'nums' e una lista di stringhe 'ops' che indicano
delle operazioni sui numeri. La funzione deve generare ricorsivamente
tutte le possibili espressioni aritmetiche, dove ciascuna espressione
e' una stringa. Le espressioni derivano dalla unione di due
o più numeri presi da 'nums' mediante operazioni del set 'ops', usando
le regole seguenti:

1. una volta che un numero e' usato nell'espressione, non puo' piu' essere usato
   Esempio:
     se nums={5,8,0} e ops=['+','*']
     '8+5+0' e' un'espressione valida ma '8+5+8' non lo e'.

2. le operazioni possono essere riutilizzate a piacimento quante volte si vuole.
   Nell'esempio precedente '8+5+0', infatti, il '+' e' stato usato 2 volte.

La funzione torna un set con tutte le espressioni generate.

Esempio: nums={5,8,0} e ops=['+','*'] la funzione deve generare il set:
{'8*5*0', '5+0+8', '5+0*8', '0+5+8', '0+8+5', '8+5*0', '0+5*8',
'0*8*5', '0*8+5', '8+5+0', '5*0*8', '8+0*5', '5*8+0', '5*0+8',
'5+8+0', '8*0+5', '0*5*8', '0+8*5', '8*5+0', '8*0*5', '5*8*0',
'5+8*0', '0*5+8', '8+0+5'}

NOTA: NON  definite la funzione ricorsiva interamente a ex2() altrimenti
non passate il test ricorsivo.
NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
"""


def ex2(nums, ops):
    # scrivi qui il tuo codice
    pass



###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

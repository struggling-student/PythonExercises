#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame e' necessario:
    - ottenere un punteggio maggiore o uguale a 18 (15 se DSA)

Il voto finale e' la somma dei punteggi dei problemi risolti.

"""
nome      = "A"
cognome   = "S"
matricola = "42"

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
da string_list tutte le parole che contengono 
la sequenza di due lettere formata dalla prima ed ultima lettera di 'word'.
La funzione restituisce il numero di parole rimosse.

Esempio:
    string_list = ['cocacola','fanta', 'assenzio', 'Minosse', 'sinfonie']
    word = 'saponette'
    expected = ['cocacola','fanta', 'sinfonie']
    N = 2
'''
def func1(string_list, word):
    N = len(string_list)
    string_list[:] = [ w for w in string_list if word[0]+word[-1] not in w ]
    return N - len(string_list)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Si definisca una funzione func2(pathname) che prende in ingresso
una stringa che rappresenta il percorso ad un file testuale. Il file
contiene su ciascuna riga una coppia "numero,matricola" separata da
una virgola. I numeri sono sempre maggiori o uguali a zero.  La
funzione deve restituire il dizionario che si crea inserendo la
'matricola' come chiave sotto forma di stringa e come valore il
'numero' ma come tipo intero.  Inoltre una matricola puo' essere
associata a piu' numeri: nel caso in cui questo accade nel dizionario
va mantenuta la media dei numeri per quella matricola.
Esempio:
Contenuto di func2_test_1.txt
 27,123456
 78,121212
 90,111111
 79,121212
 26,123456
 91,111111
La funzione func2('func2_test_1') 
ritorna {'123456': 26.5, '121212': 78.5, '111111': 90.5}
'''
def func2(pathname):
    D = {}
    with open(pathname,encoding='utf8') as f:
        for line in f:
            N,M = line.strip().split(',')
            N = int(N)
            D[M] = D.get(M,[]) + [N]
    for k in D:
        D[k] = sum(D[k])/len(D[k])
    return D

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Implementare la funzione func3(listA, pathname) che prende in input una lista di stringhe listA 
e una stringa che indica il percorso di un file pathname. 
La funzione deve scrivere nel percorso pathname un file di testo in cui 
ogni riga contiene una stringa di listA. 
Prima di scrivere le stringhe, è necessario ordinare listA in ordine:
 - crescente rispetto al numero di caratteri di ciascuna stringa; 
 - in caso di parità, in ordine alfabetico inverso ignorando la differenza tra maiuscole e minuscole;
 - in caso di parità, in ordine alfabetico inverso.
La funzione restituisce il numero totale di caratteri di tutte le stringhe in listA.

Esempio:
lista = ['ananas', 'Banana', 'pluto', 'zoroastro', 'marx', 'socrate', 'PLATO']
expected = 42
    
Gli output attesi sono disponibili in `func3_1_exp.txt`, `func3_2_exp.txt`, `func3_3_exp.txt`.
'''


def func3(listaA, pathname):
    def criterio(parola):
        return -len(parola), parola.lower(), parola
    caratteri = 0
    with open(pathname, encoding='utf-8', mode='w') as f:
        for parola in sorted(listaA, key=criterio, reverse=True):
            print(parola,file=f)
            caratteri += len(parola)
    return caratteri



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
- ciascuna parola appare nella stringa in ordine alfabetico inverso
- il numero di volte (frequenza) che una parola appare in S e'
rappresentato con un numero di asterischi uguali alla frequenza.
- l'istogramma su ciascuna riga segue il formato: 
<spazi di allineamento se necessari>parola<spazio>* per quante volte e' presente e infine \n (accapo)"
- AVVISO: quando si stampa una parola vanno aggiunti degli spazi a
  sinistra in maniera che tutte le stringhe siano allineate a destra.

che visualizzata porta a:

      una *
 topolino **
     sono *
       si *
 scordato *
purtroppo *
    prima *
    pippo *
    pesce *
  pescato *
    pasta *
 paperino *
     mare **
 mangiato *
       ma *
       in *
       il *
    hanno *
   giorno *
      era *
        e *
       di *
 chiamare *
    bella *
   andati *
       al **

NOTA: la parola piu lunga e' 'purtroppo' e dista
un solo spazio dal primo asterisco.

Si vedano test_func4_1, test_func4_2, test_func4_3
in grade.py per piu esempi
"""


def func4(S):
    non_alpha = { c for c in S if not c.isalpha() }
    for c in non_alpha:
        S = S.replace(c,' ')
    parole = S.split()
    H = {}
    L = 0
    for w in parole:
        w = w.lower()
        H[w] = H.get(w,0) + 1
        L = max(L,len(w))
    istogramma = ''
    for w in sorted(H, reverse=True):
        star = '*' * H[w]
        pad  = ' ' * (L-len(w))
        istogramma += f'{pad}{w} {star}\n'
    return istogramma

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 points
Si definisca una funzione func5(img, output_file_name) che prende in ingresso
un'immagine modellata come lista di liste e effetti una rotazione A SINISTRA
dell'immagine di 90 gradi seguita da una riflessione rispetto all'asse verticale. 

La nuova immagine deve essere salvata in output_file_name tramite il modulo images.
La funzione ritorna una tupla nel formato altezza e poi larghezza
dell'immagine ruotata e riflessa.

Esempio
immagine    rotazione       riflessione
abc         -->         cf      -->     fc
def                     be              eb
                        ad              da
"""

import images

"""
  012     01
0 abc     cf 0
1 def     be 1
          ad 2
"""

def Y(x,y,W,H):
    return x

def X(x,y,W,H):
    return W-y-1

def func5(img, output_file_name):
    W,H = len(img[0]), len(img)
    img2 = [ [ img[Y(x,y,W,H)][X(x,y,W,H)] for x in range(H) ] for y in range(W) ]
    for row in img2:
        row[:] = row[::-1]   # flip sinistra-destra della riga
    images.save(img2,output_file_name)
    return W,H


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points
Implementare una funzione ricorsiva ex1(root), o che usa un'altra funzione ricorsiva, 
che prende in input una stringa che indica il percorso di una directory 
ed esplora ricorsivamente l'albero delle directory restituendo un dizionario. 
La chiave del dizionario è il percorso assoluto a partire dalla directory `root`, 
in forma di stringa. Il valore corrisponde a una stringa costruita come segue: 
considerando una directory, prendiamo TUTTI i file in QUELLA directory 
SOLO con estensione `.txt`, ordinati in ordine alfabetico inverso. 
I file `.txt` sono file di testo in cui ogni riga contiene una serie 
di numeri interi separati da spazi. 
Un esempio è il file `ex1_A/MPkzlXmQic.txt` che contiene:

75 84 84 73 83
76 74 76

Dall'alto in basso, da sinistra a destra, leggere sequenzialmente ogni numero 
interpretandolo come valore unicode e convertendolo in un carattere. 
La concatenazione di tutti i caratteri forma una stringa.

Ad esempio, la sequenza sopra viene convertita nella stringa `KTTISLJL`.

Il valore nel dizionario è la stringa ottenuta concatenando le stringhe generate 
per ciascun file di testo di quella directory, 
secondo l'ordine alfabetico inverso dei nomi dei file `.txt`.

Se la directory non contiene file `.txt`, allora quella directory non compare nel dizionario.

NOTA: usate il separatore '/' per i path.

Quindi, ad esempio, la directory `ex1_A` contiene solo il file `ex1_A/MPkzlXmQic.txt` 
e il dizionario conterrà `ex1_A`: `KTTISLJL`.

Se la funzione viene chiamata su `ex1/A`, restituirà:

{'ex1/A': 'KTTISLJL', 'ex1/A/bkLbD': 'ĳŜǖA\x9eŻĂ'}

NOTA: È vietato usare la funzione `os.walk`. 
È possibile usare: `os.listdir`, `os.path.isfile`, `os.path.exists`, ecc.

NOTA: NON  definite la funzione ricorsiva internamente a ex2() altrimenti
non passate il test ricorsivo.
NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
"""

import os

def collect_txt(path):
    D = { path: []}
    for f in os.listdir(path):
        fullname = path +'/'+ f
        if os.path.isdir(fullname):
            D.update(collect_txt(fullname))
        elif f.endswith('.txt'):
            D[path].append(fullname)
    if not D[path]:
        del D[path]
    return D

def build_string(files):
    risultato = ''
    for f in sorted(files, reverse=True):
        with open(f) as F:
            for N in F.read().split():
                risultato = risultato + chr(int(N))
    return risultato

def ex1(directory):
    # WRITE HERE YOUR CODE
    D = {}
    # collect files
    D = collect_txt(directory)
    for k,files in D.items():
        D[k] = build_string(files)
    return D


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 7 punti

Si scriva una funzione ricorsiva ex2(nums, ops), oppure una che usi
altre funzioni ricorsive, che prende in ingresso una lista di numeri
interi positivi 'nums' e una lista di stringhe 'ops' che indicano
delle operazioni binarie tra numeri. 
NOTA: le due liste possono contenere ripetizioni.
La funzione deve generare ricorsivamente tutte le possibili espressioni aritmetiche, 
dove ciascuna espressione e' una stringa. 
Le espressioni derivano dalla concatenzione di numeri presi da 'nums' 
intervallati da operazioni prese da 'ops'. 
La funzione deve restituire tutte le espressioni costruite.
Nel costruire l'espressione valgono le seguenti regole:

1. una volta che uno dei numeri e' usato nell'espressione, non puo' piu' essere usato
(a meno che non ce ne siano altre copie nella lista)

se nums = [5, 0, 5] e ops = ['+', '*', '+']

'5+5*0' e' un'espressione valida ma '5+5*5' non lo e' perchè 5 appare troppe volte.

2. una volta che un operatore è stato usato non può più essere usato
(a meno che non ce ne siano altre copie nella lista)

quindi '5*5*0' in cui * e' usato 2 volte non va bene 

La funzione ritorna un set con tutte le espressioni create di massima lunghezza.
(che contengono tutti i numeri oppure tutti gli operatori)

Esempio:
nums = [5, 0, 5]; ops = ['+', '*', '+']
expected = {'0+5+5', '5*5+0', '0*5+5', '5+5*0', '5+0*5', '5*0+5', '5+0+5', '5+5+0', '0+5*5'} 

NOTA: NON  definite la funzione ricorsiva internamente a ex2() altrimenti
non passate il test ricorsivo.
NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
"""


def ex2(nums, ops):
    # se c'è un solo numero non posso creare una espressione
    # se son finiti gli operatori non posso creare espressioni
    if not ops or len(nums) == 1:
        return { str(x) for x in nums }
    # altrimenti posso
    R = set()
    for X in nums:           # scelgo un numero
        rest_nums = nums.copy()
        rest_nums.remove(X)
        for op in ops:       # ed un operatore
            rest_ops = ops.copy()
            rest_ops.remove(op)
            # e per ogni espressione che usa il resto dei numeri e operatori
            for sol in ex2(rest_nums, rest_ops):
                R.add(f'{X}{op}{sol}')   # gli aggiungo numero ed operatore
    return R

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

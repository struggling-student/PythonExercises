#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare questo file col nome program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la prova è necessario:
    - !!!riempire le informazioni personali nelle variabili qui sotto!!!
    - AND ottenere un punteggio maggiore o uguale a 18 (o 15 se DSA)

Il punteggio finale della prova è la somma dei punteggi dei problemi risolti.
Per i DSA il punteggio viene scalato opportunamente (32*X/26).
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ------------------------ SUGGERIMENTI PER IL DEBUG --------------------------- #
# Per eseguire solo alcuni dei test, puoi commentare le righe della lista
# 'tests' alla fine di grade.py
#
# Per facilitare il debug delle funzioni ricorsive, puoi disattivare
# il test ricorsivo impostando DEBUG=True nel file grade.py
#
# DEBUG=True attiva anche il TRACE DELLO STACK che ti permette di sapere quale
# numero di riga in program.py ha generato l'errore.
################################################################################

# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 2 punti

Implementa la funzione func1(testo:str) -> dict[str,list[int] che riceve come argomento:
- testo: una stringa di testo
e che ritorna un dizionario che ha come chiavi solo le lettere alfabetiche presenti nel testo
e come valori una lista di interi che indicano le posizioni della lettera nel testo.

Esempio:
    testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
    expected = {'s': [0, 31], 'o': [1, 32, 35], 'p': [2, 9, 20, 27, 40, 51, 58], 'r': [3, 21, 52, 56], 
                'a': [4, 7, 10, 13, 16, 19, 22, 25, 28, 38, 41, 44, 47, 50, 53, 59], 'l': [6, 15, 37, 46], 
                'n': [11, 42], 'c': [12, 18, 24, 43, 49, 55], 'm': [26], 't': [33, 34], 'e': [57]}
"""
def func1(testo:str) -> dict[str,list[int]]:
    d = dict()
    for i, c in enumerate(testo):
        if c.isalpha():
            try:
                d[c].append(i)
            except KeyError:
                d[c] = [i]
    return d
    # completa la funzione


"""
testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
expected = {'s': [0, 31], 'o': [1, 32, 35], 'p': [2, 9, 20, 27, 40, 51, 58], 'r': [3, 21, 52, 56], 
            'a': [4, 7, 10, 13, 16, 19, 22, 25, 28, 38, 41, 44, 47, 50, 53, 59], 'l': [6, 15, 37, 46], 
            'n': [11, 42], 'c': [12, 18, 24, 43, 49, 55], 'm': [26], 't': [33, 34], 'e': [57]}
print(func1(testo))
"""

# %% ----------------------------------- FUNC.2 ----------------------------------- #
"""
Func 2: 2 punti

Implementa la funzione func2(D1:dict[str,list[int]], D2: dict[int,str]) -> dict[str, list[str]] che riceve come argomenti:
- D1: un dizionario che ha come chiavi delle stringhe e come valori delle liste di interi
- D2: un dizionario che ha come chiavi degli interi e come valori delle stringhe
e che ritorna un dizionario che ha come chiavi le chiavi k di D1 
e come valori la lista di valori di D2 associati agli interi presenti in D1[k].
Le chiavi del risultato che non hanno valori associati non devono apparire nel risultato.
Le liste di valori devono essere ordinate in ordine di lunghezza decrescente, 
ed in caso di parità in ordine alfabetico crescente.

Esempio:
    D1 = {'a':[1,2,3], 'b':[3,4,5], 'c':[6,7,8]}
    D2 = {1:'ccc', 3:'qq', 4:'z', 5:'fff', 2:'zz'}
    expected = {'a': ['ccc', 'qq', 'zz'], 'b': ['fff', 'qq', 'z']}
"""
def func2(D1:dict[str,list[int]], D2: dict[int,str]) -> dict[str, list[str]]:
    d = {}
    for k, v in D1.items():
        l = []
        for i in v:
            if i in D2:
                l.append(D2[i])
        if len(l) > 0:
            d[k] = sorted(l, key= lambda x: (-len(x), x))
    return d
    pass
    # completa la funzione


'''
D1 = {'a':[1,2,3], 'b':[3,4,5], 'c':[6,7,8]}
D2 = {1:'ccc', 3:'qq', 4:'z', 5:'fff', 2:'zz'}
expected = {'a': ['ccc', 'qq', 'zz'], 'b': ['fff', 'qq', 'z']}
print(func2(D1,D2))
'''

# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 2 punti

Implementa la funzione    func3(parole: list[str], k:int, S:set[str]) -> dict[str, int] che riceve come argomento:
- parole: una lista di stringhe
- k: un intero
- S: un insieme di caratteri

La funzione deve ritornare un dizionario che ha come chiavi le parole che contengono almeno k caratteri di S
e come valori il numero di caratteri in S presenti nella stringa.

Esempio:
    parole = ['ciao', 'come', 'stai', 'bene', 'cane', 'gatto', 'topo', 'elefante', 'giraffa']
    k = 3
    S = {'a','e','i','o','u'}
    expected = {'ciao': 3, 'elefante': 4, 'giraffa': 3}
"""
def func3(parole: list[str], k:int, S:set[str]) -> dict[str, int]:
    d = {}
    for p in parole:
        val = sum(p.count(c) for c in S)
        if  val >= k:
            d[p] = val
    return d
    # completa la funzione



"""
parole = ['ciao', 'come', 'stai', 'bene', 'cane', 'gatto', 'topo', 'elefante', 'giraffa']
k = 3
S = {'a', 'e', 'i', 'o', 'u'}
print(func3(parole, k, S))
expected = {'ciao': 3, 'elefante': 4, 'giraffa': 3}
"""

# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 4: 6 punti

Implementa la funzione    func4(path_in : str, path_out : str, K : int) -> dict[str, list[str]]
che riceve come argomenti:
    - path_in:  un percorso ad un file di testo da leggere, contenente parole separate da spazi
    - path_out: un percorso ad un file di testo da scrivere
    - K: un intero
La funzione deve leggere il file di testo al percorso path_in
e ritornare un dizionario che ha come chiavi le parole presenti nel file **in almeno K righe** 
e come valori delle liste di coppie (a,b) di interi, dove a è il numero di riga in cui la parola è apparsa 
e b è il numero di volte che è apparsa in quella riga.

Successivamente la funzione deve scrivere su file path_out su ogni riga 
la parola, il numero totale di righe in cui essa appare ed il numero totale di apparizioni nel file, separati da spazio.
Le righe del file path_out devono essere ordinate 
- per numero di righe in cui sono apparse le parole in ordine decrescente 
- e in caso di parità in ordine alfabetico crescente.

Esempio:
path_in = 'func4/in_1.txt'
path_out = 'func4/out_1.txt'
k = 2
Il file in_1.txt contiene:
    a b c b a a
    aa ba ca aa ba ca
    a b
    aa b
Il file out_1.txt conterrà:
    b 3 4
    a 2 4
    aa 2 3
e la funzione restituirà:
    {'a': [(0, 3), (2, 1)], 'b': [(0, 2), (2, 1), (3, 1)], 'aa': [(1, 2), (3, 1)]}
"""
def func4(path_in : str, path_out : str, K : int) -> dict[str, list[str]]:
    with open(path_in) as f:
        words = set(f.read().split())
        f.seek(0)
        blob = f.readlines()
    d = {}
    for i, row in enumerate(blob):
        for word in words:
            if word in row.split():
                if word in d:
                    d[word].append((i, row.split().count(word)))
                else:
                    d[word] = [(i, row.split().count(word))]
    
    with open(path_out, 'w') as f:
        for w in sorted(d, key= lambda x: (-len(d[x]), x)):
            if len(d[w])>=K:
                print(w, len(d[w]), sum(p[1] for p in d[w]), file =f)
            else:
                del d[w]
    return d



'''
path_in = 'func4/in_1.txt'
path_out = 'func4/out_1.txt'
k = 2
print(func4(path_in, path_out, k))
expected={'a': [(0, 3), (2, 1)], 'b': [(0, 2), (2, 1), (3, 1)], 'aa': [(1, 2), (3, 1)]}
'''


# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 8 punti

Implementa la funzione      func5(path_png_in : str, path_png_out : str) -> dict[str, set[tuple[int,int]]]
che riceve come argomenti:
    - path_png_in:  un percorso ad un file PNG da leggere
    - path_png_out: un percorso ad un file PNG da scrivere
Il file PNG path_png_in contiene un'immagine a sfondo nero con dei rombi colorati di varie dimensioni.

Esempio che contiene un rombo 3x3 di colore d e due rombi 2x2 di colore b e c:

.....b......
..c.b.b.....
.c.c.b...d..
..c.....d.d.
.......d...d
........d.d.
.........d..

ASSUMETE che nessuno dei rombi si appoggi sul bordo della immagine o tocchi un altro rombo.

La funzione deve leggere il file PNG al percorso path_png_in e cercare tutte le posizioni
in cui compare un rombo 2x2 di pixel tutti dello stesso colore.

La funzione deve ritornare come risultato un dizionario che ha come chiavi i colori dei rombi 2x2
e come valori l'insieme delle loro posizioni .
(si intende la posizione x,y del pixel centrale del rombo 2x2)

Inoltre, deve colorare il centro di ciascun rombo 2x2 trovato con il suo colore e salvare l'immagine modificata
al percorso path_png_out.

Esempio:
    path_png_in = 'func5/in_5.png'
    path_png_in = 'func5/out_5.png'
    expected = {(203, 128, 176): {(17, 6), (4, 2), (13, 7)}, (222, 255, 190): {(14, 3)}}
"""
import images
black   = (0,0,0)
def check_it(img, row, col):
    return img[row][col] == img[row+2][col] == img[row+1][col-1] == img[row+1][col+1]

def func5(path_png_in : str, path_png_out : str) -> dict[str, set[tuple[int,int]]]:
    d = {}
    img = images.load(path_png_in)
    for row in range(len(img)-2):
        for col in range(len(img[0])-1):
            if img[row][col] != black:
                if check_it(img, row, col):
                    color = img[row][col]
                    img[row+1][col] = color
                    if color not in d:
                        d[color] = {(col, row+1),}
                    else:
                        d[color].add((col, row+1))
                        
    images.save(img, path_png_out)
    return d


'''
path_png_in = 'func5/in_5.png'
path_png_in = 'func5/out_5.png'
print(func5(path_png_in, path_png_out))
expected = {(203, 128, 176): {(17, 6), (4, 2), (13, 7)}, (222, 255, 190): {(14, 3)}}
'''

# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 6 punti

Implementa la funzione    ex1(radice : nary_tree.NaryTree, lista_pesi:list[int]) -> nary_tree.NaryTree
che riceve come argomento:
- radice: un albero n-ario formato da nodi nary_tree.NaryTree
- lista_pesi: una lista di interi
e che da esso costruisce ricorsivamente o usando funzioni o metodi ricorsivi
un secondo albero n-ario che ha la stessa struttura del primo con i valori dei figli di ciascun nodo moltiplicati 
ciascuno per x*p, dove x è l'n-esimo valore di lista_pesi e p è la profondità del nodo padre
(considerando la radice a profondità 1).

ATTENZIONE: l'albero originale deve rimanere inalterato.

Esempio:
Se l'albero in input è:
   __________1_________
   |     |            |
 __2__   3___   _____40_____
 |   |      |   |   |  |    |
 4   5      6   7   8  9   10
e lista_pesi = [2,7,3,1,2,5,9]
l'albero in output sarà:
   __________1_________            p=1 (non moltiplicato)
   |     |            |
 __4__   21__   _____120_____      p=2 (moltiplicati per [2,7,3,...])         
 |   |      |   |   |  |    |
 16  70    24   28 112 54  20      p=3 (moltiplicati per [4,14,6,2,...])
"""
import nary_tree

def _ex1(radice, pesi, prof, pos):
    if not radice.sons:
        return nary_tree.NaryTree(radice.value*pesi[pos]*prof)
    root = nary_tree.NaryTree(radice.value*pesi[pos]*prof)
    for i, figlio in enumerate(radice.sons):
        root.sons.append(_ex1(figlio, pesi, prof+1, i))
    return root
        
def ex1(radice : nary_tree.NaryTree, lista_pesi:list[int]) -> nary_tree.NaryTree:
    root = nary_tree.NaryTree(radice.value)
    
    for i, figlio in enumerate(radice.sons):
        root.sons.append(_ex1(figlio, lista_pesi, 1, i))
    return root
    # completa la funzione



'''
A1       = nary_tree.NaryTree.fromList([1, [2, [4], [5]], [3, [6]], [40, [7], [8], [9], [10]]])
A1bis    = nary_tree.NaryTree.fromList([1, [2, [4], [5]], [3, [6]], [40, [7], [8], [9], [10]]])
expected = nary_tree.NaryTree.fromList([1, [4, [16], [70]], [21, [24], [28]], [120, [112], [54], [20]]])
lista_pesi = [2,7,3,1,2,5,9]
A2 = ex1(A1, lista_pesi)
print('Risultato:\n',A2.__repr__(0))
print('Expected:\n',expected.__repr__(0))
print("L'albero originale deve restare invariato:",A1==A1bis)
'''


# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti

Implementa la funzione    ex2(path : str) -> dict[str, dict[str,int]]
che riceve come argomento:
- path: il path di una directory
- lista_estensioni: una lista di estensioni di file (stringhe)
e che esplora ricorsivamente o usando funzioni o metodi ricorsivi la directory path
e tutte le sue sottodirectory e ritorna un dizionario che ha come chiavi 
i path delle directory/sottodirectory e come valori dei dizionari.
Ciascuno di questi dizionari, a sua volta ha come chiavi le estensioni di tutti i file presenti nella directory
e come valori il numero di file con quella estensione.

ATTENZIONE: è proibito usare la funzione os.walk
NOTA: potete usare le funzioni os.listdir, os.path.isdir, os.path.isfile ...
NOTA: usate il carattere '/' per separare i path, che funziona sia su Windows che Linux

Esempio:
    directory  = 'ex2/A'
    expected   = {'ex2/A': {'txt': 3}, 'ex2/A/C': {'bak': 1, 'txt': 4, 'png': 1}, 'ex2/A/B': {'txt': 2}}
"""
import os
def ex2(path : str) -> dict[str, dict[str,int]]:
    d = {}
    for f in os.listdir(path):
        file = path+'/'+f
        if os.path.isdir(file):
            d.update(ex2(file))
        elif os.path.isfile(file):
            name, ext = os.path.splitext(file)
            ext = ext.lstrip('.')
            if path not in d:
                d[path] = {}
            d[path][ext] = d[path].get(ext, 0) + 1
    return d
    # completa la funzione





######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*' * 50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimeniti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)



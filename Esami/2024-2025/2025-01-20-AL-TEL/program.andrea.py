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
nome       = "A"
cognome    = "S"
matricola  = "42"

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
e come valori una lista di interi che indicano tutte le posizioni della lettera nel testo
in ordine crescente.

Esempio:
    testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
    expected = {'s': [0, 31], 'o': [1, 32, 35], 'p': [2, 9, 20, 27, 40, 51, 58], 'r': [3, 21, 52, 56], 
                'a': [4, 7, 10, 13, 16, 19, 22, 25, 28, 38, 41, 44, 47, 50, 53, 59], 'l': [6, 15, 37, 46], 
                'n': [11, 42], 'c': [12, 18, 24, 43, 49, 55], 'm': [26], 't': [33, 34], 'e': [57]}
"""
def func1(testo:str) -> dict[str,list[int]]:
    pass
    # completa la funzione
    D = {}
    for pos,c in enumerate(testo):
        if c.isalpha():
            if c not in D:
                D[c] = []
            D[c].append(pos)
    return D

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

Implementa la funzione func2(D1:dict[str,list[int]], D2: dict[int,str]) -> dict[str, list[str]] 
che riceve come argomenti:
- D1: un dizionario che ha come chiavi delle stringhe e come valori delle liste di interi
- D2: un dizionario che ha come chiavi degli interi e come valori delle stringhe
e che ritorna un dizionario che ha come chiavi le chiavi k di D1 
e come valori la lista di valori di D2 associati agli interi presenti in D1[k].
Le liste di valori devono essere ordinate in ordine di lunghezza decrescente, 
ed in caso di parità in ordine alfabetico crescente.
Le chiavi del risultato che non hanno nessun valore associato non devono apparire nel risultato.

Esempio:
    D1 = {'a':[1,2,3], 'b':[3,4,5,6], 'c':[6,7,8]}
    D2 = {1:'ccc', 3:'qq', 4:'z', 5:'fff', 2:'zz'}
    expected = {'a': ['ccc', 'qq', 'zz'], 'b': ['fff', 'qq', 'z']}
infatti:
- 'a' ha i valori 1,2,3   e i valori associati sono 'ccc', 'zz', 'qq', che ordinati diventano 'ccc', 'qq', 'zz'
- 'b' ha i valori 3,4,5,6 e i valori associati sono 'qq', 'z', 'fff' ma 6 non è presente in D2
- 'c' ha i valori 6,7,8   ma nessuno di questi è presente in D2, quindi 'c' non compare nel risultato
"""
def func2(D1:dict[str,list[int]], D2: dict[int,str]) -> dict[str, list[str]]:
    pass
    # completa la funzione
    D = {}
    for k in D1:
        for i in D1[k]:
            if i in D2:
                if k not in D:
                    D[k] = []
                D[k].append(D2[i])
    for k in D:
        D[k].sort(key=lambda x: (-len(x), x))
    return D


'''
D1 = {'a':[1,2,3], 'b':[3,4,5], 'c':[6,7,8]}
D2 = {1:'ccc', 3:'qq', 4:'z', 5:'fff', 2:'zz'}
expected = {'a': ['ccc', 'qq', 'zz'], 'b': ['fff', 'qq', 'z']}
print(func2(D1,D2))
'''

def genera_func2(N):
    import random
    from wonderwords import RandomWord
    rw = RandomWord()
    D1 = {rw.word(word_min_length=3, word_max_length=random.randint(3,6)): list(random.choices(range(1,N), k=random.randint(1,N))) for _ in range(N)}
    D2 = {random.randint(1,N): rw.word() for i in range(1,N)}
    R = func2(D1,D2)
    print(f'''
def test_func2_{N}(run=True):
    D1 = {D1}
    D2 = {D2}
    expected = {R}
    return do_func2_test(D1,D2,expected)
    ''')

#genera_func2(10)


# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 2 punti

Implementa la funzione    func3(parole: list[str], k:int, S:set[str]) -> dict[str, int] che riceve come argomento:
- parole: una lista di stringhe
- k: un intero
- S: un insieme di caratteri

La funzione deve ritornare un dizionario che ha come chiavi 
le parole che contengono almeno k caratteri appartenenti ad S 
e come valori il numero di caratteri appartenenti ad S presenti nella parola.

Esempio:
    parole = ['ciao', 'come', 'stai', 'bene', 'cane', 'gatto', 'topo', 'elefante', 'giraffa']
    k = 3
    S = {'a','e','i','o','u'}
    expected = {'ciao': 3, 'elefante': 4, 'giraffa': 3}
"""
def func3(parole: list[str], k:int, S:set[str]) -> dict[str, int]:
    pass
    # completa la funzione
    return { p: n for p in parole if (n:=sum(1 for c in p if c in S)) >= k}


"""
parole = ['ciao', 'come', 'stai', 'bene', 'cane', 'gatto', 'topo', 'elefante', 'giraffa']
k = 3
S = {'a', 'e', 'i', 'o', 'u'}
print(func3(parole, k, S))
expected = {'ciao': 3, 'elefante': 4, 'giraffa': 3}
"""

def genera_func3(N,d):
    from wonderwords import RandomWord
    import random
    rw = RandomWord()
    parole = [rw.word() for _ in range(N)]
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    lettere = set(random.choices(alfabeto, k=N//d))
    k = N//(2*d)
    print(f'''
def test_func3_1(run=True):
    parole = {parole}
    k = {k}
    S = {lettere}
    expected = {func3(parole, k, lettere)}
    return do_func3_test(parole,k,S,expected)
    ''')

#genera_func3(50,5)

# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 4: 4+3 punti

4 punti:
Implementa la funzione    func4(path_in : str, path_out : str, K : int) -> dict[str, list[str]]
che riceve come argomenti:
    - path_in:  un percorso ad un file di testo da leggere, contenente parole separate da spazi
    - path_out: un percorso ad un file di testo da scrivere
    - K: un intero
La funzione deve leggere il file di testo al percorso path_in
e ritornare un dizionario che ha come chiavi le parole presenti nel file **in almeno K righe** 
e come valori degli insiemi di coppie (a,b) di interi, dove a è il numero di riga in cui la parola è apparsa 
e b è il numero di volte che è apparsa in quella riga.

3 punti:
Successivamente la funzione deve scrivere su file path_out su ogni riga 
la parola, il numero totale di righe in cui essa appare ed il numero totale di apparizioni nel file, separati da spazio.
Le righe del file path_out devono essere ordinate in ordine alfabetico crescente delle parole

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
    a 2 4
    aa 2 3
    b 3 4
e la funzione restituirà:
    {'a': {(0, 3), (2, 1)}, 'b': {(0, 2), (2, 1), (3, 1)}, 'aa': {(1, 2), (3, 1)}}
"""
def func4(path_in : str, path_out : str, K : int) -> dict[str, list[str]]:
    pass
    # completa la funzione
    D = conta_parole_e_righe(path_in)
    for k in list(D.keys()):
        if len(D[k]) < K:
            del D[k]
    totals = {word: (len(coppie), sum(y for x,y in coppie)) for word,coppie in D.items()}
    with open(path_out, 'w') as f:
        for word in sorted(totals.keys()):
            f.write(f'{word} {totals[word][0]} {totals[word][1]}\n')
        #f.write('paperino 2 3\n')
    return D

def conta_parole_e_righe(path_in):
    D = {}
    with open(path_in) as f:
        for i, line in enumerate(f):
            words = line.split()
            seen = set()
            for word in words:
                if word not in D:
                    D[word] = set()
                if word not in seen:
                    D[word].add((i, words.count(word)))
                    seen.add(word)
    return D

'''
path_in = 'func4/in_1.txt'
path_out = 'func4/out_1.txt'
k = 2
print(func4(path_in, path_out, k))
expected={'a': {(0, 3), (2, 1)}, 'b': {(0, 2), (2, 1), (3, 1)}, 'aa': {(1, 2), (3, 1)}}
'''


# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 7 punti

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
def func5(path_png_in : str, path_png_out : str) -> dict[str, set[tuple[int,int]]]:
    pass
    # completa la funzione
    img = images.load(path_png_in)
    D = {}
    W,H=len(img[0]),len(img)
    for x in range(2, W-2):
        for y in range(2,H-2):
            if is_rombo(img, x, y):
                color = img[y-1][x]
                img[y][x] = color
                if color not in D:
                    D[color] = set()
                D[color].add((x,y))
    images.save(img, path_png_out)
    return D

'''
path_png_in = 'func5/in_5.png'
path_png_in = 'func5/out_5.png'
print(func5(path_png_in, path_png_out))
expected = {(203, 128, 176): {(17, 6), (4, 2), (13, 7)}, (222, 255, 190): {(14, 3)}}
'''

def is_rombo(img, x, y):
    b = 0,0,0
    return b == img[y][x] != img[y-1][x] == img[y][x-1] == img[y+1][x] == img[y][x+1]

def vuotoP(img,x,y,l):
    b = 0,0,0
    for i in range(-l,l+1):
        for j in range(-l,l+1):
            if img[y+i][x+j] != b:
                return False
    return True

def genera_rombi(W,H,N):
    import random
    colori = [(random.randint(100,255), random.randint(100,255), random.randint(100,255)) for _ in range(N//5)]
    b = 0,0,0
    img = [[b for _ in range(W)] for _ in range(H)]
    posizioni = []
    D = {}
    for _ in range(N):
        l = random.randint(2,5)
        x = random.randint(l+1,W-l-1)
        y = random.randint(l+1,H-l-1)
        if (x,y) not in posizioni and vuotoP(img, x, y, l):
            posizioni.append((x,y))
            color = random.choice(colori)
            disegna_rombo(img, x, y, l, color)
            if l == 2:
                if color not in D:
                    D[color] = set()
                D[color].add((x,y))
    images.save(img, f'func5/in_{N}.png')
    return D

def disegna_rombo(img, x, y, l, color):
    for i in range(l):
        dx = l-i-1
        dy = i
        img[y-dy][x-dx] = color
        img[y-dy][x+dx] = color
        img[y+dy][x-dx] = color
        img[y+dy][x+dx] = color

# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 6 punti

Implementa la funzione    ex1(radice : nary_tree.NaryTree, lista_pesi:list[int]) -> nary_tree.NaryTree
che riceve come argomento:
- radice: un albero n-ario formato da nodi nary_tree.NaryTree
- lista_pesi: una lista di interi
e che lo modifica ricorsivamente o usando funzioni o metodi ricorsivi in modo che,
per ciascun figlio di un nodo, che supponiamo si trovi nella posizione N nella lista che lo contiene,
il valore in esso contenuto venga moltiplicato per x*p, dove x è l'N-esimo valore di lista_pesi
p è la profondità del nodo (considerando la radice a profondità 0).
Ritornate l'albero modificato.

Esempio:
Se l'albero in input è:
   __________1_________
   |     |            |
 __2__   3___   _____40_____       i 3 nodi sono nella posizioni N=0,1,2 nella lista dei figli della radice
 |   |      |   |   |  |    |
 4   5      6   7   8  9   10     
 0°  1°    0°   0°  1°  2°   3°    posizione N del nodo nella lista dei figli che lo contiene
e lista_pesi = [2,7,3,1,2,5,9]
dopo la modifica sarà:
   __________1_________            p=0 (la radice non è moltiplicata)
   |     |            |
 __4__   21__   _____120_____      p=1 (moltiplicati per [2,7,3,...])         
 |   |      |   |   |  |    |
 16  70    24   28 112 54   20     p=2 (moltiplicati per [4,14,6,2,...])
 0°  1°    0°   0°  1°  2°   3°    posizione N del nodo nella lista dei figli che lo contiene
"""
import nary_tree

def ex1(radice : nary_tree.NaryTree, lista_pesi:list[int]) -> nary_tree.NaryTree:
    pass
    # completa la funzione
    def ex1_ric(nodo, i, p):
        nodo.value *= p*lista_pesi[i]
        for i,figlio in enumerate(nodo.sons):
            ex1_ric(figlio, i, p+1)
    for i, figlio in enumerate(radice.sons):
        ex1_ric(figlio, i, 1)
    return radice

def generate_ex1(N):
    T = nary_tree.NaryTree.randomTree(N)
    print(T.toList())
    W = [8, 7, 6, 5, 4, 3, 2, 1]
    R = ex1(T, W)
    print(R.toList())
    print(T.__repr__(0))
    print(R.__repr__(0))


'''
A1       = nary_tree.NaryTree.fromList([1, [2, [4], [5]], [3, [6]], [40, [7], [8], [9], [10]]])
expected = nary_tree.NaryTree.fromList([1, [4, [16], [70]], [21, [24], [28]], [120, [112], [54], [20]]])
lista_pesi = [2,7,3,1,2,5,9]
ex1(A1, lista_pesi)
print('Risultato:\n',A1.__repr__(0))
print('Expected:\n',expected.__repr__(0))
'''


# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti

Implementa la funzione    ex2(path : str) -> dict[str, dict[str,int]]
che riceve come argomento:
    - path: il path di una directory
e che esplora ricorsivamente o usando funzioni o metodi ricorsivi la directory path
e tutte le sue sottodirectory e ritorna un dizionario che ha come chiavi 
i path delle directory/sottodirectory e come valori dei dizionari.
Ciascuno di questi dizionari, a sua volta ha come chiavi le estensioni di tutti i file presenti nella directory
e come valori il numero di file con quella estensione in quella directory.

ATTENZIONE: è proibito usare la funzione os.walk
NOTA: potete usare le funzioni os.listdir, os.path.isdir, os.path.isfile ...
NOTA: usate il carattere '/' per separare i path, che funziona sia su Windows che Linux

Esempio:
    directory  = 'ex2/A'
    expected   = {'ex2/A': {'txt': 3}, 'ex2/A/C': {'bak': 1, 'txt': 4, 'png': 1}, 'ex2/A/B': {'txt': 2}}
"""
import os
def ex2(path : str) -> dict[str, dict[str,int]]:
    pass
    # completa la funzione
    D = { path: {}}
    for nome in os.listdir(path):
        fullname = path +'/' + nome
        if os.path.isdir(fullname):
            D.update(ex2(fullname))
        else:
            estensione = nome.split('.')[-1]
            if estensione not in D[path]:
                D[path][estensione] = 0
            D[path][estensione] += 1
    return D


def sistema_estensioni(path):
    import os, random
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for root, dirs, files in os.walk(path):
        for file in files:
            fe = file.split('.')
            if len(fe) == 1:
                estensione = ''.join(random.choices(alfabeto, k=3))
                os.rename(root + '/' + file, root + '/' + file + '.' + estensione)
                print(f'File {file} rinominato in {file}.{estensione}')

# sistema_estensioni('ex2')


# print(ex2('ex2/A'))
# expected = {'ex2/A': {'txt': 3}, 'ex2/A/C': {'bak': 1, 'txt': 4, 'png': 1}, 'ex2/A/B': {'txt': 2}}

######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*' * 50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimeniti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)



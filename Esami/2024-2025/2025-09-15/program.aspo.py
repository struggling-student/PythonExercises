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
    - ottenere un punteggio maggiore o uguale a 18 (15 se DSA)

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
import tree
import images
nome = "aspo"
cognome = "aspo"
matricola = "aspo"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(D), che riceve come parametro un dizionario
D, in cui ogni chiave è un intero positivo N e il corrispondente valore
è una lista di caratteri alfabetici L.
La funzione ritorna una con una stringa per ogni chiave del dizionario.
Le stringhe sono ottenute concatenando tutti i caratteri in L, tranne il
carattere con indice l'intero chiave corrispondente. Se l'indice è esterno
alla lista, la stringa contiene tutti i caratteri di L.
La lista è ordinata in ordine alfabetico decrescente.
Ad esempio se D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'], la funzione ritornerà
['su', 'qa']
'''


def func1(D):
    ret = []
    for k, l in D.items():
        if k < len(l):
            l.pop(k)
        ret.append(''.join(l))
    return sorted(ret, reverse = True)

# Test della funzione func1
# print(func1({2: ['s', 'u', 'e'], 3: ['q', 'a']}))
# risultato: ['su', 'qa']


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(L) che ha come parametro una lista L di N liste.
Ogni lista P della lista L può ha una o più liste che possono essere vuote
oppure avere uno o più elementi.
La funzione ritorna una lista di N interi, in cui l'elemento i-esimo
indica il numero di liste vuote nella lista in i-esima posizione di L.
Ad esempio, se L = [ [3, []], [2,[3]], [4, [], [3,4], []]]
la funzione restituirà [1, 0, 2]
'''


def func2(L):
    # Scrivi qui il tuo codice
    ret = []
    for l in L:
        ret.append(sum([1 for x in l if x == []]))
    return ret


# Test della funzione func2
# print(func2(  [ [1, []], [2,[3]], [[],[],[5,6], [1], [2]], [[]], [[],[],[]], [[3]], [[],[],[5]]])
# risultato: [1, 0, 2, 1, 3, 0, 2]

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S, m, M) che riceve in input una stringa contenente
delle parole separate da virgole ed, opzionalmente, anche da spazi.
La funzione deve estrarre le parole da S, considerando solo quelle che
hanno una lunghezza compresa fra m ed M inclusi, ed inserirle in una seconda
lista ordinata alfabeticamente senza considerare la differenza tra maiuscole
e minuscole.
Ad esempio se S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
la funzione func3(S, 3, 4) restituirà ['Brad', 'Dana','ian', 'UMA', 'Zoe']
'''


def func3(S, m, M):
    S = S.replace(',', ' ')
    return sorted([s for s in S.split() if m <= len(s) <= M], key=lambda x: x.lower())
    pass

# Test della funzione func3
# print(func3("Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe", 3, 4))
# risultato: ['Brad', 'Dana','ian', 'UMA', 'Zoe']


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Definire la funzione func4(input_filepath, output_filepath) che legge il
file indicato da input_filepath.  Il file di input contiene parole separate
da ritorni a capo, spazi, tabulazioni, virgole o punto e virgola.  

Le parole considerate vanno raggruppate secondo la lettera che occorre
con più frequenza, senza distinzione fra maiuscole e minuscole.
Per ogni gruppo occorre scrivere nel file di output una riga nel formato:

<lettera minuscola>: <lista delle parole separate da spazio>

La lettera iniziale di riga è in minuscolo, seguita da ": " (due punti più
spazio); di seguito, compare la lista delle parole che hanno quella lettera
con maggiore frequenza, indipendentemente dal fatto che la lettera nella parola
sia maiuscola o minuscola. Le righe devono apparire in ordine alfabetico
in base alla lettera. Le liste sono in ordine alfabetico, ignorando la distinzione
fra minuscole e maiuscole, oppure mantenendo l'ordine alfabetico in caso di
parole identiche, ma con diverse maiuscole.
Se una parola ha più lettere con frequenza massima, allora quella parola compare
nella riga di ognuna di tali lettere.

Attenzione, alla fine di ogni riga nel file di output NON c'e' alcuno spazio ma c'è
SEMPRE un ritorno a capo!

La funzione deve restituire il numero totale di parole, compresi i duplicati,
trovate nel file di input.

Ad esempio:

contenuto di func4/func4_in1.txt:
GE
wOa;II,see	ua;PAO,oA;wOA
pao iu;jJa,kE

Chiamata
n = func4("func4/func4_in1.txt", "func4/func4_out1.txt")

contenuto atteso di func4/func4_out1.txt:
u: 1
o: 1
i: 1
e: 3
a: 4

Valore restituito: 12
"""


def func4(input_filename, output_filename):
    with open(input_filename) as f:
        blob = f.read()
        blob = blob.replace(',', ' ').replace(';', ' ')
    ret = {}
    for word in blob.split():
        d = {c: word.lower().count(c) for c in set(word.lower())}
        m = max(d.values())
        for c, v in d.items():
            if v == m:
                if c not in ret:
                    ret[c] = [word]
                else:
                    ret[c].append(word)
    with open(output_filename, 'w') as f:
        for c in sorted(ret):
            print(
                f"{c}: {" ".join(sorted(ret[c], key=lambda x: (x.lower(), x)))}", file=f)
    return len(blob.split())
    pass


# func4('func4/in_test1.txt', 'func4/out_test1.txt')
# func4('func4/in_test2.txt', 'func4/out_test2.txt')
# func4('func4/in_test3.txt', 'func4/out_test3.txt')
# func4('func4/in_test4.txt', 'func4/out_test4.txt')
# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti
Definire la funzione func5(file_in, file_out) che usa images.load per
caricare l'immagine presente in file_in. L'immagine è una lista di liste
e ogni elemento interno è un pixel rappresentato dalla tupla (r, g, b).
Lo sfondo è completamente nero, cioè (0, 0, 0).

Nell'immagine sono presenti pixel di diverso colore.

La funzione deve individuare per ogni riga il colore che ricorre maggiormente
e sostituire con il nero tutti gli altri pixel non di quel colore.
Nel caso in cui diversi pixel di una riga compaiano lo stesso numero di volte,
si deve considerare il colore con il valore più basso nella prima componente,
in caso di parità, il valore più basso nella seconda componente, in caso di
parità, il valore più basso nella terza componente.

La funzione deve poi salvare il risultato in file_out mediante images.save e
restituire il numero di pixel sostituiti.
"""


def func5(file_in, file_out):
    im = images.load(file_in)
    count = 0
    for i, row in enumerate(im):
        if len(set(row) - {(0, 0, 0)}) == 0:
            continue
        color = min(set(row) - {(0, 0, 0)}, key=lambda x: (-row.count(x), x))
        for j, col in enumerate(row):
            if col not in {(0, 0, 0), color}:
                im[i][j] = (0, 0, 0)
                count += 1
    images.save(im, file_out)
    return count


print(func5("func5/test1_in.png", "func5/test1_out.png"))
print(func5("func5/test2_in.png", "func5/test2_out.png"))
print(func5("func5/test3_in.png", "func5/test3_out.png"))
print(func5("func5/test4_in.png", "func5/test4_out.png"))

# Test della funzione func5
# print(func5("func5/in_test1.png", "func5/out_test1.png"))
# risultato: 3 (il numero di blocchi 2x2 trovati nell'immagine di test)

# %% ----------------------------------- EX.1 ------------------------- #
'''
Ex1: 6 punti


Si consideri la classe BinaryTree contenuta nel file tree.py che definisce
un nodo di albero binario. Scrivere una funzione ex1(T, n) ricorsiva o che faccia
uso di una o piu' funzioni ricorsive.
La funzione riceve la radice di un BinaryTree come input. Nei nodi
dell'albero in input sono memorizzati degli interi.
La funzione deve individuare tutti i percorsi radice-foglia che attraversano
dei nodi per i quali la somma dei valori in essi memorizzati è pari a n.
La funzione deve ritornare una lista contenente la lista dei valori
dei nodi attraversati per ogni percorso individuati. La lista ritornata
deve essere ordinata in ordine crescente.

Ad esempio, 


        ______20_____       level 1          ______13______
       |             |                      |              |
       4__        ___1___   level 2      ___7___        ___10___
          |      |       |              |       |      |        |
          -2     1       4  level 3    _-5_    -1_    _-9_      -3
                                      |    |      |  |    |       
                            level 4   5    4      6  6   -2    

Se T è l'albero di sinistra, allora la funzione ex1(T, 22) deve ritornare
la lista [[20, 1, 1], [20, 4, -2]], se T è l'albero di destra, allora
la funzione ex1(T, 20) deve ritornare la lista [[13, 7, -5, 5], [13, 10, -9, 6], [13, 10, -3]]

'''


def ex1(T, n):
    l = _ex1(T)
    l = filter(lambda x: sum(x) == n, l)
    return sorted(l)


def _ex1(T):
    if T.right is None and T.left is None:
        return [[T.value]]
    ret = []
    if T.right is not None:
        rest = _ex1(T.right)
        for l in rest:
            ret.append([T.value]+l)
    if T.left is not None:
        rest = _ex1(T.left)
        for l in rest:
            ret.append([T.value]+l)
    return ret

# Test della funzione ex1
# print(ex1(tree.BinaryTree.fromList([20, [4,None,[-2,None,None]], [1, [1,None,None], [4,None,None]]]), 22))
# risultato: [[20, 1, 1], [20, 4, -2]]


root = tree.BinaryTree.fromList([13, [7, [-5, [5, None, None], [4, None, None]], [-1, None, [6, None, None]]],
                                 [10, [-9, [6, None, None], [-2, None, None]], [-3, None, None]]])
print(ex1(root, 20))
# Test della funzione ex1
# print(ex1(tree.BinaryTree.fromList(["", ["", ["", None, None], None], ["", None, ["", None, None]]])))
# risultato: [[20, 1, 1], [20, 4, -2]]

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Scrivere la funzione ex2(L, k) ricorsiva oppure che faccia uso di
funzioni ricorsive. L è una lista di stringhe di lunghezza variabile.
k è un intero maggiore di 0.

La funzione deve costruire e restituire il set di tutte le stringhe lunghe
k ottenute concatenando due o più stringhe di L.

Esempio:
L = ['a', 'bb', 'ccc', 'd']
k = 4

Output atteso:
{'dabb', 'dccc', 'dbba', 'bbad', 'ccca', 'abbd', 'bbda', 'cccd', 'adbb', 'accc'}
"""


# def ex2(L, k):
#     if len(L) == 1:
#         if len(L[0]) == k:
#             return {L[0]}
#     ret = set()
#     for i, w in enumerate(L):
#         if k-len(w) <0:
#             continue
#         l = L.copy()
#         l.pop(i)
#         partial = ex2(l, k-len(w))
#         for word in partial:
#             if len(w+word) == k:
#                 ret.add(w+word)
#     return ret

def ex2(L, k):
    combinations = _ex2(L)
    # print(combinations)
    return set(c for c in combinations if len(c)==k)

def _ex2(L):
    if len(L) == 2:
        return {L[0]+L[1], L[1]+L[0]}
    ret = set()
    for i, w in enumerate(L):
        partial = _ex2(L[:i]+L[i+1:])
        for word in partial:
            ret.add(w+word)
            ret.add(word+w)
            ret.add(word)
    return ret

print(ex2(['a', 'bb', 'ccc', 'd'], 4))
# Test della funzione ex2
# print(ex2(['a', 'bb', 'ccc', 'd'], 4))
# risultato: {'dabb', 'dccc', 'dbba', 'bbad', 'ccca', 'abbd', 'bbda', 'cccd', 'adbb', 'accc'}


# %%
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*' * 50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)

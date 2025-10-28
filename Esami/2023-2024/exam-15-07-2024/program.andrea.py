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
nome       = "Andrea"
cognome    = "Sterbini"
matricola  = "42"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(L) che, ricevendo come argomento una lista
di stringhe L, restituisce una lista di tuple. Ogni tupla contiene due
elementi corrispondenti agli elementi della lista L: il primo è la lunghezza
il secondo è il numero di vocali della stringa originale corrispondente,
ignorando la distinzione fra minuscole e maiuscole.
La lista di tuple deve essere ordinata in ordine decrescente rispetto al
numero di vocali e, in caso di parità, crescente rispetto alla lunghezza
della stringa.

Esempio:
L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
risultato = [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]
'''
def func1(L):
    ## Scrivi qui il tuo codice
    pass
    def contavocali(s):
        S = 0
        vocali = 'aeiouAEIOU'
        for v in vocali:
            S += s.count(v)
        return S
    def criterio(coppia):
        l, cv = coppia
        return (-cv, l)
    risultato = [(len(s), contavocali(s)) for s in L]
    risultato.sort(key=criterio)
    return risultato

def genera_func1(N):
    import wonderwords, random
    def ucaserandom(S):
        return ''.join([c.upper() if random.random() > 0.5 else c for c in S])
    ww = wonderwords.RandomWord()
    L = [ucaserandom(ww.word()) for _ in range(N)]
    return f'''
    L = {L}
    expected = {func1(L)}
    return do_func1_tests(L, expected)
    '''

# print(genera_func1(25))

# L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
# print(func1(L)) # [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(D) che, ricevendo come argomento un
dizionario D, che ha come chiavi dei valori interi e come valori delle
liste di stringhe, restituisce un insieme di tuple.

Ogni tupla contiene tre elementi: il primo è la chiave, il secondo è
la prima parola della lista di stringhe in ordine alfabetico, il terzo
l'ultima parola della lista di stringhe in ordine alfabetico.

Esempio:
D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
risultato = {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}
'''
def func2(D):
    ## Scrivi qui il tuo codice
    pass
    return {(k, sorted(v)[0], sorted(v)[-1]) for k, v in D.items()}

def genera_func2(N):
    import wonderwords, random
    ww = wonderwords.RandomWord()
    D = {i: [ww.word() for _ in range(N)] for i in range(1, 3*N)}
    return f'''
    D = {D}
    expected = {func2(D)}
    return do_func2_tests(D, expected)
    '''

#print(genera_func2(15))

# D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
# print(func2(D)) # {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(L1, L2) che, ricevendo come argomento
due liste di stringhe L1 e L2, restituisce un dizionario che ha come
chiavi le stringhe presenti solo in L1 e come valori degli insiemi di
stringhe.

Ad ogni chiave di D corrisponde l'insieme delle stringhe di L2 non
presenti in L1 e che hanno la stessa lunghezza della stringa chiave.

Esempio:
L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
risultato = {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}
'''

def func3(L1, L2):
    ## Scrivi qui il tuo codice
    pass
    return {s1: {s2 for s2 in set(L2) - set(L1) if len(s2) == len(s1)} for s1 in set(L1) - set(L2)}

def genera_func3(N):
    import wonderwords, random
    ww = wonderwords.RandomWord()
    common =  [ww.word() for _ in range(N)]
    L1 = [ww.word() for _ in range(N)] + common
    L2 = [ww.word() for _ in range(N)] + common
    random.shuffle(L1)
    random.shuffle(L2)
    return f'''
    L1 = {L1}
    L2 = {L2}
    expected = {func3(L1,L2)}
    '''

#print(genera_func3(20))

# L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
# L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
# print(func3(L1, L2)) # {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si definisca la funzione func4(file_input, file_output) che, ricevendo
come argomento il path di un file di testo file_input contenente
parole separate da spazi, tab e a capo, crea un file di testo
file_output e ritorna una tupla.

Il file in output deve contenere tutte le parole contenute nel file
indicato da file_input SENZA RIPETIZIONI e organizzate con le seguenti
regole:

- Le parole che iniziano con la stessa lettera, indipendentemente se
  maiuscola o minuscola, devono essere sulla stessa riga in ordine
  alfabetico decrescente, separate da uno spazio.

- Le righe devono essere ordinate in ordine alfabetico crescente
  rispetto alla prima parola di ogni riga.

La funzione torna il numero di parole lette dal file ed il numero
totale di caratteri letti dal file di input.

Esempio:
se il file di input contiene le 20 parole:
    casa cane gatto topo
    paperino ragno topo
    cane cip cip
    casa cane gatto topo
    paperino ragno topo
    cane cip cip
il risultato è un file di output contenente:
    cip casa cane
    gatto
    paperino
    ragno
    topo
e la funzione ritorna (20, 131)
"""

def func4(input_filename, output_filename):
    ## Scrivi qui il tuo codice
    pass
    with open(input_filename, 'r') as f:
        text = f.read()
        words = text.split()
    D = {}
    for w in set(words):
        iniziale = w[0].lower()
        D[iniziale] = D.get(iniziale, []) + [w]
    print(D)
    for k,v in D.items():
        D[k].sort(reverse=True)
    with open(output_filename, mode='w', encoding='utf8') as f:
        for k in sorted(D):
            f.write(' '.join(D[k]) + '\n')
    return len(words), len(text)

# print(func4('func4/in_0.txt', 'func4/out_0.txt')) # (20, 131)

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 punti

Si definisca la funzione func5(input_png, output_png, S) che,
ricevendo come argomento il path di un file .png input_png, e un
intero S, crea un file .png output_png che contiene l'immagine di
input, suddivisa in quadretti SxS, in cui ciascun quadretto è ruotato
in senso orario di 90°.

NOTA: se esistono quadretti che sbordano a destra o sotto, non devono
essere ruotati.

La funzione ritorna il numero di quadretti ruotati.

Esempio: se l'immagine input_png è func5/3cime.png e S=50, l'immagine
output_png sarà come func5/expected_3cime_50.png e la funzione tornerà
15.  
"""
import images

def func5(input_png, output_png, S):
    ## Scrivi qui il tuo codice
    pass
    img = images.load(input_png)
    W, H = len(img[0]), len(img)
    img2 = [[img[y][x] for x in range(W)] for y in range(H)]
    N = 0
    for X in range(0, W, S):
        if X + S >= W: continue
        for Y in range(0, H, S):
            if Y + S >= H: continue
            N += 1
            for x in range(S):
                for y in range(S):
                    img2[Y+y][X+x] = img[Y+S-x-1][X+y]
    images.save(img2, output_png)
    return N

# print(func5('func5/in_3cime.png', 'func5/out_3cime_50.png', 50)) # 15
# print(func5('func5/in_3cime.png', 'func5/out_3cime_13.png', 13)) # 294

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Define the function ex1(string, l), recursive or using recursive functions
or methods, that takes as input a string and an integer l and returns
the set with all the possible anagrams of length l without any double
character that can be built with the characters in string.
If l is bigger than the length of the string, the returned set is empty.

Example:
    ex1('aabca', 4) should return the set
    {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}

"""
import os

def ex1(string, l):
    ## Scrivi qui il tuo codice
    pass
    if len(string)==0: return set()
    if l == 1:         return set(string)
    risultato = set()
    for i in range(len(string)):
        c = string[i]
        resto = string[:i]+string[i+1:]
        for s in ex1(resto, l-1):
            if c != s[0]:
                risultato.add(c+s)
    return risultato

# print(ex1('aabca', 4)) # {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}
# print(ex1('aabca', 5)) # {'abaca', 'acaba'}

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 points

Define a function ex2(root), recursive or using recursive functions
or methods, that takes as input a tree with int values, instance of
the tree.BinaryTree class.
The function has to modify the tree in place so that every node with
two childs has the left child bigger than the right one. The exchange
has to swap the whole trees, not only the values.
The function has to return the height of the tree. 

If the input tree is:

               6
              / \
             5   3
            /   / \
           4   10  6
              /   / \
             7   8  1
             
the function modifies it in this way:

                6
              /   \
             3     5
            / \   /
           6  10  4
          / \  /  
         1  8 7   
                 
The function returns the value 4
"""
import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass
    if root is None: return 0
    if not root.left is None and not root.right is None and root.left.value > root.right.value:
        root.left, root.right = root.right, root.left
    return max(ex2(root.left), ex2(root.right)) + 1

T = tree.BinaryTree.fromList([6, [5, None, [4, None, None] ], [3, [10, [7, None, None], None],
                                                               [6, [8, None, None], [1, None, None]]]])
# print(T)
# print(ex2(T))
# print(T)
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER

To pass the exam you must:
    - solve at least 3 exercises of type func AND;
    - solve at least 1 exercise of type ex (recursive problem) AND;
    - obtain a score greater than or equal to 18

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "A"
surname = "S"
student_id = "000"


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
def contavocali(s):
    return sum(s.lower().count(i) for i in 'aeiou')
        
def func1(L):
    ## Scrivi qui il tuo codice
    pass
    return sorted([(len(s), contavocali(s)) for s in L], key=lambda x: (-x[1], x[0]))

L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
print(func1(L)) # [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]


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

# D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
# print(func2(D)) # {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca la funzione func3(L1, L2) che, ricevendo come argomento
due liste di stringhe L1 e L2, restituisce un dizionario che ha come
chiavi le stringhe presenti solo in L1 e come valori degli insiemi di
stringhe.  le stringhe presenti solo in L2.

Ad ogni chiave di D corrisponde l'insieme delle stringhe di L2 non
presenti in L1 e che hanno la stessa lunghezza della stringa chiave.

Esempio:
L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
risultato = {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}
'''

def func3(L1, L2):
    ## Scrivi qui il tuo codice
    chiavi = set(L1) - set(L2)
    valori = set(L2) - set(L1)
    return {k:{v for v in valori if len(v)==len(k)} for k in chiavi}


L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
print(func3(L1, L2)) # {'elefante': {'paperino'}, 'oca': {'cip'}, 'casa': {'topo'}}

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
    with open(input_filename) as f:
        text = f.read()
    words = text.split()
    d = {l[0].lower():set() for l in words}
    for w in words:
        d[w[0].lower()].add(w)
    with open(output_filename, 'w') as f:
        for k in sorted(d.keys()):
            print(" ".join(sorted(d[k], reverse=True)), file=f)
    return len(words), len(text)
        
print(func4('func4/in_0.txt', 'func4/out_0.txt')) # (20, 131)
# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 marks

Let us define the function func5(input_png, output_png, S) which,
receiving as an argument the path to a .png file input_png,
and an integer S, creates an output png file output_png containing
the input image, split into SxS squares, in which each 
square is rotated clockwise by 90°, respect to the input image.
Note: If there are squares that overhang to the right or below,
they should not be rotated.

The function returns the number of rotated squares.

For Example:
given the input image func5/3cime.png and S=50,
the output image is the same as in func5/3cime_expected.png
and the function returns 15.
"""
import images

def rotate_square(im, x, y, S):
    new_square = [[0]*S for _ in range(S)]
    for j, row in enumerate(new_square):
        for i, pix in enumerate(row):
            new_square[i][j] = im[x+S-1-j][y+i]
    for j, row in enumerate(new_square):
        for i, pix in enumerate(row):
            im[x+j][y+i] = new_square[j][i]

def func5(input_png, output_png, S):
    ## Write your code here
    pass
    im = images.load(input_png)
    conta = 0
    for i in range(0, len(im)- S, S):
        for j in range(0, len(im[0])-S, S):
            rotate_square(im, i, j, S)
            conta += 1
    images.save(im, output_png)
    return conta

# print(func5('func5/in_3cime.png', 'func5/3cime-rotated-50.png', 50)) # 15
# print(func5('func5/3cime.png', 'func5/3cime-rotated-13.png', 13)) # 294
# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

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
    if len(string) < l:
        return set()
    if l == 1:
        return set(string)
    anagrams = set()
    for i, c in enumerate(string):
        partial = ex1(string[:i]+string[i+1:], l-1)
        for p in partial:
            if c!=p[0]:
                anagrams.add(c+p)
    return anagrams
    
    
    ## Write your code here
    pass
print(ex1('aabca', 4))

# %% ----------------------------------- EX.2 ------------------------- #
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
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    m = max(ex2(root.left), ex2(root.right))
    if root.left is not None and root.right is not None:
        if root.left.value > root.right.value:
            root.left, root.right = root.right, root.left
    return m+1
        
T = tree.BinaryTree.fromList([6, [5, None, [4, None, None] ], [3, [10, [7, None, None], None],
                                                               [6, [8, None, None], [1, None, None]]]])
print(ex2(T))
print(T)


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

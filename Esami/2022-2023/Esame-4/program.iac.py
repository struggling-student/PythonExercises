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
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "I"
cognome    = "M"
matricola  = "1"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(a_dict, word) che prende in ingresso un
dizionario 'a_dict' e una parola 'word'. Ogni chiave del dizionario è
una stringa che ha un'altra stringa come valore. La funzione deve
rimuovere dal dizionario tutti quelle chiavi che hanno come valore una
stringa che contenga 'word'.  La funzione restituisce il numero di
chiavi rimosse dal dizionario 'a_dict'.

Esempio: se a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
  l'invocazione di func1(a, 'b') deve restituire 2 e
  a_dict deve risultare modificato in {'c': ['a', 'c']}

'''
def func1(a_dict, word):
    N = len(a_dict)
    [a_dict.pop(k) for k in list(a_dict.keys()) if word in a_dict[k]]   
    return N - len(a_dict)



# a = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
# print(func1(a, 'b'))
# print(a)
# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(a_string) che prende in ingresso una
stringa 'a_string' e restituisce un'altra stringa. La nuova stringa ha
tutte le lettere della stringa in input ripetute una volta sola e in
ordine alfabetico inverso.

Esempio: se a_string='welcome' l'invocazione di func2(a_string) dovrà
         restituire la stringa 'womlec'
'''

def func2(a_string):
    return ''.join(sorted(set(a_string), reverse=True))

# print(func2('welcome'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe con lo stesso numero di elementi e
restituisce una nuova lista composta dalle stringhe ottenute
concatenando:
 - la prima stringa della seconda lista con l'ultima stringa della
   prima lista,
 - la seconda stringa della prima lista con la penultima della seconda
   lista,
 - e così via.
La lista risultante deve essere ordinata per numero di caratteri
crescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['so', 'sin', 'vas', 'rin', 'vul']  e
            string_list2=['cane', 'casai', 'to', 'cero', 'sia']
         l'invocazione di func3(string_list1, string_list2) dovrà restituire
         la lista ['sosia','vasto','sincero','vulcane','rincasai']
'''


def func3(string_list1, string_list2):
    return sorted(map(lambda a, b: a+b, reversed(string_list1), string_list2),
                  key=lambda S: (len(S), S))

# string_list1=['so', 'sin', 'vas', 'rin', 'vul']
# string_list2=['cane', 'casai', 'to', 'cero', 'sia']
# print(func3(string_list1, string_list2) )

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorso a due file.  All'interno del file indicato da 'input_file'
sono presenti su una sola riga una serie di parole (composte da
caratteri alfabetici) separate da virgole, spazi, punti e virgole e da
punti.
La funzione deve individuare tutte le parole contenute nel file
indicate da 'input_file' e scriverle all'interno di un nuovo file
indicato da 'output_file'.  Le parole devono essere scritte
all'interno del file su una sola riga terminata dal carattere di
a capo, separate da uno spazio e con il seguente ordine:
    - numero di caratteri crescente,
    - in caso di parità, in ordine alfabetico, indipendentemente da
      maiuscole e minuscole
    - in caso di parole identiche, in ordine lessicografico.
La funzione deve restituire il numero di parole scritte nel file in
output.

Esempio: se il contenuto del file 'input_file' è il seguente
Dog,cat,dog;Cat.bird car

l'invocazione di func4('input_file', 'output_file') dovrà scrivere nel
file 'output_file' la seguente riga
car Cat cat Dog dog bird

e ritornare il valore 6.
"""


def func4(input_file, output_file):
    with open(input_file) as fr, open(output_file, mode='w') as fw:
        words = fr.read().translate(str.maketrans(', ;.',' '*4)).split()
        print(*sorted(words, key=lambda S: (len(S), S.upper(), S)), sep=' ')
    return len(words)


# print(func4('func4_test1.txt','func4_out1.txt'))
# print(func4('func4_test2.txt','func4_out2.txt'))
# print(func4('func4_test3.txt','func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata dal 'input_pngfile' contiene una serie di punti di
diversi bianchi su uno sfondo nero. La funzione deve individuare tutti
i rettangoli definiti da quattro pixel bianchi che possono essere
considerati gli spigoli di tali rettangoli.

Si può assumere che:
    - ogni riga ha al più due punti bianchi e
    - ogni colonna ha al più due punti bianchi.

La funzione deve ritornare una lista contenente l'area di tutti i rettangoli
individuati nell'immagine, ordinati per dimensione crescente.

Esempio: nell'immagine del file func5_test1.png ci sono gli spigoli del
         rettangolo (5,5),(5,45),(45,5),(45,45) con area 861
         e del rettangolo (10,10),(10,20),(20,10),(20,20) con area 121
         e c'è un pixel in (15,35), per cui l'invocazione di
         func5('func5_test1.png') deve restituire la lista [121,861]

"""

import images


def find_rect(im, x, y, h, w, white=(255,)*3):
    # LEFT
    for ix in range(x+1, w):
        if im[y][ix] == white:
            break
    else:
        return False
    # DOWN
    for iy in range(y+1, h):
        if im[iy][x] == white:
            break
    else:
        return False
    if im[iy][ix] == white:
        im[y][x] = im[iy][x] = im[y][ix] = im[iy][ix] = (0,)*3
        return (ix-x+1)*(iy-y+1)
    else:
        return False


def func5(input_pngfile):
    im = images.load(input_pngfile)
    h, w = len(im), len(im[0])
    areas = []
    for y, row in enumerate(im):
        for x, pix in enumerate(row):
            if pix == (255,)*3:
                if rect := find_rect(im, x, y, h, w):
                    areas.append(rect)
    return sorted(areas)

#print(func5('func5_test1.png'))
#print(func5('func5_test2.png'))
#print(func5('func5_test3.png'))
#print(func5('func5_test4.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.
La funzione deve explorare ricorsivamente l'albero delle directory con
radice in 'directory' e restituire un dizionario.
Le chiavi del dizionario sono i percorsi delle sotto-directory di
'directory', sottoforma di stringa.
Il valore della chiave di una directory è un set di stringhe con i nomi
di file '.txt' nella directory in cui il primo carattere è uguale all'ultimo.
Se una directory non contiene nessun file .txt con tale caratteristica,
allora quella directory non appare nel dizionario.

Se la funzione e' chiamata su 'ex1/A', ritorna:

{'ex1/A/B': {'b.txt'}, 'ex1/A/C': {'c.txt'}}

NOTA: e' proibito usare la funzione os.walk. Si possono usare:
  os.listdir, os.path.isfile, os.path.exists, etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.  """

import os


def issame(fullp):
    with open(fullp) as fr:
        S = fr.read()
    return True if S[0] == S[-1] else False

    
def ex1(root):
    out = {}
    for item in os.listdir(root):
        fullp = root + '/' + item
        if os.path.isdir(fullp):
            out.update(ex1(fullp))
        elif item.endswith('.txt') and issame(fullp):
            out[root] = out.get(root, set()) | {item}
    return out
            

# print(ex1('ex1/A'))
# print(ex1('ex1/B'))
# print(ex1('ex1'))
# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che riceve in ingresso la radice di
un albero binario, come definito nella classe `BinaryTree` del modulo
tree.py.  L'albero in ingresso ha delle stringhe come valori. La
funzione deve restituire la stringa risultante dalla concatenazione di
tutti i valori associati ai nodi dell'albero con la seguente regola:
  - la concatenazione avviene con l'ordine LNR se il nodo si trova
    in un livello pari
  - con l'ordine RNL se il nodo è in un livello dispari
dove L è il sottoalbero sinistro, N il nodo e R il sottoalbero destro.
La radice si assume a livello 0.

Esempio:

        ______A______                        ______A______
       |             |                      |             |
       B__        ___C___                __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F             _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                                      H   I      J  K   L   M   N

  Se l'albero è quello di sinistra, la funzione deve restituire il
  valore DBAFCE.

 Se l'albero è quello di destra, la funzione deve restituire il valore
   EJBHDIAMGNCKFL

  """


def ex2(root, level=0):
    L = ex2(root.left, level+1) if root.left else ''
    R = ex2(root.right, level+1) if root.right else ''
    out = [L, root.value, R]
    return ''.join(out) if level % 2 == 0 else ''.join(reversed(out))



# from tree import BinaryTree
# root = BinaryTree.fromList(['A', ['B',[],['D',[],[]]], ['C', ['E',[],[]], ['F',[],[]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',[],[]],['I',[],[]]],['E',[],['J',[],[]]]], ['C', ['F',['K',[],[]],['L',[],[]]], ['G',['M',[],[]],['N',[],[]]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',['L',[],[]],[]],[]],['E',[],['I',[],[]]]],['C', ['F',['J',[],[]],[]],['G',[],['K',[],['M',[],[]]]]]])
# print(ex2(root))
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da eseguire PRIMA:
 1) Salva questo file come program.py
 2) Assegna le variabili qui sotto con il tuo
    NOME, COGNOME e NUMERO DI MATRICOLA
 3) Quando le tue funzioni sono pronte, salva il file nella finestra per la
    consegna.

IMPORTANTE: imposta DEBUG = True in `grade.py` per migliorare il debugging; ma
ricorda che la ricorsione è testata (e valutata) solo se DEBUG = False
"""

nome = "NOE"
cognome = "OGNOME"
matricola = "ATRICOLA"



# %% ----------------------------------- FUNC1 ------------------------- #

'''func1: 2 punti
Definisci la funzione func1(L1, L2) che riceve due liste di numeri. La funzione
deve confrontare le coppie gli elementi nella stessa posizione delle due liste 
ignorando il segno e restituire una nuova lista in cui sono presenti i numeri
minori, con il segno. Se le liste hanno un numero di elementi diverso, la lista
ritornata ha lo stesso numero di elementi della lista più corta.


Esempi:
    func1([-2,3,4,-5],[1,-2,6]) ritorna [1,-2,4]
    func1([(-1,4,5,2,0,15], [4,6,0,-16,3,1,1,5,3]) ritorna [-1, 4, 0, 2, 0, 1]

'''
def func1(L1, L2):
    res = []
    for a in range(min(len(L1), len(L2))):
        if abs(L1[a]) < abs(L2[a]):
            res.append(L1[a])
        else:
            res.append(L2[a])
    return res
func1([-2,3,4,-5],[1,-2,6])
func1([-1,4,5,2,0,15], [4,6,0,-16,3,1,1,5,3]) 
       
# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 2 punti
Definisci la funzione func2(words) che riceve un set di stringhe di caratteri
alfabetici e che ritorna un dizionario. Il dizionario ritornato ha degli
interi per chiavi e per valori i set di parole che contengono un numero
di consonanti pari alla chiave corrispondente.

    Esempio:
        words = {"yak", "Gollum", "Batman", "AI", "star"}
        func2(words) ritorna {4: {'Batman', 'Gollum'}, 2: {'yak'}, 3: {'star'}, 0: {'AI'}}

'''

def consonants(w):
    vw = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for l in w:
        if not l.lower() in vw:
            count += 1
    return count

def func2(words):
    res = dict()
    for w in words:
        c = consonants(w)
        if c in res:
            res[c].add(w)
        else:
            res[c] = {w}
    return res
        

words = {"yak", "Gollum", "Batman", "AI", "star"}
func2(words)

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 4 punti
Implementa la funzione func3(sales_log_path, report_path) che elabora
legge il file indicato dalla stringa sales_log_path e genera un nuovo file
indicato dalla stringa report_path. Il file sales_log_path contiene righe
nel formato prodotto:costo_unitario:quantità, che indicano le vendite
di un certo prodotto indicando il nome del prodotto, il suo costo unitario e
le quantità vendute. Le righe di uno stesso prodotto possono ripetersi,
anche se con costi diversi.
La funzione deve calcolare e ritornare il ricavo totale dalla vendita di tutti
i prodotti e creare un file di report che contiene righe nel formato
prodotto:guadagno_totale_prodotto:quantità_totale_venduta, ordinate per ordine
alfabetico del prodotto.

'''
def func3(sales_log_path, report_path):
    gain = 0
    f = open(sales_log_path, 'r', encoding='utf-8')
    ll = f.readlines()
    f.close()
    res = dict()
    for l in ll:
        tt = l.split(':')
        if tt[0] not in res:
            res[tt[0]] = [int(tt[2]) * float(tt[1]), int(tt[2])]
        else:
            res[tt[0]] = [int(tt[2]) * float(tt[1]) + res[tt[0]][0], int(tt[2]) + res[tt[0]][1]]
    f = open(report_path, 'w', encoding='utf-8')
    for p in sorted(list(res)):
        f.write(p + ':' + str(res[p][1])+ ':' + str(res[p][0]) + '\n')
        gain += res[p][0]
    f.close()
    return gain

# func3('func3/sales01.txt', 'func3/my01.txt')

# %% ----------------------------------- FUNC4 ------------------------- #
''' Func 4: 4 punti
Definisci func4(words_file, outfile) che riceve due stringhe come input.
La funzione deve leggere il contenuto del file indicato dalla stringa
words_file, che contiene delle stringhe alfanumeriche separate da spazi, 
tabulazioni o accapi. La funzione deve poi scrivere in un nuovo file
indicato dalla stringa outfile tutte le stringhe lette, raggruppate su
righe diverse per primo carattere, separate da uno spazio e ordinate nel
seguente ordine:
    - per lunghezza decrescente di stringa
    - in caso di pari lunghezza, per numero di caratteri numerici decrescente
    - in caso di parità, in ordine alfabetico.
Le righe sono ordinate in ordine alfabetico.
La funzione ritorna il numero totale di stringhe lette.

Esempio: se il file in input contiene le stringhe 'a4er', '4ever', '40er', 'forty', '007'
  func4 ritorna il valore 5 e il file creato avrà il seguente contenuto:
007
4ever 40er
a4er
forty
'''
def my_key(x):
    counter = 0
    for c in x:
        if c.isdigit():
            counter += 1
    return (-len(x), -counter, x)

def func4(words_file, outfile):
    f = open(words_file, 'r', encoding='utf-8')
    ll = f.readlines()
    f.close()
    res = dict()
    counter = 0
    for l in ll:
        l = l.strip()
        l = l.replace('\t', ' ')
        tt = l.split()
        for w in tt:
            counter += 1
            if w[0] not in res:
                res[w[0]] = [w]
            else:
                res[w[0]].append(w)
    for l in res:
        res[l] = sorted(res[l], key=my_key)
    f = open(outfile, 'w', encoding='utf-8')
    for p in sorted(list(res)):
        f.write(' '.join(res[p]) + '\n')
    f.close
    return counter

# func4('func4/words01.txt', 'func4/my01.txt')

# print(func3(75, 'outf'))

# %% ----------------------------------- FUNC5 ------------------------- #
""" Func 5: 8 punti
Definisci la funzione func5(minr, inputfile_png, outputfile_png) che riceve come input
un valore intero minr, due stringhe che rappresentano i nomi di due file png.
La funzione deve leggere l'immagine memorizzata nel file inputfile_png, che è
un'immagine nera con pixel di diversi colori.
La funzione deve scrivere in un nuovo file outputfile_png l'immagine ottenuta
copiando dall'immagine inputfile_png solo i pixel isolati che hanno un colore la cui
prima componente (Red) è maggiore o uguale del valore minr. Un pixel si dice isolato
se ha soltanto pixel neri adiacenti in verticale e orizzontale.
    
Infine, la funzione deve restituire il numero di pixel copiati nell'immagine
di output.
Ricorda di usare le funzioni images.load e images.save per caricare e
salvare immagini da/in un file.
"""
import images

def isolated(img, x, y):
    black = (0, 0, 0)
    if x > 0:
        if img[y][x - 1] != black:
            return False
    if x < (len(img[0]) - 1):
        if img[y][x + 1] != black:
            return False
    if y > 0:
        if img[y - 1][x] != black:
            return False
    if y < (len(img) - 1):
        if img[y + 1][x] != black:
            return False
    return True

def func5(minr, inputfile_png, outputfile_png):
    img = images.load(inputfile_png)
    res = []
    counter = 0
    for y in range(len(img)):
        rrow = []
        for x in range(len(img[0])):
            if img[y][x] != (0, 0, 0) and isolated(img, x, y) and img[y][x][0] >= minr:
                counter += 1
                rrow.append(img[y][x])
            else:
                rrow.append((0, 0, 0))
        res.append(rrow)
    images.save(res, outputfile_png)
    return counter

# print(func5(-1, 'func5/img_3.png', 'func5/my_0.png'))

        
                

# %% ----------------------------------- EX1 ------------------------- #
""" Ex1: 6 punti

Il peso di un nodo di un albero corrisponde al valore del nodo moltiplicato
per la sua profondità.
Scrivi la funzione ex1(root) ricorsiva o che usa helper ricorsivi
che prende un'istanza di un nodo BinaryTree "root", in cui
ogni nodo ha come attributi value (float), left (BinaryTree o None) e right (BinaryTree o None),
e restituisce una coppia (min, max) corrispondente al peso minimo e massimo
dei nodi dell'albero, arrotondati alla seconda cifra decimale.

Considerare la profondità della radice pari a 1.

Ad esempio

profondità      root
       1         20
                /  \ 
       2       10   5
              /  \
       3    0.5  0.2

  ex1(root) ritorna la coppia (0.6, 20)    

"""
from tree import BinaryTree



def helper(root, depth):
    m, M = round(root.value * depth, 1), round(root.value * depth, 1)
    if root.left is not None:
        sm, sM = helper(root.left, depth + 1)
        m, M = min(m, sm), max(M, sM)
    if root.right is not None:
        sm, sM = helper(root.right, depth + 1)
        m, M = min(m, sm), max(M, sM)
    return m, M

def ex1(root):
    return helper(root, 1)

# root = BinaryTree.fromList([20, [10, [0.5, None, None], [0.2, None, None]], [5, None, None]])
# print(ex1(root))
# root = BinaryTree.fromList([4, [25, [-4, None, None], [-1, None, None]], [11, [11, [8, [10, None, None], [24, [-4, None, None], None]], None], [-5, None, None]]])
# print(ex1(root))
# root = BinaryTree.fromList([23, [30, None, None], [3, [20, None, None], [-1, None, None]]])
# print(ex1(root))
# root = BinaryTree.fromList([27, [22, [-6, [10, None, [16, None, None]], [17, None, None]], [1, [13, [-9, [-3, None, None], None], [-2, None, [24, None, None]]], [5, None, None]]], [23, [22, [21, None, None], None], [10, None, None]]])
# print(ex1(root))
# %% ----------------------------------- EX2 ------------------------- #
""" Ex2: 6 punti
    
Definisci la funzione ex2(lista) ricorsiva o che usa un'altra funzione o
metodo ricorsivi che riceve in ingresso una lista che può avere come elementi:
    - interi
    - stringhe
    - un'altra lista con le stesse caratteristiche.
La funzione deve ritornare la stringa ottenuta concatenando tutti i caratteri
in contenuti in essa e in tutte le sue liste, a qualsiasi livello e nello
stesso ordine in cui compaiono.

Esempio se la lista è la seguente:
    lista = [42, 'a', 
             [7, 'b', [100, 'c']], 
             9,  'z', ['x', 24]
             ]
    la funzione restituisce la stringa 'abczx'.
"""

def ex2(lista):
    res = ''
    for item in lista:
        if type(item) == str:
            res += item
        if type(item) == list:
            res += ex2(item)
    return res

# lista = [42, 'a', [7, 'b', [100, 'c']], 9, 'z', ['x', 24]]
# print(ex2(lista))

# directory_structure = ["secret_vault",["data.txt", "sec_log"],[["backup", "sec_root"],"notes.txt"]]
# key = 'sec'
# print(ex2(directory_structure, key))
#
# directory_structure = ["secret_vault",["data.txt", "sec_log", ["insect.txt", "out_sector.jpg"]],["night.txt",["backup", "sec_root"],"notes.txt",[['insect', 'sectorial']],["one, two", "three", "four"]]]
# key = 'sec'
# print(ex2(directory_structure, key))
#
# directory_structure = ["secret_vault",["data.txt", "sec_log", ["insect.txt", "out_sector.jpg"]],["night.txt",["backup", [["sec_root"]]],"notes.txt",[['insect', 'sectorial']],["one, two", "three", "four"]]]
# key = 'sec_r'
# print(ex2(directory_structure, key))
#
# directory_structure = ["secret_vault",["data.txt", "sec_log", ["insect.txt", "out_sector.jpg"]],["night.txt",["backup", [["sec_root"]]],"notes.txt', 'office.exe', ['run', 'offline'],[['insect', 'sectorial']],["one, two", "three", "four"]]]
# key = 'o'
# print(ex2(directory_structure, key))
###########################################################################
# %% --------------------- MAIN ------------------------
if __name__ == '__main__':
    # i tuoi test vanno qui
    print('*'*50)
    print('Devi eseguire grade.py se vuoi fare il debug con il valutatore automatico.')
    print('Altrimenti puoi inserire qui il tuo codice per testare le funzioni ma devi scrivere i tuoi test')
    print('*'*50)

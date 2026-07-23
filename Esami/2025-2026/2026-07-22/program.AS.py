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

nome = "A"
cognome = "S"
matricola = "42"


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
    # Scrivi qui il tuo codice
    pass
    return [ X if abs(X) < abs(Y) else Y for X,Y in zip(L1,L2)]

# print(func1([-2,3,4,-5],[1,-2,6]))
#print(func1([-1,4,5,2,0,15], [4,6,0,-16,3,1,1,5,3]))
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

def func2(words):
    # Scrivi qui il tuo codice
    pass
    D = {}
    for w in words:
        N = len([ c for c in w if c not in 'aeiouAEIOU'])
        if N not in D:
            D[N] = set()
        D[N].add(w)
    return D

# words = {"yak", "Gollum", "Batman", "AI", "star"}
# print(func2(words))

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
prodotto:quantità_totale_venduta:guadagno_totale_prodotto, ordinate per ordine
alfabetico del prodotto.

'''
def func3(sales_log_path, report_path):
    # Scrivi qui il tuo codice
    pass
    GT = {}
    QT = {}
    S  = 0
    with open(sales_log_path) as FIN:
        for line in FIN:
            P, C, Q = line.split(':')
            C = float(C)
            Q = int(Q)
            S += C*Q
            if P in GT:
                GT[P] += C*Q
                QT[P] +=   Q
            else:
                GT[P]  = C*Q
                QT[P]  =   Q
    with open(report_path, mode='w', encoding='utf8') as FOUT:
        for P in sorted(GT):
            print(f"{P}:{QT[P]}:{GT[P]}", file=FOUT)
    return S
            
    

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
def func4(words_file, outfile):
    # Scrivi qui il tuo codice
    def criterio(word):
        return -len(word), -len([c for c in word if c.isdigit()]), word
    pass
    D = {}
    N = 0
    with open(words_file) as FIN:
        for w in FIN.read().split():
            if (p:=w[0]) not in D:
                D[p] = []
            D[p].append(w)
            N += 1
    for v in D.values():
        v.sort(key=criterio)
    with open(outfile, mode='w', encoding='utf8') as FOUT:
        for iniziale in sorted(D):
            print(' '.join(D[iniziale]), file=FOUT)
    return N

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
black = (0,0,0)

def da_copiare(img,x,y,W,H,soglia):
    pixel = img[y][x]
    return (pixel != black 
            and pixel[0]>=soglia 
            and (x==0   or img[y][x-1]==black)
            and (y==0   or img[y-1][x]==black)
            and (x==W-1 or img[y][x+1]==black)
            and (y==H-1 or img[y+1][x]==black))

def func5(minr, inputfile_png, outputfile_png):
    # Scrivi qui il tuo codice
    pass
    img = images.load(inputfile_png)
    W,H=len(img[0]),len(img)
    img2 = []
    N = 0
    for y,riga in enumerate(img):
        nuova = []
        for x,pixel in enumerate(riga):
            if da_copiare(img,x,y,W,H,minr):
                nuova.append(pixel)
                N += 1
            else:
                nuova.append(black)
        img2.append(nuova)
    images.save(img2,outputfile_png)
    return N
        
                

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

def ex1(root):
    # Scrivi qui il tuo codice
    pass
    return _ex1(root,1)

def _ex1(root,profondita):
    if root is None:
        return None, None
    m = M = round(root.value * profondita, 2)
    mL, ML = _ex1(root.left,profondita+1)
    mR, MR = _ex1(root.right,profondita+1)
    return min([x for x in [m,mL,mR] if x is not None]), max([x for x in [M,ML,MR] if x is not None]), 

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
    # Scrivi qui il tuo codice
    pass
    risultato = ''
    for x in lista:
        if type(x) == str:
            risultato += x
        elif type(x) == list:
            risultato += ex2(x)
    return risultato

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

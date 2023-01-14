#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "IACOPO"
cognome     = "MASI"
matricola   = "6969696969"

################################################################################
################################################################################
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

# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 punti
Si definisca la funzione ex1(triangles) che prende in input una
lista di triple di numeri positivi ed elimina dalla lista tutte
le triple che non possono essere un triangolo rettangolo. La
funzione deve ritornare il numero di triple eliminate dalla lista
triangles.  La lista triangles deve risultare modificata alla
fine dell'esecuzione di ex1.  Per valutare se un triangolo è
rettangolo si può usare il teorema di Pitagora, per cui la somma
dei quadrati costruiti sui cateti deve essere uguale al quadrato
costruito sull'ipotenusa.
Per i confronti, si usi la funzione di arrotondamento round(x,3).

Esempio: se triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)], la
                         funzione ex1(triangles) resituisce il
valore 3 e modifica la lista in modo che
triangles = [(3, 4, 5), (12, 36.05551, 34)].
"""


def is_tri_rect(T):
    Ts = sorted(T) # ipo is always the latest
    sum_cat_sq = round(Ts[0]**2 + Ts[1]**2, 3)
    ipo_sq = round(Ts[2]**2, 3)
    return sum_cat_sq == ipo_sq


def ex1(triangles):
    count, N = 0, len(triangles)
    while count < len(triangles):
        if not is_tri_rect(triangles[count]):
            del triangles[count]
        else:
            count += 1
    return N - len(triangles)




# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex2: 8 punti
Si deve costruire un'immagine a partire da un'immagine nera con
dei punti colorati e un dizionario che associa ad alcuni colori
una tupla con esattamente due interi positivi, rappresentanti altezza e
larghezza, rispettivamente.  Si definisca la funzione ex2 che prende in 
input due stringhe (img_in e img_out, che rappresentano il nome di due
file) e un dizionario colors.  Il file indicato da img_in
contiene un'immagine PNG con sfondo nero e con alcuni punti
colorati. La funzione deve costruire per ogni punto colorato di
img_in un rettangolo in cui il punto è l'angolo superiore
sinistro e le cui dimensioni sono associate al colore del punto
nel dizionario colors. L'immagine con i rettangoli deve essere
salvata in formato PNG in un file con nome img_out.
La funzione deve ritornare il numero di rettangoli disegnati.

I rettangoli vanno disegnati nell'ordine dei punti nell'immagine,
considerando ogni punto come una tupla (riga, colonna): ad
esempio, prima il rettangolo per il punto (0,0), seguito
da quello per (0,100), seguito da (30,0). Attenzione: si deve
disegnare un rettangolo per ogni punto di un colore in colors,
pertanto anche se un punto viene coperti da un rettangolo di
un altro punto.

I rettangoli non possono superare i margini                                                                                                                                             
dell'immagine (ovvero, i rettangoli troppo larghi/alti vanno                                                                                                                            
tagliati).                                                                                                                                                                              
                                                                                                                                                                                        
Se il colore di un punto non è presente nel dizionario, quel                                                                                                                            
punto non dovrà diventare un rettangolo nell'immagine nuova,
ma dovrà essere presente anche nella nuova immagine (a meno
che non è ricoperto da un altro rettangolo).

img_in = 'ex2/immage01.png'
colors = {(100,0,0):(10,20), (0,100,0):(30,40), (0,0,100):(40,60)}
l'immagine da costruire è quella nel file ex2/expected01.png
"""

import images



def create_out(im_in, H, W, black):
    out, pts = [], []
    for y in range(H):
        row = []
        for x in range(W):
            col = im_in[y][x]
            if col != black:
                pts.append((y, x, col))
            row.append(col)
        out.append(row)
    return out, pts


def draw_rect(out, y, x, col, colors, Hmax, Wmax):
    drawn = False
    if col in colors:
        H, W = colors[col]
        # dimensions
        Wrect, Hrect = x+W, y+H
        # upper
        for xi in range(x, Wrect):
            out[y][xi] = col
            out[Hrect-1][xi] = col
        # left
        for yi in range(y, Hrect):
            out[yi][x] = col
            out[yi][Wrect-1] = col
        drawn = True
    return drawn
    

def ex2(img_in, img_out, colors):
    im_in = images.load(img_in)
    H, W, black = len(im_in), len(im_in[0]), (0, 0, 0)
    out, pts = create_out(im_in, H, W, black)
    drawn = 0
    for pt in pts:
        drawn += draw_rect(out, *pt, colors, H, W)
    images.save(out, img_out)
    return drawn

    
# %% ----------------------------------- EX.3 ----------------------------------- #
"""
ex3: 9 punti
Si definisca la funzione ricorsiva ex3 che prende una stringa directory
e una stringa namefile. La funzione deve cercare
ricorsivamente all'interno della directory indicata da directory e in tutte
le sotto-directory i file con nome uguale a namefile.  Tali file vanno
interpretati come file di testo che contengono soltanto stringhe
numeriche positive. I file hanno sempre lo stesso numero di stringhe numeriche.
La funzione deve ritornare una lista di interi ottenuta sommando le stringhe
numeriche dei file individuati, posizione per posizione.

Esempio: se vengono trovati soltanto due file e tali file contenengono
le sequenze "11 23 90" e "11 77 0", la funzione ex3 ritorna la lista [22, 100, 90].

Si suggerisce di usare le funzioni os.listdir, os.path.isfile e os.path.isdir.
e di NON usare la funzione os.join in Windows (usare la concatenazione fra stringhe
                                               con il carattere '/')
È proibito usare la funzione os.walk
"""

import os


def parse_file(filename):
    with open(filename, encoding='utf8') as fr:
        line = fr.readline()
    return [int(s) for s in line.rstrip().split()]


def sum_list(line, line2):
    if not line: return line2
    if not line2: return line
    return list(map(lambda a, b: a+b, line, line2))


def ex3(directory, namefile):
    items = os.listdir(directory)
    summed_list = []
    for item in items:
        full_path = directory + '/' + item
        if os.path.isfile(full_path) and item == namefile:
            sums = parse_file(full_path)
            summed_list = sum_list(summed_list, sums)
        elif os.path.isdir(full_path):
            summed = ex3(full_path, namefile)
            summed_list = sum_list(summed_list, summed)
        else:
            pass
    return summed_list



# %% ----------------------------------- EX.4 ----------------------------------- #


"""
Ex4: 6/9 punti
Si definisca una funzione ricorsiva (o che usa funzioni ricorsive) ex4
che prende un insieme strings di stringhe e un intero n e genera
ricorsivamente tutte le possibili stringhe che possono essere
costruite concatenando n stringhe di strings.  La funzione deve
ritornare tutte le stringhe costruite. La funzione può restituire
o un insieme con tutte le stringhe create, oppure una lista ordinata.
La lista è ordinata consideranto l'ordine decrescente della
lunghezza delle stringhe e, in caso di parità, l'ordine alfabetico.

Esempio: se strings={'a','b','c','de'}, la funzione ex4(strings, 2)
ritorna l'insieme {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 punti)
oppure la lista ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 punti)
"""


def create(strings, n, prt_s='', cat=0):
    if cat == n:
        return {prt_s}
    out = set()
    for stri in strings:
        new_set = strings - {stri}
        rez = create(new_set, n, prt_s+stri, cat=cat+1)
        out |= rez
    return out


def ex4(strings, n):
    out = create(strings, n)
    return sorted(out, key=lambda S: (-len(S), S))

###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test

    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

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
Si definisca la funzione ex1(triangles) che prende in input una lista
di triple di numeri positivi ed elimina dalla lista tutte le triple
che non possono essere i lati di un triangolo rettangolo. Ogni numero della
tripla puo' essere o cateto o ipotenusa e non vi è alcun ordine
prestabilito.  La funzione deve ritornare il numero di triple
eliminate dalla lista triangles. La lista triangles deve risultare
modificata in-place alla fine dell'esecuzione di ex1. Per valutare se un
triangolo è rettangolo si può usare il teorema di Pitagora, per cui la
somma dei quadrati costruiti sui cateti deve essere uguale al quadrato
costruito sull'ipotenusa.
Per i confronti, si usi la funzione di arrotondamento round(x,3).

Esempio: se triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         la funzione ex1(triangles) resituisce il valore 3 e modifica la lista
         in modo che
            triangles = [(3, 4, 5), (12, 36.05551, 34)].

Infatti, considerando il risultato atteso triangles = [(3, 4, 5), (12, 36.05551, 34)]
vale:
def build_triangle_list(n):
    return [build_triangles(random.randint(3,10), random.randint(2,5)) for _ in range(n)]

| tripla             | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""

def build_triangles(mu, sigma):
    a = random.gauss(mu, sigma)
    b = random.gauss(mu, sigma)
    if a<=0 or b<=0:
        return build_triangles(mu, sigma)
    a = round(a, 1)
    b = round(b, 1)
    c = round((a**2 + b**2)**(0.5), 5)
    l = [a,b,c]
    random.shuffle(l)
    return tuple(l)
    
def check(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    return round(a**2+b**2, 3) == round(c**2, 3)

def ex1(triangles):
    count = len(triangles)
    for i in range(len(triangles)-1, -1, -1):
        if not check(*triangles[i]):
            triangles.pop(i)
    return count - len(triangles)

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex2: 8 punti
Si deve costruire un'immagine a partire da un'immagine nera con dei
punti colorati e un dizionario che associa ad alcuni colori una tupla
con esattamente due interi positivi, rappresentanti altezza e
larghezza, rispettivamente.

Si definisca la funzione ex2 che prende in input due stringhe (img_in
e img_out, che rappresentano il nome di due file) e un dizionario
colors.  Il file indicato da img_in contiene un'immagine PNG con
sfondo nero e con alcuni punti colorati. La funzione deve costruire
per ogni punto colorato di img_in un rettangolo in cui il punto è
l'angolo superiore sinistro e le cui dimensioni sono associate al
colore del punto nel dizionario colors. L'immagine con i rettangoli
deve essere salvata in formato PNG in un file con nome img_out.  La
funzione deve ritornare il numero di rettangoli disegnati.

I rettangoli vanno disegnati nell'ordine dei punti nell'immagine,
considerando ogni punto come una tupla (riga, colonna): ad esempio,
prima il rettangolo per il punto (0,0), seguito da quello per (0,100),
seguito da (30,0).
ATTENZIONE: si deve disegnare un rettangolo PER OGNI punto di un colore
in colors, ANCHE SE un punto viene coperto da un rettangolo di un altro punto.

Si può assumere che le dimensioni in colors richiedono di disegnare
rettangoli con tutti i punti entro i margini dell'immagine (ovvero
i rettangoli non superano mai i margini dell'immagine).

Se il colore di un punto non è presente nel dizionario, quel punto non
dovrà diventare un rettangolo nell'immagine nuova, ma dovrà essere presente
anche nella nuova immagine—–a meno che non è ricoperto da un altro rettangolo.

img_in = 'ex2/image01.png'
colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}
l'immagine da costruire è quella nel file ex2/expected01.png

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""

import images
def build_image01():
    im = [[(0,0,0)]*100 for _ in range(100)]
    im[10][10]=(255,0,0)
    im[19][29]=(0,255,0)
    im[90][90]=(255,0,255)
    images.save(im, 'ex2/image01.png')
    colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}
    ex2('ex2/image01.png', 'ex2/expected01.png', colors)
    

def build_image02():
    im = [[(0,0,0)]*100 for _ in range(100)]
    for i in range(0,50):
        im[i][i]=(i*5,i*5,i*5)
    images.save(im, 'ex2/image02.png')
    colors = {(i*5,i*5,i*5):(100-2*i,100-2*i) for i in range(0,50)}
    ex2('ex2/image02.png', 'ex2/expected02.png', colors)
    
    
def build_image03():
    POINTS = 20
    H = W = 500
    RATIO = 5 # how many points should be without a color
    from random import randint
    random.seed('12092022')

    im = [[(0,0,0)]*W for _ in range(H)]
    
    points = {(randint(0,H-1), randint(0,W-1)): (randint(0,255), randint(0,255), randint(0,255)) for _ in range(POINTS) }
    
    colors = {}
    for point, color in points.items():
        colors[color] = (randint(2, H-point[0]), randint(2, W-point[1]))
        im[point[0]][point[1]] = color

    print(points)
    images.save(im, 'ex2/image03.png')
    print('Colors before popitem:', colors)
    for i in range(randint(0,POINTS//RATIO)):
        c = colors.popitem()
        print('removed point/color:', [(point,color) for point, color in points.items() if color == c[0]])
    print('Colors after popitem:', colors)
    ex2('ex2/image03.png', 'ex2/expected03.png', colors)
    

def draw(imm, riga, col, color, colors):
    dimensioni = colors.get(color, None)
    if not dimensioni:
        return 0
    alt, largh = dimensioni
    # for i in range(col, min(len(imm[0]), col+largh)):
    #     imm[riga][i] = color
    #     if riga+alt-1 < len(imm):
    #         imm[riga+alt-1][i] = color
    # for j in range(riga, min(len(imm), riga+alt)):
    #     imm[j][col] = color
    #     if col+largh-1 < len(imm[0]):
    #         imm[j][col+largh-1] = color
    for i in range(col, col+largh):
        imm[riga][i] = color
        imm[riga+alt-1][i] = color
    for j in range(riga, riga+alt):
        imm[j][col] = color
        imm[j][col+largh-1] = color
    return 1

def ex2(img_in, img_out, colors):
    # INSERISCI QUI IL TUO CODICE
    imm = images.load(img_in)
    drawn = 0
    todraw = []
    for riga in range(len(imm)):
        for col in range(len(imm[0])):
            if imm[riga][col] != (0,0,0):
                todraw.append((riga, col, imm[riga][col]))
    for point in todraw:
        riga, col, color = point
        drawn += draw(imm, riga, col, color, colors)
    images.save(imm, img_out)
    return drawn

    
# %% ----------------------------------- EX.3 ----------------------------------- #
"""
Ex3: 9 punti
Si definisca la funzione ricorsiva ex3 che prende una stringa
directory e una stringa namefile. La funzione deve cercare
ricorsivamente all'interno della directory indicata da directory e in
tutte le sotto-directory i file con nome uguale a namefile.  Tali file
vanno interpretati come file di testo che contengono soltanto stringhe
numeriche positive. I file con lo stesso namefile hanno sempre lo
stesso numero di stringhe numeriche.  La funzione deve ritornare una
lista di interi ottenuta sommando le stringhe numeriche dei file
individuati, posizione per posizione.

Esempio: se vengono trovati soltanto due file di nome namefile e tali
file contenengono le sequenze "11 23 90" e "11 77 0", la funzione ex3
ritorna la lista [22, 100, 90].

Si suggerisce di usare le funzioni os.listdir, os.path.isfile e
os.path.isdir.  e di NON usare la funzione os.join in Windows (usare
la concatenazione fra stringhe con il carattere '/')

È proibito usare la funzione os.walk

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""

import os


def ex3(directory, namefile):
    res = []
    for f in os.listdir(directory):
        fname = directory+'/'+f
        if os.path.isdir(fname):
            l = ex3(fname, namefile)
            if res and l:
                res = [a+b for a,b in zip(res, l)]
            elif l:
                res = l
        if os.path.isfile(fname) and f==namefile:
            with open(fname) as f:
                l = list(map(int, f.read().split() ))
            if res:
                res = [a+b for a,b in zip(res, l)]
            else:
                res = l
    return res

# %% ----------------------------------- EX.4 ----------------------------------- #
"""
Ex4: 6/9 punti
Si definisca una funzione ricorsiva (o che usa funzioni ricorsive)
ex4(strings, n) che prende un insieme strings di stringhe e un intero
n e genera ricorsivamente tutte le possibili stringhe che possono
essere costruite concatenando n stringhe di strings.  La funzione deve
ritornare tutte le stringhe costruite. La funzione può restituire o un
insieme con tutte le stringhe create (6 punti), oppure una lista
ordinata (9 punti).
La lista è ordinata consideranto l'ordine decrescente della lunghezza
delle stringhe e, in caso di parità, l'ordine alfabetico.

Esempio: se strings={'a','b','c','de'}, la funzione ex4(strings, 2)
ritorna l'insieme {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 punti)
oppure la lista ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 punti)
"""
def build(strings, n):
    if n == 1:
        return strings
    res = set()
    
    for string in strings:
        words = build(strings-{string}, n-1)
        for word in words:
            res.add(string+word)
    return res

def ex4(strings, n):
    # INSERISCI QUI IL TUO CODICE
    # return build(strings, n)
    return sorted(build(strings, n), key = lambda x: (-len(x), x))

###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    # build_image01()
    # build_image02()
    # build_image03()
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

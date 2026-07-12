#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""

nome        = "NOM"
cognome     = "COGOME"
matricola   = "MATRCOLA"

################################################################################
################################################################################
################################################################################

import tree
import images
import os

# %% ---------------------------------- FUNC1 ---------------------------------- #
"""Func 1: 2 punti

Scrivere una funzione func1(studenti) che riceve una lista di dizionari.
Ogni dizionario ha le seguenti chiavi:
  - 'name' (str): nome dello studente
  - 'scores' (list[int]): lista di voti
  - 'bonus' (int): punti bonus

La funzione deve calcolare per ogni studente:
    totale = sum(scores) + bonus

Restituire una lista di tuple (name, totale) ordinate per:
  1. totale decrescente
  2. se il totale è uguale, name in ordine alfabetico

Esempi:
    func1([
        {'name': 'Alice', 'scores': [18, 24], 'bonus': 3},
        {'name': 'Bob',   'scores': [30, 28], 'bonus': 0}
    ]) -> [('Bob', 58), ('Alice', 45)]

    func1([
        {'name': 'Zara', 'scores': [20], 'bonus': 5},
        {'name': 'Anna', 'scores': [20], 'bonus': 5}
    ]) -> [('Anna', 25), ('Zara', 25)]
"""

def func1(studenti):
    return sorted([(s['name'], sum(s['scores'])+s['bonus']) for s in studenti], key=lambda x: (-x[1], x[0]))

print(func1([
    {'name': 'Zara', 'scores': [20], 'bonus': 5},
    {'name': 'Anna', 'scores': [20], 'bonus': 5}
]))
print(func1([
    {'name': 'Alice', 'scores': [18, 24], 'bonus': 3},
    {'name': 'Bob',   'scores': [30, 28], 'bonus': 0}
]))
# %% ---------------------------------- FUNC2 ---------------------------------- #
"""Func 2: 2 punti

Scrivere una funzione func2(lista1, lista2) che riceve due liste di stringhe.
Restituire una lista ordinata (in ordine alfabetico) contenente, senza ripetizioni, 
tutte le stringhe che compaiono in UNA SOLA delle due liste (differenza simmetrica).

Esempi:
    func2(['a', 'b', 'c'], ['b', 'c', 'd']) -> ['a', 'd']
    func2(['x', 'y'], ['x', 'y']) -> []
    func2([], ['a', 'b']) -> ['a', 'b']
"""

def func2(lista1, lista2):
    return sorted(set(lista1)^set(lista2))

print(func2(['a', 'b', 'c'], ['b', 'c', 'd']))
print(func2(['x', 'y'], ['x', 'y']))
print(func2([], ['a', 'b']))
# %% ---------------------------------- FUNC3 ---------------------------------- #
"""Func 3: 2 punti

Scrivere una funzione func3(coppie) che riceve una lista di coppie
(parola, definizione), dove parola e definizione sono stringhe.

Costruire e restituire un dizionario che ha:
  - chiave: la prima lettera di ogni parola (resa minuscola) 
  - valore: la lista ordinata alfabeticamente delle chiavi (parole) la cui definizione
    contiene ALMENO 5 parole (separate da spazi)

Esempi:
    func3([
        ("cane", "animale domestico a quattro zampe"),
        ("gatto", "felino domestico"),
        ("casa", "edificio per abitare")
    ]) -> {'c': ['cane']}
    # "gatto" è escluso (la definizione ha solo 2 parole < 5)
    # "casa"  è escluso (la definizione ha solo 3 parole < 5)
    # "cane" ha la definizione con 5 parole -> è incluso sotto 'c'
"""

def func3(coppie):
    parole = [p for p,d in coppie if len(d.split())>=5]
    return {p[0].lower():sorted([x for x in parole if x[0]==p[0]]) for p in parole}

print(func3([
    ("cane", "animale domestico a quattro zampe"),
    ("gatto", "felino domestico"),
    ("casa", "edificio per abitare"),
    ('coscia', 'parte superiore della gamba vicino al busto'),
    ('occhio', 'organo dedicato alla vista presente in quasi tutti gli esseri viventi')
]))
# %% ---------------------------------- FUNC4 ---------------------------------- #
"""Func 4: 4 punti

Scrivere una funzione func4(input_path, output_path) che riceve due stringhe
rappresentanti percorsi di file.

Il file input_path contiene una parola per riga (senza spazi).

Per ogni parola, contare il numero di vocali (a, e, i, o, u) presenti,
IGNORANDO la differenza tra maiuscole e minuscole.

Scrivere nel file output_path, una riga per parola, nel formato:
    parola:numero_vocali

Le righe devono essere ordinate per:
  1. numero_vocali decrescente
  2. in caso di parita', parola in ordine alfabetico

La funzione restituisce il numero TOTALE di parole che contengono
ALMENO UNA vocale.

Esempi:
    Se input_path contiene:
        Ciao
        Mondo
        Xyzzy
        Python
        Gatto
    Il file output conterra':
        Ciao:3
        Gatto:2
        Mondo:2
        Python:1
        Xyzzy:0
    (Nota: 'Python' ha 1 vocale, 'Ciao' ne ha 3, 'Mondo' e 'Gatto' ne hanno 2)
    e la funzione restituisce 4 (Xyzzy non ha almeno una vocale).
"""

def func4(input_path, output_path):
    with open(input_path) as f:
        words = f.read().split()
    pairs = [(w, sum(w.lower().count(v) for v in 'aeiou')) for w in words]
    pairs.sort(key=lambda p: (-p[1], p[0]))
    with open(output_path, 'w') as f:
        for p in pairs:
            print(f"{p[0]}:{p[1]}", file = f)
    return len([p for p in pairs if p[1]!=0])

print(func4('func4/input_5.txt', 'func4/output_5.txt'))

# %% ---------------------------------- FUNC5 ---------------------------------- #
"""Func 5: 8 punti

Scrivere una funzione func5(input_path, output_path) che carica un'immagine
PNG dal percorso input_path, trova tutti i pixel non neri e per ciascun 
diverso colore calcola il rettangolo minimo che contiene  tutti i pixel di quel colore
(bounding box: riga_min, riga_max, colonna_min, colonna_max).

Disegna il bordo di ogni bounding box con quel colore sull'immagine
e salva il risultato in output_path.
ATTENZIONE: i rettangoli vanno disegnati nell'ordine dei colori crescenti
(ovvero per R crescenti, in casi di parità per G crescenti, in caso di parità per B crescenti)

Restituisce il numero di colori trovati.

Se non ci sono pixel non neri, restituisce 0 e salva una copia dell'immagine
originale.

Usate images.load() e images.save() per caricare e salvare le immagini.

Esempio:
    Immagine 10x10 con tre pixel a (3,6), (5,2) e (2,8)
    -> risultato 1
       rettangolo bianco con angoli in (2,2) e (5,8)

"""

def draw_rect(im, color, p1, p2):
    p1r,p1c = p1
    p2r,p2c = p2
    
    for j in range(p1c, p2c+1):
        im[p1r][j] = color
        im[p2r][j] = color
        
    for i in range(p1r, p2r+1):
        im[i][p1c] = color
        im[i][p2c] = color
            
    
def func5(input_path, output_path):
    im = images.load(input_path)
    pixels = {}
    for r, row in enumerate(im):
        for c, pixel in enumerate(row):
            if pixel != (0,0,0):
                pixels[pixel] = pixels.get(pixel, []) + [(r,c)]

    for color, pix_list in sorted(pixels.items()):
        p1r = min(p[0] for p in pix_list)
        p1c = min(p[1] for p in pix_list)
        p2r = max(p[0] for p in pix_list)
        p2c = max(p[1] for p in pix_list)
        draw_rect(im, color, (p1r,p1c), (p2r,p2c))
    images.save(im, output_path)
    return len(pixels)
    
print(func5('func5/input_4.png','func5/output_4.png'))                
                


# %% ----------------------------------- EX1 ----------------------------------- #
"""Ex 1: 7 punti

Scrivere una funzione RICORSIVA ex1(albero) che riceve un albero binario
(della classe tree.BinaryTree) e restituisce una tupla (profondita', valore),
dove:
  - profondita' e' la profondita' massima (numero di archi dalla radice) della
    foglia piu' profonda (se la radice e' una foglia, profondita' = 0)
  - valore e' il valore della foglia piu' profonda; se ci sono piu' foglie
    alla stessa profondita' massima, restituire il valore massimo tra esse.
Se l'albero e' None (vuoto), restituire (None, None).

Esempi:
    Albero:     1
            |---|---|
            2       3
        ex1(albero) -> (1, 3)  (profondita' 1, foglie con valori 2 e 3 -> max = 3)

    Albero:         1
                |---|---|
                2       3
            |---|---|
            4       5
        foglie: 4 (prof 2), 5 (prof 2), 3 (prof 1)
        ex1(albero) -> (2, 5)  (profondita' massima = 2, max valore = 5)

    Albero (sola radice 42):
            42
        ex1(albero) -> (0, 42)

    Albero vuoto: ex1(None) -> (None, None)
"""

def ex1(albero):
    if albero == None:
        return(None, None)
    return _ex1(albero, 0)
    
def _ex1(albero, depth):
    if albero == None:
        return(0, 0)
    if albero.left == None and albero.right == None:
        return depth, albero.value
    s = _ex1(albero.left, depth+1)
    d = _ex1(albero.right, depth+1)
    
    if s[0]>d[0]:
        return s
    if s[0] == d[0] and s[1]>d[1]:
        return s
    else:
        return d
        


# %% ----------------------------------- EX2 ----------------------------------- #
"""Ex 2: 7 punti

Scrivere una funzione RICORSIVA ex2(nidificata, profondita=0) che riceve una
lista annidata di interi (cioe' una lista che puo' contenere interi o altre
liste annidate).  La funzione restituisce una nuova lista contenente tutti
gli interi che si trovano a una profondita' PARI.

La profondita' si conta come segue:
  - la lista piu' esterna e' a profondita' 0
  - ogni volta che si entra in una sotto-lista, la profondita' aumenta di 1

Quindi gli interi direttamente nella lista principale sono a profondita' 0
(PARI -> inclusi), gli interi dentro una sotto-lista sono a profondita' 1
(DISPARI -> esclusi), quelli in una sotto-sotto-lista sono a profondita' 2
(PARI -> inclusi), e cosi' via.

Il parametro profondita=0 serve per la ricorsione, non va modificato nelle
chiamate esterne.

Esempi:
    ex2([1, [2, 3], 4]) -> [1, 4]
        (1 e 4 sono a profondita' 0, 2 e 3 sono a profondita' 1)

    ex2([1, [2, [3, 4], 5], 6]) -> [1, 3, 4, 6]
        (1,6: prof 0 incluso; 2,5: prof 1 escluso; 3,4: prof 2 incluso)

    ex2([]) -> []
    ex2([[1]]) -> []
        (1 e' a profondita' 1 -> escluso)
"""

def ex2(nidificata, profondita=0):
    l = []
    for el in nidificata:
        if type(el) == int and profondita%2 == 0:
            l.append(el)
        elif type(el) == list:
            l.extend((ex2(el, profondita+1)))
    return l


######################################################################################

if __name__ == '__main__':
    print('Eseguire grade.py per il test automatico.')

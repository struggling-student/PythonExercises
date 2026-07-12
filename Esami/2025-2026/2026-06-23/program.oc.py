#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""

nome        = "A"
cognome     = "S"
matricola   = "42"

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
    assert isinstance(studenti, list), "func1: student must be a list"
    for s in studenti:
        assert isinstance(s, dict), "func1: each student must be a dict"
        for k in ('name', 'scores', 'bonus'):
            assert k in s, f"func1: missing key '{k}' in student dict"
        assert isinstance(s['name'], str), "func1: 'name' must be str"
        assert isinstance(s['scores'], list) and all(isinstance(v, int) for v in s['scores']), \
            "func1: 'scores' must be list[int]"
        assert isinstance(s['bonus'], int), "func1: 'bonus' must be int"
    risultato = []
    for s in studenti:
        totale = sum(s['scores']) + s['bonus']
        risultato.append((s['name'], totale))
    risultato.sort(key=lambda x: (-x[1], x[0]))
    return risultato


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
    assert isinstance(lista1, list) and isinstance(lista2, list), \
        "func2: both arguments must be lists"
    assert all(isinstance(x, str) for x in lista1), "func2: lista1 elements must be str"
    assert all(isinstance(x, str) for x in lista2), "func2: lista2 elements must be str"
    return sorted(set(lista1) ^ set(lista2))


# %% ---------------------------------- FUNC3 ---------------------------------- #
"""Func 3: 2 punti

Scrivere una funzione func3(coppie) che riceve una lista di coppie
(parola, definizione), dove parola e definizione sono stringhe.

Costruire e restituire un dizionario che ha:
  - chiave: la prima lettera di ogni parola (resa minuscola) 
  - valore: la lista ordinata alfabeticamente delle chiavi la cui definizione
    contiene ALMENO 5 parole (separate da spazi)

Esempi:
    func3([
        ("colubro","serpente molto molto velenoso che striscia"),
        ("cane",   "animale domestico a quattro zampe"),
        ("gatto",  "felino domestico"),
        ("casa",   "edificio per abitare")
    ]) -> {'c': ['cane', 'colubro']}
    # "gatto" è escluso (la definizione ha solo 2 parole < 5)
    # "casa"  è escluso (la definizione ha solo 3 parole < 5)
    # "cane" ha la definizione con 5 parole -> è incluso sotto 'c'
    # "colubro" ha la definizione con 6 parole -> è incluso sotto 'c' dopo 'cane'
"""

def func3(coppie):
    assert isinstance(coppie, list), "func3: coppie must be a list"
    for c in coppie:
        assert isinstance(c, (list, tuple)) and len(c) == 2, \
            "func3: each pair must be a list/tuple of (word, definition)"
        assert isinstance(c[0], str) and isinstance(c[1], str), \
            "func3: word and definition must be strings"
    risultato = {}
    for parola, definizione in coppie:
        if len(definizione.split()) >= 5:
            iniziale = parola[0].lower()
            if iniziale not in risultato:
                risultato[iniziale] = []
            risultato[iniziale].append(parola)
    for k in risultato:
        risultato[k].sort()
    return risultato


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
    assert isinstance(input_path, str) and isinstance(output_path, str), \
        "func4: both arguments must be strings (file paths)"
    assert os.path.isfile(input_path), f"func4: input file not found: {input_path}"
    with open(input_path, 'r') as f:
        parole = [riga.rstrip('\n') for riga in f]

    righe = []
    conta_vocali = 0
    VOCALI = set('aeiou')

    for parola in parole:
        n_vocali = sum(1 for c in parola.lower() if c in VOCALI)
        righe.append((parola, n_vocali))
        if n_vocali > 0:
            conta_vocali += 1

    righe.sort(key=lambda x: (-x[1], x[0]))

    with open(output_path, 'w') as f:
        for parola, n in righe:
            f.write(f"{parola}:{n}\n")

    return conta_vocali


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

def func5(input_path, output_path):
    assert isinstance(input_path, str) and isinstance(output_path, str), \
        "func5: both arguments must be strings (file paths)"
    assert os.path.isfile(input_path), f"func5: input file not found: {input_path}"
    img = images.load(input_path)
    h = len(img)
    w = len(img[0]) if h > 0 else 0

    if h == 0 or w == 0:
        images.save(img, output_path)
        return 0

    # Raggruppa i pixel non neri per colore
    color_pixels = {}  # colore -> lista di (r, c)
    for r in range(h):
        for c in range(w):
            px = img[r][c]
            if px != (0, 0, 0):
                if px not in color_pixels:
                    color_pixels[px] = []
                color_pixels[px].append((r, c))

    if not color_pixels:
        images.save(img, output_path)
        return 0

    # Per ogni colore, calcola bounding box e disegna il bordo
    for colore, pixels in sorted(color_pixels.items()):
        min_r = min(p[0] for p in pixels)
        max_r = max(p[0] for p in pixels)
        min_c = min(p[1] for p in pixels)
        max_c = max(p[1] for p in pixels)

        # Bordo superiore e inferiore
        for c in range(min_c, max_c + 1):
            img[min_r][c] = colore
            img[max_r][c] = colore

        # Bordo sinistro e destro
        for r in range(min_r, max_r + 1):
            img[r][min_c] = colore
            img[r][max_c] = colore

    images.save(img, output_path)
    return len(color_pixels)


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
    assert albero is None or isinstance(albero, tree.BinaryTree), \
        "ex1: argument must be a BinaryTree or None"
    if albero is None:
        return (None, None)

    if albero.left is None and albero.right is None:
        return (0, albero.value)

    candidati = []

    if albero.left is not None:
        sub = ex1(albero.left)
        if sub[0] is not None:
            candidati.append((sub[0] + 1, sub[1]))

    if albero.right is not None:
        sub = ex1(albero.right)
        if sub[0] is not None:
            candidati.append((sub[0] + 1, sub[1]))

    max_prof = max(p for p, _ in candidati)
    miglior_valore = max(v for p, v in candidati if p == max_prof)

    return (max_prof, miglior_valore)


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

I valori raccolti nella lista finale devono essere nello stesso ordine 
in cui li si visita con una visita in preordine.

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
    assert isinstance(nidificata, list), "ex2: argument must be a nested list of ints"
    risultato = []
    for elemento in nidificata:
        if isinstance(elemento, list):
            risultato.extend(ex2(elemento, profondita + 1))
        else:
            if profondita % 2 == 0:
                risultato.append(elemento)
    return risultato


######################################################################################

if __name__ == '__main__':
    print('Eseguire grade.py per il test automatico.')

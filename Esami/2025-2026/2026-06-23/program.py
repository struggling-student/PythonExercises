#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


######################################################################################

if __name__ == '__main__':
    print('Eseguire grade.py per il test automatico.')

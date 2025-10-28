#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o 
uguale a 18.

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""

nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

################################################################################
################################################################################
################################################################################

################################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
""" func1: 6 punti

Si definisca una funzione func1(img_in) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG. La funzione deve restituire il numero dei pixel dell'immagine
il cui canale rosso ha valore maggiore (stretto) di 150.
"""


import images


def func1(img_in) -> int:
    pass


# %% ----------------------------------- FUNC2 ------------------------- #
""" func2: 8 punti

Definire una funzione che dato il nome di un file (img_in) contenente 
un'immagine, calcola l'immagine il cui canale blu viene incrementato di un 
certo numero di unità val indicato come paramentro (val). 
Quando la somma supera il valore 255, si riparte da 0. Ad es. 240+100 = 85.
L'immagine risultante viene salvata nel file con nome indicato come parametro 
(img_out).
La funzione restituisce il numero di pixel che hanno sforato 255 nel 
canale blu.
Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" 
visto a lezione.
"""


import images


def func2(img_in: str, img_out: str, val: int) -> int:
    pass

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 8 punti

Si definisca una funzione func3(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG. L'immagine indicata dal 'input_pngfile' contiene solo
pixel neri e bianchi. La funzione deve individuare tutti i segmenti
orizzontali di colore bianco e restituirli in una lista.
I segmenti orizzontali su una riga possono essere al più uno.
Inoltre un segmento puo' essere lungo quanto tutta la larghezza
dell'immagine oppure anche lungo solamente un pixel.
La funzione restituiste una lista in cui ogni segmento orizzontale
è codificato come tupla con coordinate (y, xstart, xend),
dove y è il numero di riga, xstart il primo pixel del segmento, xend
l'ultimo pixel del segmento. La lista è ordinata in ordine crescente
in base alla coordinata y.

Ad esempio data l'immagine:

 0 1 2 3 4 5
0. . . . . .
1. . . . . .
2. . x . . .
3. . . . . .
4. . . . . .
5x x x x x x

dove . è nero e x è bianco, la funzione deve restituire:
[(2,2,2), (5,0,5)].

Per vedere i casi di test si vedano le immagini in func5/image01.png etc.
"""

import images


def func3(input_pngfile):
    pass




# %% ----------------------------------- FUNC4 ------------------------- #
''' func4: 8 punti

Si definisca una funzione func4 che prende in input un'immagine RGB.
La funzione conta e restituisce il numero di pixel non neri che sono
preceduti e seguiti da pixel neri (ovvero, dato un pixel P,
c'è un pixel nero che lo precede e uno che lo segue).
Se il pixel non nero si trova sul bordo destro dell'immagine, 
si considera solo il pixel che precede. 
Allo stesso modo, se il pixel non nero si trova sul bordo sinistro
dell'immagine, si considera solo il pixel che lo segue.
Inoltre, la funzione salva un'immagine RGB con la stessa larghezza e altezza
dell'immagine di input, in cui sono copiati solo i pixel contati.

Ad esempio, se B rappresenta un pixel nero e * rappresenta
un pixel non nero, data l'immagine:

BB*BBBB*
*BBB*BBB
B*BB**B*
BBBBBB*B
*BBB**BB

La funzione restituisce 8 e salva l'immagine:

BB*BBBB*
*BBB*BBB
B*BBBBB*
BBBBBB*B
*BBBBBBB
'''

import images

def func4(input_file_name, output_file_name):
    pass
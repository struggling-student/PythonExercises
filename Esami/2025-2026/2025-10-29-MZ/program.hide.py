#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o uguale a 18.
"""

nome = "hide"
cognome = "matsumoto"
matricola = "5050"

################################################################################
################################################################################
################################################################################


################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 4 punti

Si definisca la funzione func1(a_dict, word) che prende in ingresso un
dizionario 'a_dict' e una parola 'word'. Ogni chiave del dizionario è
una stringa che ha una lista di stringhe come valore. La funzione deve
rimuovere da CIASCUNA lista di valori tutte le stringhe che hanno lo
stesso PRIMO e ULTIMO carattere della 'word' data, convertito in minuscolo.
La funzione restituisce il numero TOTALE di elementi rimossi da tutte
le liste del dizionario. Il dizionario 'a_dict' viene modificato.
'''


def func1(a_dict: dict[str, list[str]], word: str) -> int:
    if not word:
        return 0

    # start, *_, end = word
    first_char = word[0].lower()
    last_char = word[-1].lower()

    total_removed = 0

    for key in list(a_dict.keys()):
        original_list = a_dict[key]
        new_list = []

        for s in original_list:
            if len(s) > 0 and s[0].lower() == first_char and s[-1].lower() == last_char:
                total_removed += 1
            else:
                new_list.append(s)

        a_dict[key][:] = new_list


    return total_removed


################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 4 punti
Un dizionario D e' fornito come input. Le chiavi di D sono interi mentre
i valori sono liste di stringhe.

Scrivi la funzione func2(D) che costruisce e ritorna la lista W contenente
tutte le stringhe associate a ciascuna chiave K in D, tali che la lunghezza
della stringa sia STRETTAMENTE MINORE di K.

La lista W risultante deve essere ordinata per lunghezza DECRESCENTE.
In caso di parità di lunghezza, l'ordinamento è ALFABETICO DECRESCENTE.
'''


def func2(D: dict[int, list[str]]) -> list[str]:
    W = [w for k, l in D.items() for w in l if len(w)<k]
    W.sort(reverse=True)
    W.sort(key=len, reverse=True)
    return W


################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 4 punti
Implementare la func3(strList) che:
- prende in input una lista di stringhe
- per ogni stringa, conta il numero di VOCALI (a, e, i, o, u, case-insensitive).
- restituisce una lista dei conteggi ottenuti, ordinati in base al loro
  valore, in ordine DECRESCENTE.
'''


def func3(strList: list[str]) -> list[int]:
    VOWELS = "aeiou"
    counts = []

    for s in strList:
        s_lower = s.lower()
        vowel_count = 0
        for char in s_lower:
            if char in VOWELS:
                vowel_count += 1
        counts.append(vowel_count)

    # Restituisce la lista dei conteggi ordinati in base al valore decrescente
    return sorted(counts, reverse=True)


################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
'''  func4: 6 punti

Si definisca una funzione func4(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di
stringhe.
La nuova lista è costituita da tutte quelle stringhe presenti in
string_list1 ma NON in string_list2. (Differenza tra insiemi)

La lista risultante deve essere ordinata per numero di CARATTERI UNICI
(presenti nella stringa) CRESCENTE, in caso di parità, in ordine ALFABETICO CRESCENTE.
'''


def func4(string_list1: list[str], string_list2: list[str]) -> list[str]:
    set1 = set(string_list1)
    set2 = set(string_list2)
    difference = list(set1.difference(set2))

    def sort_key(s):
        num_unique_chars = len(set(s))
        return (num_unique_chars, s)

    result = sorted(difference, key=sort_key)

    return result


################################################################################
# %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################
'''
func5: 8 punti

Scrivere una funzione func5(points) che prende in ingresso una lista
di coordinate (x,y) di N punti nel piano cartesiano (N >= 3).
Ogni punto è una coppia di numeri interi.

La funzione deve:
1. Trovare i TRE punti con la coordinata Y MASSIMA. Se ci sono più
   di tre punti con la Y massima, prendere i primi tre in ordine di 
   apparizione nella lista in input.
2. Calcolare il PUNTO MEDIANO (Mx, My) di questi tre punti.
   (Mx è la mediana delle 3 coordinate X, My è la mediana delle 3
    coordinate Y).

La funzione restituisce una tupla (Mx, My) dove entrambi i valori
devono essere riportati con una precisione di 3 cifre decimali
(per farlo si può usare la funzione round).
'''

def func5(points : list[tuple[int,int]]) -> tuple[float,float]:
    if len(points) < 3:
        return (0.0, 0.0)

    sorted_points = sorted(points, key=lambda p: p[1], reverse=True)

    top_3_points = sorted_points[:3]


    X_coords = sorted([p[0] for p in top_3_points])
    Y_coords = sorted([p[1] for p in top_3_points])

    Mx = X_coords[1]
    My = Y_coords[1]

    # Restituisce la tupla arrotondata a 3 cifre decimali
    return (round(float(Mx), 3), round(float(My), 3))


################################################################################
# #%% ---------------------------- FUNC.6 ------------------------------------ #
################################################################################
'''
Func 6: 4 punti

Si definisca la funzione func6(text) che riceve come argomento:
- text: una stringa formata da parole separate da spazi e punteggiatura
e che ritorna un dizionario che ha:
  - come chiavi le CONSONANTI uniche presenti nel testo (minuscole)
  - come valore la FREQUENZA TOTALE di quella consonante nell'intero testo
    (case-insensitive).

Consonanti da considerare: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z.
'''


def func6(text: str) -> dict[str, int]:

    CONSONANTS = set("bcdfghjklmnpqrstvwxyz")
    to_return = dict()
    for char in text.lower():
        if char in CONSONANTS:
            to_return[char] = to_return.get(char, 0) + 1
    return to_return
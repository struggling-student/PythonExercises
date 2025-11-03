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

nome       = " NOME"
cognome    = " COGNOME"
matricola  = " MATRICOLA"

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

Esempio:
a_dict = {'a':['alpha','beta','gamma'], 'b':['axle','zeta']}
word = 'aura'
a_dict_exp = {'a':['beta','gamma'], 'b':['axle','zeta']}
expected = 1
'''
def func1(a_dict : dict[str,list[str]], word : str) -> int :
    # scrivi qui il tuo codice
    pass
    conta = 0
    word = word.lower()
    chars = word[0]+word[-1]
    for k,L in list(a_dict.items()):
        for parola in L.copy():
            parola = parola.lower()
            iniziofine = parola[0]+parola[-1]
            if chars == iniziofine:
                conta += 1
                L.remove(parola)
    return conta

# a_dict = {'a':['alpha','beta','gamma'], 'b':['axle','zeta']}
# word = 'aura'
# a_dict_exp = {'a':['beta','gamma'], 'b':['axle','zeta']}
# expected = 1
# print(func1(a_dict, 'aura')) # 1
# print(a_dict) # {'a':['beta','gamma'], 'b':['axle','zeta']}

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

Esempio:
dictionary = {4: ["a", "b", "c", "de", "fgh"], 2: ["a", "z", "b", "w"], 0: ["a", "b"]}
expected = ['fgh', 'de', 'z', 'w', 'c', 'b', 'b', 'a', 'a']
'''


def func2(D : dict[int, list[str]]) -> list[str]:
    # scrivi qui il tuo codice
    def criterio(parola : list[str]) -> list[str]:
        return len(parola), parola
    pass
    giuste = [ p for k,L in D.items() for p in L if len(p) < k ]
    return sorted(giuste, key=criterio, reverse=True)

# D = {4: ["a", "b", "c", "de", "fgh"], 2: ["a", "z", "b", "w"], 0: ["a", "b"]}
# print(func2(D)) # ['fgh', 'de', 'z', 'w', 'c', 'b', 'b', 'a', 'a']

################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 4 punti

Implementare la func3(strList) che:
- prende in input una lista di stringhe
- per ogni stringa, conta il numero di VOCALI (a, e, i, o, u, case-insensitive).
- restituisce una lista dei conteggi ottenuti, ordinati in base al loro
  valore, in ordine DECRESCENTE.
  
Esempio:
a_list = ["monkey", "cat", "panda", "alligator"]
expected = [4, 2, 2, 1]
'''

def func3(strList : list[str]) -> list[int]:
    # scrivi qui il tuo codice
    pass
    def conta_vocali(parola):
        vocali = 'aeiouAEIOU'
        return sum(parola.count(v) for v in vocali)
    conteggi = [conta_vocali(p.lower()) for p in strList]
    return sorted(conteggi, reverse=True)

# a_list = ["monkey", "cat", "panda", "alligator"]
# print(func3(a_list)) # [4, 2, 2, 1]

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

Esempio:
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark', 'shop', 'cat']
    expected = ['park', 'elephant', 'elichopter']

'''

def func4(string_list1 : list[str], string_list2 : list[str]) -> list[str]:
    def criterio(parola):
        return len(set(parola)), parola
    parole = [p for p in string_list1 if p not in string_list2]
    return sorted(parole, key=criterio)


# string_list1 = ['shop', 'park', 'elichopter', 'cat', 'elephant']
# string_list2 = ['ark', 'contact', 'hop', 'mark', 'shop', 'cat']
# print(func4(string_list1, string_list2)) # ['park', 'elephant', 'elichopter']

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
    
NOTA: la mediana tra più valori è il valore centrale tra i valori, ordinati (se dispari)
ovvero la media tra i due valori centrali (se pari)

La funzione restituisce una tupla (Mx, My) dove entrambi i valori
devono essere riportati con una precisione di 3 cifre decimali
(per farlo si può usare la funzione round).

Esempio:
    points = [(1, 5), (3, 2), (4, 5), (5, 1), (2, 4)]
    expected = (2, 5)
'''

def func5(points : list[tuple[int,int]]) -> tuple[float,float]:
    # scrivi qui il tuo codice
    pass
    points   = sorted(points,key=lambda P: P[1], reverse=True)[:3]
    XS = sorted([x for x,y in points])
    YS = sorted([y for x, y in points])
    return XS[1], YS[1]
    #return points[1]    # sbagliato

# points = [(1, 5), (3, 2), (4, 5), (5, 1), (2, 4)]
# print(func5(points)) # (2, 5)

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

Esempio:
text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
expected   = {'s': 2, 't': 3, 'l': 4, 'p': 6, 'n': 3, 'c': 6, 'r': 4}
'''

def func6(text : str) -> dict[str,int]:
    pass
    consonanti = "bcdfghjklmnpqrstvwxyz"
    text = text.lower()
    return {c : text.count(c) for c in consonanti if text.count(c)}

#text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
#print(func6(text)) # {'s': 2, 't': 3, 'l': 4, 'p': 6, 'n': 3, 'c': 6, 'r': 4}

################################################################################
################################################################################
################################################################################

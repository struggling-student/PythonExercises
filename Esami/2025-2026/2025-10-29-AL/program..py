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

nome       = "F"
cognome    = "L"
matricola  = "123456"

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
rimuovere dal dizionario tutte quelle chiavi associate ad una lista
che contiene una stringa che ha 'word' come sottostringa.  
La funzione restituisce il numero di chiavi rimosse dal dizionario 'a_dict'.

Esempio: se a_dict = {'a':['a','barbagianni','c'], 'b':['a','bifolco'], 'c':['a','c']}
  l'invocazione di func1(a_dict, 'b') deve restituire 2 e
  a_dict deve risultare modificato in {'c': ['a', 'c']}.
  In quanto: e' rimossa la chiave 'a' perche' la lista ['a','barbagianni','c']
  contiene 'barbagianni' che contiene la word 'b'; 
  e' inoltre rimossa la chiave 'b' perche' la lista ['a','bifolc0'] contiene 
  'bifolco' che contiene la word 'b'.
'''
def func1(a_dict : dict[str,list[str]], word : str) -> int :
    # scrivi qui il tuo codice
    pass

# a = {'a':['a','barbagianni','c'], 'b':['a','bifolco'], 'c':['a','c']}
# print(func1(a, 'b')) # 2
# print(a) # {'c': ['a', 'c']}

################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 4 punti
Un dizionario D e' fornito come input. Le chiavi di D sono interi mentre
i valori sono liste di stringhe con possibili ripetizioni.
Assumete che le chiavi del dizionario siano sempre minori della lunghezza delle liste associate.

D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}

Scrivi la funzione func2(D) che costruisice e ritorna la lista W di coppie
che contiene i valori ottenuti prendendo, per ogni chiave K in D, i due elementi 
dalla lista L associata a K, che si trovano a distanza K dall'inizio e dalla fine.
Prima di selezionare i due elementi, la funzione ordina L in ordine alfabetico inverso.

Dato D come definito sopra, la funzione ritorna:

    W = [("c","h"), ("b","w"), ("b","a")]

poiche' la prima lista, in ordine inverso e' ["h", "g", "f", "e", "c"]
e gli elementi a distanza 4 dall'inizio e dalla fine sono "c" e "h".
La seconda lista, ordinata e' ["z", "w", "b", "a"] 
e gli elementi a distanza 2 dall'inizio e dalla fine sono "b" e "w".
La terza lista, ordinata e' ["b", "a", "a"] 
e gli elementi a distanza 0 dall'inizio e dalla fine sono "b" e "a".
'''


def func2(D : dict[int, list[str]]) -> list[str]:
    # scrivi qui il tuo codice
    pass

# D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}
# print(func2(D)) # [("c","h"), ("b","w"), ("b","a")]

################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 4 punti

Implementare la func3(strList) che:
- prende in input una lista di stringhe
- calcola la somma dei codici dei caratteri di ciascuna stringa,
  ottenendo un valore intero per ogni stringa, e aggiunge tutti i valori
  ottenuti ad una lista.
- restituisce la lista degli interi ordinati in base alle stringhe della lista
  iniziale strList, in ordine:
     - di lunghezza decrescente, e in caso di parità
     - in ordine alfabetico crescente.

Ad esempio, se strList = ["monkey", "cat", "panda", "boy", "alligator"]
i valori ascii corrispondenti sono: [659, 312, 516, 330, 959]
che, in base all'ordinamento per lunghezze decrescenti e alfabetico crescente dell'elenco iniziale,
vengono restituiti come: [959, 659, 516, 330, 312]

Per convertire caratteri in codici ascii si puo' usare la funzione ord().
'''

def func3(strList : list[str]) -> list[int]:
    # scrivi qui il tuo codice
    pass

# strList = ["monkey", "cat", "panda", "boy", "alligator"]
# print(func3(strList)) # [959, 659, 516, 330, 312]

################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
'''  func4: 6 punti

Si definisca una funzione func4(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di
stringhe.
La nuova lista è costituita da tutte quelle stringhe presenti in una
delle due liste in ingresso che contengono come una sottostringa
almeno una stringa dell'altra lista.
La lista risultante deve essere ordinata per numero di caratteri
decrescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] e
            string_list2=['ark', 'contact', 'hop', 'mark']

         l'invocazione di func4(string_list1, string_list2) dovrà restituire
         la lista ['elichopter', 'park', 'shop']
         Infatti:
             'elichopter' contiene 'hop',
             'park' contiene 'ark'
             'shop' contiene 'hop'

'''

def func4(string_list1 : list[str], string_list2 : list[str]) -> list[str]:
    # INSERT HERE YOUR CODE
    pass


# string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
# string_list2=['ark', 'contact', 'hop', 'mark']
# print(func4(string_list1, string_list2)) # ['elichopter','park', 'shop']

################################################################################
# %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################
'''
func5: 8 punti

Scrivere una funzione func5(points) che prende in ingresso una lista
di coordinate (x,y) di N punti nel piano cartesiano (N >= 3).  Ogni
punto è una coppia di numeri interi.  Per ogni punto, si considera la
sua distanza dal centro del piano (0, 0).

La funzione deve restituire, come una tupla, il baricentro (X, Y) dei
3 punti più lontani al centro del piano. Tutti i valori devono essere
riportati con una precisione di 3 cifre decimali (per farlo si può
usare la funzione round).

  - NOTA: La distanza tra 2 punti (x1, y1) e (x2, y2)
    è la distanza euclidea: sqrt[(x1-x2)² + (y1-y2)²]
  - NOTA: Il baricentro di N punti è il punto (X', Y'),
    dove X' è la media delle coordinate x degli N punti
    e Y' è la media delle coordinate y degli N punti.

Ad esempio, se points = [(2, 2), (-1, 1), (3, 0), (-3, -2), (2, -1)],
prima di ordinarli, le distanze dal centro (0,0) sono:
 2.828, 1.414, 3.0, 3.606, 2.236
 Quindi i tre più distanti dall'origine sono (2, 2), (3, 0), (-3, -2)
e il baricentro risultante dei 3 punti è: (0.667, 0.0)
'''

from math import sqrt
def func5(points : list[tuple[int,int]]) -> tuple[float,float]:
    # scrivi qui il tuo codice
    pass

# points = [(2, 2), (-1, 1), (3, 0), (-3, -2), (2, -1)],
# print(func5(points)) # (0.667, 0.0)

################################################################################
# #%% ---------------------------- FUNC.6 ------------------------------------ #
################################################################################
'''
Func 6: 4 punti

Si definisca la funzione func6(text) che riceve come argomento:
- text: una stringa formata da parole separate da spazi
e che ritorna un dizionario che ha:
  - come chiavi la lettera iniziale delle parole presenti, maiuscola
  - come valore il numero di parole che non contengono quella lettera
    ignorando la differenza tra minuscole e maiuscole

Esempio:
text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
expected   = {'P': 6, 'L': 8, 'C': 6, 'S': 10}
'''

def func6(text : str) -> dict[str,int]:
    pass


#text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
#print(func6(text)) # {'P': 6, 'L': 8, 'C': 6, 'S': 10}

################################################################################
################################################################################
################################################################################

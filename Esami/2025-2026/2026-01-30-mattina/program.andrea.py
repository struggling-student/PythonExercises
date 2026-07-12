#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare questo file col nome program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la prova è necessario:
    - !!!riempire le informazioni personali nelle variabili qui sotto!!!
    - AND ottenere un punteggio maggiore o uguale a 18 (o 15 se DSA)

Il punteggio finale della prova è la somma dei punteggi dei problemi risolti.
"""
nome = "A"
cognome = "S"
matricola = "42"

################################################################################
################################################################################
################################################################################
# ------------------------ SUGGERIMENTI PER IL DEBUG --------------------------- #
# Per facilitare il debug delle funzioni ricorsive, puoi disattivare
# il test ricorsivo impostando DEBUG=True nel file grade.py
#
# DEBUG=True attiva anche il TRACE DELLO STACK che ti permette di sapere quale
# numero di riga in program.py ha generato l'errore.
################################################################################

import tree
import images
import math
import json
import os

# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 2 punti

Implementa la funzione func1(n: int, k: int) -> int che riceve:
- n: un numero intero positivo
- k: un indice di posizione (intero, partendo da 0 per il bit meno significativo)
e ritorna il valore (0 o 1) del k-esimo bit della rappresentazione binaria di n.

Se k supera il numero di bit necessari per rappresentare n, il risultato deve essere 0.

Esempio:
    n = 13 (in binario: 1101)
    func1(13, 0) -> 1  (l'ultimo bit a destra è 1)
    func1(13, 1) -> 0  (il penultimo bit è 0)
    func1(13, 5) -> 0  (oltre la lunghezza di 1101 consideriamo 0)
"""
def func1(n: int, k: int) -> int:
    pass
    # inserisci qui il tuo codice
    S = str(bin(n))
    if k > len(S):
        return 0
    else:
        return int(S[-k-1])


# %% ----------------------------------- FUNC.2 ----------------------------------- #
"""
Func 2: 2 punti

Implementa la funzione func2(nums: list[int]) -> list[int] che trova tutti i 
duplicati in una lista dove ogni intero appare una o due volte. 
La lista risultante deve contenere solo i numeri che appaiono esattamente due volte.

Esempio:
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    In questo caso, 2 e 3 appaiono due volte.
    Output: [2, 3] (l'ordine nel risultato non conta)
"""
def func2(nums: list[int]) -> list[int]:
    pass
    # inserisci qui il tuo codice
    return [ x for x in set(nums) if nums.count(x) == 2]


# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 4 punti

Implementa la funzione func3(strs: list[str]) -> list[list[str]] che raggruppa
una lista di stringhe in base agli anagrammi. Due stringhe sono anagrammi se 
contengono le stesse lettere con la stessa frequenza.

Esempio:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Anagrammi: 
    - "eat", "tea", "ate" (composte da a, e, t)
    - "tan", "nat" (composte da a, n, t)
    - "bat" (da sola)
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""


def func3(strs: list[str]) -> list[list[str]]:
    pass
    # inserisci qui il tuo codice
    D = {}
    for parola in strs:
        ana = ''.join(sorted(parola))
        if ana not in D:
            D[ana] = [parola]
        else:
            D[ana].append(parola)
    return list(D.values())


# %% ----------------------------------- FUNC.4 ----------------------------------- #
"""
Func 4: 6 punti

Implementa la funzione func4(file1: str, file2: str) -> list[str] che confronta
due file di testo riga per riga e restituisce una lista di stringhe che indica 
le differenze trovate. 

Il formato di ogni stringa di differenza deve essere: "Riga [n]: [testo1] != [testo2]"
dove [n] è il numero della riga (partendo da 1).

Nota: se un file ha più righe dell'altro ignorate le righe in più

Esempio:
    file1 contiene: "mela\npera"
    file2 contiene: "mela\nbanana"
    Output: ["Riga 2: pera != banana"]
"""


def func4(file1: str, file2: str) -> list[str]:
    pass
    # inserisci qui il tuo codice
    with open(file1, "r") as f1:
        righe1 = f1.readlines()
    with open(file2, "r") as f2:
        righe2 = f2.readlines()
    diff = []
    for i, (riga1, riga2) in enumerate(zip(righe1, righe2)):
        if riga1.endswith("\n"):
            riga1 = riga1[:-1]
        if riga2.endswith("\n"):
            riga2 = riga2[:-1]
        if riga1 != riga2:
            diff.append(f"Riga {i+1}: {riga1} != {riga2}")
    return diff

# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 6 punti

Implementa la funzione func5(path_in: str, target_color: tuple[int, int, int]) -> tuple[int, int, int, int] 
che carica l'immagine PNG specificata da path_in e identifica il "Bounding Box" 
ovvero il più piccolo rettangolo che racchiude tutti i pixel di colore target_color.

La funzione deve restituire una tupla (x, y, w, h) dove:
- x, y sono le coordinate del pixel in alto a sinistra del rettangolo.
- w, h sono la larghezza e l'altezza del rettangolo.

Se il colore non è presente, restituisci (0, 0, 0, 0).
Assumi che lo sfondo dell'immagine sia nero (0, 0, 0) e il colore target sia unico.

Esempio:
    Se i pixel di colore (255, 0, 0) si trovano solo in (10, 10) e (15, 20),
    il rettangolo minimo va da x=10 a x=15 e da y=10 a y=20.
    Output: (10, 10, 6, 11)
"""
import images
def func5(path_in: str, target_color: tuple[int, int, int]) -> tuple[int, int, int, int]:
    pass
    # inserisci qui il tuo codice
    minx = maxx = miny = maxy = None
    img = images.load(path_in)
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            if pixel == target_color:
                if minx is None or x < minx:
                    minx = x
                if maxx is None or x > maxx:
                    maxx = x
                if miny is None or y < miny:
                    miny = y
                if maxy is None or y > maxy:
                    maxy = y
    if minx is None:
        return 0,0,0,0
    else:
        return minx, miny, maxx-minx+1, maxy-miny+1


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 6 punti

Si definisca una funzione ricorsiva o che utilizza funzioni o metodi ricorsivi 
ex1(arr: list[int], n: int, s: int) -> bool che determina se NON esiste NESSUN 
sottoinsieme della lista 'arr' composto da 'n' elementi la cui somma è 's'.

Esempio:
    arr = [1, 5, 2, 10], n = 2, s = 3
    Non esiste nessun sottoinsieme di 2 elementi che somma a 3? NO: [1, 2].
    Output: False
"""


def ex1(arr: list[int], n: int, s: int) -> bool:
    pass
    # inserisci qui il tuo codice
    S = sum(arr)
    if S == s and len(arr) == n:
        return False
    for i,x in enumerate(arr):
        resto = arr.copy()
        resto.pop(i)
        if not ex1(resto, n, s):
            return False
    return True

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti

Si definisca una funzione ricorsiva o che utilizza funzioni o metodi ricorsivi 
per gestire la serializzazione di un albero binario.

Implementa la funzione ex2(root: tree.BinaryTree) -> str che restituisce 
una stringa rappresentante l'albero tramite una visita PRE-ORDER (Radice, Sinistra, Destra).
I valori dei nodi devono essere separati da virgole. I nodi vuoti (None) devono 
essere rappresentati dal carattere '#'.

Esempio:
        Albero:                |
              1                |
             / \               |
            2   3              |
           / \                 |
          #   #                |

    Visita Pre-order: 1 (radice), poi sottoalbero sinistro (2, #, #), poi destro (3, #, #).
    Stringa risultante: "1,2,#,#,3,#,#"
"""


def ex2(root: tree.BinaryTree) -> str:
    pass
    # inserisci qui il tuo codice
    if root is None:
        return '#'
    return ','.join([str(root.value),ex2(root.left),ex2(root.right)])


######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali
    print('*' * 50)
    print('Eseguire grade.py per il test automatico.')
    print('*' * 50)
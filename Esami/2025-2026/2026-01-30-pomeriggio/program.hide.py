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
    - AND risolvere almeno 3 esercizi 'func' e almeno 1 esercizio 'ex' (ricorsivo)

Il punteggio finale della prova è la somma dei punteggi dei problemi risolti.
"""
nome = "hide"
cognome = "matsumoto"
matricola = "5050"

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

import images
import tree

def func1(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


# %% ----------------------------------- FUNC.2 ----------------------------------- #
def func2(studenti: list[dict]) -> list[str]:
    return [s["nome"] for s in studenti if s["media"] > 28]


# %% ----------------------------------- FUNC.3 ----------------------------------- #
def func3(file1: str, file2: str) -> list[str]:
    diffs = []
    with open(file1, 'r', encoding='utf8') as f1, open(file2, 'r', encoding='utf8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range(max(len(lines1), len(lines2))):
            l1 = lines1[i].strip() if i < len(lines1) else ""
            l2 = lines2[i].strip() if i < len(lines2) else ""
            if l1 != l2:
                diffs.append(f"Riga {i + 1}: {l1} != {l2}")
    return diffs


# %% ----------------------------------- FUNC.4 ----------------------------------- #
def func4(n: int) -> list[tuple[int, int]]:
    return [(x, y) for x in range(n) for y in range(n) if (x + y) % 2 == 0]


# %% ----------------------------------- FUNC.5 ----------------------------------- #
def func5(path_in: str, path_out: str, k: int):
    img = images.load(path_in)
    h = len(img)
    w = len(img[0])
    for y in range(0, h, k):
        for x in range(0, w, k):
            pixels = []
            for i in range(y, min(y + k, h)):
                for j in range(x, min(x + k, w)):
                    pixels.append(img[i][j])

            avg_r = round(sum(p[0] for p in pixels) / len(pixels))
            avg_g = round(sum(p[1] for p in pixels) / len(pixels))
            avg_b = round(sum(p[2] for p in pixels) / len(pixels))
            avg_color = (avg_r, avg_g, avg_b)

            for i in range(y, min(y + k, h)):
                for j in range(x, min(x + k, w)):
                    img[i][j] = avg_color
    images.save(img, path_out)


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 6 punti

Si definisca una funzione RICORSIVA o che utilizza funzioni o metodi ricorsivi 
ex1(candidates: list[int], target: int) -> list[list[int]] che trova tutte le 
combinazioni uniche di candidati che sommano esattamente al target. 
Ogni numero della lista 'candidates' può essere usato un numero illimitato di volte.

Esempio:
    candidates = [2, 3, 6, 7], target = 7
    Combinazioni possibili: [2, 2, 3] (somma 7) e [7] (somma 7)
    Output: [[2, 2, 3], [7]] (l'ordine delle combinazioni non conta)
"""


def ex1(candidates: list[int], target: int, start=0, current_comb=None, results=None) -> list[list[int]]:
    if current_comb is None: current_comb = []
    if results is None: results = []

    if target == 0:
        results.append(list(current_comb))
        return results
    if target < 0:
        return results

    for i in range(start, len(candidates)):
        current_comb.append(candidates[i])
        ex1(candidates, target - candidates[i], i, current_comb, results)
        current_comb.pop()

    return results


# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 8 punti

Si definisca una funzione RICORSIVA o che utilizza funzioni o metodi ricorsivi 
ex2(root: tree.BinaryTree) -> str per gestire la serializzazione di un albero 
binario in formato stringa.

La funzione deve restituire una stringa che rappresenta l'albero utilizzando 
una visita PRE-ORDER (Radice, Sinistra, Destra). 
I valori dei nodi devono essere separati da una virgola. I nodi vuoti (None) 
devono essere rappresentati dal carattere '#'.

Esempio:
        Albero: 
              1
             / \
            2   3

    Visita Pre-order: 1 -> 2 (con figli None) -> 3 (con figli None)
    Output: "1,2,#,#,3,#,#"
"""


def ex2(root: tree.BinaryTree) -> str:
    if root is None:
        return "#"

    left_str = ex2(root.left)
    right_str = ex2(root.right)

    return f"{root.value},{left_str},{right_str}"



######################################################################################

if __name__ == '__main__':
    # Spazio per test manuali
    print('*' * 50)
    print('Eseguire grade.py per il test automatico.')
    print('*' * 50)
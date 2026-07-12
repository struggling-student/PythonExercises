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
    - AND risolvere almeno 3 esercizi 'func' e almeno 1 esercizio 'ex'

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

import tree
import images

def func1(n: int, k: int) -> int:
    if k < 0: return 0
    return (n >> k) & 1


# %% ----------------------------------- FUNC.2 ----------------------------------- #
def func2(nums: list[int]) -> list[int]:
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return [n for n, count in counts.items() if count == 2]


# %% ----------------------------------- FUNC.3 ----------------------------------- #
def func3(strs: list[str]) -> list[list[str]]:
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


# %% ----------------------------------- FUNC.4 ----------------------------------- #
def func4(file1: str, file2: str) -> list[str]:
    diffs = []
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range(max(len(lines1), len(lines2))):
            l1 = lines1[i].strip() if i < len(lines1) else ""
            l2 = lines2[i].strip() if i < len(lines2) else ""
            if l1 != l2:
                diffs.append(f"Riga {i+1}: {l1} != {l2}")
    return diffs


# %% ----------------------------------- FUNC.5 ----------------------------------- #
def func5(path_in: str, target_color: tuple[int, int, int]) -> tuple[int, int, int, int]:
    img = images.load(path_in)
    rows = len(img)
    cols = len(img[0])
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    found = False
    for r in range(rows):
        for c in range(cols):
            if img[r][c] == target_color:
                found = True
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    if not found:
        return (0, 0, 0, 0)
    return (min_c, min_r, max_c - min_c + 1, max_r - min_r + 1)


# %% ----------------------------------- EX.1 ----------------------------------- #
def ex1(arr: list[int], n: int, s: int, start_idx: int = 0) -> bool:
    if n == 0:
        return s == 0
    if start_idx >= len(arr):
        return False
    # Include current element
    if ex1(arr, n - 1, s - arr[start_idx], start_idx + 1):
        return True
    # Exclude current element
    return ex1(arr, n, s, start_idx + 1)


# %% ----------------------------------- EX.2 ----------------------------------- #
def ex2(root: tree.BinaryTree) -> str:
    if root is None:
        return "#"
    left_part = ex2(root.left)
    right_part = ex2(root.right)
    return f"{root.value},{left_part},{right_part}"




######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali
    print('*' * 50)
    print('Eseguire grade.py per il test automatico.')
    print('*' * 50)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OPERAZIONI PRELIMINARI:
1) Salvare il file come program.py
2) Assegnare Nome, Cognome e Matricola nelle variabili sottostanti.

REGOLE D'ESAME:
- Requisiti Minimi: almeno 3 esercizi 'func' risolti E almeno 1 esercizio 'ex' (ricorsivo) risolto.
- Punteggio: Il voto è la somma dei punti; necessario >= 18 per il superamento.
- Grader: Per testare la ricorsione, assicurarsi che DEBUG = False nel file grade.py.
"""

nome = "hide"
cognome = "matsumoto"
matricola = "5050"


# =============================================================================
# FUNC 1 (2 punti)
# =============================================================================
def func1(pokemon_list: list[dict]) -> list[str]:
    """
    Classifica i personaggi in base al "Power Score".
    Formula: (atk * 1.5) + (spd * 1.2) + def

    ORDINAMENTO E PAREGGI (TIES):
    1. Per punteggio decrescente (dal più alto al più basso).
    2. In caso di parità di punteggio, ordinare alfabeticamente per nome (A-Z).

    Restituisce: Una lista con i nomi dei primi 3 personaggi in classifica.

    Esempio:
        pokemon_list = [{'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}, # Score 37.0
                        {'name': 'B', 'atk': 10, 'spd': 10, 'def': 10}] # Score 37.0
        Restituisce: ['A', 'B'] (perché A viene prima di B in ordine alfabetico)
    """

    def get_score(p):
        return (p['atk'] * 1.5) + (p['spd'] * 1.2) + p['def']

    # Ordiniamo: -score (per decrescente) e poi name (per crescente)
    sorted_list = sorted(pokemon_list, key=lambda x: (-get_score(x), x['name']))

    # Prendiamo i primi 3 nomi
    return [p['name'] for p in sorted_list[:3]]


# =============================================================================
# FUNC 2 (4 punti)
# =============================================================================
def func2(text: str, banned_words: list[str]) -> str:
    """
    Filtro Chat: Censura le parole proibite presenti nella lista banned_words.

    REGOLE:
    - Sostituisci la parola con tanti '*' quanti sono i suoi caratteri.
    - Il controllo deve essere case-insensitive (es: 'mela' censura 'MELA').
    - Mantieni intatta la punteggiatura e il case originale delle parole non censurate.

    Esempio:
        text = "Attenzione all'ORCO nel bosco!"
        banned_words = ["orco"]
        Restituisce: "Attenzione all'**** nel bosco!"
    """
    import re
    # Creiamo un set di parole bannate in minuscolo per ricerca efficiente
    banned_set = {word.lower() for word in banned_words}

    # Funzione di sostituzione per re.sub
    def replace(match):
        word = match.group(0)
        if word.lower() in banned_set:
            return "*" * len(word)
        return word

    # Cerchiamo sequenze di caratteri alfanumerici (parole)
    return re.sub(r'\w+', replace, text)


# =============================================================================
# FUNC 3 (4 punti)
# =============================================================================
def func3(type_chart: dict, attacker_types: list[str], defender_types: list[str]) -> float:
    """
    Calcola il moltiplicatore di danno basato sui tipi.

    LOGICA:
    Moltiplica tra loro i coefficienti di ogni tipo dell'attaccante contro
    ogni tipo del difensore consultando il dizionario type_chart.

    Esempio:
        type_chart = {'Fuoco': {'Erba': 2.0, 'Acqua': 0.5}}
        attacker = ['Fuoco']
        defender = ['Erba', 'Acqua']
        Calcolo: 2.0 (Fuoco vs Erba) * 0.5 (Fuoco vs Acqua) = 1.0
    """
    total_multiplier = 1.0
    for a_type in attacker_types:
        if a_type in type_chart:
            for d_type in defender_types:
                # Se il tipo difensore è nel grafico del tipo attaccante, moltiplica
                mult = type_chart[a_type].get(d_type, 1.0)
                total_multiplier *= mult
    return total_multiplier


# =============================================================================
# FUNC 4 (4 punti)
# =============================================================================
def func4(matrix: list[list[int]]) -> list[int]:
    """
    Data una matrice M x N, restituisce i suoi elementi seguendo un ordine a spirale.
    L'ordine inizia da (0,0) verso destra, poi scende, poi sinistra, poi sale.

    Esempio:
        matrix = [[1, 2],
                  [3, 4]]
        Restituisce: [1, 2, 4, 3]
    """
    if not matrix: return []
    res = []
    r_start, r_end = 0, len(matrix) - 1
    c_start, c_end = 0, len(matrix[0]) - 1

    while r_start <= r_end and c_start <= c_end:
        # Destra
        for j in range(c_start, c_end + 1):
            res.append(matrix[r_start][j])
        r_start += 1

        # Giù
        for i in range(r_start, r_end + 1):
            res.append(matrix[i][c_end])
        c_end -= 1

        # Sinistra (se ancora valido)
        if r_start <= r_end:
            for j in range(c_end, c_start - 1, -1):
                res.append(matrix[r_end][j])
            r_end -= 1

        # Su (se ancora valido)
        if c_start <= c_end:
            for i in range(r_end, r_start - 1, -1):
                res.append(matrix[i][c_start])
            c_start += 1

    return res


# =============================================================================
# FUNC 5 (6 punti)
# =============================================================================
import images
def func5(path_in: str, target_color: tuple[int, int, int]) -> tuple[int, int, int, int]:
    """Identifica il rettangolo target con l'area maggiore."""
    img = images.load(path_in)
    h, w = len(img), len(img[0])
    visited = [[False for _ in range(w)] for _ in range(h)]

    max_area = -1
    best_rect = (0, 0, 0, 0)

    for r in range(h):
        for c in range(w):
            if img[r][c] == target_color and not visited[r][c]:
                # Trovato un nuovo rettangolo, calcoliamo dimensioni
                curr_w = 0
                while c + curr_w < w and img[r][c + curr_w] == target_color:
                    curr_w += 1

                curr_h = 0
                while r + curr_h < h and img[r + curr_h][c] == target_color:
                    curr_h += 1

                # Marciamo come visitati
                for i in range(r, r + curr_h):
                    for j in range(c, c + curr_w):
                        visited[i][j] = True

                area = curr_w * curr_h
                if area > max_area:
                    max_area = area
                    best_rect = (c, r, curr_w, curr_h)
                elif area == max_area:
                    # Tie-break: y minore, poi x minore (già garantito dal ciclo for)
                    pass

    return best_rect if max_area != -1 else (0, 0, 0, 0)


# =============================================================================
# EX 1 (6 punti) - RICORSIVO
# =============================================================================
def solve(arr, n, s, index, count, current_sum):
    # Caso base: abbiamo selezionato n elementi
    if count == n:
        return current_sum == s
    # Caso base: abbiamo finito gli elementi dell'array
    if index == len(arr):
        return False

    # Opzione 1: Includi l'elemento corrente
    include = solve(arr, n, s, index + 1, count + 1, current_sum + arr[index])
    if include: return True

    # Opzione 2: Escludi l'elemento corrente
    exclude = solve(arr, n, s, index + 1, count, current_sum)
    return exclude


def ex1(arr: list[int], n: int, s: int) -> bool:
    """
    Si definisca una funzione ricorsiva o che
    utilizza funzioni o metodi ricorsivi che determini se esiste un
    sottoinsieme di 'arr' composto da esattamente 'n' elementi la cui somma è 's'.

    Esempio:
        arr = [1, 5, 2], n = 2, s = 3
        Restituisce: True (il sottoinsieme è [1, 2])
    """



    return solve(arr, n, s, 0, 0, 0)


# =============================================================================
# EX 2 (6 punti) - RICORSIVO
# =============================================================================

def ex2(data: dict, key_chain: list[str]) -> int:
    """Esplora ricorsivamente un dizionario seguendo una catena di chiavi."""
    # Caso base: chain vuota o input non è un dizionario
    if not key_chain or not isinstance(data, dict):
        return 1

    first_key = key_chain[0]

    # Se la chiave esiste e porta a un altro dizionario, proseguiamo
    if first_key in data and isinstance(data[first_key], dict):
        return 1 + ex2(data[first_key], key_chain[1:])

    # Se la chiave esiste ma non è un dict, contiamo questo livello e finiamo
    if first_key in data:
        return 2

    # Se la chiave non esiste, abbiamo visitato solo il livello corrente
    return 1


# =============================================================================
if __name__ == '__main__':
    # Spazio per test manuali
    pass
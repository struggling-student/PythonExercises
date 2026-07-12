#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OPERAZIONI PRELIMINARI:
1) Salvare il file come program.py
2) Assegnare Nome, Cognome e Matricola nelle variabili sottostanti.

REGOLE D'ESAME:
- Punteggio: Il voto è la somma dei punti; necessario >= 18 per il superamento.
- Grader: Per testare la ricorsione, assicurarsi che DEBUG = False nel file grade.py.
"""

nome = "NOME"
cognome = "COGNOME"
matricola = "MATRICOLA"


# =============================================================================
# FUNC 1 (2 punti)
# =============================================================================
"""
Implementa la funzione func1(pokemon_list: list[dict]) -> list[str] che
- riceve come argomento una lista di pokemon
- ritorna i 3 migliori in base al loro "Power Score"

Ciascun pokemon è rappresentato da un dizionario con le chiavi 'name', 'atk', 'spd', 'def'
Ad esempio: {'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}

Il "Power Score" è ottenuto come (atk * 1.5) + (spd * 1.2) + def
Nell'esempio il valore è 37.7 = 10*1.5+10*1.2+10

I pokemon devono essere ordinati:
1. Per punteggio decrescente (dal più alto al più basso).
2. In caso di parità di punteggio, in ordine alfabetico di name (A-Z).

Restituisce: Una lista con i nomi dei primi 3 personaggi in classifica.

Esempio:
    pokemon_list = [{'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}, # Score 37.0
                    {'name': 'B', 'atk': 10, 'spd': 10, 'def': 10}] # Score 37.0
    Restituisce: ['A', 'B'] (perché A viene prima di B in ordine alfabetico)
"""
def func1(pokemon_list: list[dict]) -> list[str]:
    pass
    # inserisci qui il tuo codice

# =============================================================================
# FUNC 2 (4 punti)
# =============================================================================
"""
Filtro Chat: Censura le parole proibite presenti nella lista banned_words.

REGOLE:
- Sostituisci nel testo 'text' la parola sostituendola con tanti '*' quanti sono i suoi caratteri.
- Il controllo deve essere case-insensitive (es: 'mela' censura 'MELA').
- Mantieni intatta la punteggiatura e il case originale delle parole non censurate.

Esempio:
    text = "Attenzione all'ORCO nel bosco! (ma non all'OrCoNe)"
    banned_words = ["orco"]
    Restituisce: "Attenzione all'**** nel bosco!  (ma non all'OrCoNe)"
"""
def func2(text: str, banned_words: list[str]) -> str:
    pass
    # inserisci qui il tuo codice

# =============================================================================
# FUNC 3 (2 punti)
# =============================================================================
"""
Calcola il moltiplicatore di danno tra un attaccante e dun difensore, 
basato sui tipi di creature.

LOGICA:
Moltiplica tra loro i coefficienti di ogni tipo dell'attaccante contro
ogni tipo del difensore consultando il dizionario type_chart.

Nota: se un tipo non è presente, il suo contributo è 1.

Esempio:
    type_chart = {'Fuoco': {'Erba': 2.0, 'Acqua': 0.5}}
    attacker = ['Fuoco']
    defender = ['Erba', 'Acqua']
    Calcolo: 2.0 (Fuoco vs Erba) * 0.5 (Fuoco vs Acqua) = 1.0
"""
def func3(type_chart: dict, attacker_types: list[str], defender_types: list[str]) -> float:
    pass
    # inserisci qui il tuo codice


# =============================================================================
# FUNC 4 (4 punti)
# =============================================================================
"""
Data una matrice M x N, restituisce i suoi elementi seguendo un ordine a spirale.
L'ordine inizia da (0,0) verso destra, poi scende, poi sinistra, poi sale.

Esempio:
    matrix = [[1, 2],
              [3, 4]]
    Restituisce: [1, 2, 4, 3]
"""
def func4(matrix: list[list[int]]) -> list[int]:
    pass
    # inserisci qui il tuo codice


# =============================================================================
# FUNC 5 (8 punti)
# =============================================================================
"""
Analizza un'immagine PNG (caricata tramite images.load) contenente diversi
rettangoli pieni di colore 'target_color' su uno sfondo nero (0, 0, 0).

La funzione deve identificare il rettangolo con l'AREA MAGGIORE e 
restituire le sue informazioni come una tupla (x, y, w, h) dove:
- x, y sono le coordinate del pixel in alto a sinistra.
- w, h sono la larghezza e l'altezza del rettangolo.

REGOLE:
- I rettangoli non si toccano mai (nemmeno in diagonale).
- Se due rettangoli hanno la stessa area massima, scegli quello con 
  la coordinata 'y' minore (più in alto); se anche 'y' è uguale, 
  quello con 'x' minore.
- Se il colore non è presente, restituisci (0, 0, 0, 0).

Esempio:
    Un'immagine con un quadrato 2x2 e un rettangolo 3x4 del colore target.
    La funzione restituirà i dati relativi al rettangolo 3x4.
"""
import images
def func5(path_in: str, target_color: tuple[int, int, int]) -> tuple[int, int, int, int]:
    pass
    # inserisci qui il tuo codice


# =============================================================================
# EX 1 (6 punti) - RICORSIVO
# =============================================================================
"""
Si definisca una funzione ricorsiva o che
utilizza funzioni o metodi ricorsivi che determini se esiste un
sottoinsieme di 'arr' composto da esattamente 'n' elementi la cui somma è 's'.

Esempio:
    arr = [1, 5, 2], n = 2, s = 3
    Restituisce: True (il sottoinsieme è [1, 2])
"""


def ex1(arr: list[int], n: int, s: int) -> bool:
    pass
   # inserisci qui il tuo codice


# =============================================================================
# EX 2 (6 punti) - RICORSIVO
# =============================================================================
"""
Si definisca una funzione ricorsiva o che
utilizza funzioni o metodi ricorsivi che esplora un dizionario 'data'
seguendo una catena di chiavi 'key_chain' e restituisce la profondità
massima raggiunta (numero di dizionari attraversati).

REGOLE:
- Inizia dal dizionario 'data' (profondità 1).
- Cerca la prima chiave di 'key_chain' in 'data'.
- Se trovata e il valore è un dizionario, incrementa la profondità e
  prosegui ricorsivamente nel sottodizionario usando le chiavi rimanenti.
- Se la chiave non è presente, o il valore non è un dizionario, o
  'key_chain' è vuota, l'esplorazione termina.

Esempio:
    data = {'user': {'settings': {'theme': 'dark'}}}
    key_chain = ['user', 'settings', 'theme']
    Esplorazione: data -> user (dict) -> settings (dict) -> theme (str, fine)
    Ritorna: 3
"""


def ex2(data: dict, key_chain: list[str]) -> int:
    pass
	   # inserisci qui il tuo codice


# =============================================================================
if __name__ == '__main__':
    # Spazio per test manuali
    pass
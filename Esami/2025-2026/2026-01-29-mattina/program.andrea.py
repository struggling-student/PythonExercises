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


nome = "A"
cognome = "S"
matricola = "42"


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
    def criterio(pokemon):
        punteggio = pokemon['atk'] * 1.5 + pokemon['spd'] * 1.2 + pokemon['def']
        return -punteggio, pokemon['name']
    return [ p['name'] for p in sorted(pokemon_list, key=criterio)[:3] ]

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
    banned_lower = [ p.lower() for p in banned_words ]
    pezzi = []
    parola = ''
    for c in text:
        if c.isalpha():
            parola += c
        else:
            pezzi.append(parola)
            parola = ''
            pezzi.append(c)
    pezzi.append(parola)
    risposta = ''
    for p in pezzi:
        if p.lower() in banned_lower:
            risposta += '*'*len(p)
        else:
            risposta += p
    return risposta

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
    moltiplicatore = 1
    for x in attacker_types:
        if x in type_chart:
            for y in defender_types:
                if y in type_chart[x]:
                    moltiplicatore *= type_chart[x][y]
    return moltiplicatore


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
    W,H = len(matrix[0]), len(matrix)
    def inside(x,y):
        return 0 <= x < W and 0 <= y < H
    x,y = 0,0
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    dir = 0
    spirale=[]
    for _ in range(W*H):
        spirale.append(matrix[y][x])
        matrix[y][x] = None
        dx, dy = directions[dir]
        X = x+dx
        Y = y+dy
        if inside(X,Y) and matrix[Y][X] is not None:
            x,y = X,Y
        else:
            dir += 1
            dir %= 4
            dx, dy = directions[dir]
            x += dx
            y += dy
    return spirale

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
    img = images.load(path_in)
    W, H = len(img[0]), len(img)
    black = (0, 0, 0)
    rettangoli = []
    def is_top_left_corner(x, y):
        return (target_color == img[y][x]
                    and (x==0 or img[y][x-1] == black )
                    and (y==0 or img[y-1][x] == black))
    for y,riga in enumerate(img):
        for x,pixel in enumerate(riga):
            if is_top_left_corner(x, y):
                larghezza = 0
                for X in range(x,W):
                    if img[y][X] == black:
                        break
                    else:
                        larghezza += 1
                altezza = 0
                for Y in range(y,H):
                    if img[Y][x] == black:
                        break
                    else:
                        altezza += 1
                rettangoli.append((x,y,larghezza, altezza))
    def criterio(rettangolo):
        x, y, larghezza, altezza = rettangolo
        return -larghezza*altezza,y,x
    rettangoli.sort(key=criterio)
    #print(rettangoli)
    if rettangoli:
        return rettangoli[0]
    else:
        return 0,0,0,0

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
    if len(arr) < n:
        return False
    S = sum(arr)
    if S == s and n == len(arr):
        return True
    for i,x in enumerate(arr):
        resto = arr.copy()
        resto.pop(i)
        if ex1(resto, n, s):
            return True
    return False

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
    if type(data) != dict:
        return 1
    if not key_chain:
        return 1
    key, *rest = key_chain
    if key not in data:
        return 1
    return 1 + ex2(data[key], rest)

# =============================================================================
if __name__ == '__main__':
    # Spazio per test manuali
    pass
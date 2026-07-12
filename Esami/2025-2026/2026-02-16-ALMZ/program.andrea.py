#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Operazioni da fare PRIMA DI TUTTO:
1) Salvare questo file col nome program.py
2) Inserire NOME, COGNOME, MATRICOLA nelle variabili sottostanti

ATTENZIONE: NON importate altre librerie

Valutazione:
- Il punteggio finale è la somma dei punti degli esercizi corretti.
- Per superare la prova è necessario punteggio >= 18 (>= 15 se con DSA).
"""

nome = "A"
cognome = "S"
matricola = "42"


# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 2 punti — Retro arcade combo scoring

INPUT:
- moves: stringa di comandi composta dai caratteri:
    'L' (left), 'R' (right), 'U' (up), 'D' (down), 'F' (fire)

REGOLE:
- Ogni 'F' vale 10 punti.
- Se un carattere 'F' è preceduto IMMEDIATAMENTE dalla sequenza "UUDD"
  (cioè i 4 caratteri precedenti sono esattamente U,U,D,D), allora quel colpo vale 50 punti.
- Devi contare quante volte questa combo viene usata (cioè quante 'F' “potenziate” ci sono).

OUTPUT:
- ritorna una tupla (score_totale, numero_combo_usate)

WORKED EXAMPLE (passo-passo):
moves = "LUU D D FFR"  (senza spazi: "LUUDDFFR")
analizzo le 'F':
  - prima 'F': i 4 caratteri precedenti sono "UUDD" -> vale 50 (combo=1)
  - seconda 'F': i 4 caratteri precedenti sono "DDF"  + qualcosa, non "UUDD" -> vale 10
score = 50 + 10 = 60, combo = 1
output: (60, 1)
"""
def func1(moves: str) -> tuple[int, int]:
    pass
    totali = moves.count('F')
    combo = moves.count('UUDDF')
    return totali * 10 + combo * 40, combo


# %% ----------------------------------- FUNC.2 ----------------------------------- #
"""
Func 2: 2 punti — Carte: conteggio coppie e tris (di valori)

INPUT:
- hand: lista di interi 1..13 che rappresentano i valori delle carte (il seme non conta).

OUTPUT:
- una tupla (num_coppie, num_tris) dove:
  - num_coppie conta quanti valori compaiono ESATTAMENTE 2 volte
  - num_tris   conta quanti valori compaiono ESATTAMENTE 3 volte

NOTE IMPORTANTI:
- Un poker (4 uguali) NON conta né come coppia né come tris.
- Una full house (3+2) conta come (1 tris, 1 coppia).
- L'ordine delle carte in hand è irrilevante.

WORKED EXAMPLE (passo-passo):
hand = [2, 2, 9, 9, 9, 7, 7, 7, 7, 4, 4]
frequenze:
  2 -> 2 volte  => +1 coppia
  9 -> 3 volte  => +1 tris
  7 -> 4 volte  => poker => +0
  4 -> 2 volte  => +1 coppia
output: (2, 1)
"""
def func2(hand: list[int]) -> tuple[int, int]:
    pass
    D = { x : hand.count(x) for x in set(hand) }
    vals = list(D.values())
    return vals.count(2), vals.count(3)

# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 6 punti — Tabletop: massimo danno da notazione dadi

INPUT:
- expr: stringa che rappresenta un'espressione con termini separati da '+' o '-'.
  Ogni termine è:
    - un intero (es. "3")
    - oppure una notazione XdY (es. "2d6") con X>=1 e Y>=2

SIGNIFICATO:
- XdY rappresenta la somma di X lanci di un dado a Y facce (numerate da 1 a Y).
- Quindi XdY vale al massimo X*Y.

OUTPUT:
- un intero: il massimo valore possibile dell'espressione.

WORKED EXAMPLE (passo-passo):
expr = "3+2d18-1d6"
massimo dei termini:
  3     -> 3
  2d18  -> 2*18 = 36
  1d6   -> 1*6 = 6
applico i segni:
  3 + 36 - 6 = 33
output: 33
"""
def func3(expr: str) -> int:
    pass
    def frammenta_expr(expr: str) -> int:
        valore = ''  # parte corrente
        sequenza = []  # sequenza di parti
        for c in expr:
            if c in '+-':
                sequenza += [valore, c]
                valore = ''
            else:
                valore += c
        sequenza += [valore]
        return sequenza
    def converti(termine: str) -> int:
        if 'd' in termine:
            X, Y = termine.split('d')
            return int(X) * int(Y)
        else:
            return int(termine)
    sequenza = frammenta_expr(expr)
    print(expr, sequenza)
    risultato = converti(sequenza[0])
    for i in range(1,len(sequenza),2):
        if sequenza[i] == '-':
            risultato -= converti(sequenza[i+1])
        elif sequenza[i] == '+':
            risultato += converti(sequenza[i+1])
    return risultato

# %% ----------------------------------- FUNC.4 ----------------------------------- #
"""
Func 4: 4 punti — Deck shuffler (cut/reverse/swap)

INPUT:
- deck_size: numero di carte nel mazzo iniziale
  mazzo iniziale = [1, 2, 3, ..., deck_size]
- top_n: quante carte restituire dalla cima a fine elaborazione
- path: file di testo con un comando per riga (righe vuote ignorate)

COMANDI:
- "CUT k"
    se k > 0: sposta le prime k carte in fondo
    se k < 0: sposta le ultime |k| carte in cima
- "REVERSE"
    inverte il mazzo
- "SWAP a b"
    scambia le carte alle posizioni a e b (posizioni 0-index)

OUTPUT:
- la lista delle prime top_n carte dopo aver applicato tutti i comandi.

WORKED EXAMPLE (passo-passo):
deck_size=5 -> mazzo iniziale [1,2,3,4,5]
comandi:
  CUT 2     [1,2,3,4,5] -> [3,4,5,1,2]
  SWAP 0 3  [3,4,5,1,2] -> [1,4,5,3,2]
  REVERSE   [1,4,5,3,2] -> [2,3,5,4,1]
top_n=3 -> output: [2,3,5]
"""


def func4(path: str, deck_size: int, top_n: int) -> list[int]:
    pass
    deck = list(range(1, deck_size + 1))
    with open(path, mode='r', encoding='utf-8') as FIN:
        for line in FIN:
            if line.strip() == '': continue
            comando, *params = line.split()
            params = list(map(int, params))
            if comando == 'CUT':
                where = params[0]
                deck = deck[where:] + deck[:where]
            elif comando == 'REVERSE':
                deck = deck[::-1]
            elif comando == 'SWAP':
                X,Y = params
                deck[X], deck[Y] = deck[Y], deck[X]
    return deck[:top_n]


# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 6 punti — Retro sprite palette swap (cambio palette)

INPUT:
- path_in:  percorso dell'immagine PNG di input
- path_out: percorso dove salvare l'immagine risultante
- c1, c2: due colori RGB (tuple) da scambiare

OPERAZIONE:
- ogni pixel che è esattamente uguale a c1 diventa c2
- ogni pixel che è esattamente uguale a c2 diventa c1
- tutti gli altri pixel rimangono invariati
- salva l'immagine risultante in path_out

OUTPUT:
- ritorna (count_c1, count_c2) dove:
  - count_c1 = numero di pixel che in input erano c1
  - count_c2 = numero di pixel che in input erano c2

WORKED EXAMPLE (passo-passo):
immagine 1x3: [c1, (0,0,0), c2]
- pixel0 è c1 -> diventa c2 (count_c1=1)
- pixel1 è nero -> resta nero
- pixel2 è c2 -> diventa c1 (count_c2=1)
output: (1, 1) e l'immagine salvata è [c2, (0,0,0), c1]
"""
import images
def func5(path_in: str, path_out: str, c1: tuple[int, int, int], c2: tuple[int, int, int]) -> tuple[int, int]:
    pass
    img = images.load(path_in)
    count1 = count2 = 0
    for y, row in enumerate(img):
        for x, col in enumerate(row):
            if col == c1:
                count1 += 1
                img[y][x] = c2
            elif col == c2:
                count2 += 1
                img[y][x] = c1
    images.save(img, path_out)
    return count1, count2


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 6 punti (RICORSIVO) — Tabletop: numero di combinazioni (ordine non conta)

INPUT:
- rolls: lista di interi positivi (valori disponibili, usabili infinite volte)
- target: somma da raggiungere

OUTPUT:
- numero di modi diversi per ottenere esattamente target usando elementi di rolls,
  SENZA considerare l'ordine.
  (Quindi 1+3 e 3+1 contano come lo stesso modo.)

VINCOLO:
- Deve essere ricorsiva (o usare funzioni/metodi ricorsivi).

WORKED EXAMPLE (passo-passo):
rolls = [1, 2, 3], target = 4
modi (senza ordine):
  - 1+1+1+1
  - 1+1+2
  - 2+2
  - 1+3
totale = 4
output: 4
"""

def ex1(rolls: list[int], target: int) -> int:
    pass
    combinazioni = _ex1(rolls, target)
    return len(combinazioni)

def _ex1(rolls: list[int], target) -> set[set[int]]:
    if target == 0:
        return {tuple()}
    soluzioni = set()
    for roll in rolls:
        if roll <= target:
            remaining = target - roll
            sottosoluzioni = _ex1(rolls, remaining)
            for S in sottosoluzioni:
                soluzioni.add(tuple(sorted([*S, roll])))
    return soluzioni

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti (RICORSIVO) — Massima somma su percorso radice->foglia

DEFINIZIONE:
- Un percorso valido parte dalla radice e termina in una foglia
  (nodo senza figli).
- Il valore del percorso è la somma dei valori dei nodi attraversati.

OUTPUT:
- la massima somma ottenibile tra tutti i percorsi radice->foglia.
- se root è None: ritorna 0.

VINCOLO:
- Deve essere ricorsiva (o usare funzioni/metodi ricorsivi).

WORKED EXAMPLE (passo-passo):
      5                
     / \
   -2   7
       /
      1

percorsi:
  5 -> -2  somma = 3
  5 -> 7 -> 1 somma = 13
massimo = 13
output: 13
"""
import tree
def ex2(root: tree.BinaryTree) -> int:
    pass
    percorsi = _ex2(root)
    return max(map(sum, percorsi))

def _ex2(root: tree.BinaryTree) -> list[list[int]]:
    if root is None:
        return [[]]
    return [ [root.value,*P] for P in _ex2(root.left) + _ex2(root.right) ]


if __name__ == '__main__':
    print('*' * 50)
    print('Eseguire grade.py per il test automatico.')
    print('*' * 50)
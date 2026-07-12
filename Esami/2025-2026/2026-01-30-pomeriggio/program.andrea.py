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

# NON importate altre librerie

import images
import tree
import math
import json
import os

# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 4 punti

Implementa la funzione func1(s: str) -> bool che verifica se una stringa 
contenente solo i caratteri parentesi '(', ')', '{', '}', '[' e ']' è bilanciata.
Una stringa è bilanciata se ogni parentesi aperta viene chiusa dal tipo 
corrispondente nell'ordine corretto.

Suggerimento: usate una pila per ricordarvi quali parentesi vanno chiuse

Esempio:
    s = "{[]()[]()}" 
    Output: True

    s = "([)]" 
    Output: False (perché la parentesi ']' deve chiudere prima della ')')
"""


def func1(s: str) -> bool:
    pass
    # inserisci qui il tuo codice
    coppie = {'[':']', '{':'}', '(':')'}
    viste = []
    for c in s:
        if c in coppie:
            viste.append(coppie[c])
        else:
            if not viste:
                return False
            if viste[-1] != c:
                return False
            viste.pop()
    if viste:
        return False
    else:
        return True

# %% ----------------------------------- FUNC.2 ----------------------------------- #
"""
Func 2: 2 punti

Implementa la funzione func2(studenti: list[dict]) -> list[str] che riceve una 
lista di dizionari (es. {"nome": "Mario", "media": 29}) ed estrae i nomi di chi 
ha media strettamente superiore a 28.
REQUISITO: Usa SOLO una list comprehension.

Esempio:
    studenti = [{"nome": "A", "media": 29}, {"nome": "B", "media": 27}, {"nome": "C", "media": 28.5}]
    Output: ["A", "C"]
"""


def func2(studenti: list[dict]) -> list[str]:
    return [ s['nome'] for s in studenti if s['media'] > 28 ] # scrivi la comprehension qui dentro


# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 4 punti

Implementa la funzione func3(file1: str, file2: str) -> list[str] che confronta
due file di testo riga per riga e restituisce una lista di stringhe che indicano 
le righe che sono diverse.
Il formato deve essere: "Riga [n]: [testo1] != [testo2]" dove n parte da 1.

Esempio:
    file1 ha: "mela\npera"
    file2 ha: "mela\nbanana"
    Output: ["Riga 2: pera != banana"]
"""


def func3(file1: str, file2: str) -> list[str]:
    pass
    # inserisci qui il tuo codice
    risultato = []
    with open(file1) as f1, open(file2) as f2:
        for i, (riga1, riga2) in enumerate(zip(f1, f2), start=1):
            riga1 = riga1.replace("\n", "")
            riga2 = riga2.replace("\n", "")
            if riga1 != riga2:
                risultato.append(f"Riga {i}: {riga1} != {riga2}")
    return risultato


# %% ----------------------------------- FUNC.4 ----------------------------------- #
"""
Func 4: 2 punti

Implementa la funzione func4(n: int) -> list[tuple[int,int]] che genera una 
lista di coordinate (x, y) per una griglia n x n (con x e y da 0 a n-1) 
dove la somma x + y è un numero pari.

Esempio:
    n = 2
    Coordinate possibili: (0,0), (0,1), (1,0), (1,1)
    Somme: 0+0=0 (pari), 0+1=1 (dispari), 1+0=1 (dispari), 1+1=2 (pari)
    Output: [(0, 0), (1, 1)]
"""


def func4(n: int) -> list[tuple[int, int]]:
    pass
    # inserisci qui il tuo codice
    return [ (x,y) for x in range(n) for y in range(n) if (x+y)%2==0]

# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 6 punti

Implementa la funzione func5(path_in: str, path_out: str, k: int) che crea un 
effetto "Pixel Art" o "Mosaico". 
La funzione deve dividere l'immagine in blocchi quadrati di dimensione k x k pixel.
Per ogni blocco, calcola il colore medio (media aritmetica dei canali R, G, B) 
di tutti i pixel contenuti nel blocco e sostituisci ogni pixel del blocco 
con quel colore medio (arrotondato all'intero più vicino usando round()).

La funzione deve tornare il numero di blocchi che ha colorato.

Note:
- Gestisci i bordi: se l'immagine non è multiplo di k, l'ultimo blocco sarà più piccolo.
- Usa images.load(path_in) e images.save(img, path_out).

Esempio:
    Se k=5, un blocco 10x10 di pixel con vari colori diventeranno 4 blocchi 
    di colore uniforme pari alla media dei colori originali di ciascun blocco.
    
"""
def func5(path_in: str, path_out: str, k: int):
    pass
    # inserisci qui il tuo codice
    img = images.load(path_in)
    W,H = len(img[0]),len(img)
    def inside(x,y):
        return 0<=x<W and 0<=y<H
    blocchi = 0
    for x in range(0,W,k):
        for y in range(0,H,k):
            blocchi += 1
            R = G = B = N = 0
            for dx in range(k):
                for dy in range(k):
                    if inside(x+dx,y+dy):
                        r, g, b = img[y+dy][x+dx]
                        N +=1
                        R += r
                        G += g
                        B += b
            R = round(R/N)
            G = round(G/N)
            B = round(B/N)
            for dx in range(k):
                for dy in range(k):
                    if inside(x+dx,y+dy):
                        img[y+dy][x+dx] = (R,G,B)
    images.save(img, path_out)
    return blocchi



# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 8 punti

Si definisca una funzione RICORSIVA o che utilizza funzioni o metodi ricorsivi 
ex1(candidates: list[int], target: int) -> list[list[int]] che trova tutte le 
combinazioni uniche di candidati che sommano esattamente al target. 
Ogni numero della lista 'candidates' può essere usato un numero illimitato di volte.

Esempio:
    candidates = [2, 3, 6, 7], target = 7
    Combinazioni possibili: [2, 2, 3] (somma 7) e [7] (somma 7)
    Output: [[2, 2, 3], [7]] (l'ordine delle combinazioni non conta)
    
SUGGERIMENTO: evitate di aggiungere all'elenco delle combinazioni delle combinazioni già generate
"""


def ex1(candidates: list[int], target: int) -> list[list[int]]:
    pass
    # inserisci qui il tuo codice
    risultato = []
    if target == 0:
        return [ [] ]
    if candidates == []:
        return []
    # filter out too big
    candidates = [ x for x in candidates if x <= target ]
    for candidate in candidates:
        if candidate == target:
            if [candidate] not in risultato:
                risultato.append([candidate])
        else:
            sottosomme = ex1(candidates, target-candidate)
            for S in sottosomme:
                XX = sorted([candidate]+S)
                if XX not in risultato:
                    risultato.append(XX)
    return risultato

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti

Si definisca una funzione RICORSIVA o che utilizza funzioni o metodi ricorsivi 
ex2(root: tree.BinaryTree) -> str per gestire la serializzazione di un albero 
binario in formato stringa.

La funzione deve restituire una stringa che rappresenta l'albero utilizzando 
una visita POST-ORDER (Sinistra, Destra, Radice). 
I valori dei nodi devono essere separati da una virgola. I nodi vuoti (None) 
devono essere rappresentati dal carattere '#'.

Esempio:
        Albero: 
              1          |
             / \         |
            2   3        |

    Visita Post-order: 2 (con figli None) -> 3 (con figli None) -> 1
    Output: "#,#,2,#,#,3,1"
"""


def ex2(root: tree.BinaryTree) -> str:
    pass
    # inserisci qui il tuo codice
    if root is None:
        return "#"
    return f"{ex2(root.left)},{ex2(root.right)},{root.value}"

######################################################################################

if __name__ == '__main__':
    # Spazio per test manuali
    print('*' * 50)
    print('Eseguire grade.py per il test automatico.')
    print('*' * 50)
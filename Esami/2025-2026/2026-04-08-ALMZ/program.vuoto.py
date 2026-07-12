#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

ATTENZIONE: NON importate altre librerie oltre a quelle già presenti

Per superare l'esame è necessario:
    - ottenere un punteggio maggiore o uguale a 18 (15 per DSA)

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome = "NOME"
cognome = "COGNOME"
matricola = "MATRICOLA"


# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 2 punti

Implementa la funzione func1(n: int) -> int che conta il numero di bit impostati a 1
nella rappresentazione binaria di n.

Esempio:
    n = 31 (binario 11111) -> expected: 5
    n = 16 (binario 10000) -> expected: 1
"""
def func1(n: int) -> int:
    pass


# %% ----------------------------------- FUNC.2 ---------------------------------- #
"""
Func 2: 3 punti

Dato un messaggio contenente dei tag tipo [color:nome_colore]testo[/color], 
sostituisci i tag con i codici esadecimali presenti nel dizionario 'colors'.
Il formato di output richiesto per il tag è <#CODICE>testo</#CODICE>.

Esempio:
    message: "Benvenuto a [color:red]Fuocovivo[/color]!"
    colors: {'red': '#FF0000'}
    Risultato: "Benvenuto a <#FF0000>Fuocovivo</#FF0000>!"

NOTA: non usate la libreria 're'
"""
def func2(message: str, colors: dict) -> str:
    pass


# %% ----------------------------------- FUNC.3 ---------------------------------- #
"""
Func 3: 3 punti

Verifica se un giocatore è in grado di creare un oggetto componendolo
dai materiali nel suo inventario.
Restituisci True se ogni materiale richiesto nella ricetta è presente
nell'inventario in quantità sufficiente (maggiore o uguale). 
Se un materiale della ricetta non esiste o è insufficiente nell'inventario, 
l'esito è False.
L'inventario è un dizionario nel formato {nome_materiale: quantità}.
La ricetta è fornita nello stesso formato.

Esempio:
    inventory: {'ferro': 5, 'legno': 10}
    recipe: {'ferro': 3, 'pelle': 1}
    Risultato: False (manca la pelle nell'inventario)
"""
def func3(inventory: dict, recipe: dict) -> bool:
    pass


# %% ----------------------------------- FUNC.4 ---------------------------------- #
"""
Func 4: 4 punti

Implementa la funzione func4(base_stats: dict, equipment: list[dict]) -> dict
che riceve come argomenti:
    base_stats: un dizionario con le chiavi 'att' (attacco) e 'def' (difesa) e valori numerici
    equipment: una lista di dizionari con chiavi
        'stat': e valore 'att' o 'def'
        'type': e valore 'add' o 'mul'
        'val': e valore numerico

Calcola le statistiche finali di un giocatore applicando i bonus 
dell'equipment alle base_stats.
Ogni oggetto dell'equipment specifica quale statistica influenza tramite la chiave 'stat'.

ORDINE DI APPLICAZIONE PER OGNI STATISTICA:
1. Applica prima tutti i bonus 'add' alla specifica statistica di base.
2. Sul risultato, applica tutti i bonus 'mul' della stessa statistica.

Esempio:
    base: {'att': 100, 'def': 50}
    eq: [
        {'stat': 'att', 'type': 'add', 'val': 10},
        {'stat': 'att', 'type': 'mul', 'val': 1.1},
        {'stat': 'def', 'type': 'add', 'val': 5}
    ]
    Risultato: {'att': 121.0, 'def': 55.0}

Infatti al valore della statistica 'att' va prima sommato 10 
e poi va moltiplicato per 1.1, mentre al valore della statistica 'def' 
va sommato 5
"""
def func4(base_stats: dict, equipment: list[dict]) -> dict:
    pass


# %% ----------------------------------- FUNC.5 ---------------------------------- #
"""
Func 5: 8 punti

Implementa la funzione func5(path_in: str, path_out: str) che carica un'immagine PNG 
contenente un'unica macchia di pixel colorati su sfondo nero. 
La funzione deve:
1. Calcolare il baricentro (x_media, y_media) di tutti i pixel non neri.
2. Salvare in path_out una nuova immagine dove la macchia originale è ruotata 
   di 90 gradi in senso orario attorno al suo baricentro.
3. Tornare il baricentro (x_media, y_media)

Note:
- Usa round per ottenere le coordinate del baricentro.
- Se l'immagine ruotata esce dai bordi, ritagliala.

Suggerimento: 
    - calcolate il baricentro della macchia
    - calcolate dove si trova ciascun pixel della macchia rispetto al baricentro
    - trovate la posizione del pixel ruotato di 90° in senso orario
    - copiatelo nella nuova immagine (se è all'interno)

"""
import images
def func5(path_in: str, path_out: str):
    pass


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si implementi la funzione ex1(root: tree.BinaryTree), ricorsiva o che utilizza funzioni
o metodi ricorsivi, che verifica se l'albero binario è bilanciato in altezza.

Un albero è bilanciato se, per ogni nodo, la differenza di altezza
tra il sottoalbero sinistro e quello destro non è superiore a 1.
"""
import tree


def ex1(root: tree.BinaryTree) -> bool:
    pass


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca una funzione ricorsiva o che utilizza funzioni
o metodi ricorsivi che riceve una lista che può contenere
interi o altre liste nidificate a qualsiasi livello.
La funzione deve calcolare la somma di tutti i numeri PARI incontrati.

REGOLE:
- Se un elemento è una lista, bisogna esplorarla ricorsivamente.
- Se è un intero ed è pari, va sommato al totale.
- Se è un intero dispari o una lista vuota, non contribuisce alla somma.

Esempio:
    data = [1, [2, [3, 4]], 6]
    Numeri pari: 2, 4, 6
    Output: 12
"""
def ex2(data: list) -> int:
    pass


# %%
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*' * 50)
    print('Esegui grade.py per il test automatico.')
    print('*' * 50)
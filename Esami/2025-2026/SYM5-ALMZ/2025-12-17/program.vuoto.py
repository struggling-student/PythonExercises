#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

################################################################################
"""
Per superare la prova è necessario:
    - ottenere un punteggio maggiore o uguale a 18 (15 se con DSA)

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: è proibito importare altre librerie

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
################################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 3 punti
Si definisca la funzione 
	func1(D1 : dict[str,int], D2 : dict[int,int], D3 : dict[int,str] ) -> list[str]
che riceve come argomenti:
- D1: un dizionario con chiavi stringa e valori interi
- D2: un dizionario con chiavi interi  e valori interi
- D3: un dizionario con chiavi interi  e valori stringa
e che ritorna la lista di stringhe ottenuta concatenando le chiavi di D1 con i valori di D3
indicati dall'associazione D2 tra valori di D1 e chiavi di D3 se presenti)

La lista deve essere ordinata in ordine crescente di lunghezza e, a parimerito, in ordine decrescente alfabetico.

Esempio:
D1 = { 'uno' : 1 , 'due' : 2, 'tre' : 3 }
D2 = { 1 : 5     , 3 : 12   , 5 : 9 }
D3 = { 12 : 'papere', 90 : 'cavalli', 5 : 'sogliole' }

expected: ['trepapere', 'unosogliole']
'''

def func1(D1 : dict[str,int], D2 : dict[int,int], D3 : dict[int,str] ) -> list[str]:
    pass
    ## Scrivi qui il tuo codice


"""
# esempio
D1 = { 'uno' : 1 , 'due' : 2, 'tre' : 3 }
D2 = { 1 : 5     , 3 : 12   , 5 : 9 }
D3 = { 12 : 'papere', 90 : 'cavalli', 5 : 'sogliole' }

print(func1(D1,D2,D3))
"""

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 3 punti
Si definisca la funzione 
	func2(L1 : list[int], L2 : list[int], L3 : list[int] ) -> tuple[set[int],set[int]]
che riceve come argomenti 3 liste di interi L1, L2 ed L3, e che torna i due insiemi:
- S1 : l'insieme degli elementi che appaiono in una sola lista
- S2 : l'insieme degli elementi che appaiono in tutte le liste

Esempio:
L1 = [ 1, 2, 6, 2, 8, 4, 9, 1, 7 ]
L2 = [ 5, 6, 1, 8, 3, 2 ]
L3 = [ 10, 8, 9, 1, 2, 8, 9, 6, 10 ]

expected: ({3, 4, 5, 7, 10}, {8, 1, 2, 6})
'''
def func2(L1 : list[int], L2 : list[int], L3 : list[int] ) -> tuple[set[int],set[int]]:
    ## Scrivi qui il tuo codice
    pass


"""
# esempio
L1 = [ 1, 2, 6, 2, 8, 4, 9, 1, 7 ]
L2 = [ 5, 6, 1, 8, 3, 2 ]
L3 = [ 10, 8, 9, 1, 2, 8, 9, 6, 10 ]
print(func2(L1,L2,L3))
"""

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 punti

Si definisca la funzione 
    func3(input_filename:str, output_filename:str) -> int
che riceve come argomenti:
- input_filename: il percorso di un file di testo che contiene una matrice 
    rettangolare di interi di dimensioni N righe per 2N colonne
- output_filename: il percorso di un file in cui dovete scrivere una matrice
    triangolare NxN 
La funzione deve leggere la matrice di interi n x 2N e trasformarla 
in una matrice triangolare in cui alla riga i-esima sono presenti i+1 valori
- i primi i sono gli stessi della riga corrispondente
- l'ultimo è la somma dei rimanenti
La funzione deve inoltre tornare la somma di tutti gli ultimi elementi della 
matrice triangolare.

Esempio: il file func3/in_5.txt contiene la matrice
    -56 29 -34 -27 9 63 43 -30 -84 -9 
    37 7 17 40 -76 75 -11 -8 -17 66 
    -1 -13 77 -19 -92 53 59 -98 -50 60 
    -83 4 -54 23 -66 15 48 27 49 -1 
    43 79 57 -77 -1 29 34 31 13 99 
che deve essere trasformata nella matrice
    -96
    37 93
    -1 -13 -10
    -83 4 -54 95
    43 79 57 -77 205

risultato: 287
"""

def func3(input_filename, output_filename):
    pass
    ## Scrivi qui il tuo codice

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 8 punti
Si definisca la funzione 
    func4(file_png_in : str) -> tuple[int, int]
che riceve come argomenti il nome di un file PNG che contiene, su sfondo
nero, fiocchi di neve e alberi di natale.

Il fiocco di neve è formato da 5 pixel uguali a forma di croce (C=colore, .=nero)
C.C
.C.
C.C
mentre gli alberi di natale sono formati da 10 pixel uguali come segue
..C..
.CCC.
CCCCC
..C..

La funzione conta quanti fiocchi di neve e quanti alberi di natale ci sono e ritorna
la coppia
    FIOCCHI,ALBERI

"""
import images

def func4(file_png_in : str) -> tuple[int, int]:
    pass
    ## Scrivi qui il tuo codice




# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(dirin:str, parole:list[str]) -> dict[str,int]
ricorsiva o che utilizza funzioni o metodi ricorsivi, che riceve come argomenti
- dirin: il percorso di una directory
- parole: una lista di parole

La funzione torna un dizionario che ha come chiavi le parole 
e come valori il numero di file '.txt' che contengono quella parola. 

AVVISO 0: Definite la funzione ricorsiva a livello più esterno altrimenti
non supera il test di ricorsione.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk o importare altre librerie

"""
import os

def ex1(dirin:str, parole:list[str]) -> dict[str,int]:
    pass
    ## Scrivi qui il tuo codice


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root:BinaryTree), 
ricorsiva o che utilizza funzioni o metodi ricorsivi,
che per ogno nodo dell'albero binario root scambia il sottoalbero
sinistro con quello destro solo sui livelli dispari (root=0)
La funzione ritorna il numero di scambi fatti.

AVVISO: Definite la funzione ricorsiva a livello più esterno altrimenti
non supera il test di ricorsione.

"""
from tree import BinaryTree

def ex2(root: BinaryTree ) -> int:
    pass
    ## Scrivi qui il tuo codice

    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)

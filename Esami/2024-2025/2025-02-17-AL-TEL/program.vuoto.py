#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(S, D) che riceve in ingresso un insieme S di 
interi ed un dizionario D e restituisce un nuovo dizionario.
Il dizionario in ingresso è composto da chiavi intere e valori stringhe.
Il dizionario ritornato contiene una chiave per ogni intero in S. 
Il valore corrispondente ad una chiave x in S è il valore associato 
alla più grande chiave in D che è un multiplo o un divisore di x.

NOTA: se nessuna delle chiavi in D è un multiplo o un divisore di x,
la chiave x non appare nel dizionario ritornato.

Es: se
    S = {2, 3, 55, 4, 11, 7} e D = {11:'a', 88:'b', 66:'c', 2:'d', 100:'e', 5:'f'}
        allora la funzione ritorna il dizionario
        {2:'e', 3:'c', 55:'a', 4:'e', 11:'b'}
    
'''

def func1(S: set[int], D: dict[int,str]) -> dict[int,str]:
    # Your code here
    pass
                    
# S = {2, 3, 55, 4, 11, 7}
# D = {11:'a', 88:'b', 66:'c', 2:'d', 100:'e', 5:'f'}
# print(func1(S, D))    


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(L) che prende in ingresso una lista
di stringhe e ritorna una lista di stringhe.
Le stringhe nella lista ritornata sono ottenute mediante la concatenazione 
di tutte le stringhe che hanno la stessa lunghezza, 
mantenendo l'ordine nella lista in ingresso.
La lista ritornata ha l'ordine decrescente di lunghezza e, in caso di parità,
l'ordine alfabetico.

Es: se L = ['xx', 'asd', 'qwe', 'bb', 'cc', 'fond']
    la funzione ritorna la lista ['asdqwe', 'xxbbcc', 'fond']

'''


def func2(L: list[str]) -> str:
    # Your code here
    pass

# print(func2( ['xx', 'asd', 'qwe', 'bb', 'cc', 'fond']))



# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(strings, tuples) che prende in ingresso una lista 
'strings' di liste di parole e una lista 'tuples' di coppie. 
Ogni coppia in tuples è composta da due interi (lista, elemento) che indicano,
rispettivamente, l'indice della lista da cui prendere una parola 
e l'indice della parola da selezionare in quella lista.
La funzione deve ritornare la stringa ottenuta selezionando le parole 
dalle liste in strings usando gli indici delle tuple.
Le parole vanno concatenate, separandole con uno spazio,
nell'ordine in cui appaiono le coppie della lista tuples. 

Es: se strings = [['works', 'is'], ['science', 'magic'], ['that']] 
   tuples = [(1,0), (0,1), (1,1), (2,0), (0,0)]
   la funzione ritorna la stringa 
   'science is magic that works'
'''


def func3(strings: list[list[str]], tuples: list[tuple[int, int]]) -> str:
    # Your code here
    pass

# strings = [['works', 'is'], ['science', 'magic'], ['that']] 
# tuples = [(1,0), (0,1), (1,1), (2,0), (0,0)]
# print(func3(strings, tuples))
# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Si definisca la funzione func4(input_filename, output_filename) che
prende due nomi di file come parametri. La funzione legge il file di
testo input_filename.
Ogni riga del file input_filename contiene una serie di stringhe separate
da spazi o tab. Ogni stringa può essere composta da caratteri alfabetici
o da caratteri numerici. 
La funzione deve impiegare una funzione 'peso' per ogni stringa che consiste
nel calcolare il valore ottenuto sommando il valore unicode dei caratteri
alfabetici e il valore dei caratteri numerici che compongono la stringa.
Per calcolare il valore unicode di un carattere si può usare la funzione ord.

Per ognuna delle righe in input_filename, la funzione deve scrivere nel
file output_filename una nuova riga con tutte le stringhe della riga
corrispondente, sperate da esattamente uno spazio e ordinate con
i seguenti criteri:
    - Numero di caratteri crescente
    - in caso di parità, l'ordine alfabetico senza distinzione tra maiuscole e minuscole,
    - in caso di parità, il peso della stringa,
    - in caso di parità, l'ordine alfabetico.

La funzione restituisce la stringa con il peso massimo trovata nel file
input_filename.

NOTA: ignorate le righe vuote nel file di input

"""

def func4(input_filename: str, output_filename: str) -> int:
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5:  7 punti
Definire la funzione func5(input_imgs: list[str], output_path: str) ->
tuple che prende in ingresso una lista di stringhe dove ciascuna
stringa punta ad un'immagine PNG. Date queste immagini nella lista e'
necessario creare una nuova immagine da salvare nel file output_path.
L'immagine output e' cosi creata: le immagini di input nella lista
vanno concatenate in orizzontale seguendo l'ordine da sinistra a
destra.  Ossia se input_imgs = [img1, img2, img3] output va costruito
concatenando img1 | img2 | img3. Le immagini di input hanno larghezza e
altezza diverse.  L'immagine di output deve essere creata in modo che
sia l'immagine "minima" sia in altezza e larghezza che contiene tutte le immagini
appoggiate al bordo superiore della immagine risultato.  
Nel caso in cui vi siano delle parti in output che non sono coperte da alcuna 
immagine di ingresso, queste parti vanno colorate in nero.

La funzione restituisce la tupla (H, W) dove H e' l'altezza e W la larghezza
dell'immagine di output e salva quest'ultima in output_path.

Ad esempio date:

img 1         img2          img3
HxW           HxW           HxW
20x30        30x50          40x10

xxx          +++++           .
xxx          +++++           .
             +++++           .
                             .

x=grigio     +=verde        . = rosso

output diventa:

xxx+++++.
xxx+++++.   dove o = nero
ooo+++++.
oooooooo.

e l'immagine output e' grande 40x90 pixels.
si veda func5/in_1_1.png  func5/in_1_2.png  func5/in_1_3.png e
func5/exp_1.png e' immagine corretta in uscita

Per caricare e salvare i file PNG si possono usare load e save della
libreria immagini.
"""

import images

def func5(input_imgs: list[str], output_path: str) -> tuple:
    # Your code here
    pass

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione es1(root1: BinaryTree , root2: BinaryTree)
ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che riceve
come parametri le radici root1 e root2 di due alberi binari formati
da nodi del tipo BinaryTree definito nel modulo tree.py. I due alberi
contengono stringhe con un unico carattere come valore e sono strutturalmente
identici, se non per il fatto che il valore di nodi corrispondenti non
sempre coincide.  La funzione deve restituire una lista di tuple che
contengono triple.

Ciascuna tripla è cosi costruita:
per ogni coppia di nodi corrispondenti fra root1 e root2 che NON hanno lo
stesso valore, si salva nella tripla
- prima il livello nell'albero (considerando la radice come livello 0),
- poi il valore del nodo preso dall'albero sinistro
- e poi il valore del nodo preso dall'albero destro.

Le triple nella lista devono risultare ordinate:
- in ordine crecente di livello;
- in caso di parità sul livello, in ordine alfabetico inverso in base al secondo valore; 
- in caso di parità sul secondo valore, in ordine alfabetico in base al terzo valore.

Suggerimento: può essere utile la funzione 'ord' per ottenere il valore unicode dei caratteri

Esempio:
           root1                                 root2

        ______A______       level 0          ______A______
       |             |                      |             |
       B__        ___C___   level 1         X__        ___C___
          |      |       |                     |      |       |
          D      E       F  level 2            Y      F       G 


Se gli alberi in ingresso sono questi due sopra la funziona restituisce
la lista [(1, 'B', 'X'), (2, 'F', 'G'), (2, 'E', 'F'), (2, 'D', 'Y')]

infatti al livello 1 il nodo 'B' di root1 è diverso dal nodo 'X' di
root2 e così via. Gli altri elementi sono tutti al livello 2 quindi a
parimerito e sono ordinati in ordine alfabetico inverso in base al
secondo valore quindi F-->E-->D. 

********************************************************************
NB: se scrivete una funziona addizionale, NON definite la funzione
ricorsiva addizionale come funzione interna ma mettetela al solito
livello di ex, come funzione esterna, altrimenti non passate il test
ricorsivo!
********************************************************************
"""

from tree import BinaryTree

def ex1(node1: BinaryTree, node2: BinaryTree) -> list:
    # Your code here
    pass

# %% ----------------------------------- EX.2 -------------------------------#
'''Ex2: 3 + 3 punti
Implementare la funzione ex2(dirin, words), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, avendo come argomento:
    - dirin: il percorso di una directory esistente come stringa
    - words: una lista di parole

La funzione esaminerà tutti i file di testo (cioè i file con estensione .txt)
presenti in dirin e tutte le sue sottocartelle (a qualsiasi
livello) e conterà le occorrenze delle parole presenti nella lista 'words'.
Le parole presenti in un file sono separate da uno o più dei
seguenti caratteri: spazio, tabulazione o carattere newline.

(3 punti) La funzione restituisce una lista di tuple (parola, occ), in cui:
    - il primo valore di ogni coppia è una delle parola nella lista di input.
    - il secondo valore 'occ' della coppia è il numero totale di occorrenze
      di quella parola nei file di testo.

(+ 3 punti) La lista è ordinata in base al numero di occorrenze delle
parole (in ordine decrescente). Se due o più parole hanno lo
stesso numero di occorrenze, sono ordinate alfabeticamente (in
ordine crescente). Se una parola dell'elenco di input non si trova mai
nei file testuali, deve comunque essere restituita dalla funzione con
conteggio 0.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk o importare altre librerie

Ad esempio, data la cartella "ex2/" e se words = ["gatto", "cane"]
la funzione restituisce: [("cane", 11), ("gatto", 6)].
'''

import os


def ex2(dirin, words):
    # Your code here
    pass
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)



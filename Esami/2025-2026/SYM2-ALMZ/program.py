#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
1) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
2) entro le 12.15 consegnare SOLO il file program.py su Classroom

Il voto finale e' la somma dei punteggi dei problemi risolti.
Si supera la simulazione se si raggiunge almeno 18.
I ragazzi/e con DSA devono raggiungere almeno 15
(e devono fami comunicare dal Servizio DSA di Sapienza che sono DSA).

Attenzione! DEBUG=True nel grade.py per visualizzare la stack trace degli errori.
"""

nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

# ----------------------------------- EX.1 ----------------------------------- #

"""Func 1: 6 punti

Si progetti una funzione che riceve come argomenti i path di due file
dict1 e dict2 e ritorni come output un dizionario.  I due file
contengono delle righe di testo con parole separate da spazi e tab,
dalle quali la funzione deve generare un dizionario considerando
soltanto le righe che hanno esattamente due parole: la prima parola
sarà una chiave del dizionario e la seconda sarà il valore a questa
associato.

Il dizionario finale da ritornare deve avere:

- una chiave per ogni chiave presente in entrambi i dizionari
  costruiti da dict1 e dict2 seguendo la procedura sopra descritta,

- per valore la concatenazione mediante il carattere '-' (meno) dei due
  valori associati alla stessa chiave nei due dizionari, 
  ordinati secondo l'ordine alfabetico.

Es: se dai due file dic1 e dic2 sono generati i dizionari 
    {'a':'cane', 'c':'gatto'} e
    {'f':'giraffa', 'a':'bue'}, 
    la funzione deve ritornare il dizionario {'a':'bue-cane'}.

"""
def func1 (dict1, dict2):
    pass
    # completa il codice della funzione


#%% ----------------------------------- FUNC4 ------------------------- #
""" func2: 6 punti
Si scriva una funzione func2(input_file, output_file) che riceve come argomenti
due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.  All'interno del file indicato da 'input_file'
e' codificata una matrice, dove ogni linea del file rappresenta una riga
della matrice, con i valori separati da virgola e spazi. 
Ad esempio func2/input_1.txt contiene:

1,    2, 3,            25
 4, 5,      6, 17
7,   8,    9,          42

La funzione deve leggere il file in 'input_file' e scrivere di nuovo la
stessa matrice ma scrivendo ogni riga come una lista di numeri interi
separati da virgola e spazio, in modo da avere scritto in 'output_file':

[1, 2, 3, 25]
[4, 5, 6, 17]
[7, 8, 9, 42]

e ritornare il numero di elementi della matrice.
Si apra 'func2/input_1.txt per vedere l'input e
'func2/expected_1.txt' per vedere l'output atteso.
"""

def func2(input_file, output_file):
    pass
    # completa il codice della funzione


# print(func2('func2/input_1.txt','func2/output_1.txt'))
# print(func2('func2/input_2.txt','func2/output_2.txt'))
# print(func2('func2/input_3.txt','func2/output_3.txt'))

#%% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 punti

Definisci una funzione func3(file_in, file_out, length, chars) che riceve come argomenti:
- due stringhe che rappresentano i percorsi di due file di testo
- un intero length,
- una stringa chars.
La funzione deve restituire l'elenco di tutte le parole trovate nel file puntato
da file_in con una lunghezza *almeno* length e contenente *almeno* uno dei
caratteri nella stringa chars.
L'elenco deve essere ordinato per lunghezza decrescente e, in caso di parità, in
ordine alfabetico.
Inoltre, la funzione deve scrivere le parole dell'elenco in output nel
file puntato da file_out separate da uno spazio.

Esempio: func3('func3/in_01.txt', 'func3/out_01.txt', 5, 'asd')
     deve tornare la lista ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
     e scrivere la stringa 'hippopotamus elephant cobra horse panda snake' in func3/out_01.txt.
"""

def func3(file_in : str, file_out: str, length:int, chars:str) -> list[str]:
    pass
    # completa il codice della funzione


# print(func3('func3/in_01.txt', 'func3/out_01.txt', 5, 'asd')) # ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']

# ---------------------------- FUNC 4 ---------------------------- #
'''
Func 4: 6 punti
Definite la funzione func4(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

Il file indicato da textfile_in contiene dei numeri
float oppure interi, positivi o negativi, separati da spazi.

La funzione deve leggere i numeri, ordinarli in ordine decrescente di
di caratteri numerici presenti e in caso di parità in ordine crescente di valore.
Quindi deve scrivere questi numeri ordinati nel file textfile_out,
separati da virgola e spazio. Infine la funzione restituisce la
quantità di numeri letti da textfile_in.

Esempio:
se il file textfile_in contiene la riga
-23.5 17 -141 +322.7 -3227
Nel file textfile_out la funzione deve scrivere la riga
-3227, +322.7, -141, -23.5, 17
e tornare il valore 5
'''

def func4(textfile_in, textfile_out):
    pass
    # completa il codice della funzione


# print(func4('func4/input_1.txt', 'func4/output_1.txt')) # 5

# ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 6 punti
Si definisca la funzione func5(filein) che riceve come argomento
- filein: un file di testo contenente una matrice di interi NxM
  separati da spazi

e che ritorna la matrice trasposta rispetto alla diagonale secondaria,
ovvero quella che va dall'elemento in alto a destra a quello in basso
a sinistra. La matrice da restituire e' rappresentata come lista di liste.
Trasposta = matrice riflessa rispetto alla diagonale.

Esempio:
se il file filein contiene la matrice
1 2 3 4
5 6 7 8
9 10 11 12
la funzione dovrà tornare la matrice riflessa rispetto alla diagonale 4-9,
come lista di liste
[[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
'''
def func5(input_filename):
    pass
    # completa il codice della funzione


# ---------------------------- EOF ---------------------------- #
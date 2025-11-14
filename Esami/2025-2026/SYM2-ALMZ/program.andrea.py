#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%

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

nome       = " NOME"
cognome    = " COGNOME"
matricola  = " MATRICOLA"

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
    D1 = leggi_dizionario(dict1)
    D2 = leggi_dizionario(dict2)
    D = {}
    for k,v in D1.items():
        if k in D2:
            v2 = D2[k]
            if v <= v2:
                D[k] = v + '-' + v2
            else:
                D[k] = v2 + '-' + v
    return D

def leggi_dizionario_fake(filename, secondo=False):
    if secondo:
        return {'f':'giraffa', 'a':'bue'}
    else:
        return {'a':'cane', 'c':'gatto'}

def leggi_dizionario(filename):
    D = {}
    with open(filename, encoding='utf8') as F:
        for riga in F:
            parole = riga.split()
            if len(parole)==2:
                chiave, valore = parole
                D[chiave]=valore
    return D

print(func1('func1/input_1_a.txt','func1/input_1_b.txt'))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func2: 6 punti
Si scriva una funzione func2(input_file, output_file) che riceve come argomenti
due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.  All'interno del file indicato da 'input_file'
e' codificata una matrice, dove ogni linea del file rappresenta una riga
della matrice, con i valori separati da virgola e spazi. 
Ad esempio func2/input_1.txt contiene:

1,    2, 3,            25
 4, 5,      6, 017
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
    M,N = leggi_matrice(input_file)
    scrivi_matrice(M,output_file)
    return N

def leggi_matrice(filename):
    matrice = []
    N = 0
    with open(filename, encoding='utf8') as F:
        #for riga in F:
        for riga in F.readlines():
            numeri = riga.split(',')
            riga_di_numeri = [ int(frammento) for  frammento in numeri ]
            matrice.append(riga_di_numeri)
            N += len(riga_di_numeri)
    return matrice, N

def scrivi_matrice(matrice, filename):
    with open(filename, mode='w', encoding='utf8') as FOUT:
        for riga in matrice:
            FOUT.write(str(riga)+'\n')
            #print(riga, file=FOUT)

#print(leggi_matrice('func2/input_1.txt'))

print(func2('func2/input_1.txt','func2/output_1.txt'))
# print(func2('func2/input_2.txt','func2/output_2.txt'))
# print(func2('func2/input_3.txt','func2/output_3.txt'))

# %% ----------------------------------- FUNC3 ------------------------- #
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
    def criterio(parola):
        return -len(parola), parola
    # completa il codice della funzione
    parole = leggi_parole(file_in)
    '''
    parole_giuste = [ parola for parola in parole
                      if len(parola)>=length and 
                      any( c in parola for c in chars )
                    ]
    '''
    parole_giuste = []
    for parola in parole:
        if len(parola)>=length and esiste_carattere(chars, parola):
            parole_giuste.append(parola)
    parole_giuste.sort(key=criterio)
    with open(file_out, mode='w', encoding='utf8') as FOUT:
        FOUT.write(' '.join(parole_giuste)+'\n')
    return parole_giuste

def leggi_parole(filename):
    with open(filename, encoding='utf8') as FIN:
        testo = FIN.read()
    nonalfa = { c for c in set(testo) if not c.isalpha() }
    for c in nonalfa:
        testo = testo.replace(c, ' ')
    return testo.split()


def esiste_carattere(chars,parola):
    for c in chars:
        if c in parola:
            return True
    return False

#print(func3('func3/in_01.txt', 'func3/out_01.txt', 5, 'asd')) # ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']


# %% ----------------------------------- FUNC3 ------------------------- #
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
    def criterio(stringa):
        N =0
        for c in stringa:
            if c.isdigit():
                N += 1
        return -N, float(stringa)
    pass
    # completa il codice della funzione
    numeri = leggi_numeri(textfile_in)
    numeri.sort(key=criterio)
    with open(textfile_out, mode='w', encoding='utf8') as FOUT:
        print(*numeri, sep=', ', file=FOUT)
    return len(numeri)

def leggi_numeri(filename):
    #return ['-23.5', '17', '-141', '+322.7', '-3227']
    with open(filename, encoding='utf8') as FIN:
        return FIN.read().split()

#print(func4('func4/input_1.txt', 'func4/output_1.txt'))

# print(func4('func4/input_1.txt', 'func4/output_1.txt')) # 5


# %% ----------------------------------- FUNC3 ------------------------- #
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
[[12, 8, 4],   riga 0
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
'''
def func5(input_filename):
    pass
    # completa il codice della funzione
    matrice = leggi_matrice2(input_filename)
    L = len(matrice[0])
    A = len(matrice)
    trasposta = []
    for y in range(L):
        riga = []
        for x in range(A):
            riga.append(matrice[A-x-1][L-y-1])
        trasposta.append(riga)
    return trasposta

def leggi_matrice2(filename):
    M = []
    with open(filename, encoding='utf8') as FIN:
        for riga in FIN:
            interi = [ int(valore) for valore in riga.split() ]
            M.append(interi)
    return M

print(func5('func5/in_1.txt'))
    
# ---------------------------- EOF ---------------------------- #

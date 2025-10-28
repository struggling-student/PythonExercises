#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - ottenere un punteggio maggiore o uguale a 18 (15 se DSA)

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome       = "A"
cognome    = "S"
matricola  = "42"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(D), che riceve come parametro un dizionario
D, in cui ogni chiave è un intero positivo N e il corrispondente valore
è una lista di caratteri alfabetici L.
La funzione ritorna una lista L di stringhe con una stringa per ogni chiave del dizionario.
Le stringhe sono ottenute concatenando tutti i caratteri in L, tranne il
carattere con indice l'intero chiave corrispondente. Se l'indice è esterno
alla lista, la stringa contiene tutti i caratteri di L.
La lista è ordinata in ordine alfabetico decrescente.
Ad esempio se D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'], la funzione ritornerà
L = ['qa', 'se']
'''


def func1(D : dict[int, list[str]]) -> list[str]:
    ## Scrivi qui il tuo codice
    pass
    stringhe = []
    for chiave, lista in D.items():
        lettere = lista[:chiave]+lista[chiave+1:]
        stringhe.append(''.join(lettere))
    return sorted(stringhe, reverse=True)

# Test della funzione func1
# print(func1({2: ['s', 'u', 'e'], 3: ['q', 'a']}))
# risultato: ['qa', 'se']x


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(L) che ha come parametro una lista L di N liste.
Ogni lista P della lista L può contenere una o più liste che possono essere vuote
oppure avere uno o più elementi.
La funzione ritorna una lista di N interi, in cui l'elemento i-esimo
indica il numero di liste vuote nella lista in i-esima posizione di L.
Ad esempio, se L = [ [3, []], [2,[3]], [4, [], [3,4], []]]
la funzione restituirà [1, 0, 2]
'''


def func2(L : list[list]) -> list[int]:
    ## Scrivi qui il tuo codice
    pass
    risultato = []
    for lista in L:
        numero_liste_vuote = 0
        for elemento in lista:
            if not elemento:
                numero_liste_vuote += 1
        risultato.append(numero_liste_vuote)
    return risultato

# Test della funzione func2
# print(func2([ [3, []], [2,[3]], [4, [], [3,4], []]]))
# risultato: [1, 0, 2]

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S, m, M) che riceve in input una stringa contenente
delle parole separate da virgole ed, opzionalmente, anche da spazi.
La funzione deve estrarre le parole da S, considerando solo quelle che
hanno una lunghezza compresa fra m ed M inclusi, ed inserirle in una seconda
lista ordinata alfabeticamente senza considerare la differenza tra maiuscole
e minuscole.
Ad esempio se S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
la funzione func3(S, 3, 4) restituirà ['Brad', 'Dana','ian', 'UMA', 'Zoe']
'''


def func3(S : str, m: int, M: int) -> list[str]:
    ## Scrivi qui il tuo codice    
    pass
    parole = [p.strip() for p in S.split(',')]
    giuste = [p for p in parole if M >= len(p) >= m]
    return sorted(giuste, key=lambda x: x.lower())

# Test della funzione func3
# print(func3("Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe", 3, 4))
# risultato: ['Brad', 'Dana','ian', 'UMA', 'Zoe']


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti (8?)
Definire la funzione func4(input_filepath, output_filepath) che legge il
file indicato da input_filepath.  Il file di input contiene parole separate
da ritorni a capo, spazi, tabulazioni, virgole o punto e virgola.  

Le parole considerate vanno raggruppate secondo la lettera che occorre
con più frequenza, senza distinzione fra maiuscole e minuscole.
Per ogni gruppo occorre scrivere nel file di output una riga nel formato:

<lettera minuscola>: <lista delle parole separate da spazio>

La lettera iniziale di riga è in minuscolo, seguita da ": " (due punti più
spazio); di seguito, compare la lista delle parole che hanno quella lettera
con maggiore frequenza, indipendentemente dal fatto che la lettera nella parola
sia maiuscola o minuscola. Le righe devono apparire in ordine alfabetico
in base alla lettera. Le liste sono in ordine alfabetico, ignorando la distinzione
fra minuscole e maiuscole, oppure mantenendo l'ordine alfabetico in caso di
parole identiche, ma con diverse maiuscole.
Se una parola ha più lettere con frequenza massima, allora quella parola compare
nella riga di ognuna di tali lettere.

Attenzione, alla fine di ogni riga nel file di output NON c'e' alcuno spazio ma c'è
SEMPRE un ritorno a capo!

La funzione deve restituire il numero totale di parole, compresi i duplicati,
trovate nel file di input.

Ad esempio:

contenuto di func4/func4_in1.txt:
GE
wOa;II,see	ua;PAO,oA;wOA
pao iu;jJa,kE

Chiamata
n = func4("func4/func4_in1.txt", "func4/func4_out1.txt")

contenuto atteso di func4/func4_out1.txt:
a: oA PAO pao ua wOA wOa
e: GE kE see
g: GE
i: II iu
j: jJa
k: kE
o: oA PAO pao wOA wOa
p: PAO pao
u: iu ua
w: wOA wOa

Valore restituito: 12
"""

def leggi_parole(input_filename):
    'leggo il file e separo le parole'
    with open(input_filename) as FIN:
        testo = FIN.read()
    testo = testo.replace(',',' ')
    testo = testo.replace(';',' ')
    return testo.split()

def massime_lettere(parola:str) -> set[str]:
    'trovo tutte le lettere che appaiono più volte nella parola'
    minuscola = parola.lower()
    M = max([ minuscola.count(c) for c in minuscola])
    #le lettere non devono apparire più volte nel risultato
    return {c for c in minuscola if minuscola.count(c) == M}

def organizza_parole(parole:set[str]) -> dict[str,list[str]]:
    def criterio_ordinamento(parola):
        'ordino indipendentemente dal case, e secondo il case se uguali'
        return parola.lower(), parola
    dizionario = {}
    for parola in parole:
        frequenti = massime_lettere(parola)
        for lettera in frequenti:
            if lettera not in dizionario:
                dizionario[lettera] = []
            dizionario[lettera].append(parola)
    for lettera in dizionario:
        dizionario[lettera].sort(key=criterio_ordinamento)
    return dizionario

def save_file(dizionario : dict[str,list[str]], filename:str) -> None:
    with open(filename, 'w') as FOUT:
        for lettera in sorted(dizionario):
            print(f'{lettera}: {" ".join(dizionario[lettera])}', file=FOUT)

def func4(input_filename : str, output_filename : str) -> int:
    pass
    parole = leggi_parole(input_filename)
    dizionario = organizza_parole(parole)
    save_file(dizionario, output_filename)
    return len(parole)



# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti (6?)
Definire la funzione func5(file_in, file_out) che usa images.load per
caricare l'immagine presente in file_in. L'immagine è una lista di liste
e ogni elemento interno è un pixel rappresentato dalla tupla (r, g, b).
Lo sfondo è completamente nero, cioè (0, 0, 0).

Nell'immagine sono presenti pixel di diverso colore.

La funzione deve individuare per ogni riga il colore che ricorre maggiormente
e sostituire con il nero tutti gli altri pixel non di quel colore.
Nel caso in cui diversi pixel di una riga compaiano lo stesso numero di volte,
si deve considerare il colore con il valore più basso nella prima componente,
in caso di parità, il valore più basso nella seconda componente, in caso di
parità, il valore più basso nella terza componente.

La funzione deve poi salvare il risultato in file_out mediante images.save e
restituire il numero di pixel sostituiti.
"""
import images


def func5(file_in : str, file_out : str) -> int:
    pass
    img = images.load(file_in)
    b = 0,0,0
    count = 0
    for riga in img:
        colori = [colore for colore in set(riga) if colore != b]
        if colori:
            maxcol = max( colori, key=lambda x: (riga.count(x),-x[0],-x[1],-x[2]) )
            for i in range(len(riga)):
                if riga[i] != maxcol and riga[i] != b:
                    riga[i] = b
                    count += 1
    images.save(img, file_out)
    return count

# Test della funzione func5
# print(func5("func5/test1_in.png", "func5/test1_out.png"))
# risultato: 14 (il numero di pixel sostituiti)

# %% ----------------------------------- EX.1 ------------------------- #
'''
Ex1: 6 punti

Si consideri la classe BinaryTree contenuta nel file tree.py che definisce
un nodo di albero binario. Scrivere una funzione ex1(T, n) ricorsiva o che faccia
uso di una o più funzioni ricorsive.
La funzione riceve la radice di un BinaryTree come input e un intero n.
Nei nodi dell'albero in input sono memorizzati degli interi.
La funzione deve individuare tutti i percorsi radice-foglia che attraversano
dei nodi per i quali la somma dei valori in essi memorizzati è pari a n.
La funzione deve ritornare una lista contenente la lista dei valori
dei nodi attraversati per ogni percorso individuato. La lista ritornata
deve essere ordinata in ordine crescente.

Ad esempio, 


        ______20_____       level 1          ______13______
       |             |                      |              |
       4__        ___1___   level 2      ___7___        ___10___
          |      |       |              |       |      |        |
          -2     1       4  level 3    _-5_    -1_    _-9_       3
                                      |    |      |  |    |       
                            level 4   5    4      6  6   -2    

Se T è l'albero di sinistra, allora la funzione ex1(T, 22) deve ritornare
la lista [[20, 1, 1], [20, 4, -2]]', se T è l'albero di destra, allora
la funzione ex1(T, 20) deve ritornare la lista [[13, 7, -5, 5], [13, 10, -9, 6]]
'''
import tree

def ex1(T, N):
    ## Scrivi qui il tuo codice
    pass
    percorsi = _ex1(T)
    giusti = [p for p in percorsi if sum(p) == N]
    return sorted(giusti)

def _ex1(T):
    if T is None:
        return []
    if T.left is None and T.right is None:
        return [[T.value]]
    return [[T.value]+p for p in _ex1(T.left) + _ex1(T.right)]

# Test della funzione ex1
# print(ex1(tree.BinaryTree.fromList([20, [4,None,[-2,None,None]], [1, [1,None,None], [4,None,None]]]), 22))
# risultato: [[20, 1, 1], [20, 4, -2]]


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Scrivere la funzione ex2(L, k) ricorsiva oppure che faccia uso di
funzioni ricorsive. L è una lista di stringhe di lunghezza variabile.
k è un intero maggiore di 0.

La funzione deve costruire e restituire il set di tutte le stringhe lunghe
k ottenute concatenando due o più stringhe di L.

Esempio:
L = ['a', 'bb', 'ccc', 'd']
k = 4

Output atteso:
{'accc', 'ccca', 'adbb', }

{ accc, ccca, cccd, dccc, 
  bbbb, bbaa, bbac, bbca, 
  abba, abbc, cbba, cbbc
  aaaa, 
  aaac, aaca, acaa, caaa
  aacc, acac, acca, caca, caac, ccaa
  accc, cacc, ccac, ccca}
"""


def ex2(L : list[str], k: int) -> set[str]:
    pass
    # tengo solo le parole più corte di k in modo che ne servano almeno 2
    L1 = [l for l in L if len(l) < k]
    return _ex2(L1, k)

def _ex2(L,k):
    # se non ci sono altre lettere da aggiungere torno stringa vuota
    if k == 0:
        return {''}
    return { S+p                         # concateno la sottosoluzione S con la parola p
             for i,p in enumerate(L)     # per ogni parola p in L
             if  len(p)<=k               # ma solo se di lunghezza minore o uguale al numero di lettere mancanti
             # per ciascuna sottosoluzione S che non usa la parola p
             for S in _ex2(L[:i]+L[i+1:], k-len(p))
             }

# Test della funzione ex2
# print(ex2([['c', 'q', 'a', 'a'], ['w', 'e', 'y']], 1))
# risultato: ['aw', 'ay', 'ce', 'qe']


# %%
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*' * 50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)

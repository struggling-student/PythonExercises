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
nome       = "Mau"
cognome    = "Man"
matricola  = "1234"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti
Si definisca la funzione func1(D), che riceve come parametro un dizionario
D, in cui ogni chiave è un intero positivo N e il corrispondente valore
è una lista di caratteri alfabetici L.
La funzione ritorna una lista con una stringa per ogni chiave del dizionario.
Le stringhe sono ottenute concatenando tutti i caratteri in L, tranne il
carattere con indice l'intero chiave corrispondente. Se l'indice è esterno
alla lista, la stringa contiene tutti i caratteri di L.
La lista è ordinata in ordine alfabetico decrescente.
Ad esempio se D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'], la funzione ritornerà
L = ['qa', 'se']
'''


def func1(D):
    result = []
    for i in D:
        if i < len(D[i]):
            D[i].pop(i)
        result.append(''.join(D[i]))
    result.sort(reverse=True)
    return result

# Test della funzione func1
# print(func1({2: ['s', 'u', 'e'], 3: ['q', 'a']}))
# risultato: ['qa', 'se']


# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 2 punti
Si definisca la funzione func2(L) che ha come parametro una lista L di N liste.
Ogni lista P della lista L può contenere una o più liste che possono essere vuote
oppure avere uno o più elementi.
La funzione ritorna una lista di N interi, in cui l'elemento i-esimo
indica il numero di liste vuote nella lista in i-esima posizione di L.
Ad esempio, se L = [ [3, []], [2,[3]], [4, [], [3,4], []]]
la funzione restituirà [1, 0, 2]
'''


def func2(L):
    result = []
    for i in L:
        count = 0
        for j in i:
            if j == []:
                count += 1
        result.append(count)
    return result
        

# Test della funzione func2
# print(func2([ [3, []], [2,[3]], [4, [], [3,4], []]]))
# risultato: [1, 0, 2]

# %% ----------------------------------- FUNC3 ------------------------- #
'''func3: 2 punti
Si definisca la funzione func3(S, m, M) che riceve in input una stringa contenente
delle parole separate da virgole e, opzionalmente, anche da spazi.
La funzione deve estrarre le parole da S, considerando solo quelle che
hanno una lunghezza compresa fra m ed M inclusi, ed inserirle in una seconda
lista ordinata alfabeticamente senza considerare la differenza tra maiuscole
e minuscole.
Ad esempio se S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
la funzione func3(S, 3, 4) restituirà ['Brad', 'Dana','ian', 'UMA', 'Zoe']
'''


def func3(S, m, M):
    S = S.replace(" ", "")
    L = S.split(",")
    result = []
    for i in L:
        if len(i)>= m and len(i) <= M:
            result.append(i)
    result.sort(key=lambda x : x.lower())
    return result

# Test della funzione func3
# print(func3("Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe", 3, 4))
# risultato: ['Brad', 'Dana','ian', 'UMA', 'Zoe']


# %% ----------------------------------- FUNC4 ------------------------- #
"""func4: 8 punti
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

contenuto di func4/test1_in.txt:
GE
wOa;II,see	ua;PAO,oA;wOA
pao iu;jJa,kE

Chiamata
n = func4("func4/test1_in.txt", "func4/test1_out.txt")

contenuto atteso di func4/test1_out.txt:
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


def func4(input_filename, output_filename):
    f = open(input_filename, "r", encoding="utf-8")
    L = f.readlines()
    f.close()
    result = dict()
    count = 0
    for l in L:
        l = l.strip()
        l = l.replace("\t", " ")
        l = l.replace(",", " ")
        l = l.replace(";", " ")
        W = l.split(" ")
        for w in W:
            count += 1
            minidict = dict()
            for i in w.lower():
                if i not in minidict:
                    minidict[i] = 1
                else:
                    minidict[i] += 1
            letters = list(minidict.items())
            letters.sort(key=lambda x : -x[1])
            j = 0
            while j < len(letters):
                if j < len(letters) - 1 and letters[j][1] == letters[j + 1][1]:
                    j += 1
                else:
                    break
            letters = letters[0:j+1]
            for i in letters:
                if i[0] not in result:
                    result[i[0]] = [w]
                else:
                    result[i[0]].append(w)
    for i in result:
        result[i].sort(key=lambda x : (x.lower(), x))
    result = list(result.items())
    result.sort()
    f = open(output_filename, "w", encoding="utf-8")
    for i in result:
        f.write(i[0] + ": " + " ".join(i[1]) + "\n")
    f.close()
    return count

# n = func4("func4/test1_in.txt", "func4/test1_out.txt")
# print(n)

# %% ----------------------------------- FUNC5 ------------------------- #
"""func5: 6 punti
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
restituire il numero di pixel il cui colore e' stato sostituito col nero.
"""
import images


def func5(file_in, file_out):
    image = images.load(file_in)
    black = (0, 0, 0)
    count = 0
    out_img = []
    for row in image:
        D = dict()
        for pixel in row:
            if pixel != black:
                if pixel not in D:
                    D[pixel] = 1
                else:
                    D[pixel] += 1
        L = list(D.items())
        L.sort(key=lambda x : (-x[1], x[0][0], x[0][1], x[0][2]))
        L = L[1:]
        L = [x[0] for x in L]
        for i in range(len(row)):
            if row[i] in L:
                row[i] = black
                count += 1
        out_img.append(row)
    images.save(out_img, file_out)
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

def scantree(T, nodes, n):
    nodes = nodes + [T.value]
    if T.left is None and T.right is None:
        if sum(nodes) == n:
            return [nodes]
        else:
            return []
    else:
        result = []
        if T.left is not None:
            result += scantree(T.left, nodes, n)
        if T.right is not None:
            result += scantree(T.right, nodes, n)
        return result

def ex1(T, n):
    result = scantree(T, [], n)
    result.sort()
    return result

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
k = 3

Output atteso:
{'dbb', 'bba', 'bbd', 'abb'}
"""

def combine(L):
    if len(L) == 1:
        return {L[0]}
    result = set()
    for i in range(len(L)):
        # result.add(L[0] + i)
        # result.add(i + L[0])
        others = list(combine(L[:i]+L[i+1:]))
        for a in others:
            result.add(L[i] + a)
            result.add(a + L[i])
        result = set(list(result) + list(combine(L[:i]+L[i+1:])))
    return set(result)

def ex2(L, k):
    allcombs = combine(L)
    result = []
    for l in allcombs:
        if len(l) == k and (l not in L):
            result.append(l)
    return set(result)

    
# Test della funzione ex2
# print(ex2(['a', 'bb', 'ccc', 'd'], 4))
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

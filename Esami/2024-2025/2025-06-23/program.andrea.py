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
D, in cui ogni chiave e' un intero positivo N e il corrispondente valore
e' una lista di caratteri alfabetici L.
La funzione ritorna una lista in cui ogni item ' una stringa ottenuta ripetendo
N volte ciascuno dei caratteri in L. La lista e' ordinata in ordine alfabetico
decrescente.
Ad esempio se D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'], la funzione ritornera'
L = ['uu', 'ss', 'qqq', 'ee', 'aaa']
'''


def func1(D):
    ## Scrivi qui il tuo codice
    pass
    return sorted(
        [c * n for n, L in D.items() for c in L],
        reverse=True
    )

# Test della funzione func1
# print(func1({2: ['s', 'u', 'e'], 3: ['q', 'a']}))
# risultato: ['uu', 'ss', 'qqq', 'ee', 'aaa']


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(L) che ha come parametro una lista L di N liste.
Ogni lista P della lista L e' cosi' definita:
- P puo' essere vuota oppure contenere una sola lista, a sua volta definita come P.
La funzione ritorna una lista di N interi, in cui l'elemento i-esimo
indica il numero di liste nidificate nella lista in i-esima posizione di L.
Ad esempio, se L = [ [[]], [], [[[]]], [[]], [[[[]]]], [], [[[]]] ]
la funzione restituira' [1, 0, 2, 1, 3, 0, 2]
'''


def func2(L):
    ## Scrivi qui il tuo codice
    pass
    return [count_nested_tuples(p) for p in L]

def count_nested_tuples(p):
    """Controlla quante tuple nidificate ci sono in p."""
    if not isinstance(p, list) or not p:  # Se p non è una tupla o è vuota
        return 0
    count = 1  # Conta la tupla corrente
    for item in p:
        count += count_nested_tuples(item)  # Conta le tuple nidificate
    return count

# Test della funzione func2
# print(func2( [ [[]], [], [[[]]], [[]], [[[[]]]], [], [[[]]] ])
# risultato: [1, 0, 2, 1, 3, 0, 2]

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S) che riceve in input una stringa contenente
delle parole separate da virgole ed, opzionalmente, anche da spazi.
La funzione deve estrarre le parole da S, considerando solo quelle che
cominciano con una vocale, ed inserirle in una seconda lista ordinata
alfabeticamente senza considerare la differenza tra maiuscole e minuscole.
Ad esempio se S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
la funzione restituira': ['ALIce', 'ian', 'oscar', 'UMA']
'''


def func3(S):
    ## Scrivi qui il tuo codice
    pass
    # Split the string by commas and strip spaces
    parole = [p.strip() for p in S.split(',')]
    # Filter words that start with a vowel (case insensitive)
    parole_vocali = [p for p in parole if p and p[0].lower() in 'aeiou']
    # Sort the list alphabetically, ignoring case
    parole_vocali.sort(key=lambda x: x.lower())
    return parole_vocali

# Test della funzione func3
# print(func3("Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"))
# risultato: ['ALIce', 'ian', 'oscar', 'UMA']


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti
Definire la funzione func4(input_filepath, output_filepath) che legge il
file indicato da input_filepath.  Il file di input contiene parole separate
da ritorni a capo, spazi, tabulazioni, virgole o punto e virgola.  Due parole sono
considerate identiche se coincidono ignorando la distinzione
tra minuscole e maiuscole; in tal caso, la parola va considerata una sola volta.

Le parole considertae vanno raggruppate secondo la loro ultima lettera,
senza distinzione fra maiuscole e minuscole. Per ogni gruppo occorre
scrivere nel file di output una riga nel formato:

<lettera minuscola>: <numero parole>

La lettera iniziale di riga è in minuscolo, seguita da ": " (due punti più
spazio); di seguito, compare il numero di parole che terminano con quella lettera,
indipendentemente dal fatto che la lettera nella parola sia maiuscola o minuscola.
Le righe devono apparire in ordine alfabetico decrescente in base alla
lettera.

Attenzione, alla fine di ogni riga nel file di output NON c'e' alcuno spazio ma c'e'
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
u: 1
o: 1
i: 1
e: 3
a: 4

Valore restituito: 12
"""


def func4(input_filename, output_filename):
    ## Scrivi qui il tuo codice
    pass
    with open(input_filename, 'r', encoding='utf-8') as infile:
        # Read the file and split into words
        content = infile.read().lower()
        for char in ' \t\n,;':
            content = content.replace(char, ' ')
        words = content.split()
    totwords = len(words)
    uniques = set(words)  # Use a set to remove duplicates
    # Create a dictionary to count words by their last letter
    last_letter_count = {}
    for word in uniques:
        if word[-1] not in last_letter_count:
            last_letter_count[word[-1]] = 0
        last_letter_count[word[-1]] += 1
    # Write the results to the output file
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for letter in sorted(last_letter_count.keys(), reverse=True):
            outfile.write(f"{letter}: {last_letter_count[letter]}\n")
    return totwords

# Test della funzione func4
# print(func4("func4/in_test1.txt", "func4/func4_out1.txt"))
# risultato: 12


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti
Definire la funzione func5(file_in, file_out) che usa images.load per
caricare l'immagine presente in file_in. L'immagine è una lista di liste
e ogni elemento interno è un pixel rappresentato dalla tupla (r, g, b).
Lo sfondo è completamente nero, cioè (0, 0, 0).

Nell'immagine possono apparire solo i seguenti gruppi di pixel non neri,
tutti di colore uniforme:
- gruppi 1x1, 1x2 o 2x1
- gruppi 2x2

Non esistono gruppi più grandi di 2x2 e due o piu' gruppi distinti ma vicini
sono sempre separati da pixel neri.

La funzione deve:
1. individuare tutti i blocchi 2x2 in cui i 4 pixel sono dello
   stesso colore non nero;
2. sostituire i quattro pixel con il nero, lasciando invariato il resto
   dell'immagine;
3. salvare il risultato in file_out mediante images.save;
4. restituire il numero di blocchi 2x2 trovati e oscurati.
"""
import images


def func5(file_in, file_out):
    ## Scrivi qui il tuo codice
    pass
    img = images.load(file_in)
    count = 0
    rows = len(img)
    cols = len(img[0])
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            # Check for 2x2 blocks
            if (x < cols - 1 and y < rows - 1 and
                    pixel == img[y][x + 1] == img[y + 1][x] == img[y + 1][x + 1] != (0, 0, 0)):
                # Found a 2x2 block, replace with black
                img[y][x] = img[y][x + 1] = img[y + 1][x] = img[y + 1][x + 1] = (0, 0, 0)
                count += 1
    images.save(img, file_out)
    return count

# Test della funzione func5
# print(func5("func5/in_test1.png", "func5/out_test1.png"))
# risultato: 3 (il numero di blocchi 2x2 trovati nell'immagine di test)

# %% ----------------------------------- EX.1 ------------------------- #
'''
Ex1: 6 punti.   # NOTA: aggiungere un test con un albero asimmetrico

Si consideri la classe BinaryTree contenuta nel file tree.py che definisce
un nodo di albero binario. Scrivere una funzione ex1(T) ricorsiva o che faccia
uso di una o piu' funzioni ricorsive.
La funzione riceve la radice di un BinaryTree come input. Nei nodi
dell'albero in input sono memorizzate delle stringhe vuote.
La funzione deve percorrere tutto l'albero e modificarlo in-place,
in modo che ogni nodo contenga una stringa di N asterischi, dove
N e' il livello del nodo. La radice si trova a livello 0, quindi
alla fine dell'esecuzione di ex1 conterra' ancora una stringa vuota.
La funzione ritorna l'altezza dell'abero (un albero con solo la
radice ha altezza 0).
Ad esempio, se T e' il seguente albero:

          ""                livello 0
       --------
       |      |
      ""      ""            livello 1
  ---------    --
  |       |      |
  ""     ""     ""          livello 2
  
Dopo aver eseguito la funzione, quest ritornera' il
valore 2 e T conterra':
          ""                livello 0
       --------
       |      |
      "*"    "*"            livello 1
  ---------    --
  |       |      |
 "**"    "**"   "**"        livello 2
'''
import tree


def ex1(T):
    ## Scrivi qui il tuo codice
    pass
    return _ex1(T, 0)

def _ex1(node, level):
    if node is None:
        return level - 1  # Return the height of the tree
    # Set the string in the current node to '*' repeated level times
    node.value = '*' * level
    # Recursively process left and right children
    left_height = _ex1(node.left, level + 1)
    right_height = _ex1(node.right, level + 1)
    # Return the maximum height of the tree
    return max(left_height, right_height)

# Test della funzione ex1
# print(ex1(tree.BinaryTree.fromList(["", ["", ["", None, None], None], ["", None, ["", None, None]]])))
# risultato: 2

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 punti

Scrivere la funzione ex2(L, k) ricorsiva oppure che faccia uso di
funzioni ricorsive. L è una lista di N liste di caratteri, ciascuna non
vuota. k è un intero compreso tra 0 e N.

Ogni carattere è una stringa di lunghezza 1 composta da sole lettere
ASCII minuscole. La funzione deve costruire e restituire la lista, ordinata in
modo alfabetico crescente, di tutte le stringhe lunghe N ottenute
scegliendo un carattere dalla prima sottolista, uno dalla seconda e così
via, a condizione che il numero totale di vocali presenti nella stringa
(esattamente le lettere 'a', 'e', 'i', 'o', 'u') sia pari a k.

Se in L compaiono caratteri ripetuti, l'output non deve contenere
duplicati: ogni stringa va inserita una sola volta.

Esempio:
L = [['c', 'q', 'a', 'a'], ['w', 'e', 'y']]
k = 1

Output atteso:
['aw', 'ay', 'ce', 'qe']
"""


def ex2(L, k):
    ## Scrivi qui il tuo codice
    pass
    strings = [p for p in _ex2(L,k) if conta_vocali(p) == k ]
    return sorted(strings)

def conta_vocali(p):
    """Controlla quante vocali ci sono in p."""
    return sum(1 for c in p if c in 'aeiou')

def _ex2(L, k):
    if not L:
        return ['']
    head, *tail = L
    return [ c + s  for c in set(head)
                    for s in _ex2(tail, k)
                    if conta_vocali(c + s) <= k]


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

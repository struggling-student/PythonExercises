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
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome       = "Maurizio"
cognome    = "Mancini"
matricola  = "1234"

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
    res = []
    for k in D:
        for i in D[k]:
            res.append(k * i)
    res.sort(reverse=True)
    return res


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti
Si definisca la funzione func2(L) che ha come parametro una lista L di N tuple.
Ogni tupla P della lista L e' cosi' definita:
- P puo' essere vuota oppure contenere una sola tupla, a sua volta definita come P.
La funzione ritorna una lista di N interi, in cui l'elemento i-esimo
indica il numero di tuple nidificate nella tupla in i-esima posizione di L.
Ad esempio, se L = [(()), (), ((())), (()), (((()))), (), ((()))]
la funzione restituira' [1, 0, 2, 1, 3, 0, 2]
'''
def func2(L):
    result = []
    for item in L:
        counter = 0
        while len(item) > 0:
            item = item[0]
            counter +=1
        result.append(counter)
    return result


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S) che riceve in input una stringa contenente
delle parole separate da virgole ed, opzionalmente, anche da spazi.
La funzione deve estrarre le parole da S, considerando solo quelle che
cominciano con una vocale, ed inserirle in una seconda lista ordinata
alfabeticamente senza considerare la differenza tra maiuscole e minuscole.
Ad esempio se S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
la funzione restituira': ['ALIce', 'ian', 'oscar', 'UMA', 'Zoe']
'''

def func3(S):
    vowels = ['a', 'e', 'i', 'o', 'u']
    L = [x.strip() for x in S.split(",")]
    L = [x for x in L  if x[0].lower() in vowels]
    L.sort(key=lambda x : x.lower())
    return L


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
    f = open(input_filename, "r", encoding="utf-8")
    L = f.readlines()
    f.close()
    separators = " ,;\t\n"
    word =""
    words = []
    res = dict()
    counter = 0
    for l in L:
        for c in l:
            if c in separators and word != "":
                counter += 1
                if  word.lower() not in words:
                    word = word.lower()
                    words.append(word)
                    if word[-1] not in res:
                        res[word[-1]] = 1
                    else:
                        res[word[-1]] += 1
                word = ""
            if c not in separators:
                word+=c
    letters = sorted(res.keys(), reverse=True)
    f = open(output_filename, "w", encoding="utf-8")
    for l in letters:
        f.write(l + ": " + str(res[l]) + "\n")
    f.close()
    return counter

# print(func4("func4/in_test1.txt", "func4/out_test1.txt"))
# print(func4("func4/in_test2.txt", "func4/out_test2.txt"))
# print(func4("func4/in_test3.txt", "func4/out_test3.txt"))
# print(func4("func4/in_test4.txt", "func4/out_test4.txt"))

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
    black = (0, 0, 0)
    img_in = images.load(file_in)
    img_out = [[black for i in range(len(img_in[0]))] for j in range(len(img_in))]
    counter = 0
    for i in range(len(img_in) - 1):
        for j in range(len(img_in[0]) - 1):
            if img_in[i][j] != black and img_in[i][j+1] != black and img_in[i+1][j] != black and img_in[i+1][j+1] != black:
                counter += 1
                img_in[i][j] = black
                img_in[i+1][j] = black
                img_in[i][j+1] = black
                img_in[i+1][j+1] = black
            else:
                img_out[i][j] = img_in[i][j]

    for i in range(len(img_in)):
        img_out[i][len(img_in[0]) - 1] = img_in[i][len(img_in[0]) - 1]
    for j in range(len(img_in[0]) - 1):
        img_out[len(img_in) - 1][j] = img_in[len(img_in) - 1][j]
    images.save(img_out, file_out)
    return counter

# print(func5("func5/in_test1.png", "func5/out_test1.png"))
# print(func5("func5/in_test2.png", "func5/out_test2.png"))
# print(func5("func5/in_test3.png", "func5/out_test3.png"))
# print(func5("func5/in_test4.png", "func5/out_test4.png"))

# %% ----------------------------------- EX.1 ------------------------- #
'''
Ex1: 6 punti

Si consideri la classe BinaryTree contenuta nel file tree.py che definisce
un albero binario. Scrivere una funzione ex1(T) ricorsiva o che faccia
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


def ex1_helper(node, level):
    if node is None:
        return level - 1  # nodo vuoto: altezza -1 rispetto al padre
    node.value = '*' * level
    left_height = ex1_helper(node.left, level + 1)
    right_height = ex1_helper(node.right, level + 1)
    return max(left_height, right_height)

def ex1(T):
    return ex1_helper(T, 0)


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
['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy']
"""

def is_vowel(c):
    return c in 'aeiou'

def ex2_helper(L, k, pos, current, vowels, results):
    if pos == len(L):
        if vowels == k:
            results.add("".join(current))
        return

    seen = set()
    for c in L[pos]:
        if c in seen:
            continue
        seen.add(c)
        ex2_helper(L, k, pos + 1, current + [c], vowels + is_vowel(c), results)

def ex2(L, k):
    results = set()
    ex2_helper(L, k, 0, [], 0, results)
    return sorted(results)

    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)

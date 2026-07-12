#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Operazioni da fare PRIMA DI TUTTO:
1) Salvare questo file col nome program.py
2) Compilare le variabili sottostanti con NOME, COGNOME, MATRICOLA

Valutazione:
- Il punteggio finale è la somma dei punti degli esercizi corretti.
- Per superare la prova è necessario avere punteggio >= 18 (>= 15 se DSA).
"""
nome = "A"
cognome = "S"
matricola = "42"

# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 2 punti — Run-Length Encoding (RLE)

INPUT:
- s: stringa (può contenere qualsiasi carattere, inclusi spazi)

OUTPUT:
- una stringa che rappresenta s compressa con RLE:
  ogni blocco MASSIMO di caratteri uguali consecutivi viene sostituito da:
      <carattere><conteggio>

NOTE IMPORTANTI:
- Il conteggio è sempre in base 10 (es. 12, 3, 1, ...).
- Non inserire separatori tra i blocchi.
- Se s è vuota, ritorna la stringa vuota.

WORKED EXAMPLE (passo-passo):
s = "aaabbc"
- blocco 1: "aaa"  -> "a3"
- blocco 2: "bb"   -> "b2"
- blocco 3: "c"    -> "c1"
concateno: "a3" + "b2" + "c1" = "a3b2c1"
"""
def func1(s: str) -> str:
    pass
    # inserisci qui il tuo codice
    last = None
    count = 0
    result = ""
    for char in s:
        if last is None:         # se è il primo carattere
            last = char
            count = 1
        elif last != char:       # se cambia il carattere
            result += last + str(count)
            last = char
            count = 1
        else:                    # altrimenti è lo stesso
            count += 1
    if last is None:
        return ""
    else:
        result += last + str(count)  # resta l'ultima sequenza
        return result


# %% ----------------------------------- FUNC.2 ----------------------------------- #
"""
Func 2: 2 punti — Intersezione tra multinsiemi

INPUT:
- a, b: liste di interi

OUTPUT:
- una lista contenente gli elementi comuni ad a e b CON molteplicità.
  Per ogni valore x, x deve comparire nel risultato esattamente:
      min(freq_a(x), freq_b(x))
  volte.

NOTE IMPORTANTI:
- L'ordine nel risultato NON è importante.
- Puoi restituire gli elementi in qualunque ordine.

WORKED EXAMPLE (passo-passo):
a = [1, 2, 2, 3]
b = [2, 2, 2, 4]
frequenze:
  freq_a(2)=2, freq_b(2)=3  -> min=2  => nel risultato ci sono due "2"
  freq_a(1)=1, freq_b(1)=0  -> min=0  => nessun "1"
  freq_a(3)=1, freq_b(3)=0  -> min=0  => nessun "3"
risultato possibile: [2, 2]
"""
def func2(a: list[int], b: list[int]) -> list[int]:
    pass
    # inserisci qui il tuo codice
    comuni = set(a) & set(b)
    return [ x
             for x in comuni
             for _ in range(min(a.count(x), b.count(x)))]


# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 4 punti — Valutazione di espressioni RPN (Reverse Polish Notation)

INPUT:
- tokens: lista di stringhe. Ogni token è:
  - un intero (es. "12", "-3") oppure
  - un operatore tra: "+", "-", "*", "//"

OUTPUT:
- l'intero risultato dell'espressione, valutata da sinistra a destra con uno stack.

NOTA: uno stack è una struttura dati in cui sono disponibili le 2 operazioni
    - push: si aggiunge un elemento in fondo
    - pop: si toglie l'ultimo elemento
può essere realizzato con una lista e i suoi metodi push e pop

REGOLE OPERATIVE:
- Quando leggi un numero: push nello stack.
- Quando leggi un operatore: pop b, poi pop a, calcola (a op b), push del risultato.
  (ATTENZIONE all'ordine: è a op b, non b op a)
- "//" è la divisione intera di Python (floor division), valida anche con numeri negativi.

WORKED EXAMPLE (passo-passo):
tokens = ["2", "1", "+", "3", "*"]
stack:
  leggo "4" -> push -> [4]
  leggo "1" -> push -> [4, 1]
  leggo "-" -> pop 1 e 4 -> 4-1=3 -> push -> [3]
  leggo "3" -> push -> [3, 3]
  leggo "*" -> pop 3 e 3 -> 3*3=9 -> push -> [9]
risultato finale: 9

NOTA: potete assumere che le espressioni sono sempre corrette
- non capita mai che la stack sia vuota quando dovete fare una operazione
- nè che la stack contenga più di un valore alla fine
"""
def func3(tokens: list[str]) -> int:
    pass
    # inserisci qui il tuo codice
    stack = []
    for token in tokens:
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        elif token == "//":
            b = stack.pop()
            a = stack.pop()
            stack.append(a//b)
        else:
            stack.append(int(token))
    assert len(stack) == 1, f"restano più valori sullo stack: {stack}"
    return stack.pop()

# %% ----------------------------------- FUNC.4 ----------------------------------- #
"""
Func 4: 4 punti — Aggregazione di un "log" tipo CSV (nome,quantità)

INPUT:
- path: percorso di un file di testo.
  Ogni riga non vuota ha il formato:
      nome,quantità
  dove:
    - nome è una stringa SENZA virgole
    - quantità è un intero (può essere negativo)
  Le righe vuote o composte solo da spazi vanno ignorate.

OUTPUT:
- un dizionario {nome: somma_totale} che somma tutte le quantità con lo stesso nome.

WORKED EXAMPLE (passo-passo):
Contenuto file:
  mele,2
  pere,3
  mele,-1

calcolo:
  mele: 2 + (-1) = 1
  pere: 3
output: {"mele": 1, "pere": 3}
"""
def func4(path: str) -> dict[str, int]:
    pass
    # inserisci qui il tuo codice
    D = {}
    with open(path) as csvfile:
        for riga in csvfile:
            if riga.strip() == "": continue
            K, V = riga.split(",")
            V = int(V)
            K = K.strip()
            D[K] = D.get(K, 0) + V
    return D


# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 6 punti — Colore non-nero più frequente in un PNG

INPUT:
- path_in: percorso di un file PNG.
  L'immagine si carica con images.load(path_in) e ritorna una matrice di pixel (R,G,B).

DEFINIZIONE:
- Il colore "nero" è (0,0,0).
- Considera solo i pixel NON neri.

OUTPUT:
- una coppia (color, count) dove:
  - color è la tupla (R,G,B) del colore non-nero più frequente
  - count è quante volte appare quel colore

CASI PARTICOLARI:
- Se non esistono pixel non-neri: ritorna ((0,0,0), 0).
- In caso di parità di frequenza: scegli il colore lessicograficamente minore
  (confronto tra tuple RGB, es. (10,0,0) < (10,0,1)).

WORKED EXAMPLE (passo-passo):
Immagina una griglia 2x3 (R,G,B abbreviato):
  [(0,0,0), (1,0,0)]
  [(1,0,0), (2,0,0)]
  [(2,0,0), (2,0,0)]

conteggi non-neri:
  (1,0,0) -> 2
  (2,0,0) -> 3
più frequente: (2,0,0) con count=3
output: ((2,0,0), 3)
"""
import images
def func5(path_in: str) -> tuple[tuple[int, int, int], int]:
    pass
    # inserisci qui il tuo codice
    img =images.load(path_in)
    colori = {}
    for riga in img:
        for colore in riga:
            if colore != (0,0,0):
                colori[colore] = colori.get(colore, 0) + 1
    massimo = max(colori.values())
    massimi = [ c for c,v in colori.items() if v == massimo ]
    if massimi:
        return sorted(massimi)[0], massimo
    else:
        return (0,0,0), massimo


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 8 punti (RICORSIVO) — Parentesi bilanciate con wildcard '*'

INPUT:
- s: stringa composta solo dai caratteri '(', ')', '*'

SIGNIFICATO DI '*':
ogni '*' può essere interpretato come:
  - '('
  - ')'
  - stringa vuota ""

OUTPUT:
- True se ESISTE almeno una sostituzione dei '*' che rende la stringa bilanciata,
  altrimenti False.

VINCOLO:
- Deve essere ricorsiva (o usare funzioni/metodi ricorsivi).

WORKED EXAMPLE (passo-passo):
s = "(*))"
Possibile interpretazione:
  - sostituisco '*' con '(' -> "(())"
"(())" è bilanciata => ex1("(*))") ritorna True

NOTA: potete assumere che la stringa abbia un numero pari di caratteri
"""
def ex1(s: str) -> bool:
    pass
    # inserisci qui il tuo codice
    return rimpiazza_asterischi_e_bilancia(s)

def rimpiazza_asterischi_e_bilancia(stringa: str) -> bool:
    # se ho rimpiazzato tutti gli asterischi provo a vedere se sono bilanciate
    if stringa.count('*') == 0:
        res = bilanciata(stringa)
        #print(stringa, res)
        return res
    # altrimenti sostituisco un asterisco con le due possibilità
    caso1 = stringa.replace('*', '(', 1)
    caso2 = stringa.replace('*', ')', 1)
    return (   rimpiazza_asterischi_e_bilancia(caso1)
            or rimpiazza_asterischi_e_bilancia(caso2))

def bilanciata(stringa, aperte=0):
    "bilanciamento su una stringa di sole ( e )"
    if aperte < 0:
        return False
    if stringa == "":
        return aperte == 0
    if stringa[0] == '(':
        return bilanciata(stringa[1:], aperte+1)
    else: # )
        return bilanciata(stringa[1:], aperte-1)

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti (RICORSIVO) — Somma dei nodi ai livelli dispari

DEFINIZIONE DI LIVELLO:
- livello 0: la radice
- livello 1: i figli della radice
- livello 2: i nipoti, ecc.

OUTPUT:
- la somma dei valori dei nodi che stanno a livello dispari (1,3,5,...).
- se root è None: ritorna 0.

VINCOLO:
- Deve essere ricorsiva (o usare funzioni/metodi ricorsivi).

WORKED EXAMPLE (passo-passo):
     10
    /  \
   5    7
  /
 3

livelli:
  livello 0: 10
  livello 1: 5 + 7 = 12
  livello 2: 3
somma livelli dispari = 12
output: 12
"""
import tree
def ex2(root: tree.BinaryTree, livello=0) -> int:
    pass
    # inserisci qui il tuo codice
    if root is None:
        return 0
    else:
        S  = ex2(root.left, livello+1)
        S += ex2(root.right, livello+1)
        if livello%2:
            S += root.value
        return S

if __name__ == '__main__':
    print('*' * 50)
    print('Eseguire grade.py per il test automatico.')
    print('*' * 50)
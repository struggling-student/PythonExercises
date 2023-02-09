################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE SUBITO QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG 
#   per eseguire solo parte dei test commentare le righe 288-292 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''
    Es 1: punti 6
Un file di testo contiene una sequenza di interi separati tra loro  da spazi e andate a capo. 
progettare una funzione es1(ftesto) che, prende in input 
l'indirizzo di un file di testo siffatto e restituisce un dizionario avente per chiavi degli interi e 
per attributo delle stringhe.
Le chiavi del dizionario sono interi e si ottengono a partire dalle stringhe di interi 
presenti nel file che contengono almeno una cifra non duplicata.
La chiave della stringa si ottiene col seguente procedimento: 
- elimina le cifre che compaiono piu' volte nella stringa
- riordina cifre rimaste in ordine crescente 
- trasforma la stringa in un intero 
Nota che  stringhe di interi diversi possono generare una stessa chiave come nel caso 
delle stringhe   '2161', '3325556' e '62'  che generano tutte la chiave 26. 
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata.
Le stringhe nella lista devono comparire  ordinate per lunghezza crescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f1.txt  la funzione restituisce  il dizionario:
{
 25: ['577020', '5624466'], 
  6: ['6', '677'], 
  1: ['3122233']
}
'''
def es1(fname):
    # inserisci qui il tuo codice
    result = {}
    with open(fname) as F:
        for stringa in F.read().split():
            k = kiave(stringa)
            if k:
                k = int(k)
                if k in result:
                    result[k].append(stringa)
                else:
                    result[k] = [ stringa ]
    for k in result:
        result[k].sort(key=lambda elemento: (len(elemento), elemento))
    return result

def kiave(stringa):
    conta = {}
    for c in stringa:
        if c in conta:
            conta[c] += 1
        else:
            conta[c]  = 1
    for k,v in conta.copy().items():
        if v > 1:
            del conta[k]
    return ''.join(sorted(conta.keys()))

    
#####################################################################################


'''    
    Es 2: punti 7
    
    Data un'immagine colorata e due insiemi di colori A e B  vogliamo individuare 
    gli indici di riga e gli indici di colonna dell'immagine 
    in cui compaiono pixel di tutti i colori dell'insieme A e nessun pixel con  colori dell'insieme B.

    
    Progettare la  funzione es2(fname) che prende come parametri 
    l'indirizzo di un file .PNG contenente un'immagine colorata  e gli insiemi di colori   
    (rappresentati tramite triple RGB) A e B e restituisce la coppia di liste (X,Y) dove:
    - X contiene gli indici delle RIGHE dell'immagine in cui compaiono pixel di tutti i colori 
      dell'insieme A e nessun pixel di colori dell'insieme B 
    - Y contiene gli indici  delle COLONNE dell'immagine in cui compaiono pixel di tutti 
      i colori dell'insieme A e nessun pixel coi colori dell'insieme B 
    
    Gli indici nelle liste devono comparire in ordine crescente.    
    Ad esempio per il file Rettangoli.png e l'insieme di colori A={(0,255,0), (255,0,0)}  e B={(0,0,0)}
    la funzione restituisce la coppia ([],[40,41,42,....,69])
    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

import immagini

def es2(fname1, A, B):
    # inserisci qui il tuo codice
    img = immagini.load(fname1)
    H, W = len(img), len(img[0])
    righe = [ y for y,riga in enumerate(img) if set(riga).intersection(B) == set() and set(riga).intersection(A) == A ]
    colonne = []
    for x in range(W):
        colori = { riga[x] for riga in img }
        if colori.intersection(B) == set() and colori.intersection(A) == A:
            colonne.append(x)
    return righe, colonne


############################################################################


'''
    Es. 3: punti 9
    Un cammino dalla radice ad un nodo di un albero binario puo' essere rappresentato 
    tramite una stringa binaria:
    si parte dalla radice e scorrendo i bit della stringa si prosegue verso il nodo sinistro 
    o il nodo destro, piu' precisamente: il bit 0 indica di muoversi verso il figlio di 
    sinistra  mentre il bit 1 indica di proseguire verso il figlio di destra.  
    
    Ad esempio per l'albero:
     0
    / \
   5   6 
      / 
     3
    / \ 
   9   7

   la stringa '0' porta al nodo di valore 5, la stringa '10' porta al nodo di valore 3 mentre la stringa '100' 
   porta al nodo di valore 9 
   
    Si definisca la funzione es3(r) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che  riceve come parametri la radice r di un albero binario
    formato da nodi del tipo AlberoBinario definito nella libreria albero.py e una lista 
    di stringhe binarie rappresentanti cammini dell'albero e restituisce una lista di valori. 
    La lista restituita ha lunghezza pari a quella della lista dei cammini e in posizione i 
    contiene il valore del nodo che si raggiunge utilizzando l'i-esima stringa della lista dei cammini.


Ad esempio per l'albero:
     0
    / \
   5   6 
      / 
     3
    / \ 
   9   7

e  lista dei cammini  ['0', '10', '100']   la funzione es3 restituisce la lista [5, 3, 9]


    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''


import albero

def es3(r,cammini):
    # inserisci qui il tuo codice
    pass
    return [ trova(cammino, r) for cammino in cammini ]

def trova(cammino, radice):
    if cammino == '':
        return radice.valore
    elif cammino[0] == '0':
        return trova(cammino[1:], radice.sx)
    else:
        return trova(cammino[1:], radice.dx)


  
###########################################################################

'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es(dirname) che
    riceve come argomento il nome di una directory (dirname).
    La funzione esplora la directory dirname e le sue sottodirectory e restituisce un dizionario.  
    Le chiavi del dizionario sono i path completi delle cartelle via via incontrate, 
    attributo di ciascuna chiave e' una lista ordinata lessicograficamente 
    contenente le estensioni dei file contenuti nella cartella.  
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio con dirname='dir1'  la funzione es4 deve restituire il dizionario:
    {
    'dir1': ['c', 'exe', 'pdf', 'txt'],
    'dir1/stanza1': [], 
    'dir1/stanza1/stanza2': ['png', 'py', 'txt']     
    } 
   
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os
def es4(dirname): 
    # inserisci qui il tuo codice
    pass
    dizio = esplora(dirname)
    for k in dizio:
        dizio[k] = sorted(dizio[k])
    return dizio

def esplora(dirname):
    result = { dirname : set() }
    for name in os.listdir(dirname):
        if name[0] in '._': continue
        fullname = f"{dirname}/{name}"
        if os.path.isfile(fullname):
            parti = name.split('.')
            if len(parti) > 1:
                result[dirname].add(parti[-1])
        else:
            result.update(esplora(fullname))
    return result

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
Es 1: punti ?.
Un file contiene una sequenza  di uguaglianze tra espressioni aritmetiche del tipo somme 
di prodotti di interi positivi. E' presente un'uguaglianza per ogni 
riga del file e ciascuna riga termina con un'andata a capo.

Si veda ad esempio il file uguaglianze1.txt. 
contenente le 4 uguaglianze:

2+3+12=9+8
2+3+4=9*2
22=3+4+5+2*5
3+5+1=4+44

Si noti che le uguaglianze possono essere sia corrette (la prima e la terza) che 
sbagliate (la seconda e l’ultima).

Si progetti una funzione es1(ftesto) che prende in input   l'indirizzo 
del file contenente la sequenza di uguaglianze e restituisce una lista binaria. 
La lista binaria deve contenenre  un bit per ogni uguaglianza del file. Il bit i-esimo della lista 
vale 1 se l'i-esima uguaglianza del file  e' corretta, 0 altrimenti. 

Per il file uguaglianze1.txt la funzione e1 deve restituire la lista [1,0,1,0]. 

ATTENZIONE: è proibito usare la funzione eval o similari per valutare le stringhe 
di somme di prodotti direttamente.
'''


def es1(fname):
    # inserisci qui il tuo codice
    with open(fname, encoding='utf8') as F:
        L = []
        for line in F:
            a,b=line.split('=')
            a=valuta(a)
            b=valuta(b)
            if a==b: L.append(1)
            else: L.append(0)
        return L
        
def valuta(a):
    somma = 0
    for p in a.split('+'):
        prodotto = 1
        for x in p.split('*'):
            prodotto *= int(x)
        somma += prodotto
    return somma

   

#####################################################################################


'''    
    Es 2: punti ?
    
    Abbiamo immagini che contengono su sfondo nero rettangoli di diversi colori che non 
    si intersecano   e i cui lati sono segmenti orizzontali o verticali. 
    Si consideri ad esempio la figura Rettangoli.png.
    Progettare la  funzione es2(fname,w1,h1) che prende come parametri 
    l'indirizzo di un file .PNG con figure siffatte e le coordinate (w1,h1) 
    di un punto  appartenente ad uno dei rettangoli della figura e restituisce 
    il numero di pixel occupati dal rettangolo
    
    Ad esempio per il file Rettangoli.png e il pixel 20,20 la funzione e2 deve restituire 4200.

    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

import immagini

def es2(fname,w1,h1):
    img = immagini.load(fname)
    w,h=len(img[0]),len(img)
    colore=img[h1][w1]
    a,b=w1,h1
    while a-1>=0 and img[h1][a-1]==colore: a-=1
    lar=1
    while a+1<w and img[h1][a+1]==colore: 
        a+=1
        lar+=1
    while b-1>=0 and img[b-1][w1]==colore: b-=1
    alt=1
    while b+1<h and img[b+1][w1]==colore: 
        b+=1
        alt+=1
    return alt*lar

    

############################################################################



'''
    Es. 3: punti ?
    Dato un intero n, l'albero dei divisori di n e' definito come segue:
    il nodo radice ha valore n e ogni altro nodo dell'albero ha come figli i divisori propri del valore del padre.
    Si ricorda che i divisori propri di un numero sono tutti i numeri positivi che lo dividono 
    tranne l'uno e il numero stesso. 
    Ad esempio i tre alberi che seguono sono nell'ordine, alberi dei divisori di 8, 12 e 25.
    
    
             8                     12                            25
            _|_                ____|_____                        | 
           |   |               |  |  |   |                       5
           2   4               2  3  4   6                         
               |                     |  _|_
               2                     2 |   |
                                       2   3 
    
    Si definisca la funzione es3(n) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come argomento un intero n e 
    genera l'albero dei divisori di n. I nodi dell'albero sono del tipo  Albero definito 
    nella libreria albero.py allegata.
    La funzione deve ritornare  la radice dell'albero generato.
    
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
    il test di ricorsione
    '''

import albero

def es3(n):
    # inserisci qui il tuo codice
    radice=albero.Nodo(n)
    dp=[i for i in range(2,n) if n%i==0]
    for y in dp:
        radice.f.append(es3(y))
    return radice 

  
###########################################################################

'''
    Es. 4: punti ?
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es4(dirname) che
    riceve come argomento il nome di una directory (dirname).
    La funzione esplora la directory dirname  e le sue sottodirectory 
    alla ricerca di file con lo stesso nome ed estensione 'txt' e ritorna un dizionario.
    Le chiavi del dizionario sono i nomi dei file   che appaiono piu' volte (privati dell'estenzione 'txt')
    gli attributi  sono insiemi che contengono  il nome per estero di ciascuno dei file ripetuti.
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio per la cartella dir1 la funzione es4 deve restituire il dizionario:
    d={
    'esercizio1': {'dir1/esercizio1.txt', 'dir1/st1/st3/esercizio1.txt', 'dir1/st1/esercizio1.txt'}
    'esercizio5': {'dir1/st1/st3/esercizio5.txt', 'dir1/st2/esercizio5.txt'}, 
    }
    
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os

def es4(dirname):
    d={} 
    es4R(dirname,d)
    return {x:d[x] for x in d if len(d[x])>1}

    
def es4R(dirname, d): 
    for fn in os.listdir(dirname):
        if fn[0] in '._': continue
        filename = dirname+'/'+fn
        if os.path.isfile(filename):
            base=os.path.basename(filename)
            if base[-4:] == '.txt':
                base=base[:-4]
                if base in d: d[base].add(filename)
                else:d[base]={filename}
        else:
            es4R(filename, d)






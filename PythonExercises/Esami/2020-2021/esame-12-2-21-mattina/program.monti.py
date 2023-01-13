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
#   per eseguire solo parte dei test commentare parte della lista "tests"
#   alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

''' 
    Es 1: punti 7 
    Le righe di un file di testo contengono uno o piu' interi separati
    da spazi. Progettare una funzione es1(ftesto) che, prende in input
    l'indirizzo di un file di testo siffatto e restituisce una lista
    di coppie di interi.  La lista contiene tante coppie quante sono
    le righe del file.  La riga i-esima della lista contiene la coppia
    che ha come prima coordinata la somma degli interi nella riga
    i-esima del file e come seconda coordinata il prodotto degli
    interi nella riga i del file. 
    
    Ad Esempio, per il file di testo
    f1.txt la funzione restituisce la lista: [(7,8), (11,30), (8,8), (6,8)]
'''

def es1(fname):
    with open(fname,encoding='utf-8') as f:
        lista_righe=f.read().split('\n')
    lista=[]
    for riga in lista_righe:
        riga1=[int(x) for x in riga.split()]
        a=sum(riga1)
        b=1
        for x in riga1:b*=x
        lista.append((a,b))
    return  lista  
    
        
#####################################################################################


'''    
    Es 2: punti 8
    
    Abbiamo un'immagine dove su sfondo nero sono disegnati in bianco
    rettangoli e quadrati che non si toccano ne si intersecano e i cui
    lati sono segmenti orizzontali o verticali.  Si veda ad esempio
    l'immagine in fig1.png.  Vogliamo trovare il numero di quadrati ed
    il numero di rettangoli presenti nell'immagine.
   
    Progettare la funzione es2(fname) che prende come parametro
    l'indirizzo di un file .PNG contenente l'immagine e restituisce la
    coppia di interi (x,y) dove x e' il numero di quadrati presenti
    nell'immagine e y il numero di rettangoli presenti nell'immagine.
    Ad esempio per l'immagine fig1.png la funzione deve restituire la
    coppia (3,2).
        
    Per caricare e salvare i file PNG si possono usare load e save
    della libreria immagini.
    '''

import immagini

def es2(fname1):
    img=immagini.load(fname1)
    x=y=0
    for i in range(len(img)-1):
        for j in range(len(img[0])-1):
            if img[i][j]==(255,255,255) and img[i+1][j]==(255,255,255) and img[i][j+1]==(255,255,255):
                if quadrato(i,j,img): 
                    x+=1
                else:
                    y+=1
    return (x,y)
    
def quadrato(i,j,img):
    l=h=0
    while j+l<len(img[0]) and img[i][j+l]==(255,255,255): l+=1
    while i+h<len(img) and img[i+h][j]==(255,255,255): h+=1  
    return l==h 


############################################################################


'''
    Es. 3: punti 8
   
    Si definisca la funzione es3(r1,r2) ricorsiva (o che fa uso di
    funzioni o metodi ricorsive/i) che riceve come parametri le radici
    r1 ed r2 di due alberi binari formati da nodi del tipo
    AlberoBinario definito nella libreria albero.py. I due alberi sono
    identici se non per il fatto che il valore di nodi corrispondenti
    non sempre coincide.  La funzione deve restituire una lista di
    coppie, una coppia per ogni coppia di nodi che non hanno lo stesso
    valore. La coppia contiene il valore del nodo del primo albero
    come prima coordinata ed il valore del nodo del secondo albero
    come seconda coordinata.  Le coppie nella lista devono risultare
    ordinate in modo decrescente.

    Ad esempio per gli alberi :
         0            0
        / \          / \
       5   6        5   1
          /            /
         3            3
        / \          / \
       9   7        2   7

    la funzione es3 restituisce la lista [(9,2), (6,1)]


    NOTA: definite le vostre sottofunzioni a livello esterno
          altrimenti non passate il test di ricorsione
`'''


import albero

def es3(r1,r2):
    # inserisci qui il tuo codice
    lista= es3a(r1,r2)
    return sorted(lista,reverse=True)


def es3a(r1,r2):
    lista=[]
    if r1.sx!=None:
        lista.extend(es3a(r1.sx,r2.sx))
    if r1.dx!=None:
        lista.extend(es3a(r1.dx,r2.dx))
    if r1.valore!=r2.valore: lista.append((r1.valore,r2.valore))
    return lista

  
###########################################################################


'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive)
    es(dirname) che riceve come argomento il nome di una directory
    (dirname) ed una stringa (s).  La funzione esplora la directory
    dirname e le sue sottodirectory alla ricerca di file con
    estensione .txt e restituisce un dizionario.  Le chiavi del
    dizionario sono tutte le stringhe trovate nei file .txt che hanno
    come sottostringa la stringa s. Attributo di ciascuna chiave e' il
    numero di volte per cui quella parola appare nei file .txt.
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio con dirname='dir1'  e s='arco' la funzione 
    es4 deve restituire il dizionario:
    {'parco': 1, 'arco': 3, 'Marco': 1, 'sarcofago': 1}
   
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno
          altrimenti non passate il test di ricorsione
'''    

import os
def es4(dirname,s): 
    # inserisci qui il tuo codice
    d={}
    return crea_diz(dirname,s,d)




def crea_diz(dirname,s,d):
    #print(d)
    l_f=os.listdir(dirname)
    for el in l_f:
        if el[0] in ['.','_']:
            continue
        pathc=os.path.join(dirname,el)
        if os.path.isdir(pathc):
            d=crea_diz(pathc,s,d)
        else:
            nome,ex= os.path.splitext(pathc)
            if ex[1:]=='txt':
                with open(pathc,encoding='utf-8') as f:
                    parole=f.read().split()
                for x in parole:
                    if s in x:
                        if x in d: 
                            d[x]+=1
                        else:
                            d[x]=1
    return d
                
            

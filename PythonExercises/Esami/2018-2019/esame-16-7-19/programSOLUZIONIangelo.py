################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################

'''
Es 1: punti ?.

Si progetti la funzione es1(lista1,lista2) che, prende in input 
due liste di stringhe aventi tutte una uguale  lunghezza e  restituisce un dizionario. 
Le chiavi del dizionario sono le stringhe  della prima lista, ad ognuna di queste chiavi
e'  associata  la stringa della seconda lista che coincide con la chiave nel maggior 
numero di posizioni. 
In caso di parita'  viene associata la stringa che precede le altre lessicograficamente. 
  
Ad Esempio, per 
lista1=['caso','melo','puri','pero','rana'] e 
lista2=['velo','volo','viso', 'vaso', 'dado','dito']
viene restituito il dizionario:
{'caso': 'vaso', 'melo': 'velo', 'puri': 'dado', 'pero': 'velo', 'rana': 'dado'}
'''
def es1(lista1,lista2):
    d={}
    lista2.sort()
    for s1 in lista1:
        m=-1
        for s2 in lista2:
            y=coincidenze(s1,s2)
            if y> m:
                associata=s2
                m=y
        d[s1]=associata
    return d
    
def coincidenze(s1,s2):
    tot=0
    for i in range(len(s1)):
        if s1[i]==s2[i]: tot+=1
    return tot


################################################################################

'''
Es 2: punti ?.

Si progetti la funzione es2(lista) che, prende in input una lista di stringhe, 
ciascuna di almeno tre caratteri , e restituisce un dizionario. 
Le chiavi del dizionario sono le tringhe di tre caratteri corrispondenti ai tre caratteri 
finali delle stringhe in lista. 
Ad ogni  chiave 
e' associata una  lista contenenti le stringhe in lista che terminano con quella  chiave. 
Le stringhe nelle liste del dizionario devono comparire in ordine 
di lunghezza decrescente e, a parita' di lunghezza, in ordine lessicografico.

Esempio: se la lista e':
['amare', 'cannone', 'cantare', 'dormire',  'gommone', 'torrone', 'burrone', 
'partire','estate','morire', 'fiorire']
il dizionario prodotto e':
{'are': ['cantare', 'amare'], 
 'one': ['burrone', 'cannone', 'gommone', 'torrone'], 
 'ire': ['dormire', 'fiorire', 'partire', 'morire'], 
 'ate': ['estate']
 }

'''
def es2(lista):
    # inserisci qui il tuo codice
    d={}
    for x in lista:
        y=x[len(x)-3:]
        if y in d:
            d[y].append(x)
        else:
            d[y]=[x]
    for s in d:
        d[s].sort(key=lambda x: (-len(x), x))
    return d 


#####################################################################################

'''
Es 3: punti ?.

Abbiamo una sequenza di valori reali e due valori interi s1 ed s2 (con s1 < s2).

A partire dalla sequenza  vogliamo crearne una nuova  nel modo seguente:

a) i valori v della sequenza originale tali che v < s1 devono trovarsi tutti 
   all’inizio della nuova sequenza, seguiti dal carattere '#'
b) i valori v della sequenza originale tali che s1 <= v < s2 devono trovarsi tutti 
   al centro della nuova sequenza, seguiti dal catattere '#'
c) i valori v della sequenza originale tali che v >= s2 devono  trovarsi alla fine 
   della nuova sequenza.
e) l’ordine con cui i valori reali compaiono nelle tre parti della nuova sequenza deve 
   essere lo stesso con cui comparivano nella sequenza originaria.
 

Ad esempio, sia  2.3 4.56 2 1.23 8.65 10 -12.3 4.34 16.22 2.3 la sequenza originaria,
a) se le soglie sono rispettivamente 2 e 5, 
   la nuova sequenza sara':
   1.23 -12.3 # 2.3 4.56 2 4.34 2.3 # 8.65 10 16.22
b) se le soglie sono 20, 25, 
   la nuova sequenza sara':
   2.3 4.56 2 1.23 8.65 10 -12.3 4.34 16.22 2.3 # #
c) se le soglie sono 11 e 12,
   la nuova sequenza sara':
   2.3 4.56 2 1.23 8.65 10 -12.3 4.34 2.3 # # 16.22


Si progetti la funzione es3(ftesto1,ftesto2,s1,s2) che prende come parametri
- ftesto1: l'indirizzo di un  file di testo in cui si trova la sequenza originale 
  codificata in un unica riga con ogni elemento separato dal successivo da uno spazio.
- ftesto2: l'indirizzo di un  file di testo in cui va salvata la nuova sequenza.
- s1,s2: i due valori interi di soglia s1 ed s2
La funzione es3 legge la sequenza da ftesto1, crea la nuova sequenza in base ai valori 
soglia s1 ed s2 e la salva in ftesto2 in una unica riga con ogni elemento 
separato dal successivo da un unico spazio. Infine restituisce 
il numero di elementi che nella nuova sequenza  finiscono al 
centro  (vale a dire gli elementi v della sequenza originaria per cui s1 <= v < s2).

'''

def es3(ftesto1,ftesto2,s1,s2):
    with open(ftesto1, encoding='utf8') as f:
        lista=f.read().split()
    st1,st2,st3,c='','','',0
    for x in lista:
        if float(x)<s1: 
            st1=st1+x+' '
        elif s1<=float(x)<s2: 
            st2=st2+x+' '
            c+=1
        else:
            st3=st3+x+' '
    s=st1+'# '+st2+'# '+st3
    s=s[:-1]
    with open(ftesto2, 'w', encoding='utf8') as f:
        f.write(s)
    return c



######################################################################################

import immagini

'''    
    Es 4: punti ?.
    
    Abbiamo immagini che contengono su sfondo nero cammini di color bianco 
    che non si intrecciano ne' si toccano e sono formati da segmenti orizzontali 
    o verticali consecutivi.
    Si veda ad Esempio l'immagine f4a.png 
    Progettare la  funzione es4(fimm) che prende come parametro 
    l'indirizzo di un file .PNG siffatto e restituisce il numero di diversi 
    cammini presenti nell'immagine.
    Ad esempio per il file f4a.png deve restituire 2.
    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

def es4(fimm):
    img = immagini.load(fimm)
    tot=0
    for w1 in range(len(img[0])):
        for h1 in range(len(img)):
            if estremo(img, w1,h1):
                tot+=1
    return tot//2
    
def estremo(img,w1,h1):
    # risponde True se il pixel (w1,h1) e' l'estremo di un cammino
    if img[h1][w1]!=(255,255,255): return False
    tot=0
    w,h=len(img[0]),len(img)
    if w1+1<w and  img[h1][w1+1]==(255,255,255):
            tot+=1
    if  h1+1<h  and img[h1+1][w1]==(255,255,255):
            tot+=1
    if  0<=w1-1 and img[h1][w1-1]==(255,255,255):
            tot+=1
    if  0<=h1-1 and img[h1-1][w1]==(255,255,255):
            tot+=1
    if tot==1: return True
    return False

############################################################################

import albero

'''
    Es 5: ? punti

    Si definisca la funzione es5(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata, 
    torna come risultato la lista degli identificativi dei nodi dell'albero. 
    La lista deve risultare ordinata in modo crescente.

    
    Esempio:  la funzione es1
    - sull'albero a sinistra restituisce  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20] 
    - sull'albero a destra restituisce [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15].


              5                                     7              
      ________|_____________                _______|______         
     |          |           |              |              |        
     20         4           6              5              9        
     |     _____|______                 ___|___        ___|__      
     11   |   |  |  |  |               |       |      |      |     
          10  2  9  8  7               10      8      3      1     
            __|__                     _|_     _|_    _|_    _|_    
           |     |                   |   |   |   |  |   |  |   |   
           3     1                   1   2   12  13 15  6  4   0   
                                                                   
    '''

def es5(tree):
    # inserisci qui il tuo codice
    return sorted(es5b(tree))
    
def es5b(tree):
    # inserisci qui il tuo codice
    lista=[tree.id]
    for x in tree.f:
        lista=lista + es5b(x)
    return lista 

###########################################################################

import albero

'''
    Es 6: ? punti


    Si definisca la funzione es6(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata e 
    torna come risultato la lista degli identificativi dei nodi dell'albero che sono 
    di sottoalberi con un numero pari di nodi. 
    La lista deve risultare ordinata in modo crescente.
    
    Esempio:  la funzione es6
    - sull'albero a sinistra restituisce  [4,5,20] 
    - sull'albero a destra restituisce [4,5].

              5                                    5                    
      ________|_____________               ________|_                   
     |          |           |             |          |                  
     20         4           6             20         4                  
     |     _____|______                           ___|___               
     12   |   |  |  |  |                         |   |   |              
          10  2  9  8  7                         2   9   7              
            __|__                                                       
           |     |                                                      
           30    22                                                     
                                                                        
    '''

def es6(tree):
    # inserisci qui il tuo codice
    lista,nodi= es6b(tree)
    return sorted(lista)
    
def es6b(tree):
    # restituisce la lista con gli identificativi dei nodi dell'albero 
    # radici di sottoalberi con un numero pari di nodi e il numero di nodi in tree.  
    lista=[]
    tota=1
    for x in tree.f:
        lista1,n1= es6b(x)
        tota+=n1
        lista=lista + lista1
    if tota%2==0: lista.append(tree.id)
    return (lista,tota) 


###########################################################################



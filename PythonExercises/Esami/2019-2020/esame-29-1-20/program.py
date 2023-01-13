################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

# ATTENZIONE: SONO VIETATE TUTTE LE ALTRE LIBRERIE

################################################################################
################################################################################
################################################################################

'''
Es 1: punti 3.

Si progetti la funzione es1(s,k) che, prende in input una stringa s di caratteri 
ed un intero k e restituisce una lista di tuple. 
Nella lista, per ogni sottostringa di s di lunghezza k,  e' presente una tupla.
Il primo elemento della tupla e' la sottostringa di lunghezza k, 
il secondo elemento e' un intero che rappresenta il numero di occorrenze 
di quella sottostringa in s.
Le tuple nella lista devono essere ordinate rispetto al secondo 
elemento decrescente e, a parita' , rispetto al primo elemento crescente.

Ad esempio con es1('aaxbaaxb',3)
viene restituita  la lista:
[('aax', 2), ('axb', 2), ('baa', 1), ('xba', 1)]
'''
def es1(s,k):
    # inserisci qui il tuo codice
    pass




################################################################################

'''
Es 2: punti 4.

Si progetti la funzione es2(lista1) che, prende in input una lista  
contenente tuple e restituisce una nuova lista, lista2. 
Ogni tupla  della prima lista è una tripla con informazioni 
su quadrati contenuti in una certa immagine. La tripla (w,h,l) indica che il vertice 
in alto a sinistra del quadrato in questione occupa nell'immagine il pixel 
di coordinate w,h ed il quadrato ha lato di lunghezza l.
La lista lista2 restituita dalla funzione e' una sottolista di lista1 e si ottiene   
in base alla seguente procedura:
Il primo quadrato di lista1 viene inserito in lista2 gli altri quadrati di lista1 vengono 
considerati in sequenza e ciascuno e' aggiunto in coda a lista2  solo se interseca 
almeno uno dei quadrati gia inseriti in lista2.

Ad esempio per lista1=[(10,20,40),(60,30,20),(20,30,20),(70,40,20),(50,60,10)]
viene restituita la lista 
[(10,20,40),(20,30,20),(50,60,10)]
'''

def es2(lista1):
    # inserisci qui il tuo codice
    pass




#####################################################################################

'''
    Es 3: punti 3
    Progettare la  funzione es3(fname) che prende in input 
    l'indirizzo di un file .PNG e restituisce una lista di tuple.
    Le tuple della lista sono le terne RGB dei colori presenti nella foto. 
    Le tuple della lista devono essere ordinate in base al numero di occorrenze decrescente
    (vale a dire che i colori che compaiono di piu' devono venire prima).
    A parita' di occorrenze l'ordine e' quello indotto, nell'ordine, dalla componente R, 
    poi dalla G poi dalla B del colore. 
    
    Ad esempio per la foto f3a.png  la funzione 
    restituira' la lista [(0, 0, 0), (255, 0, 0)]
    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

import immagini
def es3(fname):
    # inserisci qui il tuo codice
    pass





######################################################################################


'''    
    Es 4: punti 6
    
    Abbiamo immagini che contengono su sfondo nero cammini di color bianco 
    che non si intrecciano ne' si toccano e sono formati da segmenti orizzontali 
    o verticali consecutivi.
    Si veda ad Esempio l'immagine f4a.png.
    Progettare la  funzione es4(fname) che prende in input  
    l'indirizzo di un file .PNG siffatto e restituisce un intero.
    L'intero restituito e' la lunghezza massima tra quelle dei cammini bianchi
    presenti nell'immagine
    Ad esempio es4('f4a.png'):
    deve restituire 60
    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''
import immagini    
def es4(fname):
    # inserisci qui il tuo codice
    pass




############################################################################


'''
    Es 5: punti 8

    Si definisca la funzione es5(r) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice r di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py 
    cancella dall'albero le foglie aggiungendo all'attributo id dei nodi padri 
    la somma dei valori degli attributi id  dei nodi figli cancellati.
    La funzione termina restituendo la somma dei valori cancellati 

    Ad esempio  l'albero a sinistra con l'invocazione di es5 diventa l'albero a destra 
    il valore restituito dalla funzione e' 10
     la funzione es5

                    10                                  10               
             _______|______                      _______|______         
            |              |                    |              |        
            3              7                    6             14        
         ___|___        ___|__                    
        |       |      |      |                
        1       2      3      4                  
                                                                                       
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione                                                             
    '''
import albero

def es5(r):
    # inserisci qui il tuo codice
    pass


###########################################################################

'''
    Es 6: punti 8


    Si definisca la funzione es6(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente triple. Le triple sono del tipo (S,a,b) dove:
      - S e' il nome di una delle sottocartelle raggiungibili visitando 
        l'albero delle cartelle radicato nella cartella pathDir. 
      - a e'  il  numero totale di file  presenti nella cartella S.
      - b e' il numero totale di  sottocartelle  presenti nella cartella S. 
      Le tuple nella lista devono risultare ordinate in modo crescente rispetto 
      alla somma del loro secondo e terzo elemento, e a parita' di somma  
      in ordine lessicografico crescente rispetto all primo elemento della tupla.
      NOTA: File e cartelle il cui nome comincia  col carattere '.' non vanno considerati.
            
    Esempio: con es6('Informatica/Software') viene restituita la lista:
    [('BasiDati', 0, 0), ('SistemiOperativi', 5, 0), ('Software', 7, 2)]
    
    Ai fini dello svolgimento dell'esercizio possono risultare utili 
    le seguenti funzioni nel modulo os:
    os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename()
    NOTA Usate il separatore "/" per costruire i path (valido sia in Windows che in Linux)

    NOTA: È VIETATO USARE LA FUNZIONE DI LIBRERIA os.walk
    NOTA: definite le vostre sottofunzioni ricorsive a livello esterno altrimenti non passate 
          il test di ricorsione                                                             
      
'''

import os

def es6(pathDir):
    # inserisci qui il tuo codice
    pass





######################################################################################################

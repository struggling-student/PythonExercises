
import copy

def es38(labirinto):
    ''' 
    Un labirinto e' rappresentato tramite una griglia.
    Le posizioni delle celle del labirinto sono determinate dalle coppie  (x,y) 
    dove y e' la riga ed x la colonna in cui si trova la cella.
    La cella in alto a sinistra ha coordinate (0,0).
    Le celle della griglia contengono l'intero 0 (libera) o l'intero 1 (ostacolo).
    E possibile spostarsi tra due celle adiacenti con soli due tipi di mosse:
    - dall'altro verso il basso  (vale a dire da una generica cella  (x,y) alla cella  (x,y+1) )
    - da sinistra verso destra   (vale a dire da una generica cella  (x,y) alla cella  (x+1,y) )
    Ci si puo' spostare in una cella solo se questa contiene l'intero 0 (e' vuota)
    Una cella (x,y) e' raggiungibile se esiste una sequenza di mosse che partendo 
    dalla cella (0,0) permette di raggiungerla.
    Si implementi la funzione es38(labirinto) che, dato un labirinto rappresentato come 
    lista di liste, restituisca le coordinate (x, y) della cella raggiungibile 
    situata piu' in basso e a parita' quella piu' a destra.
    Ad esempio per il labirinto di dimensioni 7x7:
    0001000
    1000010
    0001010
    1010010
    0011010
    1001011
    0110100
    la funzione deve restituire la tupla (4, 5).
    Nota bene: La lista di liste non deve essere modificata dalla funzione.  
    '''
    # inserisci qui il tuo codice











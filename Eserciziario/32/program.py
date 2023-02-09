import json


def es32(fname1):
    ''' 
    Si implementi la funzione es32(fname1) prende in input l'indirizzo 
    di un file json e restituisce una lista di interi.
    Il file json contiene una lista di stringhe e ogni stringa e' composta 
    da cifre decimali.
    La lista restituita ha lo stesso numero di elementi della lista originaria 
    ma ciascuna stringa risulta sostituita dalla tupla di due interi A,B. 
    Al primo posto della tupla c'e' l'intero A che si ottimene sommando le cifre 
    dispari della stringa, al secondo posto l'intero B che si ottiene sommando 
    le cifre pari della lista.
    Ad esempio:
    la lista restituita da es32(fname1) con fname1 contenente la lista ['11','24','134','1','2876']
    sara' [(2,0), (0,6), (4,4), (1,0), (7,16)]'''
    # inserisci qui il tuo codice

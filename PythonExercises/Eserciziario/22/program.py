import immagini
import json


def es22(filePng, fileJson):
    '''
    Abbiamo un file contenente un'immagine PNG che bisogna leggere, codificare e infine salvare 
    in un file JSON.
    L'immagine va codificata in una matrice (lista di liste) M di stringhe 
    di dimensioni w per h dove w e' l'ampiezza  dell'immagine  mentre h e' la sua altezza. 
    La cella M[i][j] deve contenere una stringa 
    di 9 caratteri ottenuti concatenando nell'ordine le componenti R, G e B del colore del pixel 
    corrispondente nell'immagine (dopo aver espresso ciascuno dei tre interi come stringa di 
    tre caratteri). Ad esempio  il colore (0,0,0) sara' codificato come '000000000' e 
    il colore (50,10,200) come '050010200'.
    Bisogna infine determinare la stringa di 9 caratteri che e' presente nella matrice 
    con maggior frequenza (a parita' di frequenza quella che precede lessicograficamente le altre).


    Scrivete la funzione es22(filePng, fileJson) che riceve come argomenti:
        :param filePng:  il path del file PNG che dovete codificare
        :param fileJson: il path del file json dove salvare la codifica ottenuta
        :return: la stringa lessicograficamente piu' piccola tra quelle che compaiono 
        nella matrice con piu' frequenza.
    '''
    pass

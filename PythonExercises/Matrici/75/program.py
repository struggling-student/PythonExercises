import immagini


def es75(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut):
    """
    Definite la funzione es75 che riceve come argomenti
        h:                  altezza della immagine
        w:                  larghezza della immagine
        listaColori:        una lista di N colori nel formato (R, G, B) che devono essere applicati, nell'ordine da sinistra a destra, ai rettangoli
        listaAltezze:       una lista di N altezze < h
        larghezzaPalazzo:   la larghezza di ciascuno dei rettangoli da disegnare
        filePngOut:         path del file PNG in cui salvare l'immagine
        :return             numero di pixel cambiati piu' di 1 volta
    e che crea una immagine di dimensioni w,h con sfondo blu (0,0,255).
    Sulla immagine devono essere disegnati N rettangoli equispaziati tutti di larghezza larghezzaPalazzo, appoggiati in basso.
    L'altezza ed il colore del rettangolo i-esimo (da sinistra a destra) e' data dallo i-esimo elemento delle liste listaAltezze e listaColori.
    I rettangoli devono essere disegnati in modo che i rettangoli piu' bassi restino in primo piano rispetto ai rettangoli piu' alti.
    La funzione deve inoltre ritornare il numero di pixel che appartengono a piu' di un rettangolo
    (ovvero quelli di rettangoli che sono stati coperti da almeno un altro rettangolo)

    Nota:   assumete che la larghezza w della immagine sia sempre un multiplo di (1+N),
            in modo che il centro della posizione x di ciascun palazzo sia un valore intero
    Nota:   assumete che larghezzaPalazzo sia un valore pari
    Nota:   assumete che tutte le altezze siano minori o uguali dell'altezza h della immagine
    """
    #inserisci qui il tuo codice
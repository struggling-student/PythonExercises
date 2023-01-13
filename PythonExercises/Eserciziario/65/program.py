

import immagini

def es65(k,lista1,fout):
    '''
    Un quadrato sul piano e' individuato dalla sestupla  di interi (x,y,l,r,g,b) dove
    (x,y) e' la coordinata del  vertice in alto a sinistra del quadrato,  l e' la lunghezza del lato
    e gli ultimi tre valori danno il suo colore (r,g,b).
    La funzione es65(k,lista1,fout) salva in formato PNG all'indirizzo fout un'immagine quadrata
    di lato $k$ ottenuta come segue:
    Su di uno sfondo di colore nero (0,0,0) di dimensione k per k  vengono disegnati in
    sequenza i quadrati in lista1 che ricadono in tutto o in parte nella finestra k per k.
    Il colore dei quadrati non deve necessariamente essere quello originale ma viene determinato
    in base a questa regola: il colore del quadrato e' quello originale se nessuno dei pixel su cui incide il quadrato
    ha un colore maggiore, in caso contrario il colore del quadrato sara' dato dal colore
    massimo tra quello dei pixel su cui incide.
    Un colore(x,y,z) e' maggiore di un altro (x',y',z') se x>x' o a parita' y>y' o a parita' z>z'.
    Infine la funzione deve restituire il numero di pixel di  colore nero che compaiono nell’immagine
    dopo aver inserito i quadrati.
    Ad esempio se
    lista1=[(20,50,20,0,255,0),(30,60,20,255,0,0),(60,50,20,255,0,0),(70,60,20,0,255,0)]
    con es65(100,lista1,'prova1.png') si otterra' la figura nel file prova1.png
    e verra' restituito il valore 8600.
    '''
    # inserite qui il vostro codice
    


import immagini
def es49(fimm1,fimm2,fimm3):
    '''
    Si definisca la  funzione es49(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini e crea la terza immagine da salvare all'indirizzo fimm3. 
      La terza immagine si ottiene dalle prime due. Ha ampiezza  minima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza minima tra le altezze di fimm1 e fimm2.
      il pixel [i][j] dell'immagine ha lo stesso colore del pixel corrispondente
      dell'immagine fimm1 se i e j sono entrambi numeri pari o entrambi numeri dispari, 
      ha il colore del pixel corrispondente in  fimm2 altrimenti
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel presenti nell'immagine creata per i quali  la somma delle 
      tre coordinate del colore e' un numero dispari.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    # inserisci qui il tuo codice
    img1 = immagini.load(fimm1)
    img2 = immagini.load(fimm2)
    w1, h1 = len(img1[0]), len(img1)
    w2, h2 = len(img2[0]), len(img2)
    # calcolo le dimensioni della nuova immagine
    w3 = min(w1,w2)
    h3 = min(h1,h2)
    # creo la nuova immagine
    img3 = [[(0, 0, 0) for _ in range(w3)] for _ in range(h3)]
    count = 0
    # lavoro sulla nuova immagine
    for r in range(h3):
      for c in range(w3):
        img3[r][c] = img2[r][c]
        if r % 2 == c % 2:
          img3[r][c] = img1[r][c]
        a, b, c = img3[r][c]
        if (a+b+c) % 2 == 1:
          count+=1
    immagini.save(img3, fimm3)
    return count
import immagini
def es15(fimm1,fimm2,fimm3):
    '''    
    Es 3: 6 punti
    Si definisca la  funzione es3(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
      La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
      Per quanto riguarda i colori dei pixel della nuova immagine:
      il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
      le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore 
      del pixel dell'unica immagine originaria in cui e' presente.
      (guardate le immagini di test per chiarimenti)
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    img1 = immagini.load(fimm1)
    img2 = immagini.load(fimm2)
    height = max(len(img1), len(img2))
    width = max(len(img1[0]), len(img2[0]))
    counter = 0
    result = []
    for h in range(0, height):
      row = []
      for w in range(0, width):
        if(is_inside(h, w, img1) and is_inside(h, w, img2)):
          row.append((0,0,0))
          counter += 1
        elif(not is_inside(h, w, img1) and not is_inside(h, w, img2)):
          row.append((0,0,0))
          counter += 1
        elif(is_inside(h, w, img1) and not is_inside(h, w, img2)):
          row.append(img1[h][w])
          if(img1[h][w] == (0,0,0)):
            counter += 1
        elif(is_inside(h, w, img2) and not is_inside(h, w, img1)):
          row.append(img2[h][w])
          if(img2[h][w] == (0,0,0)):
            counter += 1
      result.append(row)
    immagini.save(result, fimm3)
    return counter
    

def is_inside(x, y, l):
    if(x<len(l) and y<len(l[0])):
        return True
    return False
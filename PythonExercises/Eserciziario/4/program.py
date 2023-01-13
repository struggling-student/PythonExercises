import immagini


def es4(fimm, fimm1, h1, w1):
    '''    
    Si definisca la  funzione es4(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
    - legge l'immagine da fimm e crea una seconda  immagine. L'immagine da creare 
      ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
      sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h e ampiezza w aventi 
      tutti il colore del pixel originario.
    - salva l'immagine creata all'indirizzo fimm.
    - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
    caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    #scrivi qui il tuo codice
    imgNew = []
    imgImport = immagini.load(fimm)
    altezza = len(imgImport)
    larghezza = len(imgImport[0])
    colori = {}
    # ho creato la nuova immagine
    for _ in range(altezza*h1):
      riga=[]
      for _ in range(larghezza*w1):
        riga.append(0)
      imgNew.append(riga)
    # lavoro sulla immagine vecchia
    for x in range(altezza):
      for y in range(larghezza):
          colorePixel = imgImport[x][y]
          imgNew = disegnaRettangolo(imgNew, x*h1, y*w1, h1, w1, colorePixel)         
          if colorePixel in colori:
            colori[colorePixel]+=1
          else:
            colori[colorePixel]=1
    immagini.save(imgNew, fimm1)
    maxColore = max(colori.values())
    listaColori = (list(filter(lambda x: colori[x] == maxColore, colori)))
    return listaColori[0]
def disegnaRettangolo(img, x, y, h, w, c):
    for i in range(x,x+h):
      for j in range(y,y+w):
        img[i][j]=c
    return img  
print(es4('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Immagini/4/cubo.png','test8_1.png',2,2))
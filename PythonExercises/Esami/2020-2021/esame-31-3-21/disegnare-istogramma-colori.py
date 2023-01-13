'''
Data una immagine in formato PNG vogliamo calcolare e disegnare l'istogramma 
dei colori presenti nella immagine.
Progettate e implementate la funzione ex2(input_file, output_file) 
che riceve come argomenti:
    - input_file:   il filename dell'immagine PNG da leggere (usate la libreria images allegata)
    - output_file:  il filename dell'immagine in cui dovete salvare l'istogramma prodotto
ed inoltre torna come risultato:
    - il numero di colori diversi dell'immagine in input.

L'immagine dell'istogramma da produrre deve avere queste caratteristiche:
    - lo sfondo è nero (0,0,0)
    - le barre sono:
        - orizzontali
        - allineate a sinistra lasciando uno spazio di 2 pixel dal bordo sinistro
        - separate dal bordo superiore, dalla barra precedente e dal bordo inferiore di 2 pixel
        - alte 3 pixel
        - lunghe quanto il numero di pixel contati di quel colore
        - dello stesso colore individuato nel file originale
    - l'ordine dei colori deve essere per conteggio decrescente 
        e in caso di conteggio identico, per tupla di colore decrescente
'''

import images

def ex2(input_file, output_file):
    def draw_bin(img, x,y,w,h,c):
        for X in range(x, x+w):
            for Y in range(y, y+h):
                img[Y][X] = c
    black = (0,0,0)
    img = images.load(input_file)
    conteggio = {}
    for line in img:
        for color in line:
            if color in conteggio:
                conteggio[color] += 1
            else:
                conteggio[color]  = 1
    maxW = max(conteggio.values(), default=0)
    maxH = len(conteggio)
    print(maxW, maxH)
    istogramma = [ [ black ] * (maxW + 4) for _ in range(maxH*5 + 2) ]
    for i,(color, count) in enumerate(sorted(conteggio.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))):
        draw_bin(istogramma, 2, i*5+2, count, 3, color)
    print( *(line[:5] for line in istogramma[:5]), sep='\n')
    images.save(istogramma, output_file)
    return maxH

print(ex2('3cime.png', '3cime-hist.png'))



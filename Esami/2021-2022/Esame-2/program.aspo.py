#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################

# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Esercizio 1: x punti

"""

def ex1():
    # INSERISCI QUI IL TUO CODICE
    pass
# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Esercizio 2: x punti

"""

def ex2():
    # INSERISCI QUI IL TUO CODICE
    pass


# %% ----------------------------------- EX.3 ----------------------------------- #
'''
Esercizio 3: 10 punti (3+3+3+1)

Abbiamo delle immagini che vogliamo combinare tra loro mediante
una serie di operazioni. La sequenza di operazioni è rappresentata
mediante un albero binario che ha come valori delle stringhe. In
particolare
- le foglie dell'albero contengono stringhe che puntano al percorso delle
  immagini su disco;
- i nodi interni sono stringhe che indicano le operazioni da svolgere sui
  propri sottoalberi.

I nodi interni possono rappresentare operazioni binare o unarie, a seconda
del numero di figli. Le operazioni sono:
- 'catLR': due immagini left e right si concatenano orizzontalmente
   sistemando left alla sinistra di right.
- 'catRL': due immagini left e right si concatenano orizzontalmente
   sistemando right alla sinistra di left.
NB: è garantito che le immagini da unire hanno sempre la stessa altezza.
- 'flip_v': un'immagine viene rovesciata (flip) rispetto all'asse
   verticale. Ossia ᴐ diventa c.

In caso di nodo con operazioni binaria, l'operazione indicata
nell'attributo value si applica al risultato delle operazioni dei
sottoalberi sinistro e destro. In caso di nodo unario, l'operazione
indicata si applica al solo sottoalbero presente.

Si progetti una funzione ex3 ricorsiva o che fa uso di funzioni
ricorsive che:
- prende in ingresso un oggetto root di classe BinTree che
  punta al nodo radice di un albero binario che modella operazioni
  su immagini, come descritto sopra;
- carica le immagini alle foglie;
- esegue le operazioni descritte dai nodi interni sui sottoalberi
  fino a costruire l'immagine rappresentata dalla radice;
- salva l'immagine ottenuta alla radice in un file indicato dal percorso
  'saved_image'
- restituisce una tupla contenente altezza e larghezza dell'immagine
  costruita e salvata.

Nota: Dato un nodo, si accede al figlio sinistro e destro con gli
attributi left e right. Per chiarimenti, fare riferimento al file 
tree.py. L'attributo value di ogni nodo contiene sempre una stringa.

Ad esempio:
1)           catRL
            /   \
           o     i
costruisce l'immagine  i|o, visibile aprendo expected_img_01.png

2)             catLR
              /     \
            catRL    o
           /    \
        catRL  flip_v
        /   \       \
       a     i       ᴐ

costruisce l'immagine  c|i|a|o, visibile aprendo expected_img_03.png
'''
import images

def cat(L, R):
    # TODO: we can complicate things and NOT assume cat
    # has always two images. in case one is none, we
    # return the other. Passing this for now.
    assert not(L is None or R is None), 'Una immagine e\' None'
    return [left+right for left, right in zip(L, R)]


def flip_v(im):
    return [row[::-1] for row in im]


def compose(node):
    if not node.left and not node.right:
        return images.load(node.value)
    else:
        op = node.value
        left_im = right_im = None
        if node.left:
            left_im = compose(node.left)
        if node.right:
            right_im = compose(node.right)
        if op == 'catLR':
            return cat(left_im, right_im)
        elif op == 'catRL':
            return cat(right_im, left_im)
        elif op == 'flip_v':
            return flip_v(right_im if right_im else left_im)
        else:
            raise BaseException('Case not covered')


def ex3(root, saved_image):
    im = compose(root)
    # check the error if heigh/width ok but not image
    # images.save([[(255,255,255)]*512 for _ in range(256)], saved_image)
    images.save(im, saved_image)
    return len(im), len(im[0])

# %% ----------------------------------- EX.4 ----------------------------------- #
'''
Esercizio 4: x punti

'''
def ex4():
    # INSERISCI QUI IL TUO CODICE
    pass

###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

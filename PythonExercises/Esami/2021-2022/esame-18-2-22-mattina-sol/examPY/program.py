#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "Iacopo"
cognome     = "Masi"
matricola   = "69"*10

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per debuggare facilmente le funzioni ricorsive potete disattivare il controllo
# di ricorsione settando DEBUG=True nel file grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################

# %% ----------------------------------- EX.1 ----------------------------------- #

def l2(x1, y1, x2, y2):
    '''squared L2 distance'''
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def dist(g1, g2):
    '''
    distanza quadratica euclidea fra due gruppi

    g1 = [(x,y), (x,y).....(x,y)] length is K
    g2 = [(x,y), (x,y).....(x,y)] length is K (bari)
    torna distanza massima (aka raggio)
    '''
    return max(map(lambda p, q: l2(*p, *q), g1, g2))


def mean_xy(sub_points, K):
    '''
    ho in input [(x,y), (x,y).....(x,y)]
    sommo tutte le X e e tutte le Y
    guardando la lista come una matrice tramite unpack
    e args variabili (I miss numpy!)
    sum -> X X X X X X  = Xₛ
    sum -> Y Y Y Y Y Y  = Yₛ
    bari =  (Xₛ/K,Yₛ/K)
    '''
    return tuple(map(lambda *args: sum(args)/K, *sub_points))


def approx(T):
    return tuple(map(lambda x: round(x, 3), T))


def ex1(points, K):
    # we go from [0, 7] = 11 - 4 + 1 to include last
    end = len(points) - K + 1
    bari = [mean_xy(points[i:i+K], K) for i in range(0, end)]
    # allineo baricentro al gruppoᵢ ripetendo bariᵢ × K 
    radii = [(i, dist(points[i:i+K], [bari[i]]*K)) for i in range(0, end)]
    # each radii has its idx and the value, we search min radius value
    idx, min_radius = min(radii, key=lambda elem: elem[1])
    # now i have idx minimum and its associated radii
    return approx(bari[idx]), round(min_radius, 3)

# %% ----------------------------------- EX.2 ----------------------------------- #

import images

class Ellipse:
    ''' model ellipse'''
    def __init__(self, x1, y1, x2, y2, D, r, g, b):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.D = D
        self.col = (r, g, b)


class Point:
    ''' model a point'''
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __sub__(self, q):
        return self.x - q.x, self.y - q.y

    def __lt__(self, el):
        if isinstance(el, Ellipse):
            return self.dist(el.p1) + self.dist(el.p2) < el.D
        raise TypeError(f'lt not supported with {type(el)}')
    
    def dist(self, q, expo=2):
        return sum(map(lambda d: d**expo, self - q))**(1/expo)


# slow as hell but ok
def ex2(list_ellisses, png_filename, width, height):
    im, count = [], 0
    # per tutti i punti del lattice
    for y in range(height):
        row = []
        for x in range(width):
            # comparo il punto (x,y) ∀ ellips Σ
            pix, two, q = (0,)*3, 0, Point(x, y)
            for elparam in list_ellisses:
                el = Ellipse(*elparam)
                if q < el:
                    two += 1
                    pix = el.col
            count += (two > 1) # count more than two
            row.append(pix)
        im.append(row)
    images.save(im, png_filename)
    return count

# %% ----------------------------------- EX.3 ----------------------------------- #



from tree import BinaryTree as BinaryNode


def parse_tree(lines):
    # need to check StopIteration?
    # leggo linea distruttivamente
    try:
        v, is_left, is_right = next(lines)
    except StopIteration:
        return None
    # alloco nodo corrente
    node = BinaryNode(int(v), left=None, right=None)
    # vado a sx se necessrio altrimento left is None
    if is_left == '1':
        node.left = parse_tree(lines)
    # vado a dx se necessario senno right is None
    if is_right == '1':
        node.right = parse_tree(lines)
    return node


def ex3(file_txt):
    with open(file_txt) as fr:
        lines = (line.split(' ') for line in fr.read().split('\n')[:-1])
    return parse_tree(lines)

# %% ----------------------------------- EX.4 ----------------------------------- #



import os


def get_words(file_path):
    with open(file_path, mode='rt', encoding='utf8') as fr:
        chars = fr.read().lower() # mega string with all chars
    S_word = ''
    for c in chars:
        S_word += c if c.isalpha() else ' '
    return S_word.split()


def freq(words, parole):
    F = dict.fromkeys(parole, 0) # crea dizio parola : 0
    # per ogni word nel doc, se e' nel dizio incremento
    for w in words:
        if w in F:
            F[w] += 1
    # se non nel dizio avra frequenza 0
    return (F,) + mean_var(F)


def mean_var(F):
    N, vals = len(F.values()), F.values()
    assert N > 0, 'div by zero'
    means = [sum(vals)/N, ]*N
    return means[0], sum(map(lambda v, m: (v-m)**2, vals, means))/N


def get_max_var(L):
    '''L is list with each item dict, mean, var'''
    freq, mu, sigma = max(L, key=lambda T: T[2])
    return freq, round(sigma, 3)


def ex4(dirpath, parole, start=True):
    out = []
    for item in os.listdir(dirpath):
        full_path = dirpath + '/' + item
        # if it's a text file do the variance computation
        if os.path.isfile(full_path) and full_path.endswith('.txt'):
            # si calcola varianza dizio
            out.append(freq(get_words(full_path), parole))
        elif os.path.isdir(full_path): # se e' dir, recurse
            out.extend(ex4(full_path, parole, start=False))
        else: # if file different than txt do nothing
            pass
    # se sono nel chiamante principale calcolo il massimo senno propago in su
    return out if not start else get_max_var(out)

###################################################################################

if  __name__ == '__main__':
    pass
    # inserisci qui i tuoi test

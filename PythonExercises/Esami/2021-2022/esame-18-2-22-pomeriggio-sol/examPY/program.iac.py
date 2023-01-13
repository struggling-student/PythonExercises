#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "iac"
cognome     = "masi"
matricola   = "12"*100

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################

# %% ----------------------------------- EX.1 ----------------------------------- #

def mean(dati, K):
    return sum(dati)/K

def var(dati, K, mu):
    '''dati is 1xK, μ is 1x1
       allineo μ a 1xK ripetendolo
       cosi poi ho (1xK - 1xK)²
       ∑ₖ(1xK - 1xK)² —> 1x1  e divio per K
    '''
    return sum((map(lambda v, mu: (v-mu)**2, dati, [mu, ]*K)))/K

def ex1(S, K):
    end = len(S) - K + 1
    # from strings to nums
    nums = [sum(ord(c) for c in s) for s in S]
    # sum the nums grouped by consecutive K and divide by K
    # keep track of which mean with the index i
    means = [(i, mean(nums[i:i+K], K)) for i in range(end)]
    # idem varianza with fried potatoes
    varss = [var(nums[i:i+K], K, means[i][1]) for i in range(end)]
    # the two vectors are aligned so just select argmax of mean and
    # then select var[argmax]
    idx, max_mean = max(means, key=lambda T: T[1])
    return round(max_mean, 3), round(varss[idx], 3)


# %%----------------------------------- EX.2 ----------------------------------- #


import images


def parse_cross(im, y, x):
    ''' ugly code coming up'''
    # ----- down
    #   x
    #   x
    # x x x x
    #   x
    black = 0, 0, 0
    start = y, x
    col = im[y][x]
    col_start = col
    while col != black:
        im[y][x] = black
        y += 1
        if im[y][x-1] == col != black:
            assert im[y][x-1] == im[y][x+1], "NON CROCE!"
            center = y, x
        col = im[y][x]
    end = y - 1, x
    # ----- end down
    # left
    y, x = center
    col = im[y][x-1]
    while col != black:
        im[y][x] = black
        x -= 1
        col = im[y][x]
    left = y, x + 1
    # right
    y, x = center
    col = im[y][x+1]
    while col != black:
        im[y][x] = black
        x += 1
        col = im[y][x]
    right = y, x-1
    return start, end, left, right, col_start


def ex2(path_to_im):
    im = images.load(path_to_im)
    black = (0,)*3
    rez = {}
    for y, row in enumerate(im):
        for x, pix in enumerate(row):
            if pix != black:
                *param, col = parse_cross(im, y, x)
                rez[col] = rez.get(col, set()) | {tuple(param)}
    return rez


# ----------------------------------- EX.3 ----------------------------------- #

def game(S, level=0):
    N, leaf, out = len(S) - 2, True, set()
    for i in range(0, N):
        subS = S[i:i+3]  # i, i+1, i+2
        if set(subS) | {'0', '1'} == {'0', '1'}:
            leaf = False
            new_bit = str(int(subS, base=2))
            new_S = S[:i]+new_bit+S[i+3:]
            out |= game(new_S, level+1)
    if leaf: out.add(int(S))
    return out


def ex3(S):
    # Prova di tutti i possibili casi di errore
    # L = list(game(S)) # ricorsione ma non corretto poi si rende lista vuota 0/3
    # return [] # senza ricorsione 0/3
    # return list(game(S)) # corretto ma non odinato 2/3
    return sorted(game(S), key=lambda i: (len(str(i)), -i)) # corretto 3/3

# ----------------------------------- EX.4 ----------------------------------- #
def check_node(node, k, depth):
    '''torno un insieme con depth se multiplo senno vuoto'''
    return {depth} if not node.value % k else set()


def ex4(node, k, depth=0):
    '''
    se non sono in foglia, prendo insieme di profondità
    da sinistra poi destra, poi corrente e concateno.
    propago sopra il set finchè non arrivo a radice (depth=0)
    in quel caso devo controllare se la lista e' vuota
    foglie sono gestite con if node.sottoalbero else set()
    se entra nei 2 else siamo in una foglia
    '''   
    depth_left = ex4(node.left, k, depth+1) if node.left else set()
    depth_right = ex4(node.right, k, depth+1) if node.right else set()
    union = check_node(node, k, depth) | depth_left | depth_right
    return union if depth != 0 else max(union) if union else -1


###################################################################################

if  __name__ == '__main__':
    pass
    # inserisci qui i tuoi test

#! /usr/bin/env python3 -B

from testlib import check, runtests, check_text_file, check_img_file, check_json_file
import isrecursive

import program

#################################################################################
################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST ######
################### E' VIETATO USARLE NELLA SOLUZIONE                      ######
################### THESE FUNCTIONS BELOW ARE USED IN TESTS                ######
################### IT'S FORBIDDEN TO USE THEM IN YOUR PROGRAM             ######
#################################################################################


def test_nome_cognome_matricola():
    assert program.nome        != 'NOME',      "ATTENZIONE, NON HAI INSERITO IL TUO NOME NEL FILE program.py !!!"
    assert program.cognome     != 'COGNOME',   "ATTENZIONE, NON HAI INSERITO IL TUO COGNOME NEL FILE program.py !!!"
    assert program.matricola   != 'MATRICOLA', "ATTENZIONE, NON HAI INSERITO LA TUA MATRICOLA NEL FILE program.py !!!"
    return 0


# ---------------------------EX1------------------------------------ #
def test_es1a_1():
    '''\nPrimo test della funzione es1 sul stringhe'''
    linea = 'pluto   pippo ### paperPIPPOpippoPiPPopipp'
    ris = program.es1(linea, 'pippo')
    check(type(ris), int, None, "la funzione deve restituire un intero")
    check(ris, 1,  None, "numero non corretto")
    return 2


def test_es1a_2():
    '''\nSecondo test della funzione es1 sul stringhe'''
    linea = 'pluto   pippo ### paperPIPPOpippoPiPPopipppippopipp'
    ris = program.es1(linea, 'PIPPO')
    check(type(ris), int, None, "la funzione deve restituire un intero")
    check(ris, 3,  None, "numero non corretto")
    return 3


def test_es1a_3():
    '''\nTerzo test della funzione es1 sul stringhe'''
    linea = 'cacacacacacacacacac'
    ris = program.es1(linea, 'CAC')
    check(type(ris), int, None, "la funzione deve restituire un intero")
    check(ris, 9,  None, "numero non corretto")
    return 2

# ---------------------------EX2------------------------------------ #


def test_es2a_1():
    '''\nPrimo test della funzione es2 sul matrice board1'''
    board = [['x', 'x', 'x', 'o'],
             [' ', ' ', ' ', ' '],
             [' ', ' ', ' ', 'o'],
             [' ', ' ', ' ', 'o']]
    ris = program.es2(board)
    check(type(ris), tuple, None, "la funzione deve restituire una lista")
    check(ris, (False, []), None, "la lista restituita non e' corretta")
    return 2


def test_es2a_2():
    '''\nSecondo test della funzione es2 sul matrice board2'''
    board2 = [['x', 'x', 'x', '+'],
              [' ', ' ', '+', 'o'],
              [' ', '+', ' ', ' '],
              ['+', ' ', 'o ', 'o']]
    ris = program.es2(board2)
    check(type(ris), tuple, None, "la funzione deve restituire una lista")
    check(ris, (True, ['+']*4), None, "la lista restituita non e' corretta")
    return 2


def test_es2a_3():
    '''\nTerzo test della funzione es2 sul matrice board3'''
    board3 = [['o', ' ', ' ', '+', 'x'],
              ['o', ' ', '+', ' ', 'x'],
              ['o', '+', ' ', ' ', 'x'],
              ['+', ' ', 'o', 'o', 'x'],
              ['*', '*', '*', '*', '*']]
    ris = program.es2(board3)
    check(type(ris), tuple, None, "la funzione deve restituire una lista")
    check(ris, (True, ['*']*5), None, "la lista restituita non e' corretta")
    return 4


# ---------------------------EX3------------------------------------ #
def test_es3a(N, expected):
    try:
        isrecursive.decorate_module(program)
        program.es3(N)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris = program.es3(N)
    check(type(ris), list, None, "bisogna restituire una lista")
    check(ris, expected, None, "la lista restituita non è corretta")
    return 3


def test_es3a_1():
    '''\nPrimo test della funzione es3 con N=4
    '''
    N = 4
    gt = [('0000', 0), ('0001', 1), ('0010', 2), ('0011', 3), ('0100', 4), ('0101', 5), \
          ('0110', 6), ('0111', 7), ('1000', 8), ('1001', 9), ('1010', 10), ('1011', 11), \
          ('1100', 12), ('1101', 13), ('1110', 14), ('1111', 15)]
    return test_es3a(N, gt)


def test_es3a_2():
    '''\nPrimo test della funzione es3 con N=2
    '''
    N = 2
    gt = [('00', 0), ('01', 1), ('10', 2), ('11', 3)]
    return test_es3a(N, gt) - 1


def test_es3a_3():
    '''\nPrimo test della funzione es3 con N=6
    '''
    N = 6
    gt = [('000000', 0), ('000001', 1), ('000010', 2), ('000011', 3), ('000100', 4), ('000101', 5),\
          ('000110', 6), ('000111', 7), ('001000', 8), ('001001', 9), ('001010', 10), ('001011', 11),\
          ('001100', 12), ('001101', 13), ('001110', 14), ('001111', 15), ('010000', 16), ('010001', 17),\
          ('010010', 18), ('010011', 19), ('010100', 20), ('010101', 21), ('010110', 22), ('010111', 23),\
          ('011000', 24), ('011001', 25), ('011010', 26), ('011011', 27), ('011100', 28), ('011101', 29),\
          ('011110', 30), ('011111', 31), ('100000', 32), ('100001', 33), ('100010', 34), ('100011', 35),\
          ('100100', 36), ('100101', 37), ('100110', 38), ('100111', 39), ('101000', 40), ('101001', 41),\
          ('101010', 42), ('101011', 43), ('101100', 44), ('101101', 45), ('101110', 46), ('101111', 47),\
          ('110000', 48), ('110001', 49), ('110010', 50), ('110011', 51), ('110100', 52), ('110101', 53),\
          ('110110', 54), ('110111', 55), ('111000', 56), ('111001', 57), ('111010', 58), ('111011', 59),\
          ('111100', 60), ('111101', 61), ('111110', 62), ('111111', 63)]
    return test_es3a(N, gt)

# ---------------------------EX4------------------------------------ #


def test_es4a(dirname, expected, is_rec=True):
    if is_rec:
        try:
            isrecursive.decorate_module(program)
            program.es4(dirname)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

    # we have to check if they are using os.walk
    ris = program.es4(dirname)
    check(type(ris), dict, None, " bisogna restituire un dizionario")
    check(ris, expected, None, "il dizionario restituito non e' corretto")
    return 3


def test_es4a_1():
    '''\nPrimo test ex4 su dir_a'''
    dirname = 'dir_a'
    gt = {'dir_a/aaa': 'trojan', 'dir_a/bbb': 'maleware',
          'dir_a/aaa/bbb': 'trojanhorse'}
    return test_es4a(dirname, gt)


def test_es4a_2():
    '''\nSecond test ex4 su dir_b'''
    dirname = 'dir_b'
    gt = {'dir_b/VIPSTVZL4E': 'maleware', 'dir_b/VIPSTVZL4E/0N': 'virus',
          'dir_b/VIPSTVZL4E/0N/O': 'jacktheripper'}
    return test_es4a(dirname, gt)


def test_es4a_3():
    '''\nTerzo test ex4 su dir_c'''
    dirname = 'dir_c'
    gt = {}
    return test_es4a(dirname, gt, is_rec=False)

# TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
# PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
tests = [
    test_es1a_1, test_es1a_2, test_es1a_3, # cerca su stringa 
    test_es2a_1, test_es2a_2, test_es2a_3, # trova pattern in board
    test_es3a_1, test_es3a_2, test_es3a_3, # enumerazione binaria ricorsiva
    test_es4a_1, test_es4a_2, test_es4a_3,  # ricerca in directory
    test_nome_cognome_matricola,
    ]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################


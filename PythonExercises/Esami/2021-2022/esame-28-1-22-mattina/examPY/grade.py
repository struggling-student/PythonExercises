# -*- coding: utf-8 -*-
import testlib
import isrecursive
#from bintree import BinTree
import os

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    exit(0)
import program
class IncorrectReturn(Exception):
    pass

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


def error_message(res, expected, msg=None):
    bold = '\033[1m'
    bolde = '\033[0m'

    msg_std = f"{bold}Return value incorrect | Valore NON corretto! [NOT OK]{bolde}\n YOUR ANSWER | TUO RISULTATO = {res} \n    EXPECTED | ATTESO        = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print(bold+'*'*50+bolde)
    print(msg)
    print(bold+'*'*50+bolde)




def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################

# ----------------------------------- EX.1 ----------------------------------- #
def do_ex1_tests(D, D_rm, to_remove, expected, score=2, total=2):
    res = program.ex1(D, to_remove)
    if res == expected:
        score = 1
    else:
        error_message(res, expected, "> LEGGIMI: Il dizionario tornato non e' corretto.\n")
        score = 0

    if D == D_rm:
        score += 1
    else:
        error_message(D, D_rm, "> LEGGIMI: Il dizionario di ritorno e' corretto, ma gli interi nelle liste dentro D non sono stati tolti in maniera distruttiva\n\n")
    return score

def test_ex1_1():
    r'''
    Dizionario inverso con ripetizioni CASO 1
    '''
    D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
    D_rm = {2: [6]}
    to_remove = [4, 3, 2, 5]
    expected = {6: [2], 4: [2, 1, 1, 1], 2: [1], 3: [2, 1], 5: [2]}
    return do_ex1_tests(D, D_rm, to_remove, expected)

def test_ex1_2():
    r'''
    Dizionario inverso con ripetizioni CASO 2
    '''
    D = {0: [2, 2, 3, 3],
         10: [0],
         5: [5],
         6: [5, 1, 4, 5, 0, 3, 1, 3, 2, 3],
         9: [0],
         3: [4],
         2: [4, 3, 2, 4, 5]}

    D_rm = {0: [2, 2], 6: [1, 1, 2], 2: [2]}
    to_remove = [4, 3, 0, 5]
    expected = {4: [6, 2, 2, 3], 2: [6, 2, 0, 0], 0: [10, 6, 9], 1: [6, 6], 3: [6, 6, 6, 2, 0, 0], 5: [6, 6, 2, 5]}
    return do_ex1_tests(D, D_rm, to_remove, expected)

def test_ex1_3():
    r'''
    Dizionario inverso con ripetizioni CASO 3
    '''

    D = {0: [1],
         1: [2, 0, 0, 0, 0, 1, 2, 0, 1, 2, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
         3: [2, 1, 2, 2, 1, 0, 1, 0, 1],
         7: [0, 1, 2, 1, 0, 1, 2, 1, 1, 0, 2, 2, 2, 2, 0, 2, 0],
         6: [0, 0, 2, 1, 2, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0],
         4: [1, 1, 0, 2, 0, 1, 1, 0, 0, 2, 1, 1, 1, 2],
         2: [1, 2],
         5: [0, 1, 2]}
    D_rm = {}
    expected = {2: [6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 2, 1, 1, 1, 3, 3, 3, 5, 7, 7, 7, 7, 7, 7, 7], 0: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 5, 7, 7, 7, 7, 7], 1: [6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4, 4, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 5, 7, 7, 7, 7, 7]}
    to_remove = [2, 1, 0]
    return do_ex1_tests(D, D_rm, to_remove, expected)

# ----------------------------------- EX.2 ----------------------------------- #

def do_ex2_tests(grid, path, expected):
    res = program.ex2(grid, path)
    if res == expected:
        return 2
    else:
        if type(res) != list:
            error_message(res, expected, "> README: a list is expected, not a {}\n".format(type(res)))
        error_message(res, expected)
        raise IncorrectReturn
        return 0


def test_ex2_1():
    r'''
    Input grid:[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 0, 1, 2]]
    Input path: 'RRUSRR'
    '''
    grid =  [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
    path =  'RRUSRR'
    expected = [2,3,1,1,2,9]
    return do_ex2_tests(grid, path, expected)


def test_ex2_2():
    r'''
    Input grid:[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 0, 1, 2]]
    Input path: 'DDXUU'
    '''
    grid = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
    path =  'DDXUU'
    expected = [5,9]
    return do_ex2_tests(grid, path, expected)


def test_ex2_3():
    r'''
    Input grid: [[ 2,  1, 7,  1,  0],
                 [ 3, -1, 2,  6,  6],
                 [ 5,  1, 3,  2,  9],
                 [ 9,  0, 4,  1, -2],
                 [-2,  9, 1, -2,  5]]
    Input path: 'RRUSRR'
    '''
    grid = [[2, 1, 7, 1, 0],
                 [3, -1, 2, 6, 6],
                 [5, 1, 3, 2, 9],
                 [9, 0, 4, 1, -2],
                 [-2, 9, 1, -2, 5]]
    path =  'SDDDDDRDDDDDRDDDDDRDDDDDRDDDDDR'
    expected = [2, 3, 5, 9, -2, 2, 1, -1, 1, 0, 9, 1, 7, 2, 3, 4, 1, 7, 1, 6, 2, 1, -2, 1, 0, 6, 9, -2, 5, 0, 2]
    return do_ex2_tests(grid, path, expected)


def test_ex2_4():
    r'''
    Input grid:[[ 7,  0,  4,  2, -3, -3,  6, -5,  6, -2],
                [ 1, 10,  7, -1,  1, -2,  2,  9,  2, -5],
                [-1,  2,  4,  9,  4, -1,  8,  4,  8, -5],
                [ 2,  0,  9, -5, -5,  5,  7,  5,  5,  7],
                [ 0,  0, -4, -5,  2,  4,  5, -4,  1, -2],
                [-5, 10,  7,  0,  6, -3, -4,  1, -2, -5],
                [ 1,  2,  3, -1,  5,  1, -3,  5, -5, -2],
                [ 8, -4, -2,  1,  7, 10,  5, -5,  5, 10],
                [-3,  9,  1,  0,  9,  4,  8,  8,  2,  3],
                [ 2,  2, -4,  1, -1,  3, -1, -3,  2,  4]]
    Input path: 'RRDDDDLUSRLLUURRRRUSRRRUSRDLLLLLUR'
    '''
    grid = [[7, 0, 4, 2, -3, -3, 6, -5, 6, -2],
 [1, 10, 7, -1, 1, -2, 2, 9, 2, -5],
 [-1, 2, 4, 9, 4, -1, 8, 4, 8, -5],
 [2, 0, 9, -5, -5, 5, 7, 5, 5, 7],
 [0, 0, -4, -5, 2, 4, 5, -4, 1, -2],
 [-5, 10, 7, 0, 6, -3, -4, 1, -2, -5],
 [1, 2, 3, -1, 5, 1, -3, 5, -5, -2],
 [8, -4, -2, 1, 7, 10, 5, -5, 5, 10],
 [-3, 9, 1, 0, 9, 4, 8, 8, 2, 3],
 [2, 2, -4, 1, -1, 3, -1, -3, 2, 4]]
    path =  'RRDDDDLUSRLLUURRRRUSRRRUSRDLLLLLUR'
    expected = [0, 4, 7, 4, 9, -4, 0, 0, 0, 9, 0, 2, -1, 1, 10, 7, -1, 1, -3, -3, -3, 6, -5, -3, -3, 2, 6, -5, 6, -3, -3, 2, 1, -1]
    return do_ex2_tests(grid, path, expected)


## ----------------------------------- EX.3 ----------------------------------- #

import tree

def do_ex3_tests(root, depth, expected):
    res = program.ex3(root, depth)
    try:
        isrecursive.decorate_module(program)
        program.ex3(root, depth)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    res = program.ex3(root, depth)
    if res == expected:
        return 3
    else:
        if type(res) != int:
            error_message(res, expected, "> README: an int is expected, not a {}\n".format(type(res)))
        error_message(res, expected)
        return 0


def test_ex3_1():
    r'''
    Input tree:
            ______5______
           |             |
           8__        ___2___
              |      |       |
              3      9       1

    depth = 2
    '''
    root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None], [1, None, None]]])
    depth = 2
    expected = 36
    return do_ex3_tests(root, depth, expected)

def test_ex3_2():
    r'''
    Input tree:
                   ______2______
                  |             |
               __ 7__        ___5___
              |      |      |       |
             _4_     3_    _0_     _5_
            |   |      |  |   |   |   |
            2   -1     1  8   3   2   9

    depth = 3
    '''
    root = tree.BinaryTree.fromList( [2,[7, [4, [2, None, None],[-1, None, None]],[3, None, [1, None, None]]],[5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    depth = 3
    expected = 144
    return do_ex3_tests(root, depth, expected)

def test_ex3_3():
    r'''
                    ___________ 7 __________
                   |                        |
              _____-1____              _____9_____
             |           |            |           |
           __4__       __3__        __0__       __5__
          |     |     |     |      |     |     |     |
          8     2     3     7      1     2     8    -3
         _|_   _|_   _|_   _|_    _|_   _|_   _|_   _|_
        |   | |   | |   | |   |  |   | |   | |   | |   |
        1   1 -1 -1 1  -1 -1  1  1   1 -1 -1 1  -1 -1  1


    depth = 4
    '''
    root = tree.BinaryTree.fromList([7,
                                          [-1,
                                           [4,
                                            [8,
                                             [1, None, None],
                                             [1, None, None]],
                                            [2, [-1, None, None],
                                             [-1, None, None]]],
                                           [3,
                                            [3,
                                             [1, None, None],
                                             [-1, None, None]],
                                            [7,
                                             [-1, None, None],
                                             [1, None, None]]]],
                                          [9,
                                           [0,
                                            [1,
                                             [1, None, None],
                                             [1, None, None]],
                                            [2,
                                             [-1, None, None],
                                             [-1, None, None]]],
                                           [5,
                                            [8,
                                             [1, None, None],
                                             [-1, None, None]],
                                            [-3,
                                             [-1, None, None],
                                             [1, None, None]]]]])
    depth = 4
    expected = 0
    return do_ex3_tests(root, depth, expected)



# ----------------------------------- EX.4 ----------------------------------- #
import shutil
def do_ex4_tests(dirin, dirout, depth, expected, rmdir):
    shutil.rmtree(dirout)
    os.mkdir(dirout)
    try:
        isrecursive.decorate_module(program)
        program.ex4(dirin, dirout, depth)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    shutil.rmtree(dirout)
    os.mkdir(dirout)

    res = program.ex4(dirin, dirout, depth)
    v, to_check = expected
    if v == res:
        for f in to_check:
            if os.path.isfile(dirout+'/'+f):
                testlib.check_text_file(dirout+'/'+f, 'exp/'+f)
                os.remove(dirout+'/'+f)
            else:
                print("> the output file {} is missing\n".format(dirout+'/'+f))
                return 0
        for d in rmdir:
            try:
                os.rmdir(d)
            except OSError as e:
                #print(e.args)
                if e.args[0] in [39, 41]:
                    error_message(d, 'Error: unexpected file in directory!! | Errore: la directory contiene dei file inattesi!')
                    program.ex4(dirin, dirout, depth) ## Rilancio per ripristinare i file eliminati
                    return 0
        program.ex4(dirin, dirout, depth) ## Rilancio per ripristinare i file eliminati
        return 3
    else:
        if type(res) != int:
            error_message(res, expected, "> README: an int is expected, not a {}\n".format(type(res)))
        error_message(res, expected)
        return 0


def test_ex4_1():
    r'''
    Input dirin: 'A/B' dirout: 'test'
    Input depth: 2
    '''
    dirin = 'A/B'
    dirout = 'test'
    depth = 2
    expected = (217, ['D/F/f4.txt'])
    rmdir = ['test/D/F', 'test/D', 'test/E/K', 'test/E']
    return do_ex4_tests(dirin, dirout, depth, expected, rmdir)


def test_ex4_2():
    r'''
    Input dirin: 'A' dirout: 'test'
    Input depth: 2
    '''
    dirin = 'A'
    dirout = 'test'
    depth = 2
    expected = (1730, ['B/E/x10.txt','B/D/x11.txt','B/E/x12.txt','B/D/xx10.txt'])
    rmdir = ['test/B/D', 'test/B/E', 'test/B', 'test/C/Q', 'test/C']
    return do_ex4_tests(dirin, dirout, depth, expected, rmdir)


def test_ex4_3():
    r'''
    Input dirin: 'A' dirout: 'test'
    Input depth: 3
    '''
    dirin = 'A'
    dirout = 'test'
    depth = 3
    expected = (9622, ['C/Q/O/f2f4.exp.txt','B/D/F/f4.txt','C/Q/Z/Lorem.txt','C/Q/O/outf3f4.txt'])
    rmdir = ['test/B/D/F', 'test/B/D', 'test/B/E/K', 'test/B/E', 'test/B', 'test/C/Q/Z', 'test/C/Q/O', 'test/C/Q', 'test/C']
    return do_ex4_tests(dirin, dirout, depth, expected, rmdir)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1,  test_ex1_2,  test_ex1_3,
    test_ex2_1,  test_ex2_2,  test_ex2_3, test_ex2_4,
    test_ex3_1,  test_ex3_2,  test_ex3_3,
    test_ex4_1,  test_ex4_2, test_ex4_3,
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################




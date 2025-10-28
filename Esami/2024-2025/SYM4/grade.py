# -*- coding: utf-8 -*-
import inspect
import types

import testlib
import isrecursive
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = False


#############################################################################

def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*' * 50)
    print(msg)


def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 1e-9


###############################################################################
# %% ----------------------------------- FUNC1 ------------------------- #


def do_test_func1(ID, l, expected):
    if not DEBUG and ID < 4:
        try:
            isrecursive.decorate_module(program)
            res = program.func1(l[:])
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res == None:
                raise testlib.NotImplemented()
            raise Exception(
                "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.func1(l)
    testlib.checkDict(res, expected)
    return 2


def test_func1_1():
    ID = 1
    l = [1, 2, 3, 2, 4, 1, 5, 3, 2]
    expected = {1: 2, 2: 3, 3: 2, 4: 1, 5: 1}
    return do_test_func1(ID, l, expected)


def test_func1_2():
    ID = 4
    l = []
    expected = {}
    return do_test_func1(ID, l, expected)


def test_func1_3():
    ID = 3
    l = [1, "a", 1, "b", "a", 2, "b", 2]
    expected = {1: 2, 'a': 2, 'b': 2, 2: 2}
    return do_test_func1(ID, l, expected)


# %% ----------------------------------- FUNC2 ------------------------- #
def do_test_func2(directory, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.func2(directory)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res == None:
                raise testlib.NotImplemented()
            raise Exception(
                "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.func2(directory)
    testlib.checkDict(res, expected)
    return 3


def test_func2_1():
    '''
    directory = 'func2/A'
    '''
    directory = 'func2/A'
    expected = {'func2/A/B': {'b.txt'}, 'func2/A/C': {'c.txt'}}
    return do_test_func2(directory, expected)


def test_func2_2():
    '''
    directory = 'func2/B'
    '''
    directory = 'func2/B'
    expected = {'func2/B/B': {'b.txt'}, 'func2/B/C': {'c.txt', 'b.txt'}}
    return do_test_func2(directory, expected)


def test_func2_3():
    '''
    directory = 'func2'
    '''
    directory = 'func2'
    expected = {'func2/B/B': {'b.txt'}, 'func2/B/C': {'c.txt', 'b.txt'},
                'func2/A/B': {'b.txt'}, 'func2/A/C': {'c.txt'},
                'func2': {'a.txt'}}
    return do_test_func2(directory, expected)


# ----------------------------------- FUNC 3 ----------------------------------#

def do_func3_tests(a, b, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.func3(a, b)
            if res == None:
                raise testlib.NotImplemented()
            elif b == 0:  # caso base
                pass
            else:
                raise Exception(
                    "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        except isrecursive.RecursionDetectedError:
            pass
        finally:
            isrecursive.undecorate_module(program)

    # print('about to actually call')
    res = program.func3(a, b)
    if res != expected:
        testlib.check(type(res), type(expected), None,
                      f"Tipo di ritorno errato! Restituito={type(res)}, atteso={type(expected)}")
        testlib.check(res, expected, None,
                      f"Risultato errato! Restituito={res}, atteso={expected}")
    return 1


def test_func3_1():
    r'''
    a = 48
    b = 18
    '''
    a = 48
    b = 18
    expected = 6  # 6 è il massimo comune divisore di 48 e 18
    return do_func3_tests(a, b, expected)


def test_func3_2():
    r'''
    a = 56
    b = 0
    '''
    a = 56
    b = 0
    expected = 56  # Quando b è 0, il GCD è a
    return do_func3_tests(a, b, expected)


def test_func3_3():
    r'''
    a = 0
    b = 34
    '''
    a = 0
    b = 34
    expected = 34  # Quando a è 0, il GCD è b
    return do_func3_tests(a, b, expected)


def test_func3_4():
    r'''
    a = 17
    b = 13
    '''
    a = 17
    b = 13
    expected = 1  # 17 e 13 sono primi tra loro
    return do_func3_tests(a, b, expected)


def test_func3_5():
    r'''
    a = 100
    b = 100
    '''
    a = 100
    b = 100
    expected = 100  # Quando a e b sono uguali, il GCD è il numero stesso
    return do_func3_tests(a, b, expected)


# --------------------------------- FUNC 4 ----------------------------------- #
import tree


def do_func4_tests(root, k, expected):
    res = program.func4(root, k)
    try:
        isrecursive.decorate_module(program)
        program.func4(root, k)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception(
            "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    res = program.func4(root, k)
    if res == expected:
        return 2.5
    else:
        r = 0
        if res[0] == expected[0]:
            r += 1.25
        elif res[1] == expected[1]:
            r += 1.25
        error_message(res, expected)
        return r


def test_func4_1():
    r'''
    Input tree:
            ______5______
           |             |
           8__        ___2___
              |      |       |
              3      9       1

    k = 2
    '''
    root = tree.BinaryTree.fromList(
        [5, [8, None, [3, None, None]], [2, [9, None, None], [1, None, None]]])
    k = 2
    expected = 8, 4
    return do_func4_tests(root, k, expected)


def test_func4_2():
    r'''
    Input tree:
                   ______2______
                  |             |
               __ 7__        ___5___
              |      |      |       |
             _4_     3_    _0_     _5_
            |   |      |  |   |   |   |
            2   -1     1  8   3   2   9

    k = 3
    '''
    root = tree.BinaryTree.fromList([2,
                                     [7, [4, [2, None, None], [-1, None, None]],
                                      [3, None, [1, None, None]]],
                                     [5, [0, [8, None, None], [3, None, None]],
                                      [5, [2, None, None], [9, None, None]]]])
    k = 3
    expected = -22, 6
    return do_func4_tests(root, k, expected)


def test_func4_3():
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


    k = 4
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
    k = 4
    expected = -17, 6
    return do_func4_tests(root, k, expected)


def test_func4_4():
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


    k = 4
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
    k = 4
    expected = -17, 6
    return do_func4_tests(root, k, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3,  # 6
    test_func2_1, test_func2_2, test_func2_3,  # 9
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,  # 4
    test_func3_5,                                            # 1
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,  # 10
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################

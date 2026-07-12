# -*- coding: utf-8 -*-
import json

import testlib
import isrecursive
import os
import sys
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save your code as program.py\n'
          'ATTENZIONE: salvare il codice con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### DEBUG Mode
DEBUG = False
#############################################################################

def test_personal_data_entry(run=True):
    if 'nome' in program.__dict__:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

# ---------------------------------------------------------------------------- #
# FUNC 1: Pokemon (2pt -> 2 test)
# ---------------------------------------------------------------------------- #
def test_func1_1(run=True):
    '''Test base score'''
    p = [{'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}, {'name': 'B', 'atk': 20, 'spd': 5, 'def': 5}]
    expected = ['B', 'A']
    res = program.func1(p)
    testlib.check_list(res, expected)
    return 1.0

def test_func1_2(run=True):
    '''Test parità alfabetica'''
    p = [{'name': 'Z', 'atk': 10, 'spd': 10, 'def': 10}, {'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}]
    expected = ['A', 'Z']
    res = program.func1(p)
    testlib.check_list(res, expected)
    return 1.0

# ---------------------------------------------------------------------------- #
# FUNC 2: Censura (4pt -> 4 test)
# ---------------------------------------------------------------------------- #
def test_func2_1(run=True):
    '''Censura singola parola'''
    res = program.func2("Ciao Mondo", ["mondo"])
    testlib.check_val(res, "Ciao *****")
    return 1.0

def test_func2_2(run=True):
    '''Censura multipla'''
    res = program.func2("Mela e Pera", ["mela", "pera"])
    testlib.check_val(res, "**** e ****")
    return 1.0

def test_func2_3(run=True):
    '''Censura con punteggiatura'''
    res = program.func2("Stop! Stop.", ["stop"])
    testlib.check_val(res, "****! ****.")
    return 1.0

def test_func2_4(run=True):
    '''Nessuna parola bandita presente'''
    res = program.func2("Tutto pulito", ["sporco"])
    testlib.check_val(res, "Tutto pulito")
    return 1.0

# ---------------------------------------------------------------------------- #
# FUNC 3: Moltiplicatore Tipi (2pt -> 4 test)
# ---------------------------------------------------------------------------- #
def test_func3_1(run=True):
    '''Efficacia standard 2.0'''
    chart = {'A': {'B': 2.0}}
    res = program.func3(chart, ['A'], ['B'])
    testlib.check_val(res, 2.0)
    return 0.5

def test_func3_2(run=True):
    '''Moltiplicazione multipla'''
    chart = {'A': {'B': 2.0, 'C': 0.5}}
    res = program.func3(chart, ['A'], ['B', 'C'])
    testlib.check_val(res, 1.0)
    return 0.5

def test_func3_3(run=True):
    '''Tipo non presente in tabella (default 1.0)'''
    chart = {'A': {'B': 2.0}}
    res = program.func3(chart, ['A'], ['X'])
    testlib.check_val(res, 1.0)
    return 0.5

def test_func3_4(run=True):
    '''Attaccante multiplo'''
    chart = {'A': {'C': 2.0}, 'B': {'C': 0.5}}
    res = program.func3(chart, ['A', 'B'], ['C'])
    testlib.check_val(res, 1.0)
    return 0.5

# ---------------------------------------------------------------------------- #
# FUNC 4: Matrice Spirale (4pt -> 4 test)
# ---------------------------------------------------------------------------- #
def test_func4_1(run=True):
    '''Matrice 1x1'''
    res = program.func4([[5]])
    testlib.check_list(res, [5])
    return 1.0

def test_func4_2(run=True):
    '''Matrice 2x2'''
    res = program.func4([[1, 2], [3, 4]])
    testlib.check_list(res, [1, 2, 4, 3])
    return 1.0

def test_func4_3(run=True):
    '''Matrice 3x3'''
    res = program.func4([[1,2,3],[4,5,6],[7,8,9]])
    testlib.check_list(res, [1,2,3,6,9,8,7,4,5])
    return 1.0

def test_func4_4(run=True):
    '''Matrice rettangolare 2x3'''
    res = program.func4([[1,2,3],[4,5,6]])
    testlib.check_list(res, [1,2,3,6,5,4])
    return 1.0

# ---------------------------------------------------------------------------- #
# FUNC 5: Sequenze (8pt -> 4 test)
# ---------------------------------------------------------------------------- #
def helper_func5(id_test):
    with open('func5/tests.json', 'r') as f:
        data = json.load(f)[id_test]
    res = program.func5(data['path'], tuple(data['target']))
    testlib.check_val(tuple(res), tuple(data['expected']),
                      f"func5 test {id_test}: returned: {res} expected: {tuple(data['expected'])}")
    return 2

def test_func5_1(run=True): return helper_func5(0)
def test_func5_2(run=True): return helper_func5(1)
def test_func5_3(run=True): return helper_func5(2)
def test_func5_4(run=True): return helper_func5(3)
def test_func5_5(run=True): return helper_func5(4)
def test_func5_6(run=True): return helper_func5(5)

# ---------------------------------------------------------------------------- #
# EX 1: Sottoinsiemi Somma (6pt -> 3 test)
# ---------------------------------------------------------------------------- #
def test_ex1_1(run=True):
    '''Recursion check + Basic True'''
    if not DEBUG:
        isrecursive.decorate_module(program)
        try: program.ex1([1, 2, 3], 2, 3)
        except isrecursive.RecursionDetectedError: pass
        else: raise Exception("Ricorsione non usata!")
        finally: isrecursive.undecorate_module(program)
    res = program.ex1([1, 2, 3, 4], 2, 5) # [1,4] o [2,3]
    testlib.check_val(res, True)
    return 2.0

def test_ex1_2(run=True):
    '''Case False'''
    res = program.ex1([1, 1, 1], 2, 5)
    testlib.check_val(res, False)
    return 2.0

def test_ex1_3(run=True):
    '''K più grande della lista'''
    res = program.ex1([1, 2], 5, 3)
    testlib.check_val(res, False)
    return 2.0

# ---------------------------------------------------------------------------- #
# EX 2:  (6pt)
# ---------------------------------------------------------------------------- #
def helper_ex2(id_test):
    with open('ex2/tests.json', 'r') as f:
        data = json.load(f)[id_test]

    if not DEBUG:
        isrecursive.decorate_module(program)
        try:
            program.ex2(data['data'], data['chain'])
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata!")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(data['data'], data['chain'])
    testlib.check_val(res, data['expected'], f"ex2 test {id_test}: returned: {res} expected: {data['expected']}")
    return 1


def test_ex2_1(run=True): return helper_ex2(0)


def test_ex2_2(run=True): return helper_ex2(1)


def test_ex2_3(run=True): return helper_ex2(2)


def test_ex2_4(run=True): return helper_ex2(3)


def test_ex2_5(run=True): return helper_ex2(4)


def test_ex2_6(run=True): return helper_ex2(5)

################################################################################

tests = [
    test_func1_1, test_func1_2,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1, test_ex1_2, test_ex1_3,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5, test_ex2_6,
    test_personal_data_entry,
]

if __name__ == '__main__':
    check_expected()
    testlib.runtests(tests, verbose=True, logfile='grade.csv', stack_trace=DEBUG)
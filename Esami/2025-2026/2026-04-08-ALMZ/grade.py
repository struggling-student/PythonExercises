# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import json
import tree
import images
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.vuoto.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

# DEBUG = True # abilita la stack trace e disattiva il controllo ricorsione
DEBUG = False


def test_personal_data_entry(run=None):
    if 'nome' not in program.__dict__ or program.nome == 'NOME' or \
            'cognome' not in program.__dict__ or program.cognome == 'COGNOME' or \
            'matricola' not in program.__dict__ or program.matricola == 'MATRICOLA':
        return -1
    return 1e-9


# --- FUNC 1 (2pt) ---
def test_func1_1(run=None):
    testlib.check_val(program.func1(31), 5, "func1(31)")
    return 1


def test_func1_2(run=None):
    testlib.check_val(program.func1(0), 0, "func1(0)")
    return 1


# --- FUNC 2 (3pt) ---
def test_func2_1(run=None):
    testlib.check_val(program.func2("[color:r]A[/color]", {'r': '#F00'}), "<#F00>A</#F00>",
                                                "func2 tag r")
    return 1

def test_func2_2(run=None):
    testlib.check_val(program.func2("B", {}), "B", "func2 no tags")
    return 1

def test_func2_3(run=None):
    message  = "[color:r]A[/color][color:b]B[/color][color:g]C[/color][color:b]B[/color]"
    colors   = {'r': '#F00', 'g': '#0F0', 'b': '#00F'}
    expected = "<#F00>A</#F00><#00F>B</#00F><#0F0>C</#0F0><#00F>B</#00F>"
    returned = program.func2(message, colors)
    testlib.check_val(returned, expected,
                      f"func2: returned: {returned}, \nexpected: {expected}")
    return 1

# --- FUNC 3 (3pt) ---
def test_func3_1(run=None):
    testlib.check_val(program.func3({'a': 5}, {'a': 3}), True, "func3 match key")
    return 3/2


def test_func3_2(run=None):
    testlib.check_val(program.func3({'a': 5}, {'b': 5}), False, "func3 mismatch key")
    return 3/2


# --- FUNC 4 (4pt) ---
def test_func4_1(run=None):
    res = program.func4({'hp': 10}, [{'stat': 'hp', 'type': 'add', 'val': 5}])
    testlib.check_val(res['hp'], 15.0, "func4 add")
    return 4/3


def test_func4_2(run=None):
    res = program.func4({'mp': 10}, [{'stat': 'mp', 'type': 'mul', 'val': 2}])
    testlib.check_val(res['mp'], 20.0, "func4 mul")
    return 4/3


def test_func4_3(run=None):
    res = program.func4({'at': 10}, [])
    testlib.check_val(res['at'], 10.0, "func4 empty ops")
    return 4/3


# --- FUNC 5 (8pt) ---
def helper_func5(id_test):
    with open('func5/tests.json', 'r') as f:
        data = json.load(f)[id_test]

    in_file = data['path']
    out_file = f'func5/test_output_{id_test}.png'

    # Esecuzione funzione studente
    program.func5(in_file, out_file)

    # Verifica correttezza pixel per pixel caricando l'output salvato
    if not os.path.isfile(out_file):
        raise Exception(f"Il file di output {out_file} non è stato creato")

    testlib.check_img_file(out_file, data['expected'])


    return 8 / 6


def test_func5_0(run=None): return helper_func5(0)


def test_func5_1(run=None): return helper_func5(1)


def test_func5_2(run=None): return helper_func5(2)


def test_func5_3(run=None): return helper_func5(3)


def test_func5_4(run=None): return helper_func5(4)


def test_func5_5(run=None): return helper_func5(5)

# --- EX 1 (6pt) ---
def helper_ex1(id_test):
    json_path = f'ex1/input_{id_test}.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    t = tree.BinaryTree.fromList(data['tree'])
    expected = data['expected']

    if not DEBUG:
        isrecursive.decorate_module(program)
        try: program.ex1(t)
        except isrecursive.RecursionDetectedError: pass
        else: raise Exception("Ricorsione non usata!")
        finally: isrecursive.undecorate_module(program)

    testlib.check_val(program.ex1(t), expected, f"ex1 test {id_test}")
    return 1


def test_ex1_0(run=None): return helper_ex1(0)


def test_ex1_1(run=None): return helper_ex1(1)


def test_ex1_2(run=None): return helper_ex1(2)


def test_ex1_3(run=None): return helper_ex1(3)


def test_ex1_4(run=None): return helper_ex1(4)


def test_ex1_5(run=None): return helper_ex1(5)


# --- EX 2 (6pt) ---
def helper_ex2(id_test):
    with open('ex2/tests.json', 'r') as f:
        data = json.load(f)[id_test]

    if not DEBUG and not id_test in {4, 2}:
        isrecursive.decorate_module(program)
        try:
            program.ex2(data['data'])
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata!")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(data['data'])
    testlib.check_val(res, data['expected'], f"ex2 test {id_test}")
    return 1.0


def test_ex2_0(run=None): return helper_ex2(0)


def test_ex2_1(run=None): return helper_ex2(1)


def test_ex2_2(run=None): return helper_ex2(2)


def test_ex2_3(run=None): return helper_ex2(3)


def test_ex2_4(run=None): return helper_ex2(4)


def test_ex2_5(run=None): return helper_ex2(5)

# Lista completa dei test raggruppati per esercizio
tests = [
    test_func1_1, test_func1_2,
    test_func2_1, test_func2_2, test_func2_3,
    test_func3_1, test_func3_2,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_0, test_func5_1, test_func5_2, test_func5_3, test_func5_4, test_func5_5,
    test_ex1_0, test_ex1_1, test_ex1_2, test_ex1_3, test_ex1_4, test_ex1_5,
    test_ex2_0, test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5,
    test_personal_data_entry,
]

if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}ERRORE: Inserire dati personali in program.py{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(tests, verbose=True, logfile='grade.csv', stack_trace=DEBUG)

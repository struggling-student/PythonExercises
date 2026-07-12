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

def load_tests(func_name):
    with open(os.path.join(func_name, "tests.json"), 'r') as f:
        return json.load(f)
# --- FUNC 1 (2pt) ---
def helper_func1(id_test):
    data = load_tests("func1")[id_test]
    ret = program.func1(data['n'], data['k'])
    testlib.check_val(ret, data['expected'],
                      f"func1 test {id_test}: returned: {ret} expected: {data['expected']}")
    return 1

def test_func1_1(run=None): return helper_func1(0)
def test_func1_2(run=None): return helper_func1(1)

# --- FUNC 2 (2pt) ---
def helper_func2(id_test):
    data = load_tests("func2")[id_test]
    ret = program.func2(data['nums'])
    testlib.check_val(sorted(ret), sorted(data['expected']),
                      f"func2 test {id_test}: returned: {ret} expected: {data['expected']}")
    return 1

def test_func2_1(run=None): return helper_func2(0)
def test_func2_2(run=None): return helper_func2(1)

# --- FUNC 3 (4pt) ---
def helper_func3(id_test):
    data = load_tests("func3")[id_test]
    res = [sorted(g) for g in program.func3(data['strs'])]
    exp = [sorted(g) for g in data['expected']]
    testlib.check_val(sorted(res), sorted(exp),
                      f"func3 test {id_test}: returned: {res} expected: {exp}")
    return 1

def test_func3_1(run=None): return helper_func3(0)
def test_func3_2(run=None): return helper_func3(1)
def test_func3_3(run=None): return helper_func3(2)
def test_func3_4(run=None): return helper_func3(3)

# --- FUNC 4 (4pt) ---
def helper_func4(id_test):
    data = load_tests("func4")[id_test]
    res = program.func4(data['f1'], data['f2'])
    testlib.check_val(res, data['expected'],
                      f"func4 test {id_test}: returned: {res} expected: {data['expected']}")
    return 6/4

def test_func4_1(run=None): return helper_func4(0)
def test_func4_2(run=None): return helper_func4(1)
def test_func4_3(run=None): return helper_func4(2)
def test_func4_4(run=None): return helper_func4(3)

# --- FUNC 5 (6pt) ---
def helper_func5(id_test):
    data = load_tests("func5")[id_test]
    ret = program.func5(data['path'], tuple(data['target']))
    testlib.check_val(ret, tuple(data['expected']),
                      f"func5 test {id_test}: returned: {ret} expected: {tuple(data['expected'])}")
    return 1

def test_func5_1(run=None): return helper_func5(0)
def test_func5_2(run=None): return helper_func5(1)
def test_func5_3(run=None): return helper_func5(2)
def test_func5_4(run=None): return helper_func5(3)
def test_func5_5(run=None): return helper_func5(4)
def test_func5_6(run=None): return helper_func5(5)

# --- EX 1 (6pt) ---
def helper_ex1(id_test):
    data = load_tests("ex1")[id_test]
    if not DEBUG:
        isrecursive.decorate_module(program)
        try: program.ex1(data['arr'].copy(), data['n'], data['s'])
        except isrecursive.RecursionDetectedError: pass
        else: raise Exception("Ricorsione non usata!")
        finally: isrecursive.undecorate_module(program)
    ret = program.ex1(data['arr'], data['n'], data['s'])
    testlib.check_val(not ret, data['expected'],
                      f"ex1 test {id_test}: returned: {ret} expected: {not(data['expected'])}")
    return 1

def test_ex1_1(run=None): return helper_ex1(0)
def test_ex1_2(run=None): return helper_ex1(1)
def test_ex1_3(run=None): return helper_ex1(2)
def test_ex1_4(run=None): return helper_ex1(3)
def test_ex1_5(run=None): return helper_ex1(4)
def test_ex1_6(run=None): return helper_ex1(5)

# --- EX 2 (8pt) ---
def helper_ex2(id_test):
    data = load_tests("ex2")[id_test]
    t = tree.BinaryTree.fromList(data['tree'])
    t2 = tree.BinaryTree.fromList(data['tree'])
    if not DEBUG:
        isrecursive.decorate_module(program)
        try: program.ex2(t)
        except isrecursive.RecursionDetectedError: pass
        else: raise Exception("Ricorsione non usata!")
        finally: isrecursive.undecorate_module(program)
    ret = program.ex2(t2)
    testlib.check_val(ret, data['expected'],
                      f"ex2 test {id_test}: returned: {ret} expected: {data['expected']}")
    return 6/8

def test_ex2_1(run=None): return helper_ex2(0)
def test_ex2_2(run=None): return helper_ex2(1)
def test_ex2_3(run=None): return helper_ex2(2)
def test_ex2_4(run=None): return helper_ex2(3)
def test_ex2_5(run=None): return helper_ex2(4)
def test_ex2_6(run=None): return helper_ex2(5)
def test_ex2_7(run=None): return helper_ex2(6)
def test_ex2_8(run=None): return helper_ex2(7)

tests = [
    test_func1_1, test_func1_2,
    test_func2_1, test_func2_2,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4, test_func5_5, test_func5_6,
    test_ex1_1, test_ex1_2, test_ex1_3, test_ex1_4, test_ex1_5, test_ex1_6,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5, test_ex2_6, test_ex2_7, test_ex2_8,
    test_personal_data_entry,
]

if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')

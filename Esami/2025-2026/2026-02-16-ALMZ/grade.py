# -*- coding: utf-8 -*-
import os
import sys
import json

import testlib
import isrecursive
import tree
from testlib import COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.vuoto.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
# Con DEBUG=True la diagnostica è più ampia
# e il test di ricorsione non viene applicato, facilitando il debug
# DEBUG = True
DEBUG = False
#############################################################################


def test_personal_data_entry(run=None):
    if 'nome' not in program.__dict__ or program.nome == 'NOME' or \
            'cognome' not in program.__dict__ or program.cognome == 'COGNOME' or \
            'matricola' not in program.__dict__ or program.matricola == 'MATRICOLA':
        return -1
    return 1e-9


def load_tests(folder_name: str):
    with open(os.path.join(folder_name, "tests.json"), "r", encoding="utf-8") as f:
        return json.load(f)


# --- FUNC 1 (2pt) ---
def helper_func1(i):
    d = load_tests("func1")[i]
    res = program.func1(d["moves"])
    exp = tuple(d["expected"])
    testlib.check_val(res, exp,
        f"func1 test {i}: returned: {res}, expected: {exp}")
    return 1

def test_func1_1(run=None): return helper_func1(0)
def test_func1_2(run=None): return helper_func1(1)


# --- FUNC 2 (2pt) ---
def helper_func2(i):
    d = load_tests("func2")[i]
    ret = program.func2(d["hand"])
    exp = tuple(d["expected"])
    testlib.check_val(ret, exp,
    f"func2 test {i}: returned: {ret}, expected: {exp}")
    return 1

def test_func2_1(run=None): return helper_func2(0)
def test_func2_2(run=None): return helper_func2(1)


# --- FUNC 3 (6pt) ---
def helper_func3(i):
    d = load_tests("func3")[i]
    ret = program.func3(d["expr"])
    exp = d["expected"]
    testlib.check_val(ret, exp,
        f"func3 test {i}: returned: {ret}, expected: {exp}")
    return 6/4

def test_func3_1(run=None): return helper_func3(0)
def test_func3_2(run=None): return helper_func3(1)
def test_func3_3(run=None): return helper_func3(2)
def test_func3_4(run=None): return helper_func3(3)


# --- FUNC 4 (4pt) ---
def helper_func4(i):
    d = load_tests("func4")[i]
    ret = program.func4(d["path"], d["deck_size"], d["top_n"])
    exp = d["expected"]
    testlib.check_val(ret, exp,
        f"func4 test {i}: returned: {ret}, expected: {exp}")
    return 1

def test_func4_1(run=None): return helper_func4(0)
def test_func4_2(run=None): return helper_func4(1)
def test_func4_3(run=None): return helper_func4(2)
def test_func4_4(run=None): return helper_func4(3)


# --- FUNC 5 (6pt) ---
def helper_func5(i):
    d = load_tests("func5")[i]
    path_tmp = os.path.join("func5", f"out_{i}.png")
    c1 = tuple(d["c1"])
    c2 = tuple(d["c2"])

    counts = program.func5(d["path_in"], path_tmp, c1, c2)
    exp = tuple(d["expected_counts"])
    testlib.check_val(counts, exp,
    f"func5 counts test {i}: returned: {counts}, expected: {exp}")

    testlib.check_img_file(path_tmp, d["path_expected"])
    return 1

def test_func5_1(run=None): return helper_func5(0)
def test_func5_2(run=None): return helper_func5(1)
def test_func5_3(run=None): return helper_func5(2)
def test_func5_4(run=None): return helper_func5(3)
def test_func5_5(run=None): return helper_func5(4)
def test_func5_6(run=None): return helper_func5(5)


# --- EX 1 (6pt) ---
def helper_ex1(i):
    d = load_tests("ex1")[i]
    rolls = d["rolls"]

    if not DEBUG:
        isrecursive.decorate_module(program)
        try:
            program.ex1(rolls.copy(), d["target"])
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata!")
        finally:
            isrecursive.undecorate_module(program)

    ret = program.ex1(rolls, d["target"])
    exp = d["expected"]
    testlib.check_val(ret, exp,
        f"ex1 test {i}: returned: {ret}, expected: {exp}")
    return 1

def test_ex1_1(run=None): return helper_ex1(0)
def test_ex1_2(run=None): return helper_ex1(1)
def test_ex1_3(run=None): return helper_ex1(2)
def test_ex1_4(run=None): return helper_ex1(3)
def test_ex1_5(run=None): return helper_ex1(4)
def test_ex1_6(run=None): return helper_ex1(5)


# --- EX 2 (6pt) ---
def helper_ex2(i):
    d = load_tests("ex2")[i]
    t = tree.BinaryTree.fromList(d["tree"])
    t1 = tree.BinaryTree.fromList(d["tree"])

    if not DEBUG:
        isrecursive.decorate_module(program)
        try:
            program.ex2(t1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata!")
        finally:
            isrecursive.undecorate_module(program)

    ret = program.ex2(t)
    exp = d["expected"]
    testlib.check_val(ret, exp,
        f"ex2 test {i}: returned: {ret}, expected: {exp}")
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


if __name__ == "__main__":

    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()

    check_expected()
    testlib.runtests(tests, verbose=True, logfile="grade.csv", stack_trace=DEBUG)
    testlib.check_exam_constraints()

    print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
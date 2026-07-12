# -*- coding: utf-8 -*-

import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected
import json

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

def test_personal_data_entry(run=True):
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Student info: {program.name} {program.surname} {program.student_id}{COL["RST"]}')
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

def add_docstring(f, local):
    S = ''
    if 'run' in local: del local['run']
    for key, val in local.items():
        S += f'\n{key} = {val}'
    f.__doc__ = S


###############################################################################


# --- FUNC 1 (4pt) ---
def do_test_func1(string, expected):
    ret = program.func1(string)
    testlib.check_val(ret, expected,
                      f"func1('{string}'): expected {expected}, returned: {ret}")
    return 1


def test_func1_1(run=None):
    string = "([()])"
    expected = True
    return do_test_func1(string, expected)
def test_func1_2(run=None):
    string = "{[]()[]()}"
    expected = True
    return do_test_func1(string, expected)
def test_func1_3(run=None):
    string = "([)]"
    expected = False
    return do_test_func1(string, expected)
def test_func1_4(run=None):
    string = "{([)}]"
    expected = False
    return do_test_func1(string, expected)


# --- FUNC 2 (2pt) ---
def test_func2_1(run=None):
    studenti = [{"nome": "A", "media": 29}, {"nome": "B", "media": 27}]
    testlib.check_val(ret:=program.func2(studenti), ["A"],
                      f"func2 media > 28: expected {['A']}, returned: {ret}")
    return 1


def test_func2_2(run=None):
    studenti = [{"nome": "X", "media": 28.1}, {"nome": "Y", "media": 28}]
    testlib.check_val(ret:=program.func2(studenti), ["X"],
                      f"func2 media > 28: expected {['X']}, returned: {ret}")
    return 1


# --- FUNC 3 (4pt) ---
def do_test_func3(ID, expected):
    # This assumes existence of func3/file1_0.txt and file2_0.txt from input_generator
    file1 = f'func3/file1_{ID}.txt'
    file2 = f'func3/file2_{ID}.txt'
    res = program.func3(file1, file2)
    testlib.check_val(isinstance(res, list), True,
                      "func3 non ritorna una lista")
    testlib.check_val(res,expected, f"result: {res} expected: {expected}")
    return 4/3

def test_func3_1(run=None):
    ID = '0'
    expected = ['Riga 4: accfe != diff_accfe']
    return do_test_func3(ID, expected)

def test_func3_2(run=None):
    ID = '1'
    expected = ['Riga 1: cfcdc != diff_cfcdc',
                'Riga 6: ebdcf != diff_ebdcf',
                'Riga 8: dbaaa != diff_dbaaa',
                'Riga 9: aadbd != diff_aadbd']
    return do_test_func3(ID, expected)


def test_func3_3(run=None):
    ID = '2'
    expected = ['Riga 2: eefff != diff_eefff']
    return do_test_func3(ID, expected)


# --- FUNC 4 (2pt) ---
def do_test_func4(N, expected):
    res = program.func4(N)
    testlib.check_val(res, expected,
                      f"result: {res} expected: {expected}")
    return 1
def test_func4_1(run=None):
    N = 2
    expected = [(0, 0), (1, 1)]
    return do_test_func4(N, expected)

def test_func4_2(run=None):
    N = 3
    expected = [(0, 0),         (0, 2),
                        (1, 1),
                (2, 0),         (2, 2)]
    return do_test_func4(N, expected)

# --- FUNC 5 (6pt) ---
def helper_func5(id_test):
    path_in  = f'func5/input_{id_test}.png'
    path_out = f'func5/test_out_{id_test}.png'
    path_exp = f'func5/expected_{id_test}.png'

    with open(f'func5/params_{id_test}.json', 'r') as f:
        params = json.load(f)
    k = params['k']
    expected = params.get('expected',0)
    # Remove old output if exists
    if os.path.exists(path_out):
        os.remove(path_out)
    res = program.func5(path_in, path_out, k)
    if not os.path.exists(path_out):
        raise Exception(f"Il file di output {path_out} non è stato creato")
    testlib.check_img_file(path_out, path_exp)
    testlib.check_val(res, expected, f"returned: {res} expected: {expected}")
    return 6/4


def test_func5_1(run=None): return helper_func5(0)
def test_func5_2(run=None): return helper_func5(1)
def test_func5_3(run=None): return helper_func5(2)
def test_func5_4(run=None): return helper_func5(3)

# --- EX 1 (8pt) ---
def helper_ex1(id_test):
    with open(f'ex1/input_{id_test}.json', 'r') as f:
        data = json.load(f)

    candidates = data['arr']
    target = data['s']
    expected = data['e']

    if not DEBUG:
        isrecursive.decorate_module(program)
        try:
            program.ex1(candidates.copy(), target)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata!")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(candidates, target)
    # Check if result is a list of lists
    testlib.check_val(isinstance(res, list),
                      True, f"ex1 test {id_test} return list")
    for L in res:
        testlib.check_val(isinstance(L, list), True, f"ex1 test {id_test} contains lists")
        testlib.check_val(S:=sum(L), target,
                          f"ex1 test {id_test} torna la combinazione {L} che ha somma {S} invece di {target}")

    ret_sorted = [ sorted(L) for L in res ]
    exp_sorted = [ sorted(L) for L in expected ]
    #print(ret_sorted)
    if len(ret_sorted) != len(exp_sorted):
        raise Exception(f"Hai generato un numero di combinazioni errato")
    uniques = []
    for L in ret_sorted:
        if L not in uniques:
            uniques.append(L)
        else:
            raise Exception(f"La combinazione {L} è duplicata")
    for L in exp_sorted:
        if L not in ret_sorted:
            raise Exception(f"Manca la combinazione {L}")
    for L in ret_sorted:
        if L not in ret_sorted:
            raise Exception(f"La combinazione {L} è di troppo")
    return 8/6

def test_ex1_0(run=None): return helper_ex1('esempio')
def test_ex1_1(run=None): return helper_ex1(0)
def test_ex1_2(run=None): return helper_ex1(1)
def test_ex1_3(run=None): return helper_ex1(2)
def test_ex1_4(run=None): return helper_ex1(3)
def test_ex1_5(run=None): return helper_ex1(4)


# --- EX 2 (6pt) ---
def helper_ex2(id_test):
    with open(f'ex2/tree_{id_test}.json', 'r') as f:
        data = json.load(f)
    t  = tree.BinaryTree.fromList(data['tree'])
    t1 = tree.BinaryTree.fromList(data['tree'])
    e = data['expected']

    if not DEBUG:
        isrecursive.decorate_module(program)
        try:
            program.ex2(t)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata!")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(t1)
    testlib.check_val(isinstance(res, str), True, "ex2 return string")
    testlib.check_val(res, e, f"ex2: returned {res}, expected: {e}")
    return 6/5


def test_ex2_1(run=None): return helper_ex2(0)
def test_ex2_2(run=None): return helper_ex2(1)
def test_ex2_3(run=None): return helper_ex2(2)
def test_ex2_4(run=None): return helper_ex2(3)
def test_ex2_5(run=None): return helper_ex2(4)





tests = [
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2,
    test_func3_1, test_func3_2, test_func3_3,
    test_func4_1, test_func4_2,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1, test_ex1_2, test_ex1_3, test_ex1_4, test_ex1_5, test_ex1_0,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5,
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
################################################################################

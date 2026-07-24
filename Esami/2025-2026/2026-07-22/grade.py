# -*- coding: utf-8 -*-
import isrecursive
import testlib
import tree
import os
import sys
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: You have to rename the program.empty.py!!!\n\
Check your working directory or the correctness of the filename.')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = True
# DEBUG = False
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
        S += f'\n    {key} = {val}'
    f.__doc__ = S


###############################################################################
#%% ---

# --- FUNC 1 (2pt) ---
def do_test_func1(L1, L2, expected, run=True):
    res = program.func1(L1, L2)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_list(res, expected)
    return 0.5

def test_func1_1(run=True):
    L1=[-2,3,4,-5]
    L2=[1,-2,6]
    expected =  [1,-2,4]
    add_docstring(test_func1_1, locals())
    return do_test_func1(L1, L2, expected)  if run else None

def test_func1_2(run=True):
    L1 = [-1,4,5,2,0,15]
    L2 = [4,6,0,-16,3,1,1,5,3]
    expected =  [-1, 4, 0, 2, 0, 1]
    add_docstring(test_func1_2, locals())
    return do_test_func1(L1, L2, expected)  if run else None

def test_func1_3(run=True):
    L1 = [45, -12, 89, 0, -34, 76, -99, 23, -5, 67, 10, -50]
    L2 = [12.53, -45.71, 88.19, -2.34, 0.55, 34.92, -76.28, 99.91, -15.46, 55.57, -8.82, 42.05]
    expected = [12.53, -12, 88.19, 0, 0.55, 34.92, -76.28, 23, -5, 55.57, -8.82, 42.05]
    add_docstring(test_func1_3, locals())
    return do_test_func1(L1, L2, expected) if run else None

def test_func1_4(run=True):
    L1 = [-7, 14.22, 55, -88.91, 3, -11, 74.55, -33.33, 90, -1, 44.44, 60.15]
    L2 = [-95.12, 22, -44.49, 66.61, -11, 77.73, -33.38, 88, -55.52, 99.99, 0, -22.26]
    expected = [-7, 14.22, -44.49, 66.61, 3, -11, -33.38, -33.33, -55.52, -1, 0, -22.26]
    add_docstring(test_func1_4, locals())
    return do_test_func1(L1, L2, expected) if run else None

#%% ---
def do_func2_tests(words, expected):
    res = program.func2(words)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_dict(res, expected)
    return 0.5


def test_func2_1(run=True):
    words= {"yak", "Gollum", "Batman", "AI", "star"}
    expected ={4: {'Batman', 'Gollum'}, 2: {'yak'}, 3: {'star'}, 0: {'AI'}}

    add_docstring(test_func2_1, locals())
    return do_func2_tests(words, expected) if run else None

def test_func2_2(run=True):
    words= {    "Apple", "river", "Mountain", "guitar", "Window", "silver"}
    expected = {4: {'Mountain', 'silver', 'Window'}, 3: {'river', 'Apple', 'guitar'}}
    add_docstring(test_func2_2, locals())
    return do_func2_tests(words, expected) if run else None

def test_func2_3(run=True):
    words= {    "Courage", "journey", "Ocean", "Planet", "Library", 
    "Shadow", "thunder", "whisper", "Crystal", "Velvet"}
    expected ={4: {'Planet', 'Shadow', 'journey', 'Velvet'}, 2: {'Ocean'}, 5: {'Library', 'thunder', 'whisper'}, 6: {'Crystal'}, 3: {'Courage'}}

    add_docstring(test_func2_3, locals())
    return do_func2_tests(words, expected) if run else None

def test_func2_4(run=True):
    words={    "Adventure", "Galaxy", "Horizon", "Lantern", "Mystery", 
    "Nebula", "Oasis", "Puzzle", "Quantum", "Ripple", 
    "Sapphire", "Twilight", "Universe", "Vortex", "Wander"}
    expected ={2: {'Oasis'}, 4: {'Puzzle', 'Wander', 'Ripple', 'Horizon', 'Quantum', 'Universe', 'Vortex', 'Galaxy'}, 5: {'Adventure', 'Lantern', 'Sapphire'}, 6: {'Mystery', 'Twilight'}, 3: {'Nebula'}}

    add_docstring(test_func2_4, locals())
    return do_func2_tests(words, expected) if run else None

#%% ---
def do_func3_tests(ID, expected):
    sales_log_path = f'func3/sales0{ID}.txt'
    report_path = f'func3/report0{ID}.txt'
    exp_path = f'func3/exp0{ID}.txt'
    res = program.func3(sales_log_path, report_path)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    testlib.check_text_file(report_path, exp_path)
    return 1

def test_func3_1(run=True):
    '''
    sales_log_path = 'func3/sales01.txt'
    expected = 17.5
    '''
    file_id = 1
    expected = 17.5
    return do_func3_tests(file_id, expected) if run else None


def test_func3_2(run=True):
    '''
    sales_log_path = 'func3/sales02.txt'
    expected = 587.0
    '''
    file_id = 2
    expected = 587.0
    return do_func3_tests(file_id, expected) if run else None
def test_func3_3(run=True):
    '''
    sales_log_path = 'func3/sales03.txt'
    expected = 18105.0
    '''
    file_id = 3
    expected = 18105.0
    return do_func3_tests(file_id, expected) if run else None

def test_func3_4(run=True):
    '''
    sales_log_path = 'func3/sales04.txt'
    expected = 3508.0
    '''
    file_id = 4
    expected = 3508.0
    return do_func3_tests(file_id, expected) if run else None

#%% --- FUNC 4
def do_func4_tests(ID, expected):
    words_path = f'func4/words0{ID}.txt'
    outfile_path = f'func4/run0{ID}.txt'
    exp_path = f'func4/exp0{ID}.txt'
    res = program.func4(words_path, outfile_path)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    testlib.check_text_file(outfile_path, exp_path)
    return 1

def test_func4_1(run=True):
    '''
    words_path = 'func4/words01.txt'
    expected = 5
    '''
    file_id = 1
    expected = 5
    return do_func4_tests(file_id, expected) if run else None


def test_func4_2(run=True):
    '''
    words_path = 'func4/words02.txt'
    expected = 10
    '''
    file_id = 2
    expected = 10
    return do_func4_tests(file_id, expected) if run else None
def test_func4_3(run=True):
    '''
    words_path = 'func4/words03.txt'
    expected = 20
    '''
    file_id = 3
    expected = 20
    return do_func4_tests(file_id, expected) if run else None

def test_func4_4(run=True):
    '''
    words_path = 'func4/words04.txt'
    expected = 20
    '''
    file_id = 4
    expected = 20
    return do_func4_tests(file_id, expected) if run else None
#%% --- FUNC 5
def do_test_func5(minr, ID, expected):
    input_filename  = f'func5/img_{ID}.png'
    output_filename = f'func5/img_{ID}out{minr}.png'
    expected_filename = f'func5/img_{ID}exp{minr}.png'
    # tolgo output ogni volta
    if os.path.exists(output_filename): os.remove(output_filename)
    res = program.func5(minr, input_filename, output_filename)
    if res is None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    testlib.check_img_file(output_filename, expected_filename)
    return 1

def test_func5_1(run=True):
    file_ID = 1
    minr = 200
    expected = 18
    add_docstring(test_func5_1, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_2(run=True):
    file_ID = 2
    minr = 0
    expected = 30
    add_docstring(test_func5_2, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_3(run=True):
    file_ID = 3
    minr = 1
    expected = 24
    add_docstring(test_func5_3, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_4(run=True):
    file_ID = 4
    minr = 1
    expected = 11
    add_docstring(test_func5_4, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_5(run=True):
    file_ID = 5
    minr = 1
    expected = 14
    add_docstring(test_func5_5, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_6(run=True):
    file_ID = 0
    minr = 0
    expected = 35
    add_docstring(test_func5_6, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_7(run=True):
    file_ID = 3
    minr = -1
    expected = 38   
    add_docstring(test_func5_7, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

def test_func5_8(run=True):
    file_ID = 0
    minr = 100
    expected = 19
    add_docstring(test_func5_8, locals())  
    return do_test_func5(minr, file_ID, expected)  if run else None

#%%%  EX 1
def do_ex1_test(root, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.ex1(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res is None:
                raise testlib.NotImplemented()
            raise Exception("[ERROR] The program does not employ recursion")
        finally:
            isrecursive.undecorate_module(program)
    res = program.ex1(root)
    if res is None:
        raise testlib.NotImplemented()
    testlib.check_val(res, expected)
    return 1.5
    


def test_ex1_1(run=True):
    root = tree.BinaryTree.fromList([20, [10, [0.5, None, None], [0.2, None, None]], [5, None, None]])
    expected = (0.6, 20)
    add_docstring(test_ex1_1, locals())  
    return do_ex1_test(root, expected) if run else None


def test_ex1_2(run=True):
    root = tree.BinaryTree.fromList([4, [25, [-4, None, None], [-1, None, None]], [11, [11, [8, [10, None, None], [24, [-4, None, None], None]], None], [-5, None, None]]])
    expected = (-24, 120)
    add_docstring(test_ex1_2, locals())  
    return do_ex1_test(root, expected) if run else None

def test_ex1_3(run=True):
    root = tree.BinaryTree.fromList([23, [20, None, None], [3, [20, None, None], [-30, None, None]]])
    expected = (-90, 60)
    add_docstring(test_ex1_3, locals())  
    return do_ex1_test(root, expected) if run else None

def test_ex1_4(run=True):
    root = tree.BinaryTree.fromList([27, [22, [-6, [10, None, [16, None, None]], [17, None, None]], [1, [13, [-9, [-3, None, None], None], [-2, None, [24, None, None]]], [5, None, None]]], [23, [22, [21, None, None], None], [10, None, None]]])
    expected = (-45, 144)
    add_docstring(test_ex1_4, locals())  
    return do_ex1_test(root, expected) if run else None

################################################################################

#%% EX2
ex2data = [{'lista':[42, 'a', [7, 'b', [100, 'c']], 9, 'z', ['x', 24]], 'expected': 'abczx'},
           {'lista': [10, 'a', 20, 'b', [30, 'c', 40, ['d', 50]], 'e', 60, [70, 'f']], 'expected': 'abcdef'},
           {'lista': ['x', 'y', 'z', 1, 2, 3, ['alpha', 99, 'beta', [88, 'gamma']], 77, 'delta'], 'expected': 'xyzalphabetagammadelta'},
           {'lista': [500, [400, ['nested_char', 300, ['deep_char', 200]]], 'outer_char', 100], 'expected': 'nested_chardeep_charouter_char'},
           {'lista': ['start', ['level_1', 101, ['level_2', 202, ['level_3', 303, ['level_4', 404, 'end_of_branch']]]], 999, 'omega', ['another_branch', 55, 66, ['nested_deep', 'q']]], 'expected':'startlevel_1level_2level_3level_4end_of_branchomegaanother_branchnested_deepq'},
           {'lista': [1, 2, 3, 'x', 'y', 'z', [10, 20, 'a', 'b', ['hidden_char', 99]], 'm', 'n', 500, [7, 8, 9, ['p', 'q', 'r', [0]]], 'final_char', 777], 'expected': 'xyzabhidden_charmnpqrfinal_char'},
]

def do_ex2_test(lista, expected):
    if not DEBUG:
        isrecursive.decorate_module(program)
        try:
            res = program.ex2(lista)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res is None:
                raise testlib.NotImplemented()
            raise Exception("[ERROR] The program does not employ recursion")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(lista)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    return 1

def test_ex2_1(run=True):
    lista = ex2data[0]['lista']
    expected = ex2data[0]['expected']
    add_docstring(test_ex2_1, locals())  
    return do_ex2_test(lista, expected) if run else None

def test_ex2_2(run=True):
    lista = ex2data[1]['lista']
    expected = ex2data[1]['expected']
    add_docstring(test_ex2_2, locals())  
    return do_ex2_test(lista, expected) if run else None

def test_ex2_3(run=True):
    lista = ex2data[2]['lista']
    expected = ex2data[2]['expected']
    add_docstring(test_ex2_3, locals())  
    return do_ex2_test(lista, expected) if run else None

def test_ex2_4(run=True):
    lista = ex2data[3]['lista']
    expected = ex2data[3]['expected']
    add_docstring(test_ex2_4, locals())  
    return do_ex2_test(lista, expected) if run else None

def test_ex2_5(run=True):
    lista = ex2data[4]['lista']
    expected = ex2data[4]['expected']
    add_docstring(test_ex2_5, locals())  
    return do_ex2_test(lista, expected) if run else None

def test_ex2_6(run=True):
    lista = ex2data[5]['lista']
    expected = ex2data[5]['expected']
    add_docstring(test_ex2_6, locals())  
    return do_ex2_test(lista, expected) if run else None

#%% ---
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4, 
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4, test_func5_5, test_func5_6, test_func5_7, test_func5_8, 
    test_ex1_1, test_ex1_2, test_ex1_3, test_ex1_4,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5, test_ex2_6,
]


if __name__ == '__main__':
    if not test_personal_data_entry():
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    #testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################

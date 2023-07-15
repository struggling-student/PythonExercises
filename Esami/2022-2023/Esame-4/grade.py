# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import glob
import hashlib

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['RED']
        return func(f'{COL["BOLD"]}{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
    return wrapped_func


my_print = my_decorator(print)

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
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = True
# DEBUG = False
# %% ---------------------- TEST SECTION -------------------
#############################################################################

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m',
       'BOLD' : '\033[1m',
       'ENDC' : '\033[0m'}


def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9

###############################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
def do_func1_tests(a_dict, word, a_dict_exp, expected):
    res = program.func1(a_dict, word)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di chiavi rimosse atteso è {expected} e non {res}. / Removed strings should be {expected}, but {res} were returned.\n {'*'*50}''')
        return 0
    testlib.checkDict(a_dict, a_dict_exp)
    return 0.5


def test_func1_1():
    '''
    a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'b'
    '''
    a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'b'
    a_dict_exp = {'c': ['a', 'c']}
    expected = 2
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_2():
    '''
    a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'd'
    '''
    a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'd'
    a_dict_exp = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    expected = 0
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_3():
    '''
    a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'a'
    '''
    a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'a'
    a_dict_exp = {}
    expected = 3
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_4():
    '''
    a_dict = {'capslock'........}
    word = 'hobbledehoys'
    '''
    a_dict = {'capslock': ['electrocuted', 'mistake', 'hobbledehoys', 'superadded'], 'unhindered': ['arts'], 'backlist': ['unordered', 'hobbledehoys', 'hobbledehoys', 'allegorizes', 'mistake', 'hobbledehoys', 'unhindered'], 'arts': ['unhindered', 'superadded'], 'games': ['unhindered', 'games', 'parasol'], 'parasol': ['futons', 'allegorizes', 'prevaricate'], 'philters': ['unordered', 'mistake', 'allegorizes', 'futons'], 'hobbledehoys': ['electrocuted', 'unhindered', 'backlist', 'mdv', 'objectiveness', 'games', 'capslock'], 'mdv': ['disgusting', 'prated', 'hobbledehoys', 'philters', 'allegorizes', 'disgusting'], 'prated': ['capslock', 'hobbledehoys', 'unreleased'], 'futons': ['unhindered', 'objectiveness', 'parasol', 'disgusting', 'electrocuted'], 'electrocuted': ['hobbledehoys', 'objectiveness', 'philters', 'backlist', 'philters', 'parasol'], 'prevaricate': ['superadded', 'hobbledehoys', 'allegorizes', 'mistake', 'mdv', 'capslock'], 'mistake': ['backlist', 'electrocuted'], 'objectiveness': ['mistake', 'superadded', 'hobbledehoys', 'allegorizes'], 'allegorizes': ['allegorizes', 'superadded', 'mistake'], 'disgusting': ['unhindered', 'futons'], 'unordered': ['backlist', 'mistake', 'parasol', 'mistake', 'backlist'], 'unreleased': ['prated', 'unordered', 'mdv'], 'superadded': ['mdv', 'hobbledehoys', 'disgusting']}
    word = 'hobbledehoys'
    a_dict_exp = {'unhindered': ['arts'], 'arts': ['unhindered', 'superadded'], 'games': ['unhindered', 'games', 'parasol'], 'parasol': ['futons', 'allegorizes', 'prevaricate'], 'philters': ['unordered', 'mistake', 'allegorizes', 'futons'], 'hobbledehoys': ['electrocuted', 'unhindered', 'backlist', 'mdv', 'objectiveness', 'games', 'capslock'], 'futons': ['unhindered', 'objectiveness', 'parasol', 'disgusting', 'electrocuted'], 'mistake': ['backlist', 'electrocuted'], 'allegorizes': ['allegorizes', 'superadded', 'mistake'], 'disgusting': ['unhindered', 'futons'], 'unordered': ['backlist', 'mistake', 'parasol', 'mistake', 'backlist'], 'unreleased': ['prated', 'unordered', 'mdv']}
    expected = 8
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

# %% ----------------------------------- FUNC2 ------------------------- #
def do_func2_tests(a_string, expected):
    res = program.func2(a_string)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La stringa restituita non è corretta / The returned string is incorrect\n[ERROR] expected={expected} returned={res}.\n {'*'*50}''')
        return 0
    return 0.5


def test_func2_1():
    '''
    a_string = 'welcome'
    '''
    a_string = 'welcome'
    expected = 'womlec'
    return do_func2_tests(a_string, expected)

def test_func2_2():
    '''
    a_string = 'abracadabra'
    '''
    a_string = 'abracadabra'
    expected = 'rdcba'
    return do_func2_tests(a_string, expected)

def test_func2_3():
    '''
    a_string = ''
    '''
    a_string = ''
    expected = ''
    return do_func2_tests(a_string, expected)

def test_func2_4():
    '''
    a_string = 'capslockunhinderedbacklistartsgamesparasolphiltershobbledehoysmdvpratedfutonselectrocutedprevaricatemistakeobjectivenessallegorizesdisgustingunorderedunreleasedsuperadded'
    '''
    a_string = 'capslockunhinderedbacklistartsgamesparasolphiltershobbledehoysmdvpratedfutonselectrocutedprevaricatemistakeobjectivenessallegorizesdisgustingunorderedunreleasedsuperadded'
    expected = 'zyvutsrponmlkjihgfedcba'
    return do_func2_tests(a_string, expected)

# %% ----------------------------------- FUNC3 ------------------------- #
def do_func3_tests(string_list1, string_list2, expected):
    res = program.func3(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 2/3


def test_func3_1():
    '''
    string_list1=['so', 'sin', 'vas', 'rin', 'vul']
    string_list2=['cane', 'casai', 'to', 'cero', 'sia']
    '''
    string_list1=['so', 'sin', 'vas', 'rin', 'vul']
    string_list2=['cane', 'casai', 'to', 'cero', 'sia']
    expected = ['sosia','vasto','sincero','vulcane','rincasai']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_2():
    '''
    string_list1=['A']
    string_list2=['A']
    '''
    string_list1=['A']
    string_list2=['A']
    expected = ['AA']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_3():
    '''
    string_list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    string_list2=['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    '''
    string_list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    string_list2=['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    expected = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ']
    return do_func3_tests(string_list1, string_list2, expected)

# %% ----------------------------------- FUNC4 ------------------------- #

def do_func4_tests(ID, expected):
    input_file = f'func4/func4_test{ID}.txt'
    output_file= f'func4/func4_out{ID}.txt'
    expected_file=f'func4/func4_exp{ID}.txt'
    res = program.func4(input_file, output_file)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è corretto! / Returned value is incorrect!\n'''
              f'''[ERROR] Expected {expected} returne {res}\n {'*'*50}''')
        return 0
    testlib.check_text_file(output_file, expected_file)
    return 2


def test_func4_1():
    '''
    input_file = func4/func4_test1.txt
    output_file = func4/func4_out1.txt
    '''
    ID = 1
    expected = 6
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_file = func4/func4_test2.txt
    output_file = func4/func4_out2.txt
    '''
    ID = 2
    expected = 15
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_file = func4/func4_test3.txt
    output_file = func4/func4_out3.txt
    '''
    ID = 3
    expected = 20
    return do_func4_tests(ID, expected)

# %% ----------------------------------- FUNC5 ------------------------- #
import images

def do_test_func5(ID, expected):
    img_in  = f'func5/image0{ID}.png'

    res = program.func5(img_in)
    if res != expected:
        testlib.checkList(res, expected)
    return 2


def test_func5_1():
    '''
    imm_in = func5/image01.png
    expected = [121,861]
    '''
    ID = 1
    expected = [121,861]
    return do_test_func5(ID, expected)


def test_func5_2():
    '''
    imm_in = func5/image02.png
    expected = [100, 400, 900, 1600, 2500]
    '''
    ID = 2
    expected = [100, 400, 900, 1600, 2500]
    return do_test_func5(ID, expected)


def test_func5_3():
    '''
    imm_in = func5/image03.png
    expected = [2500]
    '''
    ID = 3
    expected = [2500]
    return do_test_func5(ID, expected)


def test_func5_4():
    '''
    imm_in = func5/image04.png
    expected = []
    '''
    ID = 4
    expected = []
    return do_test_func5(ID, expected)
# %% ----------------------------------- EX1 ------------------------- #
def do_test_ex1(directory, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.ex1(directory)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res == None:
                raise testlib.NotImplemented()
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(directory)
    testlib.checkDict(res, expected)
    return 2

def test_ex1_1():
    '''
    directory = 'ex1/A'
    '''
    directory = 'ex1/A'
    expected = {'ex1/A/B': {'b.txt'}, 'ex1/A/C': {'c.txt'}}
    return do_test_ex1(directory, expected)


def test_ex1_2():
    '''
    directory = 'ex1/B'
    '''
    directory = 'ex1/B'
    expected = {'ex1/B/B': {'b.txt'}, 'ex1/B/C': {'c.txt', 'b.txt'}}
    return do_test_ex1(directory, expected)


def test_ex1_3():
    '''
    directory = 'ex1'
    '''
    directory = 'ex1'
    expected = {'ex1/B/B': {'b.txt'}, 'ex1/B/C': {'c.txt', 'b.txt'}, 'ex1/A/B': {'b.txt'}, 'ex1/A/C': {'c.txt'}, 'ex1': {'a.txt'}}
    return do_test_ex1(directory, expected)

# %% ----------------------------------- EX2 ------------------------- #


def do_ex2_test(root, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = program.ex2(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            if res == None:
                raise testlib.NotImplemented()
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(root)
    if res == None:
        raise testlib.NotImplemented()
    if type(res) != str:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è una stringa! / Returned value is not a string!\n'''
              f'''[ERROR] Expected {expected} returned {res}\n {'*'*50}''')
        return 0
    testlib.checkString(res, expected)
    return 2

from tree import BinaryTree
def test_ex2_1():
    '''
        ______A______
       |             |
       B__        ___C___
          |      |       |
          D      E       F
    '''

    root = BinaryTree.fromList(['A', ['B',None,['D',None,None]], ['C', ['E',None,None], ['F',None,None]]])
    expected = 'DBAFCE'
    return do_ex2_test(root, expected)

def test_ex2_2():
    '''
             ______A______
            |             |
         __ B__        ___C___
        |      |      |       |
       _D_     E_    _F_     _G_
      |   |      |  |   |   |   |
      H   I      J  K   L   M   N
    '''
    root = BinaryTree.fromList(['A', ['B',['D',['H',None,None],['I',None,None]],['E',None,['J',None,None]]], ['C', ['F',['K',None,None],['L',None,None]], ['G',['M',None,None],['N',None,None]]]])
    expected = 'EJBHDIAMGNCKFL'
    return do_ex2_test(root, expected)


def test_ex2_3():
    '''
           ______A______
          |             |
       __ B__        ___C___
      |      |      |       |
     _D      E_    _F       G_
    |          |  |           |
   _H          I  J           K_
  |                             |
  L                             M
    '''
    root = BinaryTree.fromList(['A', ['B',['D',['H',['L',None,None],None],None],
                                      ['E',None,['I',None,None]]],
                  ['C', ['F',['J',None,None],None],['G',None,['K',None,['M',None,None]]]]])
    expected = 'EIBHLDAGMKCJF'
    return do_ex2_test(root, expected)


################################################################################
# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2,  test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


def check_expected():
    files = glob.glob('backup/**', recursive=True)
    # print(*files, sep='\n')
    for file_b in files:
        if os.path.isfile(file_b):
            file_e = '/'.join(file_b.split('/')[1:])
            with open(file_b, mode='rb') as frb, open(file_e, mode='rb') as fre:
                assert hashlib.md5(frb.read()).hexdigest() == hashlib.md5(fre.read()).hexdigest(),\
                    (f"{COL['BOLD']} {COL['RED']}\nWARNING: an expected or input file has been overwritten by mistake!\n"
                     f"expected/input file: {file_e}\ndiffers from:        {file_b}\nWe cannot evaluate your exam,"
                     f"please call the lecturer to fix the issue!{COL['RST']}{COL['ENDC']}")

# %% --------------------- MAIN ---------------------
if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)

    # Check Expected
    # check_expected()

    grades = {}
    total  = 0
    with open('grade.csv') as F:
        for line in F:
            test, points = line.split(',')
            _, name, *_ = test.split('_')
            if name == 'personal': continue
            total += float(points)
            grades[name] = grades.get(name, 0) + float(points)
    #%% Constraint for the exam
    constraint1 = len([name for name,grade in grades.items() if grade>0 and name.startswith('func')]) >= 3
    constraint2 = len([name for name,grade in grades.items() if grade>0 and name.startswith('ex')]) >= 1
    constraint3 = total >= 18
    constraint4 = all((constraint1, constraint2, constraint3))
    if not constraint1:
        print(f'YOU HAVE NOT PASSED AT LEAST 3 FUNC EXERCISES: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint2:
        print(f'YOU HAVE NOT PASSED AT LEAST 1 RECURSIVE EXERCISE: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint3:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
################################################################################

# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected

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

def do_func1_tests(D, expected):
    res = program.func1(D)
    testlib.check_list(res, expected)
    return 0.5                 # peso di ciascun test (4 × 0.5 = 2)

# ---------- test 1 ----------------------------------------------------
def test_func1_1(run=True):
    '''
    D = {2: ['s', 'u', 'e'], 3: ['q', 'a']}
    expected = ['qa', 'se']
    '''
    D = {2: ['s', 'u', 'e'], 3: ['q', 'a']}
    expected = ['su', 'qa']
    return do_func1_tests(D, expected) if run else None

# ---------- test 2 ----------------------------------------------------
def test_func1_2(run=True):
    '''
    D = {1: ['b', 'c'], 4: ['a'], -5:['a', 'b', 'c', 'd', 'e']}
    expected = ['bcde', 'b', 'a']
    '''
    D = {1: ['b', 'c'], 4: ['a'], -5:['a', 'b', 'c', 'd', 'e']}
    expected = ['bcde', 'b', 'a']
    return do_func1_tests(D, expected) if run else None

# ---------- test 3 ----------------------------------------------------
def test_func1_3(run=True):
    '''
    D = {3: ['extra', 'smart'], 2: ['you', "'re", "really"]}
    expected = ["you're", 'extrasmart']
    '''
    D = {3: ['extra', 'smart'], 2: ['you', "'re", "really"]}
    expected = ["you're", 'extrasmart']
    return do_func1_tests(D, expected) if run else None

# ---------- test 4 ----------------------------------------------------
def test_func1_4(run=True):
    '''
    D = {1: ['ext', 'asd', 'ra', 'smar', 't!'], 2: ['you', "'re", "really"], 0: ['really', 'really']}
    expected = ["you're", 'really!', 'extrasmart']
    '''
    D = {1: ['ext', 'asd', 'ra', 'smar', 't!'], 2: ['you', "'re", "really"], 0: ['really', 'really']}
    expected = ["you're", 'really', 'extrasmart!']
    return do_func1_tests(D, expected) if run else None


def do_func2_tests(L, expected):
    res = program.func2(L)
    testlib.check_list(res, expected)
    return 0.5

def test_func2_1(run=True):
    '''
    L = [ [3, []], [2,[3]], [4, [], [3,4], []]]
    expected = [1, 0, 2]
    '''
    L = [ [3, []], [2,[3]], [4, [], [3,4], []]]
    expected = [1, 0, 2]
    return do_func2_tests(L, expected)

def test_func2_2(run=True):
    '''
    L = [ [1, 3, [4], []], [[]], [1, [],[],[]], [[3]]]
    expected = [1, 1, 3]
    '''
    L = [ [1, 3, [4], []], [[]], [1, [],[],[]], [[3]]]
    expected = [1, 1, 3, 0]
    return do_func2_tests(L, expected)

def test_func2_3(run=True):
    '''
    L = [ [], [[]], [[], [], [44], 4]]
    expected = [0, 1, 2]
    '''
    L = [ [], [[]], [[], [], [44], 4]]
    expected = [0, 1, 2]
    return do_func2_tests(L, expected)

def test_func2_4(run=True):
    '''
    L = [ [1, []], [2,[3]], [[],[],[5,6], [1], [2]], [[]], [[],[],[]], [[3]], [[],[],[5]]]
    expected = [1, 0, 2, 1, 3, 0, 2]
    '''
    L = [ [1, []], [2,[3]], [[],[],[5,6], [1], [2]], [[]], [[],[],[]], [[3]], [[],[],[5]]]
    expected = [1, 0, 2, 1, 3, 0, 2]
    return do_func2_tests(L, expected)

# ----------------------------------- FUNC.3 ----------------------------------- #

def do_func3_tests(S, m, M, expected):
    res = program.func3(S, m, M)
    testlib.check_val(res, expected)
    return 0.5

def test_func3_1(run=True):
    '''
    S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
    m = 3
    M = 4
    expected = ['Brad', 'Dana', 'ian', 'UMA', 'Zoe']
    '''
    S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
    m = 3
    M = 4
    expected = ['Brad', 'Dana', 'ian', 'UMA', 'Zoe']
    return do_func3_tests(S, m, M, expected)

def test_func3_2(run=True):
    '''
    S = "apple, Egg, orange, banana, Umbrella, Ice"
    m = 3
    M = 5
    expected = ['apple', 'Egg', 'Ice', 'orange', 'Umbrella']
    '''
    S = "apple, Egg, orange, banana, Umbrella, Ice"
    m = 3
    M = 5
    expected = ['apple', 'Egg', 'Ice']
    return do_func3_tests(S, m, M, expected)

def test_func3_3(run=True):
    '''
    S = "Zoo, car, Dog, tree"
    m = 2
    M = 3
    expected = []
    '''
    S = "Zoo, car, Dog, tree"
    m = 2
    M = 3
    expected = ['car', 'Dog', 'Zoo']
    return do_func3_tests(S, m, M, expected)

def test_func3_4(run=True):
    '''
    S = "Eagle, igloo,   Octopus, Uranus, ant, Bee"
    m = 4
    M = 8
    expected = ['Eagle', 'igloo', 'Octopus', 'Uranus']
    '''
    S = "Eagle, igloo,   Octopus, Uranus, ant, Bee"
    m = 4
    M = 8
    expected = ['Eagle', 'igloo', 'Octopus', 'Uranus']
    return do_func3_tests(S, m, M, expected)



# ----------------------------------- FUNC.4 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename  = f'func4/test{ID}_in.txt'
    output_filename = f'func4/test{ID}_out.txt'
    expected_filename = f'func4/test{ID}_exp.txt'
    res = program.func4(input_filename, output_filename)
    testlib.check_dict(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1(run=True):
    '''
    input_filename = 'func4/test1_in.txt'
    output_filename = 'func4/test1_out.txt'
    expected_filename = 'func4/test1_exp.txt'
    expected = 12
    '''
    ID = 1
    expected = 12
    return do_func4_tests(ID, expected)


def test_func4_2(run=True):
    '''
    input_filename = 'func4/test2_in.txt'
    output_filename = 'func4/test2_out.txt'
    expected_filename = 'func4/test2_exp.txt'
    expected = 70
    '''
    ID = 2
    expected = 70
    return do_func4_tests(ID, expected)


def test_func4_3(run=True):
    '''
    input_filename = 'func4/test3_in.txt'
    output_filename = 'func4/test3_out.txt'
    expected_filename = 'func4/test3_exp.txt'
    expected = 520
    '''
    ID = 3
    expected = 520
    return do_func4_tests(ID, expected)

def test_func4_4(run=True):
    '''
    input_filename = 'func4/test4_in.txt'
    output_filename = 'func4/test4_out.txt'
    expected_filename = 'func4/test4_exp.txt'
    expected = 1700
    '''
    ID = 4
    expected = 1700
    return do_func4_tests(ID, expected)



def do_test_func5(ID, expected):
    img_in = f'func5/test{ID}_in.png'
    img_out = f'func5/test{ID}_out.png'
    img_exp = f'func5/test{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out)
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il numero di gruppi 2x2 è sbagliato! / The number of 2x2 groups is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    testlib.check_img_file(img_out, img_exp)
    return 1.5

def test_func5_1(run=True):
    '''
    imagefile = func5/test1_in.png
    output_imagefile = func5/test1_out.png
    expected_output_imagefile = func5/test1_exp.png
    '''
    ID = 1
    expected = 14
    return do_test_func5(ID, expected)


def test_func5_2(run=True):
    '''
    imagefile = func5/test2_in.png
    output_imagefile = func5/test2_out.png
    expected_output_imagefile = func5/test2_exp.png
    '''
    ID = 2
    expected = 40
    return do_test_func5(ID, expected)


def test_func5_3(run=True):
    '''
    imagefile = func5/test3_in.png
    output_imagefile = func5/test3_out.png
    expected_output_imagefile = func5/test3_exp.png
    '''
    ID = 3
    expected = 5
    return do_test_func5(ID, expected)


def test_func5_4(run=True):
    '''
    imagefile = func5/test4_in.png
    output_imagefile = func5/test4_out.png
    expected_output_imagefile = func5/test4_exp.png
    '''
    ID = 4
    expected = 874
    return do_test_func5(ID, expected)

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(input_tree, n, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(input_tree, n)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Il programma non adotta un approccio ricorsivo / The function does not use recursion")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(input_tree, n)
    testlib.check_list(res, expected)
    return 2


def test_ex1_1(run=True):
    '''
     ______20_____      
    |             |     
    4__        ___1___  
       |      |       |            
       -2     1       4 
    '''
    input_tree = tree.BinaryTree.fromList([20, [4,None,[-2,None,None]], [1, [1,None,None], [4,None,None]]])
    expected = [[20, 1, 1], [20, 4, -2]]
    return do_test_ex1(input_tree, 22, expected)


def test_ex1_2(run=True):
    '''
         ______13______	  
        |              |	  
     ___7___        ___10___  
    |       |      |        | 
   _-5_    -1_    _-9_      -3
  |    |      |  |    |       
  5    4      6  6   -2       
                            
    '''
    input_tree = tree.BinaryTree.fromList([13, [7, [-5, [5, None, None], [4, None, None]], [-1, None, [6, None, None]]],
                                     [10, [-9, [6, None, None], [-2, None, None]], [-3, None, None]]])
    expected = [[13, 7, -5, 5], [13, 10, -9, 6], [13, 10, -3]]
    return do_test_ex1(input_tree, 20, expected)

def test_ex1_3(run=True):
    '''
     A very big treee
    '''
    input_tree = tree.BinaryTree.fromList([4, [-9, [14, [11, [11, [22, [7, None, None], [21, None, None]],
                                    [1, [-2, [21, None, None], None], [-5, [-4, None, None], None]]], None], None],
                                        [-8, [11, [6, [-6, [22, [-10, [25, None, None], [10, [-2, None, None], None]],
                                        [25, None, [9, None, None]]], [10, [24, [-4, None, None], None], 
                                        [20, None, [18, None, None]]]], [20, None, [26, [-2, [3, None, [-7, None, None]],
                                        [2, None, None]], [20, [1, None, None], None]]]], 
                                    [-7, [30, [13, [4, None, None], None], [14, None, None]], [-9, [-4, [22, None, None], None],
                                    [3, [16, None, None], [20, [10, None, None], None]]]]], [6, [18, [26, [-3, [29, None, None],
                                    [7, [29, None, None], [15, [10, None, None], None]]], [8, [-1, [2, None, None], None],
                                    [2, None, [6, None, None]]]], None], [6, [14, [30, [7, None, None], None],
                                    [-6, [30, None, None], None]], [-2, [-5, [-8, None, None], [21, [-1, None, [-3, None, None]],
                                    None]], None]]]]], [24, [3, [-4, [14, [17, [2, None, [-9, None, None]], [-3, None, [24, None,
                                    None]]], [2, [7, None, None], [-9, None, [5, None, None]]]], None], [27, None, [2, [26, [23, [8, [4, None, None], None],
                                    [-1, None, None]], [8, None, [30, None, None]]], None]]], [-10, [-7, [19, [-6, [-1, None, [-3, [-7, None, None], [26, [-8, None, None], None]]],
                                    [13, [21, [26, [14, None, None], None], [15, None, None]], [26, None, None]]], [8, [-7, [0, [13, None, None], None], [1, None, [9, None, None]]],
                                    [26, [0, None, None], None]]], [18, [-10, [25, None, None], [18, None, None]], [-9, [19, [-9, None, None], [26, None, None]], [2, [3, [11, None, None],
                                    [14, [-6, None, None], [1, None, None]]], [18, None, None]]]]], [3, [22, [23, [3, None, [-3, [-5, [5, None, None],
                                    [21, None, [20, None, None]]], [25, [-4, None, None], None]]], [24, [-4, [1, [14, None, None], [14, None, None]], [5, [-6, None, [7, None, None]],
                                    [-1, None, None]]], [16, [-10, None, [13, None, [11, None, None]]], [21, [20, None, None], None]]]], [23, [2, [-10, None, None], [17, None, None]],
                                    [-1, [26, None, None], [28, None, None]]]], [0, None, [29, [-8, [23, None, [4, None, None]], [-7, [5, [-10, None, None], [5, None, None]],
                                    [6, None, [1, None, None]]]], [14, [1, None, None], [4, None, [23, None, None]]]]]]]]])                                                                                                                                  
    expected = [[4, -9, -8, 11, 6, 20, 26, -2, 3, -7],
     [4, 24, -10, -7, 18, -10, 25],
     [4, 24, -10, -7, 19, 8, -7, 0, 13]]
    return do_test_ex1(input_tree, 44, expected)

# ----------------------------------- EX. 2----------------------------------- #

def do_ex2_test(input_data, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(input_data[0], input_data[1])
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(input_data[0], input_data[1])
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    return 2

def test_ex2_1(run=True):
    '''
    L = ['a', 'bb', 'ccc', 'd']
    k = 4
    expected = {'dabb', 'dccc', 'dbba', 'bbad', 'ccca', 'abbd', 'bbda', 'cccd', 'adbb', 'accc'}
    '''
    input_data = (['a', 'bb', 'ccc', 'd'], 4)
    expected = {'dabb', 'dccc', 'dbba', 'bbad', 'ccca', 'abbd', 'bbda', 'cccd', 'adbb', 'accc'}
    return do_ex2_test(input_data, expected)

def test_ex2_2(run=True):
    '''
    L = ['a', 'bb', 'ccc', 'd']
    k = 5
    expected = {'dccca', 'cccad', 'daccc', 'adccc', 'acccd', 'bbccc', 'cccbb', 'cccda'}
    '''
    input_data = (['a', 'bb', 'ccc', 'd'], 5)
    expected = {'dccca', 'cccad', 'daccc', 'adccc', 'acccd', 'bbccc', 'cccbb', 'cccda'}
    return do_ex2_test(input_data, expected)

def test_ex2_3(run=True):
    '''
    L = ['a', 'bb', 'ccc', 'd']
    k = 3
    expected = {'dbb', 'bba', 'bbd', 'abb'}
    '''
    input_data = (['a', 'bb', 'ccc', 'd'], 3)
    expected = {'dbb', 'bba', 'bbd', 'abb'}
    return do_ex2_test(input_data, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,   test_ex1_2, test_ex1_3,
    test_ex2_1,   test_ex2_2, test_ex2_3,
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

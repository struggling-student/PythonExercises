# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['BOLD']+COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['BOLD']+COL['RED']
        if col:
            return func(f'{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
        else:
            return func(*args, **kwargs, )
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
DEBUG = True
#DEBUG = False
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


def do_func1_tests(string_list1, string_list2, expected):
    res = program.func1(string_list1, string_list2)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista ritornata è sbagliata! / The returned list is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func1_1():
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','d']
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','d']
    expected = ['d', 'c', 'b']
    return do_func1_tests(string_list1, string_list2, expected)

def test_func1_2():
    '''
    string_list1 = ['coke', 'fanta', 'sprite', 'lambdala', 'lemonsoda', 'oransoda']
    string_list2 = ['coke', 'fanta', 'oransoda', 'pepsi']
    '''
    string_list1 = ['a','b','c']
    string_list2 = []
    expected = ['c', 'b', 'a']
    return do_func1_tests(string_list1, string_list2, expected)

def test_func1_3():
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','b','c']
    '''
    string_list1 = ['a','b','c']
    string_list2 = ['a','b','c']
    expected = []
    return do_func1_tests(string_list1, string_list2, expected)

def test_func1_4():
    '''
    string_list1 = ['a','b','c']
    string_list2 = []
    '''
    string_list1 = ['a','b','c']
    string_list2 = []
    expected = ['c', 'b', 'a']
    return do_func1_tests(string_list1, string_list2, expected)

def do_func2_tests(pathname, expected):
    res = program.func2(pathname)

    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        for k in expected:
            if expected[k] != res[k]:
                my_print(f'''[ERROR] Ad esempio, il carattere {k} dovrebbe avere una frequenza {expected[k]} invece che {res[k]}.''')
                my_print(f'''[ERROR] For example, char {k} frequency should be {expected[k]} instead of {res[k]}.''')
                break
        return 0
    return 0.5


def test_func2_1():
    '''
    pathname = 'func2/func2_test_1.txt'
    '''
    pathname = 'func2/func2_test_1.txt'
    expected = {'c': 1, 'f': 1, ' ': 2, 't': 4, '\n': 1, 'r': 2, 'a': 4}
    return do_func2_tests(pathname, expected)

def test_func2_2():
    '''
    pathname = 'func2/func2_test_2.txt'
    '''
    pathname = 'func2/func2_test_2.txt'
    expected = {'b': 4, ' ': 2, 'B': 3, 'd': 2, 'i': 5, '\n': 1, 'o': 3}
    return do_func2_tests(pathname, expected)

def test_func2_3():
    '''
    pathname = 'func2/func2_test_3.txt'
    '''
    pathname = 'func2/func2_test_3.txt'
    expected = {}
    return do_func2_tests(pathname, expected)

def test_func2_4():
    '''
    pathname = 'func2/func2_test_4.txt'
    '''
    pathname = 'func2/func2_test_4.txt'
    expected = {'e': 37, 'v': 3, 'm': 17, ' ': 68, 'o': 29, 'E': 1, 'u': 28, 's': 18, ',': 4, 'i': 42, 'U': 1, 'b': 3, 'f': 3, 'h': 1, 'D': 1, 'p': 11, 'r': 22, 'x': 3, 'g': 3, 'l': 21, 'c': 16, 'L': 1, 'q': 5, '.': 4, 't': 32, 'n': 24, 'd': 18, 'a': 29}
    return do_func2_tests(pathname, expected)


def do_func3_tests(a_list, a_list_expected, expected):
    res = program.func3(a_list)
    if a_list != a_list_expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista non è stata modificata! / The list is unchanged!.\nList={a_list}, expected list={a_list_expected}.\n{'*'*50}''')
        return 0
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func3_1():
    '''
    a_list = [3, 12, -3, 4, 6, 12]
    '''
    a_list = [3, 12, -3, 4, 6, 12]
    a_list_expected = [3, 4, 6]
    expected = 3
    return do_func3_tests(a_list, a_list_expected, expected)

def test_func3_2():
    '''
    a_list = [3, 12, 3, 12, 3, 3, 3, 3, 12, 12]
    '''
    a_list = [3, 12, 3, 12, 3, 3, 3, 3, 12, 12]
    a_list_expected = []
    expected = 10
    return do_func3_tests(a_list, a_list_expected, expected)

def test_func3_3():
    '''
    a_list = [0, 0, 0, 0, 0, 0, 0]
    '''
    a_list = [0, 0, 0, 0, 0, 0, 0]
    a_list_expected = []
    expected = 7
    return do_func3_tests(a_list, a_list_expected, expected)

def test_func3_4():
    '''
    a_list = [3.2, 12, -3, -10.4, 4, 6, 12, -10.4, -10.4,]
    '''
    a_list = [3.2, 12, -3, -10.4, 4, 6, 12, -10.4, -10.4, 10]
    a_list_expected = [3.2, -3, 4, 6, 10]
    expected = 5
    return do_func3_tests(a_list, a_list_expected, expected)


# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename  = f'func4/func4_test{ID}.txt'
    output_filename = f'func4/func4_out{ID}.txt'
    expected_filename = f'func4/func4_exp{ID}.txt'
    res = program.func4(input_filename, output_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di righe ritornato è sbagliato! / The number of written rows is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1():
    '''
    input_filename = 'func4/func4_test1.txt'
    '''
    ID = 1
    expected = 3
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_filename = 'func4/func4_test2.txt'
    '''
    ID = 2
    expected = 5
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_filename = 'func4/func4_test3.txt'
    '''

    ID = 3
    expected = 18
    return do_func4_tests(ID, expected)

def do_test_func5(ID, color, expected):
    img_in  = f'func5/image0{ID}.png'
    img_out = f'func5/your_image0{ID}.png'
    img_exp = f'func5/expected0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out, color)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di segmenti colorati è sbagliato! / The number of colored segments is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''
    imagefile = func5/image01.png
    output_imagefile = func5/expected01.png
    color = (255,0,0)
    '''
    ID = 1
    color = (255,0,0)
    expected = 1
    return do_test_func5(ID, color, expected)


def test_func5_2():
    '''
    imagefile = func5/image02.png
    output_imagefile = func5/expected02.png
    color = (255,0,0)
    '''
    ID = 2
    color = (255,0,0)
    expected = 1
    return do_test_func5(ID, color, expected)


def test_func5_3():
    '''
    imagefile = func5/image03.png
    output_imagefile = func5/expected03.png
    color = (100,160,200)
    '''
    ID = 3
    color = (100,160,200)
    expected = 45
    return do_test_func5(ID, color, expected)


def test_func5_4():
    '''
    imagefile = func5/image04.png
    output_imagefile = func5/expected04.png
    color = (0,0,0)
    '''
    ID = 4
    color = (0,0,0)
    expected = 90
    return do_test_func5(ID, color, expected)

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(directory, ext, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(directory, ext)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(directory, ext)
    testlib.check(res, expected, None, f'''{'*'*50}\n[ERROR]Il dizionario ritornato non è corretto! / Incorrect dictionary!\nReturned={res}, expected={expected}''')
    return 2

def test_ex1_1():
    '''
    directory = 'ex1/A'
    ext = '.py'
    '''
    directory = 'ex1/A'
    ext = '.py'
    expected = {'ex1/A': 92, 'ex1/A/C': 92}
    return do_test_ex1(directory, ext, expected)


def test_ex1_2():
    '''
    directory = 'ex1/B'
    ext = '.txt'
    '''
    directory = 'ex1/B'
    ext = '.txt'
    expected = {'ex1/B/D': 106, 'ex1/B/B': 25, 'ex1/B': 56, 'ex1/B/C': 145}
    return do_test_ex1(directory, ext, expected)


def test_ex1_3():
    '''
    directory = 'ex1'
    ext = '.txt'
    '''
    directory = 'ex1'
    ext = '.txt'
    expected = {'ex1/B/D': 106, 'ex1/B/B': 25, 'ex1/B': 56, 'ex1/B/C': 145, 'ex1/A/B': 25, 'ex1/A': 53, 'ex1/A/C': 145, 'ex1': 106}
    return do_test_ex1(directory, ext, expected)

# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(root)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    return 2


def test_ex2_1():
    '''
    ______5______
   |             |
   8__        ___2___
      |      |       |
      3      9       1
    '''
    root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    expected = 8
    return do_ex2_test(root, expected)

def test_ex2_2():
    '''
        ______2______
       |             |
    __ 7__        ___5___
   |      |      |       |
  _4_     3_    _0_     _5_
 |   |      |  |   |   |   |
 2   -1     1  8   3   2   9
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    expected =  -22
    return do_ex2_test(root, expected)


def test_ex2_3():
    '''
    A big tree
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = -338
    return do_ex2_test(root, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
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
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['BOLD']+COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
################################################################################

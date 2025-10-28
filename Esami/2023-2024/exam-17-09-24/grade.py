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

# %%----------------------------------- Func 1 ----------------------------------- #
def do_func1_tests(D1, D2, expected):
    res = program.func1(D1, D2)
    testlib.check_list(res, expected)
    return 0.5


def test_func1_1(run=True):
    '''
    D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
    D2 = {4:'bb', 1:'ff', 2:'ggg'}
    expected = ['bbggg', 'aaff', 'ccff', 'ebb']
    '''
    D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
    D2 = {4:'bb', 1:'ff', 2:'ggg'}
    expected = ['bbggg', 'aaff', 'ccff', 'ebb']
    return do_func1_tests(D1, D2, expected)

def test_func1_2(run=True):
    '''
    D1 = {'aa': 1, 'bb': 1, 'cc': 1, 'dd': 1, 'ee':1}
    D2 = {4:'bb', 1:'ff', 2:'ggg'}
    expected = ['aaff', 'bbff', 'ccff', 'ddff', 'eeff']
    '''
    D1 = {'aa': 1, 'bb': 1, 'cc': 1, 'dd': 1, 'ee':1}
    D2 = {4:'bb', 1:'ff', 2:'ggg'}
    expected = ['aaff', 'bbff', 'ccff', 'ddff', 'eeff']
    return do_func1_tests(D1, D2, expected)

def test_func1_3(run=True):
    '''
    D1 = {'aa': 1, 'bb': 1, 'cc': 1, 'dd': 1, 'e':1}
    D2 = {4:'bb', 2:'ff', 3:'ggg'}
    expected = []
    '''
    D1 = {'aa': 1, 'bb': 1, 'cc': 1, 'dd': 1, 'e':1}
    D2 = {4:'bb', 2:'ff', 3:'ggg'}
    expected = []
    return do_func1_tests(D1, D2, expected)

def test_func1_4(run=True):
    '''
    D1 = {'aa': 4, 'bb': 4, 'cc': 3, 'dd': 3, 'ee':3, 'ff':2, 'gg':2}
    D2 = {4:'bb', 2:'ff', 3:'ggg'}
    expected = ['ccggg', 'ddggg', 'eeggg', 'aabb', 'bbbb', 'ffff', 'ggff']
    '''
    D1 = {'aa': 4, 'bb': 4, 'cc': 3, 'dd': 3, 'ee':3, 'ff':2, 'gg':2}
    D2 = {4:'bb', 2:'ff', 3:'ggg'}
    expected = ['ccggg', 'ddggg', 'eeggg', 'aabb', 'bbbb', 'ffff', 'ggff']
    return do_func1_tests(D1, D2, expected)

# %%----------------------------------- Func 2 ----------------------------------- #
def do_func2_tests(l, new_l, expected):
    res = program.func2(l)
    testlib.check_list(l, new_l)
    testlib.check(res, expected, expl=f'\nIl valore ritornato non è corretto | The returned value is not correct.\nreturned: {res}\t expected: {expected}')
    return 0.5

def test_func2_1(run=True):
    '''
    l = [3, -3, 6, -1, 10]
    expected = 15
    new_l = [3, 0, 6, 5, 15]
    '''
    l = [3, -3, 6, -1, 10]
    expected = 15
    new_l = [3, 0, 6, 5, 15]
    return do_func2_tests(l, new_l, expected)

def test_func2_2(run=True):
    '''
    l = [3, -3, 3, -3, 3, -3]
    expected = 0
    new_l = [3, 0, 3, 0, 3, 0]
    '''
    l = [3, -3, 3, -3, 3, -3]
    expected = 0
    new_l = [3, 0, 3, 0, 3, 0]
    return do_func2_tests(l, new_l, expected)

def test_func2_3(run=True):
    '''
    l = [-73, -64, 65, -40, -33, 93, -1, 65, -73, 100]
    expected = 39
    new_l = [-73, -137, -72, -112, -145, -52, -53, 12, -61, 39]
    '''
    l = [-73, -64, 65, -40, -33, 93, -1, 65, -73, 100]
    expected = 39
    new_l = [-73, -137, -72, -112, -145, -52, -53, 12, -61, 39]
    return do_func2_tests(l, new_l, expected)

def test_func2_4(run=True):
    '''
    l = [-768, 726, 29, 193, 922, 226, 848, -570, 123, -309, 959, -588, 473, -633, 963, 490, 167, 987, 917, -6]
    expected = 5149
    new_l = [-768, -42, -13, 180, 1102, 1328, 2176, 1606, 1729, 1420, 2379, 1791, 2264, 1631, 2594, 3084, 3251, 4238, 5155, 5149]
    '''
    l = [-768, 726, 29, 193, 922, 226, 848, -570, 123, -309, 959, -588, 473, -633, 963, 490, 167, 987, 917, -6]
    expected = 5149
    new_l = [-768, -42, -13, 180, 1102, 1328, 2176, 1606, 1729, 1420, 2379, 1791, 2264, 1631, 2594, 3084, 3251, 4238, 5155, 5149]
    return do_func2_tests(l, new_l, expected)


# %%----------------------------------- Func 3 ----------------------------------- #
def do_func3_tests(words, l, expected):
    res = program.func3(words, l)
    testlib.check_val(res, expected)
    return 0.5


def test_func3_1(run=True):
    '''
    words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
    l=3
    expected = {'cat', 'bert'}
    '''
    words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
    l=3
    expected = {'cat', 'bert'}
    return do_func3_tests(words, l, expected)

def test_func3_2(run=True):
    '''
    words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
    l=2
    expected = {'be', 'cat', 'bert'}
    '''
    words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
    l=2
    expected = {'be', 'cat', 'bert'}
    return do_func3_tests(words, l, expected)

def test_func3_3(run=True):
    '''
    words = {'lodestones', 'lode', 'mandrake', 'drake', 'brakes', 'lodestar', 'imploded', 'rake'}
    l=5
    expected = {'drake')
    '''
    words = {'lodestones', 'lode', 'mandrake', 'drake', 'brakes', 'lodestar', 'imploded', 'rake'}
    l=5
    expected = {'drake'}
    return do_func3_tests(words, l, expected)

def test_func3_4(run=True):
    '''
    words = {'cheerio', 'reattachment', 'attaching', 'punched', 'cheeriest', 'spirited', 'reattaches', 'puncheons', 'pashas', 'reattach', 'cheer', 'cheering', 'reattaching', 'cheerless', 'attaches', 'cowpuncher', 'reattached', 'cheerfully', 'cheerleader', 'unattached', 'attache', 'cowpunchers', 'cheers', 'cheerily', 'keypunch', 'keypunched', 'resorcinol', 'attach', 'skewers', 'attachment', 'cheerleaders', 'punchers', 'gasify', 'philanderer', 'cheerful', 'arguments', 'punch', 'keypunches', 'punches', 'cheery', 'exercises', 'unpunched', 'purloins', 'cheeriness', 'siberians', 'reattachments', 'alaska', 'causa', 'punchy', 'punchbowl', 'cheerlessly', 'cheerier', 'attached', 'synchronisation', 'outran', 'keypunching', 'eyestrain', 'cheered', 'puncheon', 'cheerfulness', 'attachable', 'puncher', 'airlock', 'pluralist', 'attachments', 'punchbowls', 'perverse', 'collectivise', 'punching', 'wirral'}
    l=10
    expected = {'attachment', 'attachments', 'cheerleader', 'cowpuncher', 'reattachment'}
    '''
    words = {'cheerio', 'reattachment', 'attaching', 'punched', 'cheeriest', 'spirited', 'reattaches', 'puncheons', 'pashas', 'reattach', 'cheer', 'cheering', 'reattaching', 'cheerless', 'attaches', 'cowpuncher', 'reattached', 'cheerfully', 'cheerleader', 'unattached', 'attache', 'cowpunchers', 'cheers', 'cheerily', 'keypunch', 'keypunched', 'resorcinol', 'attach', 'skewers', 'attachment', 'cheerleaders', 'punchers', 'gasify', 'philanderer', 'cheerful', 'arguments', 'punch', 'keypunches', 'punches', 'cheery', 'exercises', 'unpunched', 'purloins', 'cheeriness', 'siberians', 'reattachments', 'alaska', 'causa', 'punchy', 'punchbowl', 'cheerlessly', 'cheerier', 'attached', 'synchronisation', 'outran', 'keypunching', 'eyestrain', 'cheered', 'puncheon', 'cheerfulness', 'attachable', 'puncher', 'airlock', 'pluralist', 'attachments', 'punchbowls', 'perverse', 'collectivise', 'punching', 'wirral'}
    l=10
    expected = {'attachment', 'attachments', 'cheerleader', 'cowpuncher', 'reattachment'}
    return do_func3_tests(words, l, expected)


# %%----------------------------------- Func 4 ----------------------------------- #

def do_func4_tests(ID, length, chars, expected):
    input_filename  = f'func4/in_0{ID}.txt'
    output_filename = f'func4/out_0{ID}.txt'
    expected_filename = f'func4/exp_0{ID}.txt'
    res = program.func4(input_filename, output_filename, length, chars)
    testlib.check_list(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1(run=True):
    '''
    input_filename = 'func4/in_01.txt'
    ouput_filename = 'func4/out_01.txt'
    expected_filename = 'func4/exp_01.txt'
    length = 5
    chars = 'asd'
    expected = ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
    '''
    ID = 1
    length = 5
    chars = 'asd'
    expected = ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
    return do_func4_tests(ID, length, chars, expected)

def test_func4_2(run=True):
    '''
    input_filename = 'func4/in_02.txt'
    ouput_filename = 'func4/out_02.txt'
    expected_filename = 'func4/exp_02.txt'
    length = 8
    chars = 'qwerty'
    expected = ['chronologies', 'annuitants', 'bridgeport', 'precluding', 'sauerkraut', 'cutworms', 'speculum', 'subfloor']
    '''
    ID = 2
    length = 8
    chars = 'qwerty'
    expected = ['chronologies', 'annuitants', 'bridgeport', 'precluding', 'sauerkraut', 'cutworms', 'speculum', 'subfloor']
    return do_func4_tests(ID, length, chars, expected)

def test_func4_3(run=True):
    '''
    input_filename = 'func4/in_03.txt'
    ouput_filename = 'func4/out_03.txt'
    expected_filename = 'func4/exp_03.txt'
    length = 2
    chars = 'aiu'
    expected = ['psychologically', 'mephistopheles', 'modifications', 'apotheosizes', 'midwesterner', 'forewarning', 'magnetising', 'mellifluous', 'sulfonamide', 'altercates', 'deficiency', 'fascinator', 'cufflinks', 'euthenics', 'inserting', 'prompting', 'rewriting', 'brasilia', 'cinching', 'gnarling', 'harpists', 'chacers', 'triadic', 'viaduct', 'geisha', 'aires', 'scite']
    '''
    ID = 3
    length = 2
    chars = 'aiu'
    expected = ['psychologically', 'mephistopheles', 'modifications', 'apotheosizes', 'midwesterner', 'forewarning', 'magnetising', 'mellifluous', 'sulfonamide', 'altercates', 'deficiency', 'fascinator', 'cufflinks', 'euthenics', 'inserting', 'prompting', 'rewriting', 'brasilia', 'cinching', 'gnarling', 'harpists', 'chacers', 'triadic', 'viaduct', 'geisha', 'aires', 'scite']
    return do_func4_tests(ID, length, chars, expected)

# %%----------------------------------- Func 5 ----------------------------------- #

def do_test_func5(ID, m, M, expected):
    img_in = f'func5/func5_test{ID}.png'
    img_out = f'func5/func5_out{ID}.png'
    img_exp = f'func5/func5_exp{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out, m, M)
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1(run=True):
    '''
    imagefile = func5/func5_test1.png
    output_imagefile = func5/func5_out1.png
    '''
    ID = 1
    m = 1
    M = 20
    expected = 6
    return do_test_func5(ID, m, M, expected)


def test_func5_2(run=True):
    '''
    imagefile = func5/func5_test2.png
    output_imagefile = func5/func5_out2.png
    color = (255,0,0)
    '''
    ID = 2
    m = 20
    M = 40
    expected = 14
    return do_test_func5(ID, m, M, expected)


def test_func5_3(run=True):
    '''
    imagefile = func5/func5_test3.png
    output_imagefile = func5/func5_out3.png
    '''
    ID = 3
    m = 40
    M = 100
    expected = 28
    return do_test_func5(ID, m, M, expected)


def test_func5_4(run=True):
    '''
    imagefile = func5/func5_test4.png
    output_imagefile = func5/func5_out4.png
    '''
    ID = 4
    m = 10
    M = 40
    expected = 37
    return do_test_func5(ID, m, M, expected)

# %%----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(chars, l, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(chars, l)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(chars, l)
    testlib.check_list(res, expected)
    return 2

def test_ex1_1(run=True):
    '''
    chars = {'a', 'b', 'c'}
    l = 3
    expected = {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}
    '''
    chars = {'a', 'b', 'c'}
    l = 3
    expected = {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}
    return do_test_ex1(chars, l, expected)

def test_ex1_2(run=True):
    '''
    chars = {'a', 'b', 'c'}
    l = 4
    expected = {'bbbb', 'caac', 'acca', 'abba', 'bccb', 'cccc', 'aaaa', 'cbbc', 'baab'}
    '''
    chars = {'a', 'b', 'c'}
    l = 4
    expected = {'bbbb', 'caac', 'acca', 'abba', 'bccb', 'cccc', 'aaaa', 'cbbc', 'baab'}
    return do_test_ex1(chars, l, expected)


def test_ex1_3(run=True):
    '''
    chars = {'a', 'b', 'c', 'd'}
    l = 5
    expected = {'cadac', 'adcda', 'cdcdc', 'dcccd', 'bdcdb', 'cabac', 'abdba', 'ccccc', 'bdadb', 'bdbdb', 'aadaa', 'baaab', 'bbbbb', 'cbabc', 'ddbdd', 'cdddc', 'bcdcb', 'dcbcd', 'ddadd', 'badab', 'ddcdd', 'acdca', 'dacad', 'dbbbd', 'cbcbc', 'accca', 'aaaaa', 'addda', 'bdddb', 'cbdbc', 'dadad', 'adada', 'bcacb', 'bbcbb', 'ababa', 'cdadc', 'adbda', 'acbca', 'caaac', 'acaca', 'ccdcc', 'babab', 'dcdcd', 'abcba', 'bcbcb', 'aacaa', 'aabaa', 'bbabb', 'ccacc', 'cdbdc', 'cacac', 'dbabd', 'ccbcc', 'dabad', 'bacab', 'ddddd', 'dbdbd', 'abbba', 'dcacd', 'cbbbc', 'daaad', 'bbdbb', 'dbcbd', 'bcccb'}
    '''
    chars = {'a', 'b', 'c', 'd'}
    l = 5
    expected = {'cadac', 'adcda', 'cdcdc', 'dcccd', 'bdcdb', 'cabac', 'abdba', 'ccccc', 'bdadb', 'bdbdb', 'aadaa', 'baaab', 'bbbbb', 'cbabc', 'ddbdd', 'cdddc', 'bcdcb', 'dcbcd', 'ddadd', 'badab', 'ddcdd', 'acdca', 'dacad', 'dbbbd', 'cbcbc', 'accca', 'aaaaa', 'addda', 'bdddb', 'cbdbc', 'dadad', 'adada', 'bcacb', 'bbcbb', 'ababa', 'cdadc', 'adbda', 'acbca', 'caaac', 'acaca', 'ccdcc', 'babab', 'dcdcd', 'abcba', 'bcbcb', 'aacaa', 'aabaa', 'bbabb', 'ccacc', 'cdbdc', 'cacac', 'dbabd', 'ccbcc', 'dabad', 'bacab', 'ddddd', 'dbdbd', 'abbba', 'dcacd', 'cbbbc', 'daaad', 'bbdbb', 'dbcbd', 'bcccb'}
    return do_test_ex1(chars, l, expected)

# %%----------------------------------- EX. 2----------------------------------- #


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


def test_ex2_1(run=True):
    '''
              root
          _____6_____
         |           |
     ___5         ___3___
    |            |       |
    4          _10_      6_
              |    |       |
              7    8       1
    '''
    root = tree.BinaryTree.fromList([6, [5, [4, None, None], None ], [16, [10, [7, None, None], None],
                                                                    [6, [8, None, None], [1, None, None]]]])
    expected = (16, 2)
    return do_ex2_test(root, expected)

def test_ex2_2(run=True):
    '''
              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _34_    13_   _10_    _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = 4
    '''
    root = tree.BinaryTree.fromList([2, [7, [34, [2, None, None], [-1, None, None]], [30, None, [1, None, None]]], [15, [10, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
    expected =  (34, 3)
    return do_ex2_test(root, expected)


def test_ex2_3(run=True):
    '''
    A big tree
    expected = (45, 8)
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [45, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = (45, 8)
    return do_ex2_test(root, expected)


#%%###############################################################################

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

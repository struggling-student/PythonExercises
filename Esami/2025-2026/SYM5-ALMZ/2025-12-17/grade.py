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


def do_func1_tests(D1, D2, D3, expected):
    res = program.func1(D1, D2, D3)
    testlib.check_list(res, expected)
    return 3/4


def test_func1_1(run=True):
    '''
    D1 = { 'uno' : 1 , 'due' : 2, 'tre' : 3 }
    D2 = { 1 : 5     , 3 : 12   , 5 : 9 }
    D3 = { 12 : 'papere', 90 : 'cavalli', 5 : 'sogliole' }
    expected = ['trepapere', 'unosogliole']
    '''
    D1 = { 'uno' : 1 , 'due' : 2, 'tre' : 3 }
    D2 = { 1 : 5     , 3 : 12   , 5 : 9 }
    D3 = { 12 : 'papere', 90 : 'cavalli', 5 : 'sogliole' }
    expected = ['trepapere', 'unosogliole']
    return do_func1_tests(D1, D2, D3, expected)

def test_func1_2(run=True):
    D1 = {'intestine': 61, 'ritzy': 96, 'matchmaker': 71, 'enthusiastic': 23, 'effectiveness': 48, 'tested': 16, 'neon': 85}
    D2 = {16: 76, 48: 81, 23: 81, 85: 69, 96: 76, 55: 80, 71: 57, 26: 8, 100: 70, 28: 54, 82: 56, 88: 69, 84: 59, 90: 55, 56: 3}
    D3 = {76: 'ritzy', 98: 'ritzy', 69: 'matchmaker', 60: 'point', 56: 'ritzy', 81: 'enthusiastic', 83: 'ritzy', 36: 'intestine', 77: 'neon'}
    expected=['ritzyritzy', 'testedritzy', 'neonmatchmaker', 'enthusiasticenthusiastic', 'effectivenessenthusiastic']
    return do_func1_tests(D1,D2,D3,expected)

def test_func1_3(run=True):
    D1 = {'staircase': 14, 'mom': 95, 'poppy': 26, 'hydrolyze': 45, 'spike': 29, 'bathroom': 13, 'adhesive': 48, 'bench': 60, 'succotash': 85, 'rough': 4, 'iceberg': 10, 'regulator': 7}
    D2 = {48: 80, 60: 80, 7: 37, 13: 43, 85: 68, 26: 31, 95: 20, 4: 33, 45: 69, 8: 40, 74: 10, 89: 40, 98: 97, 93: 18, 10: 28, 23: 77, 16: 16, 68: 49, 44: 55, 69: 82, 72: 39, 40: 17, 88: 90, 33: 7}
    D3 = {30: 'contrast', 12: 'staircase', 69: 'bathroom', 20: 'hydrolyze', 50: 'switching', 2: 'contrast', 31: 'hydrolyze', 33: 'iceberg', 80: 'staircase', 44: 'switching', 13: 'poppy', 65: 'succotash', 11: 'staircase', 23: 'ginger', 68: 'succotash', 34: 'acid', 35: 'adhesive', 66: 'acid', 72: 'bench', 63: 'weight'}
    expected=['roughiceberg', 'momhydrolyze', 'poppyhydrolyze', 'benchstaircase', 'hydrolyzebathroom', 'adhesivestaircase', 'succotashsuccotash']
    return do_func1_tests(D1,D2,D3,expected)

def test_func1_4(run=True):
    D1 = {'spur': 23, 'class': 34, 'house': 54, 'lick': 50, 'didactic': 22, 'culvert': 71, 'standing': 4, 'mean': 82, 'boatyard': 3, 'scarf': 30, 'dressing': 63, 'godmother': 8, 'retrieve': 58, 'moose': 77, 'boxspring': 99, 'pepper': 28, 'rotten': 79, 'shiver': 14, 'analytics': 88, 'thesis': 57}
    D2 = {82: 81, 50: 26, 22: 97, 57: 69, 4: 22, 34: 100, 63: 86, 8: 76, 23: 60, 71: 86, 28: 90, 3: 11, 58: 42, 88: 18, 99: 45, 79: 61, 61: 87, 41: 99, 95: 45, 42: 1, 74: 8, 44: 7, 91: 5, 76: 60, 15: 54, 54: 28, 65: 82, 52: 18, 93: 4, 60: 68, 24: 74, 73: 37, 20: 19, 46: 44, 6: 12}
    D3 = {29: 'lick', 56: 'boxspring', 26: 'lick', 86: 'mean', 41: 'moose', 40: 'thesis', 94: 'amuck', 93: 'culvert', 39: 'rotten', 18: 'bewildered', 97: 'culvert', 20: 'godmother', 90: 'bewildered', 42: 'digestive', 100: 'culvert', 61: 'analytics', 22: 'digestive', 52: 'boatyard', 36: 'house', 14: 'shiver', 44: 'godmother', 91: 'moose', 60: 'house', 81: 'moose', 76: 'analytics', 11: 'scarf'}
    expected=['licklick', 'spurhouse', 'meanmoose', 'culvertmean', 'dressingmean', 'classculvert', 'boatyardscarf', 'rottenanalytics', 'didacticculvert', 'pepperbewildered', 'standingdigestive', 'retrievedigestive', 'godmotheranalytics', 'analyticsbewildered']
    return do_func1_tests(D1,D2,D3,expected)

###############################################################################

def do_func2_tests(L1, L2, L3, expected):
    res = program.func2(L1, L2, L3)
    try:
        testlib.check_list(res, expected)
    except:
        testlib.check_val(res, expected)   # FIXED
    return 3/4

def test_func2_1(run=True):
    '''
    L1 = [ 1, 2, 6, 2, 8, 4, 9, 1, 7 ]
    L2 = [ 5, 6, 1, 8, 3, 2 ]
    L3 = [ 10, 8, 9, 1, 2, 8, 9, 6, 10 ]
    expected = ({3, 4, 5, 7, 10}, {8, 1, 2, 6})
    '''
    L1 = [ 1, 2, 6, 2, 8, 4, 9, 1, 7 ]
    L2 = [ 5, 6, 1, 8, 3, 2 ]
    L3 = [ 10, 8, 9, 1, 2, 8, 9, 6, 10 ]
    expected = ({3, 4, 5, 7, 10}, {8, 1, 2, 6})
    return do_func2_tests(L1, L2, L3, expected)

def test_func2_2(run=True):
    L1 = [2, 4, 10, 15, 12, 9, 18, 2, 11, 5]
    L2 = [11, 5, 3, 18, 18, 5, 5, 4, 17, 16]
    L3 = [18, 11, 17, 18, 19, 15, 18, 16, 6, 11]
    expected = ({2, 3, 6, 9, 10, 12, 19}, {18, 11})
    return do_func2_tests(L1,L2,L3,expected)

def test_func2_3(run=True):
    L1 = [12, 16, 10, 2, 13, 16, 16, 0, 4, 8]
    L2 = [0, 19, 19, 9, 2, 9, 17, 8, 19, 0, 16, 19, 10, 13, 17, 3, 9, 8, 6, 11]
    L3 = [2, 19, 12, 14, 5, 12, 5, 3, 17, 11, 17, 15, 18, 8, 18, 4, 17, 1, 14, 18, 14, 11, 4, 15, 2, 10, 11, 10, 17, 5]
    expected = ({1, 5, 6, 9, 14, 15, 18}, {8, 2, 10})
    return do_func2_tests(L1,L2,L3,expected)

def test_func2_4(run=True):
    L1 = [81, 89, 76, 19, 72, 82, 27, 64, 14, 84, 79, 26, 56, 60, 37, 74, 81, 25, 65, 2]
    L2 = [51, 45, 40, 22, 26, 74, 43, 82, 58, 30, 81, 16, 0, 30, 87, 18, 58, 13, 83, 51, 15, 93, 73, 8, 40, 35, 17, 64, 16, 90, 43, 17, 6, 72, 72, 99, 16, 66, 14, 30]
    L3 = [72, 93, 68, 37, 98, 1, 5, 21, 81, 56, 13, 46, 86, 37, 25, 18, 87, 88, 15, 35, 51, 46, 66, 61, 6, 0, 53, 34, 26, 55, 17, 97, 87, 4, 40, 77, 63, 22, 4, 89, 2, 69, 75, 66, 47, 45, 8, 92, 44, 53, 80, 18, 36, 99, 71, 27, 37, 53, 57, 18]
    expected = ({1, 4, 5, 16, 19, 21, 30, 34, 36, 43, 44, 46, 47, 53, 55, 57, 58, 60, 61, 63, 65, 68, 69, 71, 73, 75, 76, 77, 79, 80, 83, 84, 86, 88, 90, 92, 97, 98}, {72, 81, 26})
    return do_func2_tests(L1,L2,L3,expected)

###############################################################################

def do_func3_tests(ID, expected):
    input_filename  = f'func3/in_{ID}.txt'
    output_filename = f'func3/out_{ID}.txt'
    expected_filename = f'func3/exp_{ID}.txt'
    res = program.func3(input_filename, output_filename)
    testlib.check(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 1.5


def test_func3_1(run=True):
    '''
    input_filename = 'func3/in_5.txt'
    ouput_filename = 'func3/out_5.txt'
    expected_filename = 'func3/exp_5.txt'
    expected = 
    '''
    ID = 5
    expected = 287
    return do_func3_tests(ID, expected)

def test_func3_2(run=True):
    '''
    input_filename = 'func3/in_10.txt'
    ouput_filename = 'func3/out_10.txt'
    expected_filename = 'func3/exp_10.txt'
    expected = 
    '''
    ID = 10
    expected = -249 
    return do_func3_tests(ID, expected)

def test_func3_3(run=True):
    '''
    input_filename = 'func3/in_20.txt'
    ouput_filename = 'func3/out_20.txt'
    expected_filename = 'func3/exp_20.txt'
    expected = 
    '''
    ID = 20
    expected = 1054
    return do_func3_tests(ID, expected)

def test_func3_4(run=True):
    '''
    input_filename = 'func3/in_30.txt'
    ouput_filename = 'func3/out_30.txt'
    expected_filename = 'func3/exp_30.txt'
    expected = 
    '''
    ID = 30
    expected = 714
    return do_func3_tests(ID, expected)

###############################################################################

def do_test_func4(filename, expected):

    res = program.func4(filename)
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il numero di segmenti colorati è sbagliato! / The number of colored segments is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    return 2


def test_func4_1(run=True):
    '''
    filename = "func4/func4_100_100_10.png"
    expected = 3, 7
    '''
    filename = "func4/func4_100_100_10.png"
    expected = 3, 7
    return do_test_func4(filename, expected)


def test_func4_2(run=True):
    '''
    filename = "func4/func4_100_100_50.png"
    expected = 26, 24
    '''
    filename = "func4/func4_100_100_50.png"
    expected = 26, 24
    return do_test_func4(filename, expected)


def test_func4_3(run=True):
    '''
    filename = "func4/func4_100_100_100.png"
    expected = 58, 42
    '''
    filename = "func4/func4_100_100_100.png"
    expected = 58, 42
    return do_test_func4(filename, expected)


def test_func4_4(run=True):
    '''
    filename = "func4/func4_400_200_1000.png"
    expected = 524, 476
    '''
    filename = "func4/func4_400_200_1000.png"
    expected = 524, 476
    return do_test_func4(filename, expected)

###############################################################################

def do_test_ex1(dirin, parole, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(dirin, parole)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(dirin, parole)
    testlib.check_dict(res, expected)
    return 2

def test_ex1_1(run=True):
    dirin = 'ex1/A'
    parole = ['user', 'recommendation', 'swanky', 'ski', 'user', 'fetch', 'payoff', 'ski', 'agenda']
    expected = {'user': 0, 'recommendation': 1, 'swanky': 0, 'ski': 0, 'fetch': 1, 'payoff': 0, 'agenda': 1}
    return do_test_ex1(dirin,parole, expected)

def test_ex1_2(run=True):
    dirin = 'ex1/B'
    parole = ['subexpression', 'terrify', 'line', 'become', 'pour', 'tuna', 'evaluate', 'money', 'ugly', 'sickness', 'inventory', 'balloon', 'fav', 'euphonium', 'rethinking', 'majority', 'sickness', 'euphonium', 'career', 'nexus', 'ectodermal', 'balloon', 'nexus', 'euphonium', 'prescribe', 'libido', 'euphonium', 'bob', 'ugly']
    expected = {'subexpression': 0, 'terrify': 1, 'line': 1, 'become': 0, 'pour': 0, 'tuna': 0, 'evaluate': 0, 'money': 0, 'ugly': 0, 'sickness': 0, 'inventory': 1, 'balloon': 0, 'fav': 0, 'euphonium': 0, 'rethinking': 1, 'majority': 0, 'career': 0, 'nexus': 0, 'ectodermal': 0, 'prescribe': 0, 'libido': 1, 'bob': 0}
    return do_test_ex1(dirin,parole, expected)


def test_ex1_3(run=True):
    dirin = 'ex1/C'
    parole = ['tired', 'sable', 'diploma', 'eviction', 'acrid', 'owl', 'shipyard', 'snowboarding', 'dirndl', 'marriage', 'vine', 'oats', 'mime', 'legging', 'mile', 'hunter', 'royal', 'aspic', 'exist', 'gravitas', 'stand', 'icing', 'collateral', 'cliff', 'oriented', 'doubling', 'disk', 'coverage', 'sweep', 'normal', 'timer', 'undershirt', 'decrease', 'tip', 'decrease', 'pheromone', 'gelatin', 'award', 'mint', 'leader', 'harmonica', 'mandolin', 'dungeon', 'self']
    expected = {'tired': 1, 'sable': 3, 'diploma': 2, 'eviction': 1, 'acrid': 5, 'owl': 1, 'shipyard': 2, 'snowboarding': 4, 'dirndl': 2, 'marriage': 1, 'vine': 2, 'oats': 3, 'mime': 2, 'legging': 1, 'mile': 4, 'hunter': 4, 'royal': 4, 'aspic': 3, 'exist': 4, 'gravitas': 0, 'stand': 7, 'icing': 2, 'collateral': 2, 'cliff': 6, 'oriented': 1, 'doubling': 3, 'disk': 6, 'coverage': 5, 'sweep': 4, 'normal': 4, 'timer': 2, 'undershirt': 3, 'decrease': 0, 'tip': 4, 'pheromone': 2, 'gelatin': 2, 'award': 3, 'mint': 2, 'leader': 3, 'harmonica': 3, 'mandolin': 3, 'dungeon': 4, 'self': 1}
    try:
        return do_test_ex1(dirin,parole, expected)
    except:
        expected = {'tired': 1, 'sable': 3, 'diploma': 2, 'eviction': 1, 'acrid': 5, 'owl': 1, 'shipyard': 2, 'snowboarding': 4, 'dirndl': 2, 'marriage': 1, 'vine': 2, 'oats': 3, 'mime': 2, 'legging': 1, 'mile': 4, 'hunter': 4, 'royal': 4, 'aspic': 3, 'exist': 4, 'gravitas': 0, 'stand': 8, 'icing': 2, 'collateral': 2, 'cliff': 6, 'oriented': 1, 'doubling': 3, 'disk': 6, 'coverage': 5, 'sweep': 4, 'normal': 4, 'timer': 2, 'undershirt': 3, 'decrease': 0, 'tip': 4, 'pheromone': 2, 'gelatin': 2, 'award': 3, 'mint': 2, 'leader': 3, 'harmonica': 3, 'mandolin': 3, 'dungeon': 4, 'self': 1}
        return do_test_ex1(dirin,parole, expected) # FIXED

###############################################################################

def do_ex2_test(root, expected, expected_tree):
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
    if root != expected_tree:
        my_print(f'''{'*'*50}\n[ERROR]L'albero non è stato trasformato bene!!\nReturned={root.toList()}, expected={expected_tree}''')
        return 0
        
    return 2


def test_ex2_1(run=True):
    '''
        root         diventa       root
    ______25______               ___25____
   |             |              |         |
   8__        ___2___        ___8    _____2_____
      |      |       |      |       |           |
      3      9       1      3       1           9

      expected = 2
    '''
    root = tree.BinaryTree.fromList([25, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    exproot = tree.BinaryTree.fromList([25, [8, [3, None, None], None], [2, [1, None, None], [9, None, None]]])
    expected = 2
    return do_ex2_test(root, expected, exproot)

def test_ex2_2(run=True):
    '''
              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4_     3_    _0_     _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = 2
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [15, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [-9, None, None]]]])
    exproot = tree.BinaryTree.fromList([2, [7, [3, None, [1, None, None]], [4, [2, None, None], [-1, None, None]]], [15, [5, [2, None, None], [-9, None, None]], [0, [8, None, None], [3, None, None]]]])
    expected =  2
    return do_ex2_test(root, expected, exproot)


def test_ex2_3(run=True):
    '''
    A big tree
    expected = 104
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    exproot = tree.BinaryTree.fromList([-2, [5, [-5, [13, [5, [2, [5, [15, [15, None, None], None], [22, [6, None, None], [15, None, None]]], [14, [3, None, None], [0, None, None]]], None], [20, None, [17, None, [17, [25, None, [4, [5, None, [-4, [21, None, None], None]], [-3, None, [21, None, None]]]], [14, [10, None, [7, [19, [0, None, None], None], [12, None, None]]], [-10, [5, [28, [15, [7, None, None], [7, None, [12, None, None]]], [24, [-2, None, None], None]], None], [-4, [14, None, None], [2, None, None]]]]]]]], [-7, [-2, [20, [-4, [19, [-8, [12, [8, None, None], [21, None, None]], [3, [23, None, None], [7, None, [17, None, None]]]], [-9, None, [-1, None, None]]], [25, [12, [4, None, [-10, None, None]], [18, [13, None, None], [15, [27, None, None], [-2, None, None]]]], [3, [19, [-4, [25, None, None], None], None], [-10, None, None]]]], [-10, [2, [28, [-9, None, [11, None, None]], [1, None, None]], None], [13, [-2, None, None], [10, None, None]]]], [-6, [-9, [29, [30, [24, [2, [25, None, None], [-9, None, [3, None, None]]], [6, [25, None, None], [24, None, None]]], [16, [30, None, None], [0, None, [-1, None, None]]]], [23, None, [25, None, [20, None, None]]]], [28, [23, [16, [16, None, [16, None, None]], [-7, [7, None, None], [12, None, None]]], [-8, [2, [23, None, None], [14, None, None]], [24, None, [5, None, None]]]], [25, [5, [9, [4, None, None], None], [3, None, None]], [-8, [21, None, None], None]]]], [29, [17, [-2, [-3, [-8, None, None], None], [-7, None, None]], [-4, None, [-5, None, None]]], [8, None, [11, [21, [2, None, None], [-3, None, [2, None, None]]], [-6, None, None]]]]]], [-7, [14, [-8, [4, [15, [20, None, None], [28, [-7, [-5, None, None], [10, None, None]], None]], [-10, [10, [5, None, [14, None, None]], [27, None, None]], [10, [16, None, None], [27, None, None]]]], [25, [20, [4, None, None], [22, [21, [27, None, None], None], [22, None, None]]], [17, [7, [-4, [3, None, None], [12, None, None]], [19, None, None]], [12, [2, None, None], [23, None, None]]]]], [5, [24, [3, [4, None, [10, None, None]], [27, None, None]], None], [-5, [24, None, None], [30, None, None]]]], [9, [1, [-9, [28, [19, [8, None, [4, None, None]], [-3, None, [25, [10, None, None], None]]], [11, [24, None, [-10, None, None]], [8, None, None]]], [-10, [26, None, [17, None, None]], [28, [-6, None, [30, None, None]], [-2, [22, None, None], None]]]], [26, None, [29, [-10, None, None], [-6, None, None]]]], [12, [6, [25, [11, None, None], [25, None, None]], [-4, [-2, None, None], [11, [18, None, None], None]]], [7, [8, None, [25, [-2, [27, None, None], [-4, None, None]], [2, None, [-4, None, None]]]], [10, [6, [18, None, [0, None, None]], [18, None, None]], [30, None, [5, None, None]]]]]]]]], [13, [-7, [8, [11, [6, [24, None, None], [19, None, None]], [-2, [4, None, None], [5, None, None]]], [9, [1, [18, [-3, None, None], None], [22, [-10, [5, None, None], None], None]], None]], [2, [26, [10, [28, None, None], [-1, [19, None, None], [-3, [30, None, None], [-9, None, None]]]], [27, [10, [14, None, None], [0, None, [24, None, None]]], [13, [-3, None, [-1, None, None]], [30, [2, None, None], None]]]], None]], [17, [-1, None, [6, [28, [-4, None, None], [-10, None, None]], [30, [22, None, None], None]]], [12, [26, [-3, [-2, [7, [-4, None, None], None], [-3, None, [-2, [21, None, None], [28, None, None]]]], [-1, [24, [4, None, None], [30, None, [-4, None, None]]], [2, [18, None, None], [-2, None, None]]]], [10, [21, [1, None, None], None], [26, [30, None, None], None]]], [-2, [-8, [2, [-10, None, None], None], [20, [0, None, [-4, None, None]], [21, [7, None, None], [-5, None, [20, None, None]]]]], [16, None, [9, [21, None, None], [17, [23, None, None], None]]]]]]]], [20, None, [20, [19, [-10, [21, [5, None, [18, None, None]], [26, [24, None, None], None]], [-4, [1, None, None], [1, None, None]]], [-2, [-1, [10, None, None], [3, [24, None, [12, None, None]], [5, None, None]]], [27, [30, [-9, None, [4, None, None]], None], [29, [24, None, None], None]]]], [23, [14, [12, [27, [-5, None, None], [10, None, None]], None], [6, [3, None, None], [18, None, None]]], [2, [4, None, [21, None, [30, None, None]]], [16, [6, None, None], [-8, None, None]]]]]]])
    expected = 104
    
    return do_ex2_test(root, expected, exproot)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1,  test_func1_2, test_func1_3, test_func1_4, # 3/4
    test_func2_1,  test_func2_2, test_func2_3, test_func2_4, # 3/4
    test_func3_1,  test_func3_2, test_func3_3, test_func3_4, # 6/4
    test_func4_1,  test_func4_2, test_func4_3, test_func4_4, # 8/2
    test_ex1_1,    test_ex1_2,   test_ex1_3,                 # 6/3
    test_ex2_1,    test_ex2_2,   test_ex2_3,                 # 6/3
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

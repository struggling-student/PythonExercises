# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected, check_list, check_val

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print(  'WARNING: Save program.empty.py as program.py\n'
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
# DEBUG = True
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
# ----------------------------------- FUNC. 1----------------------------------- #
def do_func1_test(testo,expected):
    res = program.func1(testo)
    if res != expected:
        my_print(
            f'''{'*' * 50}\n[ERROR]Il valore ritornato non è corretto!\nReturned={res}\nExpected={expected}''')
        return 0
    return 1

def test_func1_1(run=True):
    testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
    expected = {'s': 0.03, 'o': 0.05, 'p': 0.12, 'r': 0.07, 'a': 0.27, 'l': 0.07,
                'n': 0.03, 'c': 0.1, 'm': 0.02, 't': 0.03, 'e': 0.02}
    return do_func1_test(testo,expected)

def test_func1_2(run=True):
    testo = '''essere o non essere, questo è il dilemma: 
               se sia più nobile nella mente soffrire colpi di fionda e dardi d’atroce fortuna 
               o prender armi contro un mare d’affanni e, opponendosi, por loro fine? 
               morire, dormire; nient’altro; e con un sonno dire che poniamo fine al dolore 
               del cuore e ai mille tumulti naturali di cui è erede la carne: 
               è una conclusione da desiderarsi devotamente'''
    expected = {'e': 0.1, 's': 0.03, 'r': 0.06, 'o': 0.07, 'n': 0.06, 'q': 0.0, 'u': 0.02, 't': 0.03, 'è': 0.01, 'i': 0.06, 'l': 0.04, 'd': 0.04, 'm': 0.02, 'a': 0.05, 'p': 0.02, 'ù': 0.0, 'b': 0.0, 'f': 0.02, 'c': 0.02, 'h': 0.0, 'v': 0.0}
    return do_func1_test(testo,expected)


###############################################################################
# ----------------------------------- FUNC. 2 -------------------------------- #


def do_func2_tests(int_list, expected):
    res = program.func2(int_list)
    if res == None:
        return 0
    testlib.check_list(res, expected)
    return 0.5


def test_func2_1(run=True):
    lists = [[4, 4, 10, 4, 1, 10], [4, 2, 1], [1, 4]]
    expected = [10, 10, 2]
    ## We could use a decorator but could mess up things
    add_docstring(test_func2_1, locals())
    return do_func2_tests(lists, expected) if run else None

def test_func2_2(run=True):
    lists = [[-4, 5, 5, -1, 8, 6, -5, 3, 2, 3], [7, -7, -2, -3, -8, 2, 2, -3, -8, -5], [-10, -4, 4, -1, 7, 1, -8, -8, 1, -5]]
    expected = [8, 6, 5, 5, 4, 3, 3, 1, 1, -2, -3, -3, -7, -10]
    ## We could use a decorator but could mess up things
    add_docstring(test_func2_2, locals())
    return do_func2_tests(lists, expected) if run else None


def test_func2_3(run=True):
    lists = [[-4, 5, 5, -1, 8, 6, -5, 3, 2, 3], [7, -7, 5, -2,8, -3, -8, 2, 2, -3, -8, -5], [-10, -4, 4, -1, 7, 1,5,8, -8, -8, 1, -5]]
    expected = [6, 4, 3, 3, 1, 1, -2, -3, -3, -7, -10]
    ## We could use a decorator but could mess up things
    add_docstring(test_func2_3, locals())
    return do_func2_tests(lists, expected) if run else None


def test_func2_4(run=True):
    lists = [[36, -92, 12, 42, 89, -63, -52, 8, 38, 12, -3, 6, -80, 57, 83, -43, 69, -19, -25, 65],
             [-63, 6, 12, 38, 89, -19, -25, 36, -43, -3, -92, 57, 12, 8, 42, 69, -52, -80, 65, 83],
             [69, 12, -43, 6, 57, 89, 36, -92, 42, -52, -19, -3, 12, -25, 83, -80, 65, 38, 8, -63]]
    expected = []
    ## We could use a decorator but could mess up things
    add_docstring(test_func2_4, locals())
    return do_func2_tests(lists, expected) if run else None


###############################################################################
# ----------------------------------- FUNC. 3 -------------------------------- #

def do_func3_tests(ID, expected):
    input_filename    = f'func3/in_{ID}.txt'
    output_filename   = f'func3/your_output_{ID}.txt'
    expected_filename = f'func3/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func3(input_filename, output_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 1


def test_func3_1(run=True):
    '''
    textfile_in  = 'func3/in_1.txt'
    textfile_out = 'func3/your_output_1.txt'
    expected     = 'func3/expected_1.txt'
    '''
    ID = 1
    expected = (236, 93)
    return do_func3_tests(ID, expected)

def test_func3_2(run=True):
    '''
    textfile_in  = 'func3/in_2.txt'
    textfile_out = 'func3/your_output_2.txt'
    expected     = 'func3/expected_2.txt'
    '''
    ID = 2
    expected = (1308, -1002)
    return do_func3_tests(ID, expected)

def test_func3_3(run=True):
    '''
    textfile_in  = 'func3/in_3.txt'
    textfile_out = 'func3/your_output_3.txt'
    expected     = 'func3/expected_3.txt'
    '''
    ID = 3
    expected = (1230, 1483)
    return do_func3_tests(ID, expected)

def test_func3_4(run=True):
    '''
    textfile_in  = 'func3/in_4.txt'
    textfile_out = 'func3/your_output_4.txt'
    expected     = 'func3/expected_4.txt'
    '''
    ID = 4
    expected = (3706, 107)
    return do_func3_tests(ID, expected)


###############################################################################
# ----------------------------------- FUNC. 4 -------------------------------- #



def do_func4_tests(str1, str2, expected):
    res = program.func4(str1, str2)
    testlib.check_dict(res, expected)
    return 0.5


def test_func4_1(run=True):
    '''
    S1 = {'a', 'b', 'c', 'e'}
    S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
    expected = {'a': ['ab', 'aa', 'abc'], 'c': ['cd', 'cc', 'bc', 'abc'], 'b': ['bc', 'bb', 'ab', 'abc']}
    '''
    S1 = {'a', 'b', 'c', 'e'}
    S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
    expected = {'a': ['abc', 'aa', 'ab'], 'b': ['abc', 'ab', 'bb', 'bc'], 'c': ['abc', 'bc', 'cc', 'cd']}
    return do_func4_tests(S1, S2, expected)

def test_func4_2(run=True):
    '''
    S1 = {'pros', 'jum', 'r', 'on', 'p', 'i', 'ove', 'te', 'ex', 're'}
    S2 = {'temple', 'webinar', 'atelier', 'rid', 'beast', 'prosecution', 'eponym', 'cenotaph', 'reservation', 'onset'}
    expected = {'p': ['temple', 'eponym', 'cenotaph', 'prosecution'], 'pros': ['prosecution'], 're': ['reservation'], 'te': ['temple', 'atelier'], 'on': ['onset', 'eponym', 'reservation', 'prosecution'], 'r': ['rid', 'webinar', 'atelier', 'reservation', 'prosecution'], 'i': ['rid', 'webinar', 'atelier', 'reservation', 'prosecution']}
    '''
    S1 = {'pros', 'jum', 'r', 'on', 'p', 'i', 'ove', 'te', 'ex', 're'}
    S2 = {'temple', 'webinar', 'atelier', 'rid', 'beast', 'prosecution', 'eponym', 'cenotaph', 'reservation', 'onset'}
    expected = {'te': ['atelier', 'temple'], 'on': ['prosecution', 'reservation', 'eponym', 'onset'], 'p': ['prosecution', 'cenotaph', 'eponym', 'temple'], 'i': ['prosecution', 'reservation', 'atelier', 'webinar', 'rid'], 're': ['reservation'], 'pros': ['prosecution'], 'r': ['prosecution', 'reservation', 'atelier', 'webinar', 'rid']}
    return do_func4_tests(S1, S2, expected)

def test_func4_3(run=True):
    '''
    S1 = {'ma', 't', 's', 'st', 'rec', 'm', 'cro', 'T', 'w', 'ch', 'ou', 'cra', 'ow', 'fur', 'wis', 'han', 'sno', 'c', 'rid', 'te'}
    S2 = {'hand-holding', 'messy', 'commander', 'earring', 'effect', 'chem', 'stitch', 'madam', 'motel', 'snowman', 'charter', 'walnut', 'crotch', 'furnace', 'handover', 'gloom', 'cloudy', 'territory', 'moldy', 'collector'}
    expected = {'han': ['handover', 'hand-holding'], 'te': ['motel', 'charter', 'territory'], 'ma': ['madam', 'snowman', 'commander'], 'm': ['chem', 'motel', 'moldy', 'messy', 'madam', 'gloom', 'snowman', 'commander'], 'c': ['chem', 'stitch', 'effect', 'crotch', 'cloudy', 'furnace', 'charter', 'commander', 'collector'], 'cro': ['crotch'], 'sno': ['snowman'], 'fur': ['furnace'], 'ou': ['cloudy'], 'ch': ['chem', 'stitch', 'crotch', 'charter'], 'st': ['stitch'], 't': ['motel', 'walnut', 'stitch', 'effect', 'crotch', 'charter', 'territory', 'collector'], 'ow': ['snowman'], 's': ['messy', 'stitch', 'snowman'], 'w': ['walnut', 'snowman']}
    '''
    S1 = {'ma', 't', 's', 'st', 'rec', 'm', 'cro', 'T', 'w', 'ch', 'ou', 'cra', 'ow', 'fur', 'wis', 'han', 'sno', 'c', 'rid', 'te'}
    S2 = {'hand-holding', 'messy', 'commander', 'earring', 'effect', 'chem', 'stitch', 'madam', 'motel', 'snowman', 'charter', 'walnut', 'crotch', 'furnace', 'handover', 'gloom', 'cloudy', 'territory', 'moldy', 'collector'}
    expected = {'fur': ['furnace'], 'sno': ['snowman'], 'ou': ['cloudy'], 'ma': ['commander', 'snowman', 'madam'], 'ch': ['charter', 'crotch', 'stitch', 'chem'], 'st': ['stitch'], 'ow': ['snowman'], 'c': ['collector', 'commander', 'charter', 'furnace', 'cloudy', 'crotch', 'effect', 'stitch', 'chem'], 't': ['collector', 'territory', 'charter', 'crotch', 'effect', 'stitch', 'walnut', 'motel'], 'te': ['territory', 'charter', 'motel'], 'w': ['snowman', 'walnut'], 's': ['snowman', 'stitch', 'messy'], 'han': ['hand-holding', 'handover'], 'cro': ['crotch'], 'm': ['commander', 'snowman', 'gloom', 'madam', 'messy', 'moldy', 'motel', 'chem']}
    return do_func4_tests(S1, S2, expected)

def test_func4_4(run=True):
    '''
    S1 = {'gh', 'pla', 'eco', 'c', 'n', 'st', 'loa', 'ga', 'ad', 'con', 'alt', 'imi', 'w', 'bi', 'agg', 'r', 'f', 'em', 'wet', 't', 'of', 'gl', 'ho', 'h', 'p', 'suc', 'iso'}
    S2 = {'cooking', 'offering', 'wooden', 'void', 'disclosure', 'home', 'knit', 'altitude', 'wick', 'policeman', 'patty', 'stack', 'catch', 'living', 'cleavage', 'achievement', 'buck', 'drill', 'hygienic', 'storey', 'tab', 'planet', 'soul', 'bind', 'pail', 'success', 'devastation', 'behest', 'contention', 'fantastic'}
    expected = {'suc': ['success'], 'n': ['knit', 'bind', 'wooden', 'planet', 'living', 'cooking', 'offering', 'hygienic', 'policeman', 'fantastic', 'contention', 'devastation', 'achievement'], 't': ['tab', 'knit', 'stack', 'patty', 'catch', 'storey', 'planet', 'behest', 'altitude', 'fantastic', 'contention', 'devastation', 'achievement'], 'con': ['contention'], 'alt': ['altitude'], 'of': ['offering'], 'st': ['stack', 'storey', 'behest', 'fantastic', 'devastation'], 'c': ['wick', 'buck', 'stack', 'catch', 'success', 'cooking', 'hygienic', 'cleavage', 'policeman', 'fantastic', 'disclosure', 'contention', 'achievement'], 'r': ['drill', 'storey', 'offering', 'disclosure'], 'ho': ['home'], 'pla': ['planet'], 'p': ['pail', 'patty', 'planet', 'policeman'], 'f': ['offering', 'fantastic'], 'bi': ['bind'], 'w': ['wick', 'wooden'], 'em': ['policeman', 'achievement'], 'h': ['home', 'catch', 'behest', 'hygienic', 'achievement']}
    '''
    S1 = {'gh', 'pla', 'eco', 'c', 'n', 'st', 'loa', 'ga', 'ad', 'con', 'alt', 'imi', 'w', 'bi', 'agg', 'r', 'f', 'em', 'wet', 't', 'of', 'gl', 'ho', 'h', 'p', 'suc', 'iso'}
    S2 = {'cooking', 'offering', 'wooden', 'void', 'disclosure', 'home', 'knit', 'altitude', 'wick', 'policeman', 'patty', 'stack', 'catch', 'living', 'cleavage', 'achievement', 'buck', 'drill', 'hygienic', 'storey', 'tab', 'planet', 'soul', 'bind', 'pail', 'success', 'devastation', 'behest', 'contention', 'fantastic'}
    expected = {'suc': ['success'], 'n': ['achievement', 'devastation', 'contention', 'fantastic', 'policeman', 'hygienic', 'offering', 'cooking', 'living', 'planet', 'wooden', 'bind', 'knit'], 'h': ['achievement', 'hygienic', 'behest', 'catch', 'home'], 'st': ['devastation', 'fantastic', 'behest', 'storey', 'stack'], 'ho': ['home'], 'con': ['contention'], 'alt': ['altitude'], 'f': ['fantastic', 'offering'], 'r': ['disclosure', 'offering', 'storey', 'drill'], 'c': ['achievement', 'contention', 'disclosure', 'fantastic', 'policeman', 'cleavage', 'hygienic', 'cooking', 'success', 'catch', 'stack', 'buck', 'wick'], 'pla': ['planet'], 'em': ['achievement', 'policeman'], 'of': ['offering'], 't': ['achievement', 'devastation', 'contention', 'fantastic', 'altitude', 'behest', 'planet', 'storey', 'catch', 'patty', 'stack', 'knit', 'tab'], 'w': ['wooden', 'wick'], 'p': ['policeman', 'planet', 'patty', 'pail'], 'bi': ['bind']}
    return do_func4_tests(S1, S2, expected)


###############################################################################
# ----------------------------------- FUNC. 5 -------------------------------- #

def do_test_func5(ID, expected):
    png_in  = f'func5/in_{ID:02}.png'
    res = program.func5(png_in)
    testlib.check_dict(res, expected)
    return 2

def test_func5_1(run=True):
    ID = 1
    expected = {(28, 33, 221): 1, (187, 0, 0): 1, (187, 177, 0): 1, (191, 190, 186): 1, (0, 255, 7): 1}
    add_docstring(test_func5_1, locals())  
    return do_test_func5(ID, expected) if run else None


def test_func5_2(run=True):
    ID = 2
    expected = {(254, 254, 254): 4, (230, 230, 230): 4, (175, 175, 175): 4, (255, 0, 234): 2}
    add_docstring(test_func5_2, locals())  
    return do_test_func5(ID, expected) if run else None


def test_func5_3(run=True):
    ID = 3
    expected = {(48, 26, 6): 1, (90, 231, 162): 1, (117, 100, 100): 1, (76, 138, 67): 1, (135, 170, 79): 1, (100, 34, 145): 1, (167, 190, 185): 1, (95, 86, 54): 1, (111, 32, 126): 1}
    add_docstring(test_func5_3, locals())  
    return do_test_func5(ID, expected) if run else None

def test_func5_4(run=True):
    ID = 4
    expected = {(42, 210, 206): 1, (84, 87, 21): 1, (48, 26, 6): 1, (122, 120, 92): 1, (117, 100, 100): 1, (76, 138, 67): 1, (173, 45, 45): 1, (45, 59, 173): 1, (135, 170, 79): 1, (47, 51, 82): 1, (100, 34, 145): 1, (167, 190, 185): 1, (95, 86, 54): 1, (210, 42, 169): 1, (111, 32, 126): 1}
    add_docstring(test_func5_4, locals())  
    return do_test_func5(ID, expected) if run else None


###############################################################################
# ----------------------------------- EX. 1 -------------------------------- #

def do_ex1_test(root, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(root)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("[ERROR] The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    res = program.ex1(root)
    testlib.check_val(res, expected)
    return 2


def test_ex1_1(run=True):
    '''
        ______20_____      
       |             |     
      15__        ___1___  
          |      |       | 
          -2    11       4
    '''

    root = tree.BinaryTree.fromList([20, [15,None,[-2,None,None]],
    [1, [11,None,None], [4,None,None]]])
    expected = 33
    return do_ex1_test(root, expected)


def test_ex1_2(run=True):
    '''
         ______13_____           level 1
        |             |           
     ___7___        ___10___     level 2
     |      |      |        |
   _-5_    -1_    _9_      _3_   level 3    
  |    |      |  |   |    |   |
-10    4      6  5  -2    -6  2  level 4 
    '''
    root = tree.BinaryTree.fromList([13,
    [7,[-5,[-10,None,None],[4,None,None]],[-1,None,[6,None,None]]],
    [10, [9,[5,None,None],[-2,None,None]],
     [3,[-6,None,None],[2,None,None]]]])
    expected = 27
    return do_ex1_test(root, expected)


def test_ex1_3(run=True):
    '''
      A big tree
    '''
    root = tree.BinaryTree.fromList([4, [-9, [14, [11, [11, [22, [7, None, None], [21, None, None]],
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
    expected = 261
    return do_ex1_test(root, expected)


###############################################################################
# ----------------------------------- EX. 2 -------------------------------- #

def do_ex2_test(I, m, M, expected, score=2):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(I.copy(), m, M)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    res = program.ex2(I.copy(), m, M)
    testlib.check_list(res, expected)
    return score


def test_ex2_1(run=True):
    I, m, M = ({1, 2, 3, 7}, 1, 15)
    expected = [1, 2, 3, 6, 7, 14]
    add_docstring(test_ex2_1, locals())
    return do_ex2_test(I, m, M, expected) if run else None


def test_ex2_2(run=True):
    I, m, M = ({2,3,4,5,6}, 5, 50)
    expected = [5, 6, 8, 10, 12, 15, 18, 20, 24, 30, 36, 40, 48]
    add_docstring(test_ex2_2, locals())
    return do_ex2_test(I, m, M, expected) if run else None

def test_ex2_3(run=True):
    I, m, M = ({10, 100, 1000, 10000}, 10**3, 10**6)
    expected = [1000, 10000, 100000, 1000000]
    add_docstring(test_ex2_2, locals())
    return do_ex2_test(I, m, M, expected) if run else None


def test_ex2_4(run=True):
    I, m, M = ({0, 1, 2, 3, 4, 5, 6}, 1, 100)
    expected = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20, 24, 30, 36, 40, 48, 60, 72, 90]
    add_docstring(test_ex2_1, locals())
    return do_ex2_test(I, m, M, expected) if run else None






################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
                                                               
    test_func1_1, test_func1_2,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,  test_ex2_2, test_ex2_3, test_ex2_4,
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(tests,
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

# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected

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
DEBUG = True
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

# ----------------------------------- FUNC. 1 --------------------------------
def do_func1_tests(S, D, expected):
    res = program.func1(S, D)
    testlib.check_dict(res, expected)
    return .5

def test_func1_1(run=True):
    S = {2, 3, 55, 4, 11}
    D = {11:'a', 88:'b', 66:'c', 2:'d', 100:'e', 5:'f'}

    expected =  {2:'e', 3:'c', 55:'a', 4:'e', 11:'b'}
    add_docstring(test_func1_1, locals())
    return do_func1_tests(S, D, expected) if run else None


def test_func1_2(run=True):
   S = {18, 19, 69, 83, 8}
   D = {76: '^', 62: 'M', 59: 'w', 22: 'y', 82: ']', 10: 'E', 25: 'u', 13: 'R', 66: 'O', 2: 'l'}
   expected =  {18: 'l', 19: '^', 8: 'l'}
   add_docstring(test_func1_2, locals())
   return do_func1_tests(S, D, expected) if run else None

def test_func1_3(run=True):
    S = {31, 36, 37, 44, 47, 49, 63, 86, 88, 95}
    D = {45: 'P', 43: 'v', 23: '`', 9: '[', 63: 'O', 79: 'y', 91: 'j', 65: 'w', 37: ']', 24: 'H', 34: 'w', 42: 'r', 10: 'O', 30: 'o', 92: '^', 74: 'o', 93: 'o', 5: 'l'}
    expected = {36: '[', 37: 'o', 86: 'v', 31: 'o', 95: 'l', 63: 'O'}
    add_docstring(test_func1_3, locals())
    return do_func1_tests(S, D, expected) if run else None


def test_func1_4(run=True):
    S = {7, 10, 11, 22, 26, 32, 38, 61, 66}
    D = {37: 'T', 40: 'z', 23: 'y', 32: '`', 47: 'Y', 93: '[', 44: 'q', 30: 'J', 74: 'Z', 5: '\\', 29: 'S', 50: 'R', 8: 'Z', 25: 'k', 15: 'w', 39: 'G', 66: 'z', 90: 'o', 11: 'K', 91: 'D', 3: 'H', 89: 'J', 53: 'i', 84: 'S', 41: 'P', 21: ']', 36: 'b', 65: 'f', 59: 'Q', 73: 't', 95: 'f', 85: 'Z', 55: 'D', 27: 's', 19: 'j', 20: 'o', 43: 'O', 86: 'D', 70: 'w', 38: 'e'}
    expected = {32: '`', 66: 'z', 38: 'e', 7: 'D', 10: 'o', 11: 'z', 22: 'z'}
    add_docstring(test_func1_4, locals())
    return do_func1_tests(S, D, expected) if run else None

# ----------------------------------- FUNC. 2 --------------------------------

def do_func2_tests(L, expected):
    res = program.func2(L)
    testlib.check_val(res, expected)
    return 1
        


def test_func2_1(run=True):
    L = ['xx', 'asd', 'qwe', 'bb', 'cc', 'fond']
    expected = ['asdqwe', 'xxbbcc', 'fond']
    add_docstring(test_func2_1, locals())
    return do_func2_tests(L, expected) if run else None


def test_func2_2(run=True):
    L = ['cat', 'best', 'dog', 'bird', 'bye', 'bye', 'frog', 'muscle']
    expected = ['bestbirdfrog', 'catdogbyebye', 'muscle']
    add_docstring(test_func2_2, locals())
    return do_func2_tests(L, expected) if run else None


def test_func2_3(run=True):
    L = ["testy", "abacus", "scissors", "sulfur", "semicolon", "blowgun", "ziggurat", "loud", "charset", "mow", "spud", "yogurt", "learn", "analysis", "ill", "sorrow", "avenue", "brother", "backbone", "optimisation", "tavern", "hip", "airbus", "socialism", "engineer", "tussle", "ceaseless"]
    expected = ['abacussulfuryogurtsorrowavenuetavernairbustussle', 'scissorszigguratanalysisbackboneengineer', 'semicolonsocialismceaseless', 'blowguncharsetbrother', 'optimisation', 'testylearn', 'mowillhip', 'loudspud']
    add_docstring(test_func2_3, locals())
    return do_func2_tests(L, expected) if run else None

# ----------------------------------- FUNC. 3 --------------------------------

def do_func3_tests(strings, tuples, expected):
    res = program.func3(strings, tuples)
    testlib.check_val(res, expected)
    return 0.5

def test_func3_1(run=True):
    strings = [['works', 'is'], ['science', 'magic'], ['that']] 
    tuples = [(1,0), (0,1), (1,1), (2,0), (0,0)]
    expected = 'science is magic that works'
    add_docstring(test_func3_1, locals())
    return do_func3_tests(strings, tuples, expected) if run else None


def test_func3_2(run=True):
    strings = [['magic', 'Any'], ['technology','indistinguishable','is','from'], ['advanced', 'sufficiently']]
    tuples = [(0,1), (2,1), (2,0), (1,0), (1,2), (1,1),(1,3),(0,0)]
    expected = 'Any sufficiently advanced technology is indistinguishable from magic'
    add_docstring(test_func3_2, locals())
    return do_func3_tests(strings, tuples, expected) if run else None

def test_func3_3(run=True):
    strings = [["semicolon", "blowgun", "ziggurat", "loud", "charset", "mow", "spud"], ["yogurt", "learn"], ["analysis"], ["ill", "sorrow", "avenue"]]
    tuples = [(1, 1), (2, 0), (1, 1), (3, 1), (0, 3), (1, 0), (0, 0), (0, 1), (3, 2), (0, 6), (0, 2), (0, 5), (1, 0), (0, 4), (3, 0)]
    expected = 'learn analysis learn sorrow loud yogurt semicolon blowgun avenue spud ziggurat mow yogurt charset ill'
    add_docstring(test_func3_3, locals())
    return do_func3_tests(strings, tuples, expected) if run else None


def test_func3_4(run=True):
    strings = [["testy", "abacus", "scissors", "sulfur", "semicolon", "blowgun", "ziggurat"], ["loud", "charset", "mow", "spud", "yogurt", "learn", "analysis"], ["ill", "sorrow", "avenue", "brother", "backbone", "optimisation", "tavern", "hip"], ["airbus", "socialism", "engineer", "tussle", "ceaseless"]]
    tuples = [(1, 1), (3, 0), (2, 4), (2, 1), (2, 2), (1, 5), (2, 0), (3, 1), (2, 6), (1, 3), (1, 4), (0, 0), (3, 2), (1, 0), (2, 7), (1, 2), (0, 3), (0, 1), (2, 5), (0, 4), (3, 4), (0, 6), (3, 3), (1, 6), (2, 3), (0, 2), (0, 5)]
    expected = 'charset airbus backbone sorrow avenue learn ill socialism tavern spud yogurt testy engineer loud hip mow sulfur abacus optimisation semicolon ceaseless ziggurat tussle analysis brother scissors blowgun'
    add_docstring(test_func3_4, locals())
    return do_func3_tests(strings, tuples, expected) if run else None

# ----------------------------------- FUNC. 4 --------------------------------

def do_func4_tests(ID, expected):
    input_filename  = f'func4/in_0{ID}.txt'
    output_filename = f'func4/out_0{ID}.txt'
    expected_filename = f'func4/exp_0{ID}.txt'
    # tolgo output ogni volta
    if os.path.exists(output_filename): os.remove(output_filename)
    res = program.func4(input_filename, output_filename)
    testlib.check_val(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1(run=True):
    ID = 1
    expected = 'qerTY4'
    add_docstring(test_func4_1, locals())
    return do_func4_tests(ID, expected) if run else None


def test_func4_2(run=True):
    ID = 2
    expected = '5LOXVV44eW1k'
    add_docstring(test_func4_2, locals())
    return do_func4_tests(ID, expected) if run else None


def test_func4_3(run=True):
    ID = 3
    expected = 'WZT2znEeL7nilf'
    add_docstring(test_func4_3, locals())
    return do_func4_tests(ID, expected) if run else None

# ----------------------------------- FUNC. 5 --------------------------------

def do_test_func5(ID, expected):
    input_filenames  = [f'func5/{ID}/in_{ID}_1.png', f'func5/{ID}/in_{ID}_2.png', f'func5/{ID}/in_{ID}_3.png']
    output_filename = f'func5/{ID}/out_{ID}.png'
    expected_filename = f'func5/{ID}/exp_{ID}.png'
    # tolgo output ogni volta
    if os.path.exists(output_filename): os.remove(output_filename)
    res = program.func5(input_filenames, output_filename)
    testlib.check_val(res, expected)
    testlib.check_img_file(output_filename, expected_filename)
    if res == expected:
        return 3 if ID == 2 else 2
    else:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0


def test_func5_1(run=True):
    ID = 1
    expected = (40, 90)
    add_docstring(test_func5_1, locals())  
    return do_test_func5(ID, expected) if run else None


def test_func5_2(run=True):
    ID = 2
    expected = (150, 205)
    add_docstring(test_func5_2, locals())  
    return do_test_func5(ID, expected) if run else None


def test_func5_3(run=True):
    ID = 3
    expected = (181, 301)
    add_docstring(test_func5_3, locals())  
    return do_test_func5(ID, expected) if run else None


# ----------------------------------- EX.1 ----------------------------------- #

def do_ex1_test(root, root2, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(root, root2)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("[ERROR] The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    res = program.ex1(root, root2)
    if res is None:
        return 0
    if res == expected:
        return 2
    else:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    return 0


def test_ex1_1(run=True):
    '''
               root1                                 root2

        ______A______       level 0          ______A______
       |             |                      |             |
       B__        ___C___   level 1         X__        ___C___
          |      |       |                     |      |       |
          D      E       F  level 2            Y      F       G 
    '''

    root = tree.BinaryTree.fromList(['A', ['B',None,['D',None,None]],
    ['C', ['E',None,None], ['F',None,None]]])
    root2 = tree.BinaryTree.fromList(['A', ['X',None,['Y',None,None]],
    ['C', ['F',None,None], ['G',None,None]]])

    expected = [(1, 'B', 'X'), (2, 'F', 'G'), (2, 'E', 'F'), (2, 'D', 'Y')]
    return do_ex1_test(root, root2, expected)


def test_ex1_2(run=True):
    '''
                    root1                                   root2
                ______A______                           ______A______ 
               |             |                         |             | 
        ______ B______   ____C_____             _____ B______   _____C_____  
       |             |  |          |           |             |  |           |  
    __D__          __E   __F__    __G__      __D__         __E   __F__     __G__  
   |     |          |   |     |  |     |    |     |         |   |     |   |     |  
   H     I          J   K     L  M     N    I     J         K   L     M   N     Z  
    '''
    
    root = tree.BinaryTree.fromList(['A',
    ['B',['D',['H',None,None],['I',None,None]],['E',None,['J',None,None]]],
    ['C', ['F',['K',None,None],['L',None,None]],
     ['G',['M',None,None],['N',None,None]]]])
    
    root2 = tree.BinaryTree.fromList(['A',
    ['B',['D',['I',None,None],['J',None,None]],['E',None,['K',None,None]]],
    ['C', ['F',['L',None,None],['M',None,None]],
     ['G',['N',None,None],['Z',None,None]]]])

    expected = [(3, 'N', 'Z'), (3, 'M', 'N'), (3, 'L', 'M'), (3, 'K', 'L'), (3, 'J', 'K'), (3, 'I', 'J'), (3, 'H', 'I')]
    return do_ex1_test(root, root2, expected)


def test_ex1_3(run=True):
    '''
              root 1
           ______A______
          |             |
       __ A__        ___A___
      |      |      |       |
     _B      B_    _B       B_
    |          |  |           |
   _C          C  C           C_
  |                             |
  D                             D

              root 2
           ______X______
          |             |
       __ X__        ___X___
      |      |      |       |
     _B      B_    _B       B_
    |          |  |           |
   _Z          w  z           e_
  |                             |
  T                             y

    '''
    root = tree.BinaryTree.fromList(['A', ['A',['B',['C',['D',None,None],None],None],
                                               ['B',None,['C',None,None]]],
                                          ['A', ['B',['C',None,None],None],['B',None,['C',None,['D',None,None]]]]])
    
    root2 = tree.BinaryTree.fromList(['X', ['X',['B',['e',['y',None,None],None],None],
                                               ['B',None,['z',None,None]]],
                                          ['X', ['B',['w',None,None],None],['B',None,['Z',None,['T',None,None]]]]])

    expected = [(0, 'A', 'X'), (1, 'A', 'X'), (1, 'A', 'X'), (3, 'C', 'Z'), (3, 'C', 'e'), (3, 'C', 'w'), (3, 'C', 'z'), (4, 'D', 'T'), (4, 'D', 'y')]
    return do_ex1_test(root, root2, expected)


# ----------------------------------- EX. 2----------------------------------- #
# ----------------------------------- EX.2 ----------------------------------- #
def do_ex2_test(directory, words, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(directory, words)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(directory, words)
    if res is None: return 0
    if res == expected:
        my_print(f'[OK]La lista ritornata è corretta! / The returned list is correct!!')
        return 2
    if set(res) == set(expected):
        my_print(f'[OK]I valori ritornati sono corretti ma non nell\'ordine giusto! / The returned values are correct but in the wrong order!!')
        return 1
    my_print(
        f'''{'*' * 50}\n[ERROR]La lista ritornata non è corretta! / The returned list is incorrect!!\nReturned={res}, expected={expected}''')
    return 0


def test_ex2_1(run=True):
    directory = 'ex2'
    words = ["cat", "dog"]
    expected = [('dog', 10), ('cat', 5)]
    add_docstring(test_ex2_1, locals()) 
    return do_ex2_test(directory, words, expected)


def test_ex2_2(run=True):
    directory = 'ex2/A'
    words = ["gnu", "cat", "fish"]
    expected = [('cat', 3), ('fish', 3),  ('gnu', 1)]
    add_docstring(test_ex2_2, locals()) 
    return do_ex2_test(directory, words, expected)


def test_ex2_3(run=True):
    directory = 'ex2'
    words = ["bird", "dog", "gnu", "tuna"][::-1]
    expected = [('dog', 10), ('bird', 8), ('tuna', 2), ('gnu', 1)]
    add_docstring(test_ex2_3, locals()) 
    return do_ex2_test(directory, words, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
                                                               
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3,
    test_ex1_1,  test_ex1_2,    test_ex1_3,
    test_ex2_1,  test_ex2_2, test_ex2_3,
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

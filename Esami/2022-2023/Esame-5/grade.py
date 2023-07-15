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
def do_func1_tests(list_a, list_b, list_c, expected):
    res = program.func1(list_a, list_b, list_c)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista risultante è {expected} e non {res}. / The expected list is {expected}, but {res} were returned.\n {'*'*50}''')
        return 0
    testlib.checkList(res, expected)
    return 0.5


def test_func1_2():
    '''
    list_a = ['pippo', 'pluto', 'minnie', 'pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pippo', 'pluto', 'gastone', 'pippo', 'analecto']
    expected = ['pippo']
    '''
    list_a = ['pippo', 'pluto', 'minnie', 'pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pippo', 'pluto', 'gastone', 'pippo', 'analecto']
    expected = ['pippo']
    return do_func1_tests(list_a, list_b, list_c, expected)

def test_func1_1():
    '''
    list_a = ['pippo', 'pluto', 'minnie', 'minnie','pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pippo', 'pluto', 'gastone', 'pippo', 'analecto','minnie']
    expected = ['minnie', 'pippo']
    '''
    list_a = ['pippo', 'pluto', 'minnie', 'minnie','pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pippo', 'pluto', 'gastone', 'pippo', 'analecto','minnie']
    expected = ['minnie', 'pippo']
    return do_func1_tests(list_a, list_b, list_c, expected)


def test_func1_3():
    '''
    list_a = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    expected = ['analecto', 'gambadilegno', 'minnie', 'pippo']
    '''
    list_a = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    expected = ['analecto', 'gambadilegno', 'minnie', 'pippo']
    return do_func1_tests(list_a, list_b, list_c, expected)

def test_func1_4():
    '''
    list_a = ['pippo', 'pluto', 'minnie', 'pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pluto', 'gastone', 'paperoga', 'analecto']
    expected = []
    '''
    list_a = ['pippo', 'pluto', 'minnie', 'pippo']
    list_b = ['analecto', 'pippo', 'gambadilegno', 'minnie', 'pippo']
    list_c = ['pluto', 'gastone', 'paperoga', 'analecto']
    expected = []
    return do_func1_tests(list_a, list_b, list_c, expected)

# %% ----------------------------------- FUNC2 ------------------------- #
def do_func2_tests(d1, d2, expected):
    res = program.func2(d1, d2)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La stringa restituita non è corretta / The returned string is incorrect\n[ERROR] expected={expected} returned={res}.\n {'*'*50}''')
        return 0
    testlib.checkDict(res, expected)
    return 0.5


def test_func2_1():
    '''
    d1 = {'pippo': [5, 2,],
          'pluto': [1, 2, 3],
          'gastone': [50, 50 ]}
    d2 = {'gastone': [5, 23, 2],
          'paperino': [3, 2, 1],
          'pluto': [10, -1]}

    expected = {'gastone': [50, 50, 5, 23, 2], 'pluto': [1, 2, 3, 10, -1]}
    '''
    d1 = {'pippo': [5, 2,],
          'pluto': [1, 2, 3],
          'gastone': [50, 50 ]}
    d2 = {'gastone': [5, 23, 2],
          'paperino': [3, 2, 1],
          'pluto': [10, -1]}

    expected = {'gastone': [50, 50, 5, 23, 2], 'pluto': [1, 2, 3, 10, -1]}
    return do_func2_tests(d1, d2, expected)

def test_func2_2():
    '''
    d1 = {'pippo': [5, 23, 2, 3, 5],
          'pluto': [1, 2, 3],
          'gastone': [50, ]*7}
    d2 = {'gastone': [5, 23, 2, 3, 5],
          'paperino': [3, 2, 1],
          'pluto': [10, 10, -1]}

    expected = {'gastone': [50, 50, 50, 50, 50, 50, 50, 5, 23, 2, 3, 5],
                'pluto': [1, 2, 3, 10, 10, -1]}
    '''
    d1 = {'pippo': [5, 23, 2, 3, 5],
          'pluto': [1, 2, 3],
          'gastone': [50, ]*7}

    d2 = {'gastone': [5, 23, 2, 3, 5],
          'paperino': [3, 2, 1],
          'pluto': [10, 10, -1]}

    expected = {'gastone': [50, 50, 50, 50, 50, 50, 50, 5, 23, 2, 3, 5],
                'pluto': [1, 2, 3, 10, 10, -1]}
    return do_func2_tests(d1, d2, expected)

def test_func2_3():
    '''
    d1 = {'pippo': [5, 23, 2, 3, 5],
          'pluto': [1, 2, 3],
          'gastone': [50, ]*7}
    d2 = {'paperoga': [5, 23, 2, 3, 5],
          'topolino': [3, 2, 1],
          'minnie': [10, 10, -1]}

    expected = {}
    '''
    d1 = {'pippo': [5, 23, 2, 3, 5],
          'pluto': [1, 2, 3],
          'gastone': [50, ]*7}

    d2 = {'paperoga': [5, 23, 2, 3, 5],
          'topolino': [3, 2, 1],
          'minnie': [10, 10, -1]}

    expected = {}
    return do_func2_tests(d1, d2, expected)

def test_func2_4():
    '''
    d1 = {'pippo': [5, 23, 2, 3, 5],
          'pluto': [1, 2, 3],
          'gastone': [50, ]*7,
          'paperoga': [5, 23, 2, 3, 5],
          'topolino': [3, 2, 1],
          'minnie': [10, 10, -1]}
    d2 = {'paperoga': [5, 23, 2, 3, 5],
          'topolino': [3, 2, 1],
          'minnie': [10, 10, -1]}

    expected = {'minnie': [10, 10, -1, 10, 10, -1], 'paperoga': [5, 23, 2, 3, 5, 5, 23, 2, 3, 5], 'topolino': [3, 2, 1, 3, 2, 1]}
    '''
    d1 = {'pippo': [5, 23, 2, 3, 5],
          'pluto': [1, 2, 3],
          'gastone': [50, ]*7,
          'paperoga': [5, 23, 2, 3, 5],
          'topolino': [3, 2, 1],
          'minnie': [10, 10, -1]}

    d2 = {'paperoga': [5, 23, 2, 3, 5],
          'topolino': [3, 2, 1],
          'minnie': [10, 10, -1]}

    expected = {'minnie': [10, 10, -1, 10, 10, -1], 'paperoga': [5, 23, 2, 3, 5, 5, 23, 2, 3, 5], 'topolino': [3, 2, 1, 3, 2, 1]}
    return do_func2_tests(d1, d2, expected)


# %% ----------------------------------- FUNC3 ------------------------- #
def do_func3_tests(string_list1, string_list2, expected):
    res = program.func3(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 2/3


def test_func3_1():
    '''
    string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
    string_list2=['ce', 'cas', 'too', 'ceo', 'sia']
    expected = ['SIA', 'TOO', 'cAs', 'ceo', 'cE']
    '''
    string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
    string_list2=['ce', 'cas', 'too', 'ceo', 'sia']
    expected = ['SIA', 'TOO', 'cAs', 'ceo', 'cE']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_2():
    '''
    string_list1=['A']
    string_list2=['A']
    '''
    string_list1=['AAA', 'fkjskfjsdkABCHGHF', '']
    string_list2=['bbb', 'BBBBBBBBBBcmcmcmmc' '']
    expected = ['bbbbbbbbbbCMCMCMM', 'BBB']
    return do_func3_tests(string_list1, string_list2, expected)

def test_func3_3():
    '''
    string_list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    string_list2=['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    '''
    string_list1=['a', 'b', 'c', 'd', 'e', 'F', 'G', 'H', 'I', 'J']
    string_list2=['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    expected =  ['A', 'B', 'C', 'D', 'E', 'f', 'g', 'h', 'i', 'j']
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
    expected = 9
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_file = func4/func4_test2.txt
    output_file = func4/func4_out2.txt
    '''
    ID = 2
    expected = 10
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_file = func4/func4_test3.txt
    output_file = func4/func4_out3.txt
    '''
    ID = 3
    expected = 32
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
    expected = [(6, 8, 11), (18, 11, 42), (33, 12, 18), (34, 19, 31)]
    return do_test_func5(ID, expected)


def test_func5_2():
    '''
    imm_in = func5/image02.png
    expected = [100, 400, 900, 1600, 2500]
    '''
    ID = 2
    expected = [(6, 8, 8), (49, 0, 49)]
    return do_test_func5(ID, expected)


def test_func5_3():
    '''
    imm_in = func5/image03.png
    expected = [2500]
    '''
    ID = 3
    expected = [(0, 0, 49), (1, 0, 49), (2, 0, 49), (3, 0, 49), (4, 0, 49), (5, 0, 49), (6, 0, 49), (49, 0, 49)]
    return do_test_func5(ID, expected)


def test_func5_4():
    '''
    imm_in = func5/image04.png
    expected = []
    '''
    ID = 4
    expected = [(0, 0, 49), (1, 0, 49), (2, 0, 49), (3, 0, 49), (4, 0, 49), (5, 0, 49), (6, 0, 49), (7, 25, 25), (8, 25, 25), (9, 25, 25), (10, 25, 25), (11, 25, 25), (12, 25, 25), (13, 25, 25), (14, 25, 25), (15, 25, 25), (16, 25, 25), (17, 25, 25), (18, 25, 25), (19, 25, 25), (20, 25, 25), (21, 25, 25), (22, 25, 25), (23, 25, 25), (24, 25, 25), (25, 25, 25), (26, 25, 25), (27, 25, 25), (28, 25, 25), (29, 25, 25), (30, 25, 25), (31, 25, 25), (32, 25, 25), (33, 25, 25), (34, 25, 25), (35, 25, 25), (36, 25, 25), (37, 25, 25), (38, 25, 25), (39, 25, 25), (40, 25, 25), (41, 25, 25), (42, 25, 25), (43, 25, 25), (44, 25, 25), (45, 25, 25), (46, 25, 25), (47, 25, 25), (48, 25, 25), (49, 0, 49)]
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
    testlib.checkList(res, expected)
    return 2

def test_ex1_1():
    '''
    directory = 'ex1/A'
    '''
    directory = 'ex1/A'
    expected = [('ex1/A/QBwXM/KVobU.txt', 19)]
    return do_test_ex1(directory, expected)


def test_ex1_2():
    '''
    directory = 'ex1/B'
    '''
    directory = 'ex1/B'
    expected =  [('ex1/B/NTeiT/EZDOA.txt', 11), ('ex1/B/OkUCm/MnoZY/AgwDD.txt', 13), ('ex1/B/XNbrp/nSlKw/IDpRs.txt', 15), ('ex1/B/XNbrp/fqAXO/GTFET.txt', 17), ('ex1/B/NTeiT/EdwAG.txt', 19), ('ex1/B/NTeiT/rwbme/eBCxC.txt', 19), ('ex1/B/OkUCm/MnoZY/RhPfc.txt', 19), ('ex1/B/OkUCm/RpnHv/zvNoP.txt', 19), ('ex1/B/OkUCm/jPNex.txt', 19), ('ex1/B/OkUCm/sNMOc/eIkqL.txt', 19), ('ex1/B/XNbrp/XOsqY/AdpBA.txt', 19), ('ex1/B/XNbrp/XOsqY/JVXTq.txt', 19), ('ex1/B/XNbrp/nSlKw/CPynp.txt', 19), ('ex1/B/XNbrp/nSlKw/npcaf.txt', 19)]
    return do_test_ex1(directory, expected)


def test_ex1_3():
    '''
    directory = 'ex1/C'
    '''
    directory = 'ex1/C'
    expected = [('ex1/C/uFkHM/ZCdCN/MXNrc/CLMGY.txt', 1), ('ex1/C/ywrqT/IwXhW.txt', 5), ('ex1/C/uFkHM/ZCdCN/MXNrc/ZoNCv.txt', 7), ('ex1/C/ywrqT/utmAq/QgSNp/nZXqQ.txt', 7), ('ex1/C/uFkHM/xCHoI/eyjzA/wxHCZ.txt', 9), ('ex1/C/ywrqT/Kbmla/ICORS/LtcjW.txt', 11), ('ex1/C/ywrqT/utmAq/QgSNp/imCKP.txt', 11), ('ex1/C/uFkHM/xCHoI/DsZyV/pobLV.txt', 13), ('ex1/C/ywrqT/utmAq/DAAFw.txt', 13), ('ex1/C/MgrCB.txt', 15), ('ex1/C/uFkHM/ZCdCN/FLGOL/yqnet.txt', 15), ('ex1/C/uFkHM/oaLZo/dIURA/XSqCj.txt', 15), ('ex1/C/uFkHM/oaLZo/sKXTp/itjqo.txt', 15), ('ex1/C/uFkHM/pGqIt/HuIGq.txt', 15), ('ex1/C/uFkHM/xCHoI/NENyh/QjvKE.txt', 15), ('ex1/C/uFkHM/ZCdCN/MXNrc/hHhEc.txt', 17), ('ex1/C/uFkHM/oaLZo/Cvtaw/DCBUs.txt', 17), ('ex1/C/uFkHM/oaLZo/iRnKF/hXTCt.txt', 17), ('ex1/C/uFkHM/xCHoI/ePyon.txt', 17), ('ex1/C/ywrqT/Kbmla/FzcWW/xffWg.txt', 17), ('ex1/C/ywrqT/utmAq/caOzd/LqZEd.txt', 17), ('ex1/C/WAXeh.txt', 19), ('ex1/C/ftmeB.txt', 19), ('ex1/C/uFkHM/IBCOF.txt', 19), ('ex1/C/uFkHM/ZCdCN/FLGOL/CSMSk.txt', 19), ('ex1/C/uFkHM/ZCdCN/MXNrc/QRdMJ.txt', 19), ('ex1/C/uFkHM/ZCdCN/kUOSX.txt', 19), ('ex1/C/uFkHM/ZCdCN/qoMyZ/gSpht.txt', 19), ('ex1/C/uFkHM/ZCdCN/vHfPt.txt', 19), ('ex1/C/uFkHM/oaLZo/Cvtaw/AbOeM.txt', 19), ('ex1/C/uFkHM/oaLZo/Cvtaw/MRCmv.txt', 19), ('ex1/C/uFkHM/oaLZo/PrXtK/LrRhm.txt', 19), ('ex1/C/uFkHM/oaLZo/dIURA/ewHBD.txt', 19), ('ex1/C/uFkHM/oaLZo/iRnKF/ECWpc.txt', 19), ('ex1/C/uFkHM/oaLZo/iRnKF/MstOB.txt', 19), ('ex1/C/uFkHM/pGqIt/RxBwU.txt', 19), ('ex1/C/uFkHM/pGqIt/TTLqX/IZUQB.txt', 19), ('ex1/C/uFkHM/xCHoI/dXAQa/Galxu.txt', 19), ('ex1/C/uFkHM/xCHoI/dXAQa/gIepl.txt', 19), ('ex1/C/ywrqT/Kbmla/Dyzmn.txt', 19), ('ex1/C/ywrqT/Kbmla/FzcWW/toSVd.txt', 19), ('ex1/C/ywrqT/Kbmla/ICORS/BoOJp.txt', 19), ('ex1/C/ywrqT/Kbmla/ICORS/GUBPg.txt', 19), ('ex1/C/ywrqT/Kbmla/PvMPQ/uhHbx.txt', 19), ('ex1/C/ywrqT/lULMz.txt', 19), ('ex1/C/ywrqT/utmAq/HvbKE.txt', 19), ('ex1/C/ywrqT/utmAq/QgSNp/WAlGv.txt', 19), ('ex1/C/ywrqT/utmAq/zuCHL.txt', 19)]
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
    expected = 'A-BC-DEF'
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
    expected = 'A-BC-DEFG-HIJKLMN'
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
    expected = 'A-BC-DEFG-HIJK-LM'
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
    check_expected()

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

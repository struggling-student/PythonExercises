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


def do_func1_tests(int_list, bottom, up, expected_return, expected_list):
    res = program.func1(int_list, bottom, up)
    if res != expected_return:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!\nReturned={res}, expected={expected_return}.\n{'*'*50}''')
        return 0
    if int_list != expected_list:
        my_print(f'''{'*'*50}\n[ERROR] La lista in input non è stata modificata correttamente! / The input list has not been correctly modified!\nint_list={int_list}, expected int_list={expected_list}.\n{'*'*50}''')
    return 0.5


def test_func1_1():
    '''
    int_list = [4, 5, 10, 3, -1, 2]
    bottom = 0
    up = 5
    expected_return = 2
    expected_list = [4, 5, 3, 2]
    '''
    int_list = [4, 5, 10, 3, -1, 2]
    bottom = 0
    up = 5
    expected_return = 2
    expected_list = [4, 5, 3, 2]
    return do_func1_tests(int_list, bottom, up, expected_return, expected_list)

def test_func1_2():
    '''
    int_list = [-5, 4, 5, 10, 3, -1, 2, 12]
    bottom = 0
    up = 0
    expected_return = 8
    expected_list = []
    '''
    int_list = [-5, 4, 5, 10, 3, -1, 2, 12]
    bottom = 0
    up = 0
    expected_return = 8
    expected_list = []
    return do_func1_tests(int_list, bottom, up, expected_return, expected_list)

def test_func1_3():
    '''
    int_list = []
    bottom = 0
    up = 5
    expected_return = 0
    expected_list = []
    '''
    int_list = []
    bottom = 0
    up = 5
    expected_return = 0
    expected_list = []
    return do_func1_tests(int_list, bottom, up, expected_return, expected_list)

def test_func1_4():
    '''
    int_list = [-78, 10, 76, 82, -27, -39, -65, -19, 74, 18, 20, -25, -38, -71, -52, -49, -69, 21, -27, 58]
    bottom = -69
    up = 57
    expected_return = 6
    expected_list = [10, -27, -39, -65, -19, 18, 20, -25, -38, -52, -49, -69, 21, -27]
    '''
    int_list = [-78, 10, 76, 82, -27, -39, -65, -19, 74, 18, 20, -25, -38, -71, -52, -49, -69, 21, -27, 58]
    bottom = -69
    up = 57
    expected_return = 6
    expected_list = [10, -27, -39, -65, -19, 18, 20, -25, -38, -52, -49, -69, 21, -27]
    return do_func1_tests(int_list, bottom, up, expected_return, expected_list)

def do_func2_tests(dict1, dict2, expected):
    try:
        res = program.func2(dict1, dict2)
        if res != expected:
            my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
            for k in expected:
                if expected[k] != res[k]:
                    my_print(f'''[ERROR] Ad esempio, la chiave {k} dovrebbe avere il valore {expected[k]} invece che {res[k]}.''')
                    my_print(f'''[ERROR] For example, the key {k} should have the value {expected[k]} instead of {res[k]}.''')
                    break
            return 0
        return 0.5
    except:
        my_print(
            f'''{'*' * 50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*' * 50}''')
        return 0

def test_func2_1():
    '''
    dict1 = {'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}
    dict2 = {'a':'Bad', 'c':'greaT'}
    expected =  {'a':'bad', 'c':'excellent'}
    '''
    dict1 = {'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}
    dict2 = {'a':'Bad', 'c':'greaT'}
    expected =  {'a':'bad', 'c':'excellent'}
    return do_func2_tests(dict1, dict2, expected)

def test_func2_2():
    '''
    dict1 = {'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}
    dict2 = {'A':'Bad', 'D':'greaT'}
    expected =  {}
    '''
    dict1 = {'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}
    dict2 = {'A':'Bad', 'D':'greaT'}
    expected =  {}
    return do_func2_tests(dict1, dict2, expected)

def test_func2_3():
    '''
    dict1 = {1:'AAA', 2:'BBB', 3:'CCC'}
    dict2 = {2:'AAA', 3:'CCC', 4:'DDD'}
    expected =  {2:'aaa', 3:'ccc'}
    '''
    dict1 = {1:'AAA', 2:'BBB', 3:'CCC'}
    dict2 = {2:'AAA', 3:'CCC', 4:'DDD'}
    expected =  {2:'aaa', 3:'ccc'}
    return do_func2_tests(dict1, dict2, expected)

def test_func2_4():
    '''
    dict1 = {0: 'TRIgoNalLY', 1: 'caMoUfLAGE', 2: 'funGICIDE', 3: 'UnchaINs', 4: 'inDustriAlIze', 5: 'SPAcEShIPS', 6: 'vuLgaRItIEs', 7: 'VIbES', 8: 'AcOUStics', 9: 'pUntErS', 10: 'mONoPHtHONgs', 11: 'traNsVersELY', 12: 'BYGoNeS', 13: 'floWN', 14: 'SubmItS', 15: 'dIaChRONIC', 16: 'cRIbs', 17: 'oUtcroPpinG', 18: 'SnOWlIne', 19: 'LocKSMiTHs'}
    dict2 = {0: 'HogTIed', 1: 'CliNked', 2: 'TwinING', 3: 'BoarDINgHoUSe', 4: 'thiCKEtS', 5: 'ROArINgeST', 6: 'befrIeNdING', 7: 'coNVENES', 8: 'tHIRSTs', 9: 'CaRPeNTErInG', 10: 'askANcE', 11: 'triPE', 12: 'RecovERinG', 13: 'LaMeLy', 14: 'ClIPPeRs', 15: 'NaMESAKEs', 16: 'unSeRVILE', 17: 'maNumiSSioN', 18: 'APpOsitIvElY', 19: 'UpSTAGiNG'}
    expected =  {0: 'hogtied', 1: 'clinked', 2: 'twining', 3: 'boardinghouse', 4: 'industrialize', 5: 'roaringest', 6: 'befriending', 7: 'vibes', 8: 'acoustics', 9: 'carpentering', 10: 'askance', 11: 'transversely', 12: 'bygones', 13: 'lamely', 14: 'clippers', 15: 'namesakes', 16: 'cribs', 17: 'manumission', 18: 'appositively', 19: 'locksmiths'}, expected={'a': 'bad', 'c': 'excellent'}
    '''
    dict1 = {0: 'TRIgoNalLY', 1: 'caMoUfLAGE', 2: 'funGICIDE', 3: 'UnchaINs', 4: 'inDustriAlIze', 5: 'SPAcEShIPS', 6: 'vuLgaRItIEs', 7: 'VIbES', 8: 'AcOUStics', 9: 'pUntErS', 10: 'mONoPHtHONgs', 11: 'traNsVersELY', 12: 'BYGoNeS', 13: 'floWN', 14: 'SubmItS', 15: 'dIaChRONIC', 16: 'cRIbs', 17: 'oUtcroPpinG', 18: 'SnOWlIne', 19: 'LocKSMiTHs'}
    dict2 = {0: 'HogTIed', 1: 'CliNked', 2: 'TwinING', 3: 'BoarDINgHoUSe', 4: 'thiCKEtS', 5: 'ROArINgeST', 6: 'befrIeNdING', 7: 'coNVENES', 8: 'tHIRSTs', 9: 'CaRPeNTErInG', 10: 'askANcE', 11: 'triPE', 12: 'RecovERinG', 13: 'LaMeLy', 14: 'ClIPPeRs', 15: 'NaMESAKEs', 16: 'unSeRVILE', 17: 'maNumiSSioN', 18: 'APpOsitIvElY', 19: 'UpSTAGiNG'}
    expected =  {0: 'hogtied', 1: 'clinked', 2: 'twining', 3: 'boardinghouse', 4: 'industrialize', 5: 'roaringest', 6: 'befriending', 7: 'vibes', 8: 'acoustics', 9: 'carpentering', 10: 'askance', 11: 'transversely', 12: 'bygones', 13: 'lamely', 14: 'clippers', 15: 'namesakes', 16: 'cribs', 17: 'manumission', 18: 'appositively', 19: 'locksmiths'}
    return do_func2_tests(dict1, dict2, expected)


def do_func3_tests(str1, str2, expected):
    res = program.func3(str1, str2)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func3_1():
    '''
    str1 = 'abracadabra'
    str2 = 'ABerrant'
    expected = 'ABa'
    '''
    str1 = 'abracadabra'
    str2 = 'ABerrant'
    expected = 'ABa'
    return do_func3_tests(str1, str2, expected)

def test_func3_2():
    '''
    str1 = 'abracadabra'
    str2 = ''
    expected = ''
    '''
    str1 = 'abracadabra'
    str2 = ''
    expected = ''
    return do_func3_tests(str1, str2, expected)

def test_func3_3():
    '''
    str1 = 'infaTuAtION'
    str2 = 'IntANGIbLenESS'
    expected = 'inaN'
    '''
    str1 = 'infaTuAtION'
    str2 = 'IntANGIbLenESS'
    expected = 'inaN'
    return do_func3_tests(str1, str2, expected)

def test_func3_4():
    '''
    str1 = 'delIberAtIVelY',
    str2 = 'ReproductIvE'
    expected = 'etIvE'
    '''
    str1 = 'delIberAtIVelY'
    str2 = 'ReproductIvE'
    expected = 'etIvE'
    return do_func3_tests(str1, str2, expected)


# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(ID, length, expected):
    input_filename  = f'func4/func4_test{ID}.txt'
    output_filename = f'func4/func4_out{ID}.txt'
    expected_filename = f'func4/func4_exp{ID}.txt'
    res = program.func4(input_filename, output_filename, length)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di righe ritornato è sbagliato! / The number of written rows is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func4_1():
    '''
    input_filename = 'func4/func4_test1.txt'
    expected = 7
    '''
    ID = 1
    length = 3
    expected = 7
    return do_func4_tests(ID, length, expected)

def test_func4_2():
    '''
    input_filename = 'func4/func4_test2.txt'
    '''
    ID = 2
    length = 8
    expected = 5
    return do_func4_tests(ID, length, expected)


def test_func4_3():
    '''
    input_filename = 'func4/func4_test3.txt'
    '''

    ID = 3
    length = 7
    expected = 20
    return do_func4_tests(ID, length, expected)

def do_test_func5(ID, expected):
    txt_in  = f'func5/func5_test{ID}.txt'
    img_out = f'func5/func5_out{ID}.png'
    img_exp = f'func5/func5_exp{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(txt_in, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di figure disegnate è sbagliato! / The number of drawn figures is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''
    imagefile = func5/func5_test1.png
    output_imagefile = func5/func5_out1.png
    '''
    ID = 1
    expected = 2
    return do_test_func5(ID, expected)


def test_func5_2():
    '''
    imagefile = func5/func5_test2.png
    output_imagefile = func5/func5_out2.png
    color = (255,0,0)
    '''
    ID = 2
    expected = 21
    return do_test_func5(ID, expected)


def test_func5_3():
    '''
    imagefile = func5/func5_test3.png
    output_imagefile = func5/func5_out3.png
    '''
    ID = 3
    expected = 25
    return do_test_func5(ID, expected)


def test_func5_4():
    '''
    imagefile = func5/func5_test4.png
    output_imagefile = func5/func5_out4.png
    '''
    ID = 4
    expected = 50
    return do_test_func5(ID, expected)

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(n, faces, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(n, faces)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(n, faces)
    testlib.check(res, expected, None, f'''{'*'*50}\n[ERROR]Il risultato restituito non è corretto / Incorrect value returned!\nReturned={res}, expected={expected}''')
    return 2

def test_ex1_1():
    '''
    n = 2
    faces = 3
    expected = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    '''
    n = 2
    faces = 3
    expected = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    return do_test_ex1(n, faces, expected)

def test_ex1_2():
    '''
    n = 3
    faces = 4
    expected = [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 1), (1, 3, 2), (1, 3, 3), (1, 3, 4), (1, 4, 1), (1, 4, 2), (1, 4, 3), (1, 4, 4), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 4), (2, 4, 1), (2, 4, 2), (2, 4, 3), (2, 4, 4), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 1, 4), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 2, 4), (3, 3, 1), (3, 3, 2), (3, 3, 3), (3, 3, 4), (3, 4, 1), (3, 4, 2), (3, 4, 3), (3, 4, 4), (4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 1, 4), (4, 2, 1), (4, 2, 2), (4, 2, 3), (4, 2, 4), (4, 3, 1), (4, 3, 2), (4, 3, 3), (4, 3, 4), (4, 4, 1), (4, 4, 2), (4, 4, 3), (4, 4, 4)]
    '''
    n = 3
    faces = 4
    expected = [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 1), (1, 3, 2), (1, 3, 3), (1, 3, 4), (1, 4, 1), (1, 4, 2), (1, 4, 3), (1, 4, 4), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 4), (2, 4, 1), (2, 4, 2), (2, 4, 3), (2, 4, 4), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 1, 4), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 2, 4), (3, 3, 1), (3, 3, 2), (3, 3, 3), (3, 3, 4), (3, 4, 1), (3, 4, 2), (3, 4, 3), (3, 4, 4), (4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 1, 4), (4, 2, 1), (4, 2, 2), (4, 2, 3), (4, 2, 4), (4, 3, 1), (4, 3, 2), (4, 3, 3), (4, 3, 4), (4, 4, 1), (4, 4, 2), (4, 4, 3), (4, 4, 4)]
    return do_test_ex1(n, faces, expected)


def test_ex1_3():
    '''
    n = 5
    faces = 6
    expected = [(1, 1, 1, 1, 1), (1, 1, 1, 1, 2),......., (6, 6, 6, 6, 5), (6, 6, 6, 6, 6)]
    '''
    from itertools import product
    n = 5
    faces = 6
    expected = list(product(range(1,7),range(1,7),range(1,7),range(1,7),range(1,7)))
    return do_test_ex1(n, faces, expected)

# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root, expected, new_root):
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
    if tree.BinaryTree.toList(root) != tree.BinaryTree.toList(new_root):
        my_print(f'''{'*'*50}\n[ERROR]L'albero non è stato modificato correttamente/ The tree has not been correctly modified!!\nReturned={res}, expected={expected}''')
        return 0
    return 2


def test_ex2_1():
    '''
        root                   expected root
    ______5______              ______5______
   |             |            |             |
   8__        ___2___         2__        ___8___
      |      |       |           |      |       |
      3      9       1           3      1       9

      expected = 2
    '''
    root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    expected = 2
    new_root = tree.BinaryTree.fromList([5, [2, None, [3, None, None]], [8, [1, None, None], [9, None, None]]])
    return do_ex2_test(root, expected, new_root)

def test_ex2_2():
    '''
              root                          expected root        
          ______2______                      ______2______       
         |             |                    |             |      
      __ 7__        ___5___              __ 5__        ___7___   
     |      |      |       |            |      |      |       |  
    _4_     3_    _0_     _5_          _3_     4_    _0_     _5_ 
   |   |      |  |   |   |   |        |   |      |  |   |   |   |
   2   -1     1  8   3   2   9       -1   2      1  3   8   2   9

       expected = 4
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    expected =  4
    new_root = tree.BinaryTree.fromList([2, [5, [3, [-1, None, None], [2, None, None]], [4, None, [1, None, None]]], [7, [0, [3, None, None], [8, None, None]], [5, [2, None, None], [9, None, None]]]])
    return do_ex2_test(root, expected, new_root)


def test_ex2_3():
    '''
    A big tree
    expected = 67
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = 67
    new_root = tree.BinaryTree.fromList([-2, [5, [-5, [-7, [2, [26, [10, [10, [0, None, [24, None, None]], [14, None, None]], [13, [-3, [2, None, None], None], [30, None, [-1, None, None]]]], [27, [-1, None, None], [28, [-3, [-9, None, None], [30, None, None]], [19, None, None]]]], None], [8, [9, [-2, [4, None, None], [5, None, None]], [6, [19, None, None], [24, None, None]]], [11, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [-1, [-2, [-3, [21, None, [1, None, None]], [26, None, [30, None, None]]], [10, [-2, [-3, None, [-2, [21, None, None], [28, None, None]]], [7, [-4, None, None], None]], [-1, [2, [-2, None, None], [18, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [26, [-8, None, [9, [17, [23, None, None], None], [21, None, None]]], [16, [2, None, [-10, None, None]], [20, [0, [-5, None, None], [7, [20, None, None], None]], [21, None, [-4, None, None]]]]]], [12, None, [6, [28, [22, None, None], None], [30, [-10, None, None], [-4, None, None]]]]]], [13, [-7, [5, None, [17, [17, [14, [4, [-3, [-4, [21, None, None], None], None], [5, [21, None, None], None]], None], [25, [-10, [-4, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [5, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [20, [2, [5, [0, None, None], [3, None, None]], [14, [15, None, [15, None, None]], [22, [6, None, None], [15, None, None]]]], None]], [13, [-7, [9, [-8, [-5, None, [3, [4, [10, None, None], None], [27, None, None]]], [24, [24, None, None], [30, None, None]]], [5, [4, [-10, [10, [5, None, None], [27, None, [14, None, None]]], [10, [16, None, None], [27, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [-4, None, None], [19, [3, None, None], [12, None, None]]], [12, [2, None, None], [23, None, None]]], [20, [4, None, None], [22, [21, None, None], [22, [27, None, None], None]]]]]], [14, [1, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [8, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [10, None, [25, [-2, None, [-4, None, None]], [2, [-4, None, None], [27, None, None]]]]]], [12, [-9, [-10, [26, [17, None, None], None], [28, [-6, [22, None, None], None], [-2, None, [30, None, None]]]], [28, [11, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [19, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [-6, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [-2, None, None], [10, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [3, [8, None, None], [21, None, None]], [12, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [-10, None, [-4, [25, None, None], None]], [19, None, None]], [12, [4, [-10, None, None], None], [18, [13, [-2, None, None], [27, None, None]], [15, None, None]]]]]], [20, [-9, [8, [-4, None, [-5, None, None]], [-2, [-7, None, [-8, None, None]], [-3, None, None]]], [17, [11, [-6, [-3, None, [2, None, None]], [2, None, None]], [21, None, None]], None]], [29, [28, [23, None, [25, [20, None, None], None]], [30, [16, [2, [24, None, None], [25, None, None]], [6, [-9, None, None], [25, [3, None, None], None]]], [24, [0, None, [-1, None, None]], [30, None, None]]]], [29, [23, [-8, [3, None, None], [9, [4, None, None], None]], [5, None, [21, None, None]]], [25, [-8, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [16, [2, None, [5, None, None]], [24, [14, None, None], [23, None, None]]]]]]]]]]], [20, [20, [19, [-10, [-1, [3, [5, [12, None, None], None], [24, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-2, [-4, [5, [24, None, None], None], [26, None, [18, None, None]]], [21, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [6, None, [27, [-5, None, None], [10, None, None]]], [12, [3, None, None], [18, None, None]]]]], None]])
    return do_ex2_test(root, expected, new_root)


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

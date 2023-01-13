# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
from tree import BinaryTree as BinTree

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

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
#DEBUG = True
DEBUG = False
#############################################################################

def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)

def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################


# ----------------------------------- EX.1 ----------------------------------- #

def do_ex1_tests(qfile, dbfile, k, expected):
    res = program.ex1(qfile, dbfile, k)
    testlib.check(type(res), type(expected), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The k nearest index should be {expected} instead of {res}.\n'''
              f'''[ERROR] I k indici piu vicini dovrebbero essere  {expected} invece che {res}.\n{'*'*50}''')
        return 0
    return 2


def test_ex1_1():
    Q = (-5, -5)
    dbfile = 'ex1/db_00.txt'
    k = 2
    expected = [2, 1]
    return do_ex1_tests(Q, dbfile, k, expected)


def test_ex1_2():
    Q = (3, -4)
    dbfile = 'ex1/db_01.txt'
    k = 4
    expected = [9, 0, 7, 6]
    return do_ex1_tests(Q, dbfile, k, expected)


def test_ex1_3():
    Q = (41, 17)
    dbfile = 'ex1/db_02.txt'
    k = 7
    expected = [31, 91, 26, 24, 42, 25, 80]
    return do_ex1_tests(Q, dbfile, k, expected)


# ----------------------------------- EX.2 ----------------------------------- #
def do_test_ex2(ID, expected, points = (2,1)):

    p = 0
    img_out = f'ex2_your_result_img_{ID}.png'
    img_in = f'ex2/img_{ID}.png'
    img_exp = f'ex2/img_{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.ex2(img_in, img_out)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The number of successive lines with segments should be {expected} instead of {res}.\n[ERROR] Il numero di righe consecutive con segmenti deve essere {expected} invece che {res}.\n{'*'*50}''')
    else:
        p+=points[1]
    e = ''
    try:
        testlib.check_img_file(img_out, img_exp)
    except Exception as exc:
        e = exc
    if e:
        print(e)
    else:
        p+=points[0]
    return p

def test_ex2_1():
    '''ex2/img_1.png'''
    ID = 1 # ex2/img_1.png
    expected = 18
    return do_test_ex2(ID, expected)

def test_ex2_2():
    '''ex2/img_2.png'''
    ID = 2 # ex2/img_2.png
    expected = 1
    return do_test_ex2(ID, expected)


def test_ex2_3():
    '''ex2/img_3.png'''
    ID = 3 # ex2/img_3.png
    expected = 4
    return do_test_ex2(ID, expected)



# ----------------------------------- EX.3 ----------------------------------- #


def do_ex3_tests(path, k, expected):
    
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex3(path, k)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / "
                            "Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex3(path, k)
    if res != expected:
        testlib.check(type(res), type(expected), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")
        testlib.check(res, expected, None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")
    return 2


def test_ex3_1():
    r'''
    path = 'ex3/A'
    k = 7
    '''
    path = 'ex3/A'
    k = 7
    expected = {'ex3/A/a.txt': 56}
    return do_ex3_tests(path, k, expected)


def test_ex3_2():
    r'''
    path = 'ex3/AA'
    k = 19
    '''
    path = 'ex3/AA'
    k = 19
    expected = {'ex3/AA/b.txt': 8531}
    return do_ex3_tests(path, k, expected)

def test_ex3_3():
    r'''
    path = 'ex3/AAA'
    k = 7
    '''
    path = 'ex3/AAA'
    k = 3
    expected = {'ex3/AAA/CCC/jkdmm.txt': 363663,
                'ex3/AAA/CCC/DDD/EEE/rekn.txt': 455997,
                'ex3/AAA/CCC/DDD/EEE/fghh.txt': 22233}
    return do_ex3_tests(path, k, expected)

def test_ex3_4():
    r'''
    path = 'ex3'
    k = 1
    '''
    path = 'ex3'
    k = 1
    expected = {'ex3/A/a.txt': 56,
                'ex3/AAA/BBB/c.txt': 602,
                'ex3/AAA/CCC/jkdmm.txt': 363663,
                'ex3/AAA/CCC/FFF/jhirj.txt': 3046,
                'ex3/AAA/CCC/DDD/EEE/rekn.txt': 455997,
                'ex3/AAA/CCC/DDD/EEE/fghh.txt': 22233,
                'ex3/AAA/DDD/jkdmm.txt': 397,
                'ex3/AAA/DDD/HHH/qews.txt': 46,
                'ex3/a.txt': 56,
                'ex3/AA/BB/c.txt': 602,
                'ex3/AA/b.txt': 8531,
                'ex3/AA/a.txt': 56}
    return do_ex3_tests(path, k, expected)



def do_ex4_test(string, numbers, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex4(string, numbers)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex4(string, numbers)
    if not isinstance(res, (list, set)):
        testlib.check(type(res), set, None, f"Wrong return type! Returned={type(res)}, expected=list or set")
    p=0
    if type(res) == list:
        testlib.check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
        print("Correct list returned", end=' ')
        p=3
    elif type(res) == set:
        testlib.check(res, set(expected), None, f"Wrong set! Returned={res}, expected={expected}")
        print("Correct set returned", end=' ')
        p=2
    return p

def test_ex4_1():
    '''
    start = 'aa'
    words = {'abb', 'acc', 'bdd', 'be'}
    '''

    start = 'aa'
    words = {'abb', 'acc', 'bdd', 'be'}
    expected = ['aacc', 'aabbe', 'aabbdd']
    return do_ex4_test(start, words, expected)

def test_ex4_2():
    '''
    start = 'dog'
    words = {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'}
    '''
    
    start = 'dog'
    words = {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'}
    expected = ['dogoat', 'dogost', 'dogoodoomood', 'dogaspoolongoat', 'dogaspoolongost', 'dogaspooloudoomood', 'dogaspoolongoodoomood']
    return do_ex4_test(start, words, expected)

def test_ex4_3():
    '''
    start = 'pale'
    words = {'poor', 'queen', 'rich', 'extra', 'hertz', 'asleep', 'early', 'yeah', 'hello', 'ostrich', 'echo', 'rhino', 'robot', 'turbo'}
    '''
    start = 'pale'
    words = {'poor', 'queen', 'rich', 'extra', 'hertz', 'asleep', 'early', 'yeah', 'hello', 'ostrich', 'echo', 'rhino', 'robot', 'turbo'}
    expected = ['palearlyeahertz', 'palechostrichello', 'palechostrichertz', 'palextrasleepoorichertz', 'palearlyeahellostrichertz', 'palextrasleepoorhinostrichello', 'palextrasleepoorhinostrichertz', 'palextrasleepoorichellostrichertz', 'palextrasleepooroboturbostrichello', 'palextrasleepooroboturbostrichertz']
    return do_ex4_test(start, words, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1,  test_ex1_2, test_ex1_3,              # k nearest
    test_ex2_1, test_ex2_2, test_ex2_3,               # immagine 
    test_ex3_1, test_ex3_2, test_ex3_3, test_ex3_4,   # recursive file sum numeric module
    test_ex4_1, test_ex4_2, test_ex4_3,               # parole accodate massimali
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################

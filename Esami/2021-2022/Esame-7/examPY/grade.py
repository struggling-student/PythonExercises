# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    exit(0)
import program
class IncorrectReturn(Exception):
    pass

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


def error_message(res, expected, msg=None):
    bold = '\033[1m'
    bolde = '\033[0m'
    
    msg_std = f"{bold}Return value incorrect | Valore NON corretto! [NOT OK]{bolde}\n YOUR ANSWER | TUO RISULTATO = {res} \n    EXPECTED | ATTESO        = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print(bold+'*'*50+bolde)
    print(msg)
    print(bold+'*'*50+bolde)




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
def do_ex1_tests(f1, f2, f3, expf, expected):
    res = program.ex1(f1, f2, f3)
    if not os.path.isfile(f3):
        error_message(res, expected, f"> README: file {f3} not found\n")
        return 0
    testlib.check_text_file(f3, expf)
    if res == expected:
        return 2
    else:
        if type(res) != tuple:
            error_message(res, expected, "> README: a tuple is expected, not a {}\n".format(type(res)))
        if len(res) != 2:
            error_message(res, expected, "> README: a tuple with two elements is expected.\n")
        error_message(res, expected)
        raise IncorrectReturn
        return 0


def test_ex1_1():
    r'''
    Input files: f1.txt and f2.txt
    '''
    expected = (3, 2)
    return do_ex1_tests('ex1/f1.txt','ex1/f2.txt','outf1f2.txt','ex1/f1f2.exp.txt', expected)

def test_ex1_2():
    r'''
    Input files: f2.txt and f3.txt
    '''
    expected = (2, 2)
    return do_ex1_tests('ex1/f2.txt','ex1/f3.txt','outf2f3.txt','ex1/f2f3.exp.txt', expected)

def test_ex1_3():
    r'''
    Input files: f3.txt and f4.txt
    '''
    expected = (13, 3)
    return 1 + do_ex1_tests('ex1/f3.txt','ex1/f4.txt','outf3f4.txt','ex1/f3f4.exp.txt', expected)


# ----------------------------------- EX.2 ----------------------------------- #

def do_ex2_tests(path, expected):
    res = program.ex2(path)
    if res == expected:
        return 2
    else:
        if type(res) != int:
            error_message(res, expected, "> README: an integer is expected, not a {}\n".format(type(res)))
        error_message(res, expected)
        raise IncorrectReturn
        return 0


def test_ex2_1():
    r'''
    Input path: 'ex2/grid01.json'
    '''
    path =  'ex2/grid01.json'
    expected = 4
    return do_ex2_tests(path, expected)


def test_ex2_2():
    r'''
    Input path: 'ex2/grid02.json'
    '''
    path =  'ex2/grid02.json'
    expected = -1
    return do_ex2_tests(path, expected)


def test_ex2_3():
    r'''
    Input path: 'ex2/grid03.json'
    '''
    path =  'ex2/grid03.json'
    expected = -1
    return 1 + do_ex2_tests(path, expected)

# ----------------------------------- EX.3 ----------------------------------- #

def do_ex3_tests(a, b, k, expected):
    try:
        isrecursive.decorate_module(program)
        program.ex3(a, b, k)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    res = program.ex3(a, b, k)
    if res == expected:
        return 3
    else:
        if type(res) != list:
            error_message(res, expected, "> README: a list is expected, not a {}\n".format(type(res)))
        error_message(res, expected)
        return 0


def test_ex3_1():
    r'''
    Input words: 'casa', 'riccio'
    Input k: 3
    '''
    expected = ['casric', 'casicc', 'cascci', 'cascio', 'asaric', 'asaicc', 'asacci', 'asacio']
    return do_ex3_tests('casa', 'riccio', 3, expected)


def test_ex3_2():
    r'''
    Input words: 'karol', 'rogers'
    Input k: 2
    '''
    expected = ['karo', 'kaog', 'kage', 'kaer', 'kars', 'arro', 'arog', 'arge', 'arer', 'arrs', 'roro', 'roog', 'roge', 'roer', 'rors', 'olro', 'olog', 'olge', 'oler', 'olrs']
    return do_ex3_tests('karol', 'rogers', 2, expected)


def test_ex3_3():
    r'''
    Input words: 'elephant','hippopotamus'
    Input k: 3
    '''
    expected = ['elephipp', 'elepippo', 'elepppop', 'eleppopo', 'elepopot', 'eleppota', 'elepotam', 'eleptamu', 'elepamus', 'lephhipp', 'lephippo', 'lephppop', 'lephpopo', 'lephopot', 'lephpota', 'lephotam', 'lephtamu', 'lephamus', 'ephahipp', 'ephaippo', 'ephappop', 'ephapopo', 'ephaopot', 'ephapota', 'ephaotam', 'ephatamu', 'ephaamus', 'phanhipp', 'phanippo', 'phanppop', 'phanpopo', 'phanopot', 'phanpota', 'phanotam', 'phantamu', 'phanamus', 'hanthipp', 'hantippo', 'hantppop', 'hantpopo', 'hantopot', 'hantpota', 'hantotam', 'hanttamu', 'hantamus']
    return do_ex3_tests('elephant','hippopotamus', 4, expected)


# ----------------------------------- EX.4 ----------------------------------- #

def do_ex4_tests(path, expected):
    res = program.ex4(path)
    if res == expected:
        return 3
    else:
        if type(res) != dict:
            error_message(res, expected, "> README: a dictionary is expected, not a {}\n".format(type(res)))
        error_message(res, expected)
        raise IncorrectReturn
        return 0


def test_ex4_1():
    r'''
    Input path: 'ex4/test01'
    '''
    path =  'ex4/test01'
    expected = {'ex4/test01/f1/f1-1/t2.txt': 1722, 'ex4/test01/t1.txt': 1116}
    return do_ex4_tests(path, expected)


def test_ex4_2():
    r'''
    Input path: 'ex4/test02'
    '''
    path =  'ex4/test02'
    expected = {'ex4/test02/f1/f1-1/t1.txt': 42248, 'ex4/test02/f1/f1-2/t2.txt': 83019, 'ex4/test02/f2/f2-1/t1.txt': 1289763, 'ex4/test02/f2/f2-2/t2.txt': 3901830}
    return do_ex4_tests(path, expected)


def test_ex4_3():
    r'''
    Input path: 'ex4/test03'
    '''
    path =  'ex4/test03'
    expected = {'ex4/test03/f1/t1.txt': 93045, 'ex4/test03/f2/f2-1/f2-1-1/t2.txt': 30296, 'ex4/test03/f2/f2-1/t1.txt': 108093, 'ex4/test03/f3/t2.txt': 9808}
    return do_ex4_tests(path, expected)

## ----------------------------------- EX.5 ----------------------------------- #

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1,  test_ex1_2,  test_ex1_3,
    #test_ex2_1,  test_ex2_2,  test_ex2_3, 
    test_ex3_1,  test_ex3_2,  test_ex3_3, 
    test_ex4_1,  test_ex4_2, test_ex4_3,
    #test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################




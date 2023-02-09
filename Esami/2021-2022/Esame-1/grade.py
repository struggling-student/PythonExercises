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

def do_ex1_tests(triangles, expected):
    val = len(triangles) - len(expected)
    res = program.ex1(triangles)
    
    testlib.check(type(res), type(val), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")

    if triangles != expected:
        print(f'''{'*'*50}\n[ERROR] The list triangles should be modified in {expected} instead of {triangles}.\n'''
              f'''[ERROR] La lista triangles dovrebbe essere modificata in {expected} invece che {triangles}.\n{'*'*50}''')
        return 0
    if res != val:
        print(f'''{'*'*50}\n[ERROR] The expected removed element be {expected} instead of {triangles}.\n'''
              f'''[ERROR] In numero di elementi rimosse deve essere {expected} invece che {triangles}.\n{'*'*50}''')
        return 0
    return 2


def test_ex1_1():
    '''
    triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = [(3, 4, 5), (12, 36.05551, 34)]
    '''
    triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = [(3, 4, 5), (12, 36.05551, 34)]
    return do_ex1_tests(triangles, expected)

def test_ex1_2():
    '''
    triangles = [(3, 4, 6), (11, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = []
    '''
    triangles = [(3, 4, 6), (11, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = []
    return do_ex1_tests(triangles, expected)

def test_ex1_3():
    '''
    triangles = [(6.0208, 4.0, 4.5),
             (5.5, 8.74586, 6.8),
             (12.8, 10.2, 16.3704),
             (2.3, 8.51645, 8.2),
             (7.9, 10.29417, 6),
             (12.5873, 8.8, 9.0)]
    expected = [(6.0208, 4.0, 4.5), (5.5, 8.74586, 6.8), (2.3, 8.51645, 8.2), (12.5873, 8.8, 9.0)]
    '''
    triangles = [(6.0208, 4.0, 4.5),
             (5.5, 8.74586, 6.8),
             (12.8, 10.2, 16.3704),
             (2.3, 8.51645, 8.2),
             (7.9, 10.29417, 6),
             (12.5873, 8.8, 9.0)]
    expected = [(6.0208, 4.0, 4.5), (5.5, 8.74586, 6.8), (2.3, 8.51645, 8.2), (12.5873, 8.8, 9.0)]
    return do_ex1_tests(triangles, expected)


# ----------------------------------- EX.2 ----------------------------------- #
def do_test_ex2(ID, colors, expected, score=3):
    p = 0
    img_in  = f'ex2/image0{ID}.png'
    img_out = f'ex2_your_image0{ID}.png'
    img_exp = f'ex2/expected0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.ex2(img_in, img_out, colors)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The number of rectangle should be {expected} instead of {res}.\n'''
              f'''[ERROR] Il numero di rettangoli deve essere {expected} invece che {res}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return score
    



def test_ex2_1():
    '''imm_in = ex2/image01.png
    imm_out = ex2/expected01.png
    expected = 3
    colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}'''
    ID = 1 
    expected = 3
    colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}
    return do_test_ex2(ID, colors, expected, score=2)

def test_ex2_2():
    '''imm_in = ex2/image02.png
    imm_out = ex2/expected02.png
    expected = 49
    colors = {(i*5,i*5,i*5):(100-2*i,100-2*i) for i in range(0,50)}'''
    ID = 2 
    expected = 49
    colors = {(i*5,i*5,i*5):(100-2*i,100-2*i) for i in range(0,50)} 
    return do_test_ex2(ID, colors, expected)


def test_ex2_3():
    '''imm_in = ex2/image03.png
    imm_out = ex2/expected03.png
    expected = 19
    colors = {...}'''
    ID = 3 
    expected = 17
    colors = {(201, 207, 77): (85, 27), (92, 232, 214): (285, 134), (175, 175, 75): (65, 126), (216, 252, 199): (24, 2), (34, 179, 158): (92, 34), (215, 152, 228): (150, 70), (104, 237, 205): (179, 76), (242, 79, 250): (82, 169), (125, 148, 229): (10, 302), (45, 189, 17): (40, 38), (108, 118, 26): (52, 67), (168, 25, 123): (29, 470), (6, 230, 4): (18, 6), (12, 19, 238): (255, 65), (80, 102, 90): (98, 19), (26, 210, 123): (287, 206), (8, 230, 123): (127, 275)}
    return do_test_ex2(ID, colors, expected)



# ----------------------------------- EX.3 ----------------------------------- #
def do_test_ex3(directory, namefile, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex3(directory, namefile)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex3(directory, namefile)
    testlib.check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
    return 3

def test_ex3_1():
    '''directory = 'ex3/A'
    filename = 'a.txt'
    expected = [22, 100, 90]
    '''
    directory = 'ex3/A'
    filename = 'a.txt'
    expected = [22, 100, 90]
    return do_test_ex3(directory, filename, expected)


def test_ex3_2():
    '''directory = 'ex3/B'
    filename = 'b.txt'
    expected = [33, 69, 270]
    '''
    directory = 'ex3/B'
    filename = 'b.txt'
    expected = [33, 69, 270]
    return do_test_ex3(directory, filename, expected)


def test_ex3_3():
    '''directory = 'ex3/C'
    filename = 'a.txt'
    expected = [23, 728, 490, 335, 11111]
    '''
    directory = 'ex3/C'
    filename = 'a.txt'
    expected = [23, 728, 490, 335, 11111]
    return do_test_ex3(directory, filename, expected)
# ----------------------------------- EX.4 ----------------------------------- #


def do_ex4_test(strings, n, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex4(strings, n)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex4(strings, n)
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
    strings = {'a','b','c','de'}
    n = 2
    expected = ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    '''
    strings = {'a','b','c','de'}
    n = 2
    expected = ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    return do_ex4_test(strings, n, expected)

def test_ex4_2():
    '''
    strings = {'p', 'ro', 'gra', 'mmin', 'Python'}
    n = 3
    expected = ['Pythongrammin', 'Pythonmmingra', 'graPythonmmin', 'gramminPython', 'mminPythongra', 'mmingraPython', 'Pythonmminro', 'Pythonrommin', 'mminPythonro', 'mminroPython', 'roPythonmmin', 'romminPython', 'Pythongraro', 'Pythonmminp', 'Pythonpmmin', 'Pythonrogra', 'graPythonro', 'graroPython', 'mminPythonp', 'mminpPython', 'pPythonmmin', 'pmminPython', 'roPythongra', 'rograPython', 'Pythongrap', 'Pythonpgra', 'graPythonp', 'grapPython', 'pPythongra', 'pgraPython', 'Pythonpro', 'Pythonrop', 'gramminro', 'grarommin', 'mmingraro', 'mminrogra', 'pPythonro', 'proPython', 'roPythonp', 'rogrammin', 'rommingra', 'ropPython', 'gramminp', 'grapmmin', 'mmingrap', 'mminpgra', 'pgrammin', 'pmmingra', 'mminpro', 'mminrop', 'pmminro', 'prommin', 'romminp', 'ropmmin', 'grapro', 'grarop', 'pgraro', 'progra', 'rograp', 'ropgra']
    '''
    strings =  {'p', 'ro', 'gra', 'mmin', 'Python'}
    n = 3
    expected = ['Pythongrammin', 'Pythonmmingra', 'graPythonmmin', 'gramminPython', 'mminPythongra', 'mmingraPython', 'Pythonmminro', 'Pythonrommin', 'mminPythonro', 'mminroPython', 'roPythonmmin', 'romminPython', 'Pythongraro', 'Pythonmminp', 'Pythonpmmin', 'Pythonrogra', 'graPythonro', 'graroPython', 'mminPythonp', 'mminpPython', 'pPythonmmin', 'pmminPython', 'roPythongra', 'rograPython', 'Pythongrap', 'Pythonpgra', 'graPythonp', 'grapPython', 'pPythongra', 'pgraPython', 'Pythonpro', 'Pythonrop', 'gramminro', 'grarommin', 'mmingraro', 'mminrogra', 'pPythonro', 'proPython', 'roPythonp', 'rogrammin', 'rommingra', 'ropPython', 'gramminp', 'grapmmin', 'mmingrap', 'mminpgra', 'pgrammin', 'pmmingra', 'mminpro', 'mminrop', 'pmminro', 'prommin', 'romminp', 'ropmmin', 'grapro', 'grarop', 'pgraro', 'progra', 'rograp', 'ropgra']
    return do_ex4_test(strings, n, expected)

def test_ex4_3():
    '''
    strings = {'bim','bum','ba','le','giu'}
    n = 5
    expected = ['babimbumgiule', 'babimbumlegiu', 'babimgiubumle', 'babimgiulebum', 'babimlebumgiu', 'babimlegiubum', 'babumbimgiule', 'babumbimlegiu', 'babumgiubimle', 'babumgiulebim', 'babumlebimgiu', 'babumlegiubim', 'bagiubimbumle', 'bagiubimlebum', 'bagiubumbimle', 'bagiubumlebim', 'bagiulebimbum', 'bagiulebumbim', 'balebimbumgiu', 'balebimgiubum', 'balebumbimgiu', 'balebumgiubim', 'balegiubimbum', 'balegiubumbim', 'bimbabumgiule', 'bimbabumlegiu', 'bimbagiubumle', 'bimbagiulebum', 'bimbalebumgiu', 'bimbalegiubum', 'bimbumbagiule', 'bimbumbalegiu', 'bimbumgiubale', 'bimbumgiuleba', 'bimbumlebagiu', 'bimbumlegiuba', 'bimgiubabumle', 'bimgiubalebum', 'bimgiubumbale', 'bimgiubumleba', 'bimgiulebabum', 'bimgiulebumba', 'bimlebabumgiu', 'bimlebagiubum', 'bimlebumbagiu', 'bimlebumgiuba', 'bimlegiubabum', 'bimlegiubumba', 'bumbabimgiule', 'bumbabimlegiu', 'bumbagiubimle', 'bumbagiulebim', 'bumbalebimgiu', 'bumbalegiubim', 'bumbimbagiule', 'bumbimbalegiu', 'bumbimgiubale', 'bumbimgiuleba', 'bumbimlebagiu', 'bumbimlegiuba', 'bumgiubabimle', 'bumgiubalebim', 'bumgiubimbale', 'bumgiubimleba', 'bumgiulebabim', 'bumgiulebimba', 'bumlebabimgiu', 'bumlebagiubim', 'bumlebimbagiu', 'bumlebimgiuba', 'bumlegiubabim', 'bumlegiubimba', 'giubabimbumle', 'giubabimlebum', 'giubabumbimle', 'giubabumlebim', 'giubalebimbum', 'giubalebumbim', 'giubimbabumle', 'giubimbalebum', 'giubimbumbale', 'giubimbumleba', 'giubimlebabum', 'giubimlebumba', 'giubumbabimle', 'giubumbalebim', 'giubumbimbale', 'giubumbimleba', 'giubumlebabim', 'giubumlebimba', 'giulebabimbum', 'giulebabumbim', 'giulebimbabum', 'giulebimbumba', 'giulebumbabim', 'giulebumbimba', 'lebabimbumgiu', 'lebabimgiubum', 'lebabumbimgiu', 'lebabumgiubim', 'lebagiubimbum', 'lebagiubumbim', 'lebimbabumgiu', 'lebimbagiubum', 'lebimbumbagiu', 'lebimbumgiuba', 'lebimgiubabum', 'lebimgiubumba', 'lebumbabimgiu', 'lebumbagiubim', 'lebumbimbagiu', 'lebumbimgiuba', 'lebumgiubabim', 'lebumgiubimba', 'legiubabimbum', 'legiubabumbim', 'legiubimbabum', 'legiubimbumba', 'legiubumbabim', 'legiubumbimba']
    '''
    strings = {'bim','bum','ba','le','giu'}
    n = 5
    expected = ['babimbumgiule', 'babimbumlegiu', 'babimgiubumle', 'babimgiulebum', 'babimlebumgiu', 'babimlegiubum', 'babumbimgiule', 'babumbimlegiu', 'babumgiubimle', 'babumgiulebim', 'babumlebimgiu', 'babumlegiubim', 'bagiubimbumle', 'bagiubimlebum', 'bagiubumbimle', 'bagiubumlebim', 'bagiulebimbum', 'bagiulebumbim', 'balebimbumgiu', 'balebimgiubum', 'balebumbimgiu', 'balebumgiubim', 'balegiubimbum', 'balegiubumbim', 'bimbabumgiule', 'bimbabumlegiu', 'bimbagiubumle', 'bimbagiulebum', 'bimbalebumgiu', 'bimbalegiubum', 'bimbumbagiule', 'bimbumbalegiu', 'bimbumgiubale', 'bimbumgiuleba', 'bimbumlebagiu', 'bimbumlegiuba', 'bimgiubabumle', 'bimgiubalebum', 'bimgiubumbale', 'bimgiubumleba', 'bimgiulebabum', 'bimgiulebumba', 'bimlebabumgiu', 'bimlebagiubum', 'bimlebumbagiu', 'bimlebumgiuba', 'bimlegiubabum', 'bimlegiubumba', 'bumbabimgiule', 'bumbabimlegiu', 'bumbagiubimle', 'bumbagiulebim', 'bumbalebimgiu', 'bumbalegiubim', 'bumbimbagiule', 'bumbimbalegiu', 'bumbimgiubale', 'bumbimgiuleba', 'bumbimlebagiu', 'bumbimlegiuba', 'bumgiubabimle', 'bumgiubalebim', 'bumgiubimbale', 'bumgiubimleba', 'bumgiulebabim', 'bumgiulebimba', 'bumlebabimgiu', 'bumlebagiubim', 'bumlebimbagiu', 'bumlebimgiuba', 'bumlegiubabim', 'bumlegiubimba', 'giubabimbumle', 'giubabimlebum', 'giubabumbimle', 'giubabumlebim', 'giubalebimbum', 'giubalebumbim', 'giubimbabumle', 'giubimbalebum', 'giubimbumbale', 'giubimbumleba', 'giubimlebabum', 'giubimlebumba', 'giubumbabimle', 'giubumbalebim', 'giubumbimbale', 'giubumbimleba', 'giubumlebabim', 'giubumlebimba', 'giulebabimbum', 'giulebabumbim', 'giulebimbabum', 'giulebimbumba', 'giulebumbabim', 'giulebumbimba', 'lebabimbumgiu', 'lebabimgiubum', 'lebabumbimgiu', 'lebabumgiubim', 'lebagiubimbum', 'lebagiubumbim', 'lebimbabumgiu', 'lebimbagiubum', 'lebimbumbagiu', 'lebimbumgiuba', 'lebimgiubabum', 'lebimgiubumba', 'lebumbabimgiu', 'lebumbagiubim', 'lebumbimbagiu', 'lebumbimgiuba', 'lebumgiubabim', 'lebumgiubimba', 'legiubabimbum', 'legiubabumbim', 'legiubimbabum', 'legiubimbumba', 'legiubumbabim', 'legiubumbimba']
    return do_ex4_test(strings, n, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    #test_ex1_1,  test_ex1_2, test_ex1_3,            # lista triangoli
    test_ex2_1, test_ex2_2, test_ex2_3,             # disegni rettangoli
    test_ex3_1, test_ex3_2, test_ex3_3,             # file con liste
    #test_ex4_1,  test_ex4_2, test_ex4_3,             # combinazioni stringhe
    #test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################

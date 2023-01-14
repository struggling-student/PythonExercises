# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    exit(0)
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

class IncorrectReturn(Exception):
    pass

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

def do_ex1_tests(words, K, expected, score=2):
    res = program.ex1(words, K)
    testlib.check(type(res), type(expected), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")
    for r,e in zip(res,expected):
        testlib.check(type(r), type(e), None, f"Wrong return type of element! Returned={type(r)}, expected={type(e)}")
        testlib.check(r, e, None, f"Wrong return value! Returned={res}, expected={expected}")
    return score


def test_ex1_1():
    words = ['casa', 'coso', 'cosa', 'chiuso']
    K = 2
    expected = (536.5, 13110.25)
    return do_ex1_tests(words, K, expected)


def test_ex1_2():
    words = ['self-righteousness', 'baggage', 'subovated', 'hierurgy', 'backfire', 'jaspery', 'Huygenian', 'rociest', 'metrocarat', 'Mid-march']
    K = 3
    expected = (1191.0, 262164.667)
    return do_ex1_tests(words, K, expected)


def test_ex1_3():
    words = ['singultation', 'strange-favored', 'arginase', 'ralphed', 'Formicinae', 'gansey', 'noncontiguous', 'white-leaved', 'self-generation', 'deep-versed', 'Manaker', 'printline', 'Celene', 'well-soaked', 'Liddie', 'Sicklerville', 'waggonway', 'plagal', 'outvaunting', 'simpling', 'usaron', 'Neona', 'Anaxagorean', 'aforetimes', 'semiferous']
    K = 9
    expected = (1143.556, 106012.469)
    return do_ex1_tests(words, K, expected, score=3)

# ----------------------------------- EX.2 ----------------------------------- #

def do_ex2_tests(ID, expected, total=2):
    file_png = f"crosses/cross_{ID}.png"
    res = program.ex2(file_png)
    if res != expected:
        error_message(res, expected)
        for c, l in expected.items():
            assert sorted(l) == sorted(res[c])
        return 0
    return total


def test_ex2_1():
    r'''
    Trovate le croci su immagine crosses/cross_01.png
    '''
    ID = '01'
    expected = {(255, 255,   0): {((123, 516), (161, 516), (142, 497), (142, 535))},
                (255,   0, 255): {((129,  97), (383,  97), (256,  62), (256, 132))},
                (  0,   0, 255): {((140,  41), (390,  41), (265,  24), (265,  58))},
                (255,   0,   0): {((450, 310), (526, 310), (488, 217), (488, 403))}}
    return do_ex2_tests(ID, expected)

def test_ex2_2():
    r'''
    Trovate le croci su immagine crosses/cross_02.png
    '''

    ID = '02'
    expected = {(255, 255, 255): {((21, 266), (41, 266), (31, 162), (31, 370))},
                (0, 0, 255): {((25, 101), (49, 101), (37, 56), (37, 146)), ((36, 244), (108, 244), (72, 140), (72, 348))},
                (255, 0, 0): {((60, 64), (134, 64), (97, 34), (97, 94))},
                (255, 0, 255): {((127, 505), (213, 505), (170, 502), (170, 508))},
                (0, 255, 0): {((130, 394), (194, 394), (162, 356), (162, 432))},
                (0, 255, 255): {((140, 103), (222, 103), (181, 74), (181, 132))},
                (255, 255, 0): {((188, 294), (266, 294), (227, 281), (227, 307)), ((253, 209), (311, 209), (282, 147), (282, 271)), ((266, 127), (294, 127), (280, 105), (280, 149))}}
    return do_ex2_tests(ID, expected)

def test_ex2_3():
    r'''
    Trovate le croci su immagine crosses/cross_03.png
    '''

    ID = '03'
    expected = {(0, 255, 255): {((2, 44), (4, 44), (3, 28), (3, 60)), ((4, 18), (8, 18), (6, 15), (6, 21)), ((29, 178), (83, 178), (56, 174), (56, 182)), ((124, 15), (132, 15), (128, 10), (128, 20)), ((124, 83), (188, 83), (156, 75), (156, 91)), ((211, 94), (215, 94), (213, 86), (213, 102))},
                (255, 255, 0): {((13, 215), (27, 215), (20, 197), (20, 233)), ((22, 15), (28, 15), (25, 8), (25, 22)), ((100, 180), (168, 180), (134, 161), (134, 199)), ((173, 43), (183, 43), (178, 35), (178, 51))},
                (255, 0, 255): {((22, 64), (38, 64), (30, 44), (30, 84)), ((26, 210), (68, 210), (47, 208), (47, 212)), ((50, 122), (56, 122), (53, 74), (53, 170)), ((114, 66), (128, 66), (121, 61), (121, 71)), ((202, 60), (232, 60), (217, 52), (217, 68)), ((226, 162), (238, 162), (232, 127), (232, 197))},
                (255, 255, 255): {((25, 5), (73, 5), (49, 4), (49, 6)), ((68, 161), (102, 161), (85, 148), (85, 174)), ((98, 5), (180, 5), (139, 3), (139, 7)), ((121, 212), (173, 212), (147, 207), (147, 217)), ((145, 126), (193, 126), (169, 87), (169, 168))},
                (0, 255, 0): {((54, 187), (84, 187), (69, 182), (69, 195)), ((87, 223), (173, 223), (130, 217), (130, 229)), ((165, 25), (193, 25), (179, 18), (179, 32))},
                (0, 0, 255): {((201, 150), (221, 150), (211, 122), (211, 178))}}
    return do_ex2_tests(ID, expected, total=3)

# ----------------------------------- EX.3 ----------------------------------- #

def do_test_ex3(S, expected, total=3):
    try:
        isrecursive.decorate_module(program)
        program.ex3(S)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    res = program.ex3(S)
    score = 0
    # se i valori dentro sono OK
    # ma non ordinati per bene
    # rendo cmq 2
    if set(res) == set(expected):
        score = 2
    else:
        # altrimenti se nemmeno i valori sono giusti rendo 0
        error_message(res, expected)
        return 0#, total
    # se sono qui, i valori dentro sono giusti
    # e potrebbero essere ordinati bene
    if res == expected:
        # sono anche ordinati bene
        # aggiungo 1 (3 in totale)
        score += 1
    else:
        error_message(res, expected, "> LEGGIMI: L' ordinamento e' la parte SCORRETTA. I valori delle foglie vanno bene\n\n")
    # altrimenti se non sono ordinati bene
    # mantengo 2 ma avverto
    return score#, total


def test_ex3_1():
    r'''
    Albero di gioco con input 5111001
    '''
    # in
    S = '5111001'
    # out
    expected = [571, 517, 51601, 51141]
    return do_test_ex3(S, expected)

def test_ex3_2():
    r'''
    Albero di gioco con input 1010100001
    '''

    # in
    S = '1010100001'
    # out
    expected = [53, 5201, 5041, 1241, 1211, 1051]
    return do_test_ex3(S, expected)

def test_ex3_3():
    r'''
    Albero di gioco con input 31020040000100010
    '''
    # in
    S = '31020040000100010'
    # out
    expected = [310200450, 310200442, 310200412, 31020040210, 31020040202, 31020040050, 31020040042]
    return do_test_ex3(S, expected)


# ----------------------------------- EX.4 ----------------------------------- #
import tree

def do_test_ex4(itree, K, expected_depth, score=2):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex4(itree, K)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    out = program.ex4(itree, K)
    testlib.check(out, expected_depth, None, f"Wrong type of value: expecting int but received {type(out)}.")
    testlib.check(out, expected_depth, None, f"Wrong value: expecting {expected_depth} but received {out}.")
    return score


def test_ex4_1():
    ''' lowest multiple of 5 in example.txt -> depth 3 '''
    itree = tree.BinaryTree.fromList([1, [25, [3, [4, None, None], [55, None, None]], [65, None, None]], [7, None, None]])
    K              = 5
    expected_depth = 3
    return do_test_ex4(itree, K, expected_depth, score=1)

def test_ex4_2():
    ''' lowest multiple of 9 in tree-10-60.txt -> depth 6 '''
    itree = tree.BinaryTree.fromList([269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]])
    K              = 9
    expected_depth = 6
    return do_test_ex4(itree, K, expected_depth)

def test_ex4_3():
    ''' lowest multiple of 7 in tree-10-60.txt -> depth -1 (not found) '''
    itree = tree.BinaryTree.fromList([269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]])
    K             = 7
    expected_depth= -1
    return do_test_ex4(itree, K, expected_depth)


def test_ex4_4():
    ''' lowest multiple of 11 in tree-20-60.txt -> depth 14 '''
    tree_list = [783508, [-991165, None, [-403114, [694375, None, [-625776, [-984200, None, [-567675, None, None]], [-77560, None, None]]], [-124358, [-810037, None, [-429701, [317231, None, [919617, [-372775, [974707, [-428019, [634010, None, [631589, [245491, None, None], None]], None], [-860703, [-386442, None, None], [90256, [721441, None, None], [-956206, [236568, [340989, None, None], [-722839, [-541788, [-114194, [-285235, None, None], None], [-69670, None, [-658259, [565754, [-534894, None, None], [183819, None, None]], None]]], [-869311, [415418, None, None], None]]], None]]]], [-585669, [-859079, None, [-521882, None, [904930, [733448, [690672, [-351223, None, None], None], [581866, [693281, [-20457, None, None], None], [-389156, [-352329, None, [-413166, [209195, None, [19733, None, None]], None]], [434097, None, [-910322, [-388475, [285460, None, None], [335300, None, None]], [693920, [27441, None, None], [-790347, None, None]]]]]]], [338990, None, [-327537, None, [-574650, None, None]]]]]], None]], None]], None]], None]]], None]
    itree = tree.BinaryTree.fromList(tree_list)
    K             = 11
    expected_depth= 14
    return do_test_ex4(itree, K, expected_depth)

def test_ex4_5():
    ''' lowest multiple of 17 in tree-10-80.txt -> depth 8 '''
    expected_tree = [202842, [-645741, [-170691, None, [-165619, [222351, [100026, [-742935, [-350330, [346608, [924340, None, None], [-96809, None, None]], [470258, [-556482, None, None], [-377624, None, None]]], [403163, [264749, [-484352, None, None], [110219, None, None]], [-817934, [803773, None, None], [-169027, None, None]]]], [-337484, [360694, [916882, [-160455, None, None], [720819, None, None]], [797288, [-169054, None, None], [236718, None, None]]], [-6231, [436611, [985353, None, None], [881664, None, None]], [-913123, [-199797, None, None], [-783762, None, None]]]]], None], [-256813, [-702310, [677198, [721889, [32689, None, [452226, None, None]], [669594, None, [-628440, None, None]]], [-214851, [-62873, [-934471, None, None], None], [-711761, [-734368, None, None], [-556399, None, None]]]], [-265749, [327995, [-211601, [-271193, None, None], None], None], [71319, [-668323, [-362537, None, None], [-222064, None, None]], [-712034, [-393509, None, None], None]]]], [-312818, [46788, [-387131, [411132, [-471632, None, None], [-861109, None, None]], [858489, [606158, None, None], [352025, None, None]]], [-210168, [779036, [707104, None, None], [945391, None, None]], [776990, [913775, None, None], [-597112, None, None]]]], [682908, [-950136, [473635, [15850, None, None], [259694, None, None]], [708537, [4775, None, None], [-328988, None, None]]], [-808248, None, None]]]]]], None], None]
    itree = tree.BinaryTree.fromList(expected_tree)
    K              = 17
    expected_depth = 8
    return do_test_ex4(itree, K, expected_depth)
################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1,  test_ex1_2, test_ex1_3,                        # string means max
    test_ex2_1, test_ex2_2, test_ex2_3,                            # search crosses
    test_ex3_1, test_ex3_2, test_ex3_3,                            # game tree int/str
    test_ex4_1, test_ex4_2, test_ex4_3, test_ex4_4,  test_ex4_5,   # alberi max depth multiple of k
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################

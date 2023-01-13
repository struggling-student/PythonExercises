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

def do_ex1_tests(punti, K, expected, points=2):
    res = program.ex1(punti, K)
    testlib.check(type(res), type(expected), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")
    testlib.check(res,       expected, None, f"Wrong return value! Returned={res}, expected={expected}")
    return points

def test_ex1_1():
    """
    punti = [(-1, 3), (1, 3), (3, 11), (5, 27), (7, 51), (9, 83), (11, 123), (13, 171), (15, 227), (17, 291), (19, 363)]
    K = 4
    """
    punti = [(-1, 3), (1, 3), (3, 11), (5, 27), (7, 51), (9, 83), (11, 123), (13, 171), (15, 227), (17, 291), (19, 363)]
    K     = 4
    expected = ((2.0, 11.0), 16.279)
    return do_ex1_tests(punti, K, expected)

def test_ex1_2():
    """
    punti = punti sulla parabola y=2*x**2+5      nell'intervallo [-3, +4] a passi di 0.5
    K = 3
    """
    punti = punti = [ (x/10,2*((x/10)**2)+5) for x in range(-30, 41, 5)  ]
    K     = 3
    expected = ((0.0, 5.333), 0.527)
    return do_ex1_tests(punti, K, expected)

def test_ex1_3():
    """
    punti = 15 punti con X tra -50 e 50 ordinate da sinistra a destra e Y casuali tra -50 e 50
    K = 3
    """
    punti=[(-47, -7), (-43, -8), (-41, -47), (-41, -38), (-25, -21), (-23, 46), (-6, 19), (1, 44),
           (9, 27), (11, -47), (22, 9), (32, 31), (40, -16), (40, -13), (43, -24)]
    expected = ((-39.4, -24.2), 22.856)
    K = 5
    return do_ex1_tests(punti, K, expected)

# ----------------------------------- EX.2 ----------------------------------- #
def do_test_ex2(lista_ellissi, ID, W, H, expected):
    copia_ellissi = lista_ellissi.copy()
    expected_png = f'ex2/{ID}.png'
    filename_png = f'your_result_img_{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(filename_png):
        os.remove(filename_png)
    # now run
    res = program.ex2(lista_ellissi, filename_png, W, H)
    testlib.check(lista_ellissi, copia_ellissi, None, "the list has been modified / la lista è stata modificata")
    testlib.check_img_file(filename_png, expected_png)
    if res == expected:
        return 2
    else:
        print(f'''{'*'*50}\n[ERROR] The number of pixels painted by at least 2 ellipses should be {expected} instead than {res}.\n[ERROR] Il numero di pixel colorati da almeno 2 ellissi deve essere {expected} invece che {res}.\n{'*'*50}''')
        return 1.5

def test_ex2_1():    # x1   y1    x2   y2    D     R    G    B
    ''' 3 ellissi casuali:
    lista_ellissi=[  (160, 185,  182, 199,   28,  110, 146, 109),
                     (233, 187,  161, 173,   83,  148, 175, 239),
                     (133, 152,  253, 176,  125,  220, 161, 227)] '''
    lista_ellissi=[  (160, 185,  182, 199,   28,  110, 146, 109),
                     (233, 187,  161, 173,   83,  148, 175, 239),
                     (133, 152,  253, 176,  125,  220, 161, 227)]
    ID=3
    W=279
    H=233
    expected=1077
    return do_test_ex2(lista_ellissi, ID, W, H, expected)

def test_ex2_2():    # x1   y1    x2   y2    D     R    G    B
    '''10 ellissi casuali'''
    lista_ellissi=[  ( 38, 193,  244, 330,  307,  237, 189, 177),
                     ( 34, 234,  270, 254,  275,  110, 229, 131),
                     (194, 274,  196, 211,  106,  135, 162, 175),
                     ( 55,  92,   95, 316,  291,  237, 127, 120),
                     (162, 233,  193,  41,  284,  132, 239, 249),
                     (189,  96,  151, 334,  463,  231, 192, 105),
                     ( 76, 278,  288, 283,  216,  198, 243, 116),
                     (106, 153,  148, 232,  136,  150, 101, 105),
                     (135, 348,  121, 155,  385,  135, 205, 219),
                     (270,  24,   33,  50,  260,  237, 244, 183)]
    ID=10
    W=295
    H=348
    expected=94044
    return do_test_ex2(lista_ellissi, ID, W, H, expected)

def test_ex2_3():    # x1   y1    x2   y2    D     R    G    B
    '''15 ellissi casuali'''
    lista_ellissi=[  ( 80, 210,   34, 130,  142,  243, 218, 157),
                     ( 62,  59,    6,  35,   90,  229, 135, 209),
                     (  0, 230,    0,   4,  368,  100, 108, 142),
                     ( 77,  66,  149,  25,   99,  138, 148, 170),
                     (158, 295,  163, 111,  326,  203, 185, 143),
                     ( 87, 203,   40,   5,  340,  231, 207, 149),
                     ( 11,  95,  127, 335,  453,  117, 136, 129),
                     ( 46, 211,    0, 311,  189,  107, 158, 164),
                     (125, 353,  160, 257,  172,  215, 161, 189),
                     (148, 210,   89, 174,   98,  230, 248, 222),
                     ( 29, 182,   76, 246,  120,  125, 221, 188),
                     ( 41, 189,  151, 348,  373,  119, 252, 126),
                     (160,  78,  141, 258,  295,  149, 124, 122),
                     ( 49,  26,  104, 274,  292,  215, 235, 248),
                     ( 53, 214,  116, 158,  153,  169, 177, 219)]
    ID=15
    W=166
    H=356
    expected=58342
    return do_test_ex2(lista_ellissi, ID, W, H, expected)

def test_ex2_4():    # x1   y1    x2   y2    D     R    G    B
    ''' 20 ellissi casuali '''
    lista_ellissi=[  (286, 285,   84, 302,  383,  166, 153, 245),
                     (165,  83,  325,   8,  327,  107, 138, 148),
                     (125,  93,   33, 178,  189,  109, 160, 249),
                     ( 87, 196,  136, 182,  100,  132, 145, 100),
                     (225, 221,   89,  81,  338,  132, 244, 218),
                     (328,  70,  164, 197,  390,  215, 206, 102),
                     (125, 276,   81, 157,  175,  184, 199, 171),
                     (333, 188,  257, 122,  189,  153, 121, 166),
                     (201,  42,  202, 260,  268,  249, 169, 111),
                     (  5,   8,  314,  11,  408,  136, 168, 121),
                     (156, 207,  337,  40,  463,  210, 163, 162),
                     (  6,  75,  247, 187,  521,  148, 110, 178),
                     (334,  18,  325,  90,   79,  184, 108, 130),
                     (227, 200,  112,  32,  307,  135, 223, 241),
                     (241, 201,   17, 271,  394,  154, 103, 144),
                     ( 75,  59,  304, 293,  547,  168, 171, 173),
                     (244, 245,   31, 223,  373,  239, 251, 133),
                     (175, 263,   59,  92,  360,  204, 165, 130),
                     (304, 276,  223, 116,  262,  214, 118, 117),
                     ( 45, 273,  245,  92,  286,  186, 211, 166)]
    ID=20
    W=344
    H=312
    expected=107328
    ret = do_test_ex2(lista_ellissi, ID, W, H, expected)
    return 3 if ret == 2 else 1.5



# ----------------------------------- EX.3 ----------------------------------- #
import tree


def do_test_ex3(file_txt, expected_tree, score=2):
    file_txt = 'ex3/'+file_txt
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex3(file_txt)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    out = program.ex3(file_txt)
    testlib.check(type(out), tree.BinaryTree, None, f"Wrong return type: got {type(out)} instead than tree.BinaryTree")
    testlib.check(out.toList(), expected_tree, None, "The returned tree is wrong")
    return score


def test_ex3_1():
    ''' Tree built from file ex3/example.txt
        Node_140697357043360: 1
        |  Node_140697357043072: 25
        |  |  Node_140697359194336: 3
        |  |  |  Node_140697356896864: 4
        |  |  |  |  None
        |  |  |  |  None
        |  |  |  Node_140697356896720: 55
        |  |  |  |  None
        |  |  |  |  None
        |  |  Node_140697359194240: 65
        |  |  |  None
        |  |  |  None
        |  Node_140697357043312: 7
        |  |  None
        |  |  None
    '''
    filename      = 'example.txt'
    expected_tree = [1, [25, [3, [4, None, None], [55, None, None]], [65, None, None]], [7, None, None]]
    return do_test_ex3(filename, expected_tree, score=1)

def test_ex3_2():
    ''' Tree built from file ex3/tree-10-60.txt'''
    filename      = 'tree-10-60.txt'
    expected_tree = [269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]]
    return do_test_ex3(filename, expected_tree, score=1)

def test_ex3_3():
    filename      = 'tree-10-60.txt'
    expected_tree = [269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]]
    return do_test_ex3(filename, expected_tree)

def test_ex3_4():
    filename      = 'tree-20-60.txt'
    expected_tree = [783508, [-991165, None, [-403114, [694375, None, [-625776, [-984200, None, [-567675, None, None]], [-77560, None, None]]], [-124358, [-810037, None, [-429701, [317231, None, [919617, [-372775, [974707, [-428019, [634010, None, [631589, [245491, None, None], None]], None], [-860703, [-386442, None, None], [90256, [721441, None, None], [-956206, [236568, [340989, None, None], [-722839, [-541788, [-114194, [-285235, None, None], None], [-69670, None, [-658259, [565754, [-534894, None, None], [183819, None, None]], None]]], [-869311, [415418, None, None], None]]], None]]]], [-585669, [-859079, None, [-521882, None, [904930, [733448, [690672, [-351223, None, None], None], [581866, [693281, [-20457, None, None], None], [-389156, [-352329, None, [-413166, [209195, None, [19733, None, None]], None]], [434097, None, [-910322, [-388475, [285460, None, None], [335300, None, None]], [693920, [27441, None, None], [-790347, None, None]]]]]]], [338990, None, [-327537, None, [-574650, None, None]]]]]], None]], None]], None]], None]]], None]
    return do_test_ex3(filename, expected_tree)

def test_ex3_5():
    filename      = 'tree-10-80.txt'
    expected_tree = [202842, [-645741, [-170691, None, [-165619, [222351, [100026, [-742935, [-350330, [346608, [924340, None, None], [-96809, None, None]], [470258, [-556482, None, None], [-377624, None, None]]], [403163, [264749, [-484352, None, None], [110219, None, None]], [-817934, [803773, None, None], [-169027, None, None]]]], [-337484, [360694, [916882, [-160455, None, None], [720819, None, None]], [797288, [-169054, None, None], [236718, None, None]]], [-6231, [436611, [985353, None, None], [881664, None, None]], [-913123, [-199797, None, None], [-783762, None, None]]]]], None], [-256813, [-702310, [677198, [721889, [32689, None, [452226, None, None]], [669594, None, [-628440, None, None]]], [-214851, [-62873, [-934471, None, None], None], [-711761, [-734368, None, None], [-556399, None, None]]]], [-265749, [327995, [-211601, [-271193, None, None], None], None], [71319, [-668323, [-362537, None, None], [-222064, None, None]], [-712034, [-393509, None, None], None]]]], [-312818, [46788, [-387131, [411132, [-471632, None, None], [-861109, None, None]], [858489, [606158, None, None], [352025, None, None]]], [-210168, [779036, [707104, None, None], [945391, None, None]], [776990, [913775, None, None], [-597112, None, None]]]], [682908, [-950136, [473635, [15850, None, None], [259694, None, None]], [708537, [4775, None, None], [-328988, None, None]]], [-808248, None, None]]]]]], None], None]
    return do_test_ex3(filename, expected_tree)

def do_exB_test(dirpath, parole, expected, variance):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex4(dirpath, parole)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex4(dirpath, parole)
    testlib.check(type(res), tuple, None, f"Wrong return type! Returned={type(res)}, expected=tuple")

    diz, var = res
    testlib.check(diz, expected, None, f"Wrong dictionary! Returned={diz}, expected={expected}")
    if var == variance:
        return 3
    else:
        print(f"{'*'*50}\n README: the returned dictionary is correct (2 points) but the returned variance ({var}) is not, expected = {variance} vs {var}\n{'*'*50}")
        return 2

def test_ex4_1():
    expected = {'scelerisque': 0, 'a': 0, 'lacus': 1, 'at': 3, 'hendrerit': 0, 'semper': 0, 'erat': 0}
    parole = list(expected.keys())
    dirpath = 'A/B/D'
    variance = 1.102
    return do_exB_test(dirpath, parole, expected, variance)

def test_ex4_2():
    expected = {'lemonade': 6, 'orange': 8, 'pear': 8, 'apple': 3, 'cider': 3, 'watermelon': 3}
    parole = list(expected.keys())
    dirpath = 'A'
    variance = 5.139
    return do_exB_test(dirpath, parole, expected, variance)

def test_ex4_3():
    expected = {'commodo': 13, 'nisl': 10, 'libero': 5, 'in': 37, 'gravida': 6, 'lacus': 14}
    parole = list(expected.keys())
    dirpath = 'A'
    variance = 115.139
    return do_exB_test(dirpath, parole, expected, variance)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1, test_ex1_2, test_ex1_3,                            # max circles
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4,             # draw ellipses
    test_ex3_1, test_ex3_2, test_ex3_3, test_ex3_4,  test_ex3_5,# alberi parse preorder tree
    test_ex4_1, test_ex4_2, test_ex4_3,                         # max variance word count in txt files
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################

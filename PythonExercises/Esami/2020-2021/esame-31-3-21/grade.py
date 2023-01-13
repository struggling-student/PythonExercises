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

def test_personal_data_entry():
    if program.name:
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

def do_test_ex1(ID, expected):
    filein       = f'games_{ID}.txt'
    fileout      = f'scores_{ID}.txt'
    fileexpexted = f'expected_scores_{ID}.txt'
    res = program.ex1(filein, fileout)
    testlib.check(res, expected)
    testlib.check_text_file(fileout, fileexpexted)
    return 2

def test_ex1_0():
    ID = 'same'
    expected = 4
    return 1 if do_test_ex1(ID, expected) else 0

def test_ex1_1():
    ID = '1'
    expected = 4
    return do_test_ex1(ID, expected)

def test_ex1_2():
    ID = '10'
    expected = 15
    return do_test_ex1(ID, expected)

def test_ex1_3():
    ID = '30'
    expected = 31
    return do_test_ex1(ID, expected)

# ----------------------------------- EX.2 ----------------------------------- #

def do_test_ex2(ID, expected):
    filein              = f'{ID}.png'
    fileout             = f'histogram_{ID}.png'
    fileout_expected    = f'expected_histogram_{ID}.png'
    res = program.ex2(filein, fileout)
    testlib.check(res, expected)
    testlib.check_img_file(fileout_expected, fileout)
    return 2

def test_ex2_1():
    ID = '5-5-10'
    expected = 9
    return do_test_ex2(ID, expected)

def test_ex2_2():
    ID = '100-100-10'
    expected = 10
    return do_test_ex2(ID, expected)

def test_ex2_3():
    ID = '20-20-100'
    expected = 16
    return do_test_ex2(ID, expected)

def test_ex2_4():
    ID = '200-200-60'
    expected = 60
    return do_test_ex2(ID, expected)


# ----------------------------------- EX.3 ----------------------------------- #
from tree import BinaryTree

def fromList(encoded_tree):
    if encoded_tree is None: return None
    value, left, right = encoded_tree
    return BinaryTree(value, fromList(left), fromList(right))


def toList(tree):
    if tree is None: return None
    return [ tree.value, toList(tree.left), toList(tree.right) ]


def do_test_ex3(lista, expected):
    albero = fromList(lista)
    
    try:
        isrecursive.decorate_module(program)
        program.ex3(albero)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    albero = fromList(lista)
    lista_res = program.ex3(albero)
    testlib.check(lista_res, expected)
    return 3


def test_ex3_1():
    '''
Example tree / Albero dell'esempio:
                    6
                /       \\
             5             1
          /     \       /     \\
         2       4     6       8
                / \\           / \\
              15   3         2   10
The function should return / deve restituire [4,5,8,6]
############################################
    '''
    lista = [6, [5, [2, None, None], 
                    [4, [15, None, None], 
                        [3, None, None]
                    ],
                 ],
                [1, [6, None, None], 
                    [8, [2, None, None], 
                        [10, None, None]
                    ]
                ]
    ]
    expected = [4,5,8,6]
    return do_test_ex3(lista, expected)

def test_ex3_2():
    '''
Tree n. 2
                          76                            
            ______________|_______________              
           |                              |             
          595                             35            
     ______|                     _________|_____        
     |                          |               |       
     3                         71              100     
     |__                     __|__            __|___    
        |                   |     |          |      |   
        18                  90   10         23      138 
       __|__                 ____|______      \    /  \  
      |     |               |           |      0  2   44 
      4     4               72          8               
                                         \              
                                          67            
The function should return / deve restituire [18,10,71,138,100,76]
#################################################
'''
    lista = [76, [595, [3, None, [18, [4, None, None],
                                      [4, None, None]]],
                  None], 
                 [35, [71, [90, None, None], 
                              [10, [72, None, None], 
                                   [8, None, 
                                       [67, None, None]]]], 
                         [100, [23, None, 
                                    [0, None, None]], 
                               [138, [2, None, None], 
                                     [44, None, None]]]]]
    expected = [18, 10,71,138,100,76]
    return do_test_ex3(lista, expected)

def test_ex3_3():
    '''
Tree n. 3
                          76                            
            ______________|_______________              
           |                              |             
          12                              36            
    _______|_______              _________|_____        
   |               |            |               |       
   90             15           25              100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
5     20        47      94  92   46         23      138 
   ___|___    __|___         ____|______      \      \  
  |       |  |      |       |           |     81     44 
  196     28 87     29      72          8               
                                         \              
                                          30            
                                          _|_           
                                         |   |          
                                        46  23          
The function should return / deve restituire
    [20, 90, 47, 15, 12, 30, 46, 25, 100, 36, 76]
################################################################
'''
    lista=[76, [12, [90,
                        [5,None,None],
                        [20, [196,None,None],
                             [28,None,None]]],
                     [15, [47, [87,None,None],
                               [29,None,None]],
                          [94,None,None]]],
               [36, [25, [92,None,None],
                         [46, [72,None,None],
                              [8, None, 
                                  [30, [46,None,None],
                                       [23,None,None]]]]],
                    [100, [23, None,
                               [81,None,None]],
                          [138, None,
                                [44,None,None]]]]]
    expected = [20, 90, 47, 15, 12, 30, 46, 25, 100, 36, 76] 
    return do_test_ex3(lista, expected)


# ----------------------------------- EX.4 ----------------------------------- #

def test_ex4(N, expected):
    try:
        isrecursive.decorate_module(program)
        program.ex4(N)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris = program.ex4(N)
    testlib.check(type(ris), list, None, "bisogna restituire una lista")
    testlib.check(ris, expected, None, "la lista restituita non è corretta")
    return 3


def test_ex4_1():
    '''
First test for ex4 (having n=2) / Primo test della funzione ex4 con n=2

    [('00', 0, 1),
    ('01', 1, 1),
    ('02', 2, 2),
    ('10', 3, 2),
    ('11', 4, 3),
    ('12', 5, 3),
    ('20', 6, 3),
    ('21', 7, 3),
    ('22', 8, 4)]

    '''
    N = 2
    gt = [('00', 0, 1),
          ('01', 1, 1),
          ('02', 2, 2),
          ('10', 3, 2),
          ('11', 4, 3),
          ('12', 5, 3),
          ('20', 6, 3),
          ('21', 7, 3),
          ('22', 8, 4)]
    return test_ex4(N, gt) - 1 


def test_ex4_2():
    '''
Second test for ex4 (having h=3) / Secondo test della funzione ex4 con n=3

    [('000', 0, 1),
     ('001', 1, 1),
     ('002', 2, 2),
     ('010', 3, 2),
     ('011', 4, 3),
     ('012', 5, 3),
     ('020', 6, 3),
     ('021', 7, 3),
     ('022', 8, 4),
     ('100', 9, 4),
     ('101', 10, 4),
     ('102', 11, 4),
     ('110', 12, 4),
     ('111', 13, 4),
     ('112', 14, 4),
     ('120', 15, 4),
     ('121', 16, 5),
     ('122', 17, 5),
     ('200', 18, 5),
     ('201', 19, 5),
     ('202', 20, 5),
     ('210', 21, 5),
     ('211', 22, 5),
     ('212', 23, 5),
     ('220', 24, 5),
     ('221', 25, 5),
     ('222', 26, 5)]

    '''
    N = 3
    gt = [('000', 0, 1), ('001', 1, 1), ('002', 2, 2), ('010', 3, 2), ('011', 4, 3), ('012', 5, 3), ('020', 6, 3), ('021', 7, 3), ('022', 8, 4), ('100', 9, 4), ('101', 10, 4), ('102', 11, 4), ('110', 12, 4), ('111', 13, 4), ('112', 14, 4), ('120', 15, 4), ('121', 16, 5), ('122', 17, 5), ('200', 18, 5), ('201', 19, 5), ('202', 20, 5), ('210', 21, 5), ('211', 22, 5), ('212', 23, 5), ('220', 24, 5), ('221', 25, 5), ('222', 26, 5)]
    return test_ex4(N, gt)


def test_ex4_3():
    '''
Third test of ex4 (having n=4) / Terzo test della funzione ex4 con n=4

    [('0000', 0, 1),
     ('0001', 1, 1),
     ('0002', 2, 2),
     ('0010', 3, 2),
     ('0011', 4, 3),
     ('0012', 5, 3),
     ('0020', 6, 3),
     ('0021', 7, 3),
     ('0022', 8, 4),
     ('0100', 9, 4),
     ('0101', 10, 4),
     ('0102', 11, 4),
     ('0110', 12, 4),
     ('0111', 13, 4),
     ('0112', 14, 4),
     ('0120', 15, 4),
     ('0121', 16, 5),
     ('0122', 17, 5),
     ('0200', 18, 5),
     ('0201', 19, 5),
     ('0202', 20, 5),
     ('0210', 21, 5),
     ('0211', 22, 5),
     ('0212', 23, 5),
     ('0220', 24, 5),
     ('0221', 25, 5),
     ('0222', 26, 5),
     ('1000', 27, 5),
     ('1001', 28, 5),
     ('1002', 29, 5),
     ('1010', 30, 5),
     ('1011', 31, 5),
     ('1012', 32, 6),
     ('1020', 33, 6),
     ('1021', 34, 6),
     ('1022', 35, 6),
     ('1100', 36, 6),
     ('1101', 37, 6),
     ('1102', 38, 6),
     ('1110', 39, 6),
     ('1111', 40, 6),
     ('1112', 41, 6),
     ('1120', 42, 6),
     ('1121', 43, 6),
     ('1122', 44, 6),
     ('1200', 45, 6),
     ('1201', 46, 6),
     ('1202', 47, 6),
     ('1210', 48, 6),
     ('1211', 49, 6),
     ('1212', 50, 6),
     ('1220', 51, 6),
     ('1221', 52, 6),
     ('1222', 53, 6),
     ('2000', 54, 6),
     ('2001', 55, 6),
     ('2002', 56, 6),
     ('2010', 57, 6),
     ('2011', 58, 6),
     ('2012', 59, 6),
     ('2020', 60, 6),
     ('2021', 61, 6),
     ('2022', 62, 6),
     ('2100', 63, 6),
     ('2101', 64, 7),
     ('2102', 65, 7),
     ('2110', 66, 7),
     ('2111', 67, 7),
     ('2112', 68, 7),
     ('2120', 69, 7),
     ('2121', 70, 7),
     ('2122', 71, 7),
     ('2200', 72, 7),
     ('2201', 73, 7),
     ('2202', 74, 7),
     ('2210', 75, 7),
     ('2211', 76, 7),
     ('2212', 77, 7),
     ('2220', 78, 7),
     ('2221', 79, 7),
     ('2222', 80, 7)]

    '''
    
    N = 4
    gt = [('0000', 0, 1), ('0001', 1, 1), ('0002', 2, 2), ('0010', 3, 2), ('0011', 4, 3), ('0012', 5, 3), ('0020', 6, 3), ('0021', 7, 3), ('0022', 8, 4), ('0100', 9, 4), ('0101', 10, 4), ('0102', 11, 4), ('0110', 12, 4), ('0111', 13, 4), ('0112', 14, 4), ('0120', 15, 4), ('0121', 16, 5), ('0122', 17, 5), ('0200', 18, 5), ('0201', 19, 5), ('0202', 20, 5), ('0210', 21, 5), ('0211', 22, 5), ('0212', 23, 5), ('0220', 24, 5), ('0221', 25, 5), ('0222', 26, 5), ('1000', 27, 5), ('1001', 28, 5), ('1002', 29, 5), ('1010', 30, 5), ('1011', 31, 5), ('1012', 32, 6), ('1020', 33, 6), ('1021', 34, 6), ('1022', 35, 6), ('1100', 36, 6), ('1101', 37, 6), ('1102', 38, 6), ('1110', 39, 6), ('1111', 40, 6), ('1112', 41, 6), ('1120', 42, 6), ('1121', 43, 6), ('1122', 44, 6), ('1200', 45, 6), ('1201', 46, 6), ('1202', 47, 6), ('1210', 48, 6), ('1211', 49, 6), ('1212', 50, 6), ('1220', 51, 6), ('1221', 52, 6), ('1222', 53, 6), ('2000', 54, 6), ('2001', 55, 6), ('2002', 56, 6), ('2010', 57, 6), ('2011', 58, 6), ('2012', 59, 6), ('2020', 60, 6), ('2021', 61, 6), ('2022', 62, 6), ('2100', 63, 6), ('2101', 64, 7), ('2102', 65, 7), ('2110', 66, 7), ('2111', 67, 7), ('2112', 68, 7), ('2120', 69, 7), ('2121', 70, 7), ('2122', 71, 7), ('2200', 72, 7), ('2201', 73, 7), ('2202', 74, 7), ('2210', 75, 7), ('2211', 76, 7), ('2212', 77, 7), ('2220', 78, 7), ('2221', 79, 7), ('2222', 80, 7)]
    return test_ex4(N, gt)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_0, test_ex1_1, test_ex1_2, test_ex1_3,      # football league standings / classifica di calcio
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4,      # colours histogram / istogramma dei colori
    test_ex3_1, test_ex3_2, test_ex3_3,      # binary tree / albero binario
    test_ex4_1, test_ex4_2, test_ex4_3,      # recursive enumeration / enumerazione ricorsiva
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################


import isrecursive
import testlib
import copy
import tree

import program

#################################################################################
################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST ######
################### E' VIETATO USARLE NELLA SOLUZIONE                      ######
################### THESE FUNCTIONS BELOW ARE USED IN TESTS                ######
################### IT'S FORBIDDEN TO USE THEM IN YOUR PROGRAM             ######
#################################################################################

def do_test_es1(tabella, colonne, elimina, expected):
    res = program.es1(tabella, colonne, elimina)
    testlib.check(tabella, expected)
    testlib.check(res, len(elimina))
    return 2

def test_es1_1():
    tabella = [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
        ]
    colonne=['Nome', 'Cognome']
    elimina=['Telefono']
    expected= [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Indirizzo': 'via degli Angeli 17' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Indirizzo': 'via degli Angeli 14' },
        ]
    return do_test_es1(tabella, colonne, elimina, expected)

def test_es1_2():
    tabella = [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
        ]
    colonne=['Telefono', 'Nome', 'Indirizzo']
    elimina=[]
    expected= [   
            { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
        ]
    return do_test_es1(tabella, colonne, elimina, expected)

def test_es1_3():
    tabella = [   
            { 'Nome': 'Andrea',  'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
            { 'Nome': 'Gianni',  'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Nome': 'Gianni',  'Cognome': 'Paperino', 'Telefono': 137487469, 'Indirizzo': 'via degli Angeli 17' },
            { 'Nome': 'Paolino', 'Cognome': 'Paperino', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 313' },
        ]
    colonne=['Cognome', 'Telefono', 'Indirizzo']
    elimina=['Nome', 'Cognome']
    expected= [   
            { 'Telefono': 137487468, 'Indirizzo': 'via del Pero 313' },
            { 'Telefono': 137487469, 'Indirizzo': 'via degli Angeli 17' },
            { 'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
            { 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
        ]
    return do_test_es1(tabella, colonne, elimina, expected)
#################################################################################

def do_test_es2(file_png, colori, expected):
    res      = program.es2(file_png, colori)
    testlib.check(res, expected, "")
    return 2

def test_es2_1():
    """
    Test 1: Bounding boxes dei colori 
    [ (221, 184, 132), (87, 166, 243), (27, 30, 35), (0, 200, 200) ] 
    estratti da '3cime.png'"""
    file_png = '3cime.png'
    colori   = [ (221, 184, 132), (87, 166, 243), (27, 30, 35), (0, 200, 200) ]
    expected = [(137, 10, 191, 31), (95, 121, 95, 121), (149, 47, 149, 47), None]
    return do_test_es2(file_png, colori, expected)

def test_es2_2():
    """
    Test 2: Bounding boxes dei colori 
    [ (0, 0, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 255, 255) ] 
    estratti da '6-rectangles.png'"""
    file_png = '6-rectangles.png'
    colori = [ (255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 0, 0), (255, 255, 255), (0, 255, 0), (0, 0, 255), 
            (255, 0, 0), ]
    expected = [ (0, 0, 499, 499), (100, 100, 300, 300), (150, 50, 340, 90), (110, 60, 160, 150), (280, 120, 330, 170),
            (310, 80, 350, 130), (120, 130, 140, 180), None,]
    return 1 + do_test_es2(file_png, colori, expected)

def test_es2_3():
    """
    Test 3: Bounding boxes dei colori 
    colori = [ (0, 0, 0), (103, 50, 77), (109, 147, 61), (128, 193, 157), (130, 116, 144), (134, 82, 243),
            (151, 165, 252), (174, 61, 80), (175, 148, 56), (185, 164, 178), (186, 224, 199), 
            (202, 250, 104), (206, 227, 189), (208, 64, 140), (214, 252, 215), (255, 0, 0),        
            (255, 255, 0), (255, 255, 255), (91, 150, 235), (91, 156, 214), (92, 63, 152), (93, 169, 204), ]
    estratti da 'random-150-1074-863.png'"""
    file_png = 'random-150-1074-863.png'
    colori = [ (0, 0, 0), (103, 50, 77), (109, 147, 61), (128, 193, 157), (130, 116, 144), (134, 82, 243),
            (151, 165, 252), (174, 61, 80), (175, 148, 56), (185, 164, 178), (186, 224, 199), 
            (202, 250, 104), (206, 227, 189), (208, 64, 140), (214, 252, 215), (255, 0, 0),        
            (255, 255, 0), (255, 255, 255), (91, 150, 235), (91, 156, 214), (92, 63, 152), (93, 169, 204), ]
    expected = [ (0, 0, 1073, 862), (614, 227, 707, 310), (461, 445, 557, 515), (76, 450, 164, 525),
        (899, 48, 994, 117), (12, 466, 111, 532), (60, 504, 155, 571), (774, 209, 855, 287),
        (132, 678, 230, 741), (211, 340, 285, 420), (819, 166, 884, 257), (125, 312, 190, 402),
        (167, 366, 238, 448), (197, 637, 275, 711), (219, 539, 279, 634), (597, 269, 675, 342),
        (343, 691, 402, 786), (692, 158, 766, 232), (929, 90, 1003, 163), None, None, None, ]
    return 1 + do_test_es2(file_png, colori, expected)

#################################################################################

from tree import BinaryTree

def fromList(encoded_tree):
    if encoded_tree is None: return None
    ID, left, right = encoded_tree
    return BinaryTree(ID, fromList(left), fromList(right))

def toList(tree):
    if tree is None: return None
    return [ tree.ID, toList(tree.left), toList(tree.right) ]

def do_test_es3(lista, k, expected):
    lista1 = copy.deepcopy(lista)
    albero1= fromList(lista1)
    
    try:
        isrecursive.decorate_module(program)
        program.es3(albero1,k)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)

    albero = fromList(lista)
    program.es3(albero, k)
    lista_res = toList(albero)
    testlib.check(lista_res, expected)
    return 3

def test_es3_1():
    '''
    Albero dell'esempio
    '''
    lista = [6, [7, [2, None, None], 
                    [4, [15, None, None], 
                        None]], 
                [5, [6, None, None], 
                    [8, None, 
                        [10, None, None]]]]
    k = 5
    expected = [6, [7, [2, None, None], 
                       [4, [0, None, None], 
                           None]], 
                   [24, None, None]]
    return do_test_es3(lista, k, expected)

def test_es3_2():
    '''
Albero 2
                          76                            
            ______________|_______________              
           |                              |             
          595                             37            
                                 _________|_____        
                                |               |       
                               71              100     
                             __|__            __|___    
                            |     |          |      |   
                            92   65         23      121 
                             ____|______      \      \  
                            |           |      0     44 
                            70          8               
                                         \              
                                          67            
che deve diventare
                          76                            
            ______________|_______________              
           |                              |             
           0                              37            
                                 _________|_____        
                                |               |       
                               71              188     
                             __|__                      
                            |     |                     
                            92   145                       

'''
    lista = [76, [595, None, None], 
                    [37, [71, [92, None, None], 
                              [65, [70, None, None], 
                                   [8, None, 
                                       [67, None, None]]]], 
                         [100, [23, None, 
                                    [0, None, None]], 
                               [121, None, 
                                     [44, None, None]]]]]
    k = 5
    expected = [76, [0, None, None], 
                    [37, [71, [92, None, None], 
                              [145, None, None]],
                         [188, None, None]]] 
    return do_test_es3(lista, k, expected)

def test_es3_3():
    '''
Albero 3
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |               |       
   80             15           71              100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
5     19        47      96  92   67         23      121 
   ___|___    __|___         ____|______      \      \  
  |       |  |      |       |           |     81     44 
  181     28 94     29      70          8               
                                         \              
                                          30            
                                          _|_           
                                         |   |          
                                        46  21          
che deve diventare

                          76                            
            ______________|_______________              
           |                              |             
          594                             37            
                                 _________|_____        
                                |               |       
                               71              100     
                             __|__            __|___    
                            |     |          |      |   
                            92   67         23      121 
                             ____|______      \      \  
                            |           |      0     44 
                            70          8               
                                         \              
                                          67            
'''
    lista=[76, [12, [80,
                        [5,None,None],
                        [19, [181,None,None],
                             [28,None,None]]],
                     [15, [47, [94,None,None],
                               [29,None,None]],
                          [96,None,None]]],
               [37, [71, [92,None,None],
                         [67, [70,None,None],
                              [8, None, 
                                  [30, [46,None,None],
                                       [21,None,None]]]]],
                    [100, [23, None,
                               [81,None,None]],
                          [121, None,
                                [44,None,None]]]]]
    k = 3
    expected = [76, [594, None, None], 
                    [37, [71, [92, None, None], 
                              [67, [70, None, None], 
                                   [8, None, 
                                       [67, None, None]]]], 
                         [100, [23, None, 
                                    [0, None, None]], 
                               [121, None, 
                                     [44, None, None]]]]]
    return do_test_es3(lista, k, expected)

###############################################################################
def fromListN(lista):
    ID, *sons = lista
    return tree.NaryTree(ID, [ fromListN(son) for son in sons ])

def do_test_es4(lista, k, expected):
    radice = fromListN(lista)

    try:
        isrecursive.decorate_module(program)
        program.es4(radice,k)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)

    res = program.es4(radice,k)
    testlib.check(res, expected)
    return 3

def test_es4_1():
    ''' 
    Esempio:                  17
                              |
            -------------------------------------------
            |      |          |         |             |
            13     21        95        32            26
            |      |          |                       |
        --------   |     ---------------------        |
        |   |  |   |     |   |   |   |   |   |        |
        4   7  9   5    -3  -4  -5  -6   -8  -10      42
    '''
    lista = [17, [13, [4], [7], [9] ],
                 [21, [5] ],
                 [95, [-3], [-4], [-5], [-6], [-8], [-10], ],
                 [32],
                 [26, [42]],
            ]
    k = 4
    expected = 1, 78
    return do_test_es4(lista, k, expected)

def test_es4_2():
    ''' 
    Esempio:                  17
                              |
            -------------------------------------------
            |      |          |         |             |
            13     21        95        32            26
            |      |          |                       |
        --------   |          |                       |
        |   |  |   |          |                       |
        4   7  9   5         -3                      42
                              |
                             -4
                              |
                             -5
                              |
                             -6
                              |
                    --------------------
                    |   |  |  |  |  |  |
                    28 29 30 31 32 33 34
    '''
    lista = [17, [13, [4], [7], [9]],
                 [21, [5]],
                 [95, [-3, [-4, [-5, [-6, [28], [29], [30], [31], [32], [33], [34]]]]]],
                 [32],
                 [26, [42]],
            ]
    k = 5
    expected = 5, -23
    return do_test_es4(lista, k, expected)

def test_es4_3():
    ''' 
    Esempio:                  17
                              |
                   ------------
                   |          |
                   21        95
                   |          |
                   |          |
                   |          |
                   5         -3
                   |          |
                   6         -4
                   |          |
                   7         -5
                   |          |
                   8         -6
                   |          |
             -------         -7
             |  |  |          |
            11 12 13          |
                        ----------------
                        |  |  |  |  |  |
                       29 30 31 32 33 34
    '''
    lista = [17, [21, [5, [6, [7, [8, [11], [12], [13]]]]]],
                 [95, [-3, [-4, [-5, [-6, [-7, [29], [30], [31], [32], [33], [34]]]]]]],
            ]
    k = 3
    expected = 1, -15
    return do_test_es4(lista, k, expected)

###################################################################################

def test_nome_cognome_matricola():
    assert program.matricola != 'MATRICOLA', "Inserisci la tua matricola all'inizio del file"
    assert program.cognome   != 'COGNOME',   "Inserisci il tuo cognome all'inizio del file"
    assert program.nome      != 'NOME',      "Inserisci il tuo nome all'inizio del file"

###################################################################################

tests = [
    # PER DISATTIVARE ALCUNI TEST BASTA COMMENTARE LE RIGHE CHE SEGUONO
    test_es1_1, test_es1_2, test_es1_3,     # lista di dizionari
    test_es2_1, test_es2_2, test_es2_3,     # bounding boxes
    test_es3_1, test_es3_2, test_es3_3,     # albero binario
    test_es4_1, test_es4_2, test_es4_3,      # albero n-ario
    test_nome_cognome_matricola,
    ]

if __name__ == '__main__':
    # runtests(tests)
    testlib.runtests(tests, logfile='grade.csv')

###############################################################################

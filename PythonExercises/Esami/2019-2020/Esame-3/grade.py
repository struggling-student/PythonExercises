#! /usr/bin/env python3 -B

from testlib import check, runtests, check_text_file, check_img_file, check_json_file
import isrecursive

import albero

import program

###############################################################################
def test_nome_cognome_matricola():
    assert program.nome        != 'NOME',      "ATTENZIONE, NON HAI INSERITO IL TUO NOME NEL FILE program.py !!!"
    assert program.cognome     != 'COGNOME',   "ATTENZIONE, NON HAI INSERITO IL TUO COGNOME NEL FILE program.py !!!"
    assert program.matricola   != 'MATRICOLA', "ATTENZIONE, NON HAI INSERITO LA TUA MATRICOLA NEL FILE program.py !!!"
    return 0

###############################################################################

def test_es1a_1():
    ''' \nPrimo test della funzione es1 con fname='mat1.txt'
    '''
    lista1= [[1,2],[3,4],[5,6]]
    ris = program.es1('mat1.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),list, None," la lista restituita deve contenere liste")
    check(type(ris[0][0]),int, None," la lista di liste restituita deve contenere interi")
    check(ris, lista1, None, " la matrice restituita  non e' corretta")
    return 2

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con fname='mat2.txt'
    '''
    lista1= [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 
    ris = program.es1('mat2.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),list, None," la lista restituita deve contenere liste")
    check(type(ris[0][0]),int, None," la lista di liste restituita deve contenere interi")
    check(ris, lista1, None, " la matrice restituita  non e' corretta")
    return 2

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con fname='mat3.txt'
    '''
    lista1= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27], 
    [0, 4, 8, 12, 16, 20, 24, 28, 32, 36], 
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45], 
    [0, 6, 12, 18, 24, 30, 36, 42, 48, 54], 
    [0, 7, 14, 21, 28, 35, 42, 49, 56, 63], 
    [0, 8, 16, 24, 32, 40, 48, 56, 64, 72], 
    [0, 9, 18, 27, 36, 45, 54, 63, 72, 81]
    ]
    ris = program.es1('mat3.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),list, None," la lista restituita deve contenere liste")
    check(type(ris[0][0]),int, None," la lista di liste restituita deve contenere interi")
    check(ris, lista1, None, " la matrice restituita  non e' corretta")
    return 2

################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 con k=4 e  Rettangoli.png'''
    ris1={((0, 0, 255), (0, 255, 0), (100, 100, 100), (255, 0, 0)): {(39, 60), (39, 59), (40, 59), (40, 60)}}
    ris= program.es2(4, 'Rettangoli.png')
    check(type(ris),dict, None,"la funzione deve restituire un dizionario")
    check(ris,ris1,None,"il dizionario  restituito   non e' corretto")
    return 2

def test_es2a_2():
    '''\nSecondo test della funzione es2 con k=3 e Rettangoli.png'''
    ris1={
    ((0, 255, 0), (100, 100, 100), (255, 0, 0)): {(39, 20), (39, 19), (40, 19), (40, 20)}, 
    ((0, 0, 0), (0, 255, 0), (255, 0, 0)): {(70, 59), (70, 60), (69, 60), (69, 59)}
    }
    ris= program.es2(3, 'Rettangoli.png')
    check(type(ris),dict, None,"la funzione deve restituire un dizionario ")
    check(ris,ris1,None,"il dizionario  restituito   non e' corretto")
    return 2

def test_es2a_3():
    '''\nTerzo test della funzione es2 con k=2 e Rettangoli.png'''
    ris1={
    ((0, 255, 0), (255, 0, 0)): {(40, 3), (44, 59), (39, 4), (50, 60), (39, 17), (40, 13), (53, 59), (40, 0), (48, 59), (39, 11), (61, 60), (51, 60), (40, 10), (57, 59), (40, 16), (39, 14), (51, 59), (46, 59), (62, 60), (52, 60), (40, 7), (39, 0), (39, 13), (65, 59), (57, 60), (40, 4), (63, 60), (58, 59), (54, 59), (39, 7), (39, 16), (52, 59), (40, 14), (47, 59), (40, 1), (58, 60), (48, 60), (45, 60), (39, 10), (65, 60), (66, 59), (61, 59), (41, 59), (40, 11), (56, 59), (40, 17), (55, 59), (59, 60), (39, 9), (66, 60), (40, 8), (39, 3), (64, 59), (59, 59), (39, 12), (60, 60), (41, 60), (42, 59), (67, 60), (40, 5), (39, 6), (67, 59), (40, 15), (42, 60), (62, 59), (68, 60), (40, 2), (45, 59), (39, 5), (60, 59), (46, 60), (40, 12), (56, 60), (53, 60), (43, 60), (40, 18), (49, 59), (39, 8), (68, 59), (40, 9), (63, 59), (47, 60), (43, 59), (54, 60), (44, 60), (39, 2), (64, 60), (39, 15), (40, 6), (49, 60), (39, 1), (55, 60), (50, 59), (39, 18)}, 
    ((0, 0, 0), (255, 0, 0)): {(70, 40), (69, 48), (69, 15), (70, 12), (69, 28), (70, 19), (69, 41), (70, 38), (69, 38), (70, 53), (69, 51), (70, 56), (69, 2), (70, 9), (69, 31), (70, 28), (69, 44), (70, 35), (69, 57), (70, 54), (69, 54), (69, 8), (70, 7), (69, 5), (70, 10), (69, 18), (70, 25), (69, 47), (70, 44), (70, 51), (69, 11), (70, 0), (69, 24), (70, 23), (69, 21), (70, 26), (69, 34), (70, 41), (69, 14), (70, 13), (69, 27), (70, 16), (69, 40), (70, 39), (69, 37), (70, 42), (69, 50), (70, 57), (69, 1), (70, 14), (69, 30), (70, 29), (69, 43), (70, 32), (69, 56), (70, 55), (69, 53), (70, 58), (70, 4), (69, 4), (70, 11), (69, 17), (70, 30), (69, 46), (70, 45), (70, 48), (69, 10), (70, 1), (69, 7), (70, 20), (69, 20), (70, 27), (69, 33), (70, 46), (69, 13), (70, 2), (69, 26), (70, 17), (69, 23), (70, 36), (69, 36), (70, 43), (69, 49), (69, 0), (70, 15), (69, 29), (70, 18), (69, 42), (70, 33), (69, 39), (70, 52), (69, 52), (70, 5), (69, 3), (70, 8), (69, 16), (70, 31), (69, 45), (70, 34), (69, 58), (70, 49), (69, 55), (69, 9), (70, 6), (69, 6), (70, 21), (69, 19), (70, 24), (69, 32), (70, 47), (70, 50), (69, 12), (70, 3), (69, 25), (70, 22), (69, 22), (70, 37), (69, 35)}, 
    ((0, 255, 0), (100, 100, 100)): {(19, 19), (0, 20), (15, 20), (31, 19), (20, 20), (17, 20), (22, 19), (38, 20), (37, 20), (18, 19), (4, 19), (7, 19), (13, 20), (18, 20), (33, 20), (34, 19), (20, 19), (16, 19), (23, 19), (29, 20), (34, 20), (9, 19), (32, 19), (25, 19), (37, 19), (9, 20), (14, 19), (30, 20), (10, 19), (35, 20), (1, 19), (13, 19), (6, 20), (5, 20), (11, 20), (35, 19), (10, 20), (16, 20), (31, 20), (25, 20), (36, 20), (26, 19), (38, 19), (29, 19), (8, 19), (15, 19), (11, 19), (1, 20), (7, 20), (22, 20), (21, 20), (12, 20), (2, 19), (26, 20), (27, 20), (32, 20), (24, 19), (36, 19), (27, 19), (2, 20), (23, 20), (28, 20), (0, 19), (12, 19), (5, 19), (28, 19), (3, 20), (8, 20), (30, 19), (21, 19), (17, 19), (3, 19), (14, 20), (4, 20), (19, 20), (24, 20), (6, 19), (33, 19)}, 
    ((100, 100, 100), (255, 0, 0)): {(39, 46), (40, 45), (39, 26), (39, 33), (40, 55), (40, 22), (40, 32), (40, 31), (39, 50), (40, 41), (39, 30), (39, 37), (40, 51), (40, 27), (39, 54), (40, 37), (39, 41), (40, 46), (39, 21), (39, 32), (40, 56), (40, 23), (39, 58), (40, 33), (39, 45), (40, 42), (39, 25), (39, 36), (40, 52), (40, 28), (39, 49), (40, 38), (39, 29), (39, 40), (40, 48), (40, 47), (40, 57), (39, 35), (40, 24), (39, 53), (40, 34), (39, 44), (40, 43), (39, 24), (39, 39), (40, 53), (39, 57), (40, 29), (39, 48), (40, 39), (39, 55), (39, 28), (39, 43), (40, 49), (39, 23), (39, 34), (40, 58), (40, 25), (39, 52), (40, 35), (39, 47), (40, 44), (39, 27), (39, 38), (40, 54), (40, 21), (39, 56), (40, 30), (39, 51), (40, 40), (39, 31), (39, 42), (40, 50), (39, 22), (40, 26), (40, 36)}, 
    ((0, 0, 255), (100, 100, 100)): {(23, 60), (14, 59), (30, 60), (12, 59), (8, 60), (5, 60), (25, 60), (31, 60), (26, 59), (21, 59), (1, 59), (15, 59), (19, 60), (6, 60), (26, 60), (16, 60), (29, 59), (24, 59), (19, 59), (20, 60), (1, 60), (7, 60), (37, 60), (2, 59), (27, 60), (33, 59), (27, 59), (2, 60), (22, 59), (38, 60), (28, 60), (5, 59), (20, 59), (0, 59), (13, 60), (3, 60), (33, 60), (34, 59), (30, 59), (9, 59), (28, 59), (23, 59), (3, 59), (14, 60), (4, 60), (34, 60), (24, 60), (37, 59), (17, 59), (32, 59), (9, 60), (15, 60), (31, 59), (10, 59), (35, 60), (6, 59), (4, 59), (10, 60), (35, 59), (0, 60), (36, 60), (17, 60), (18, 59), (13, 59), (8, 59), (7, 59), (21, 60), (11, 60), (18, 60), (38, 59), (36, 59), (16, 59), (11, 59), (22, 60), (12, 60), (32, 60), (29, 60), (25, 59)}, 
    ((0, 0, 0), (0, 255, 0)): {(95, 60), (96, 59), (90, 59), (91, 59), (85, 59), (86, 59), (92, 60), (73, 60), (79, 60), (95, 59), (80, 59), (74, 59), (75, 59), (99, 60), (86, 60), (76, 60), (84, 59), (96, 60), (79, 59), (93, 60), (83, 60), (90, 60), (80, 60), (77, 60), (89, 59), (97, 60), (98, 59), (99, 59), (74, 60), (93, 59), (94, 59), (73, 59), (81, 60), (87, 60), (88, 59), (82, 59), (83, 59), (77, 59), (78, 59), (94, 60), (84, 60), (92, 59), (71, 60), (87, 59), (72, 59), (91, 60), (78, 60), (98, 60), (76, 59), (88, 60), (71, 59), (85, 60), (97, 59), (75, 60), (82, 60), (72, 60), (81, 59), (89, 60)}, 
    ((0, 0, 255), (0, 255, 0)): {(40, 88), (39, 70), (39, 83), (39, 92), (40, 79), (39, 98), (40, 66), (40, 85), (39, 62), (39, 69), (39, 86), (40, 76), (39, 97), (40, 95), (40, 82), (39, 61), (39, 72), (39, 85), (40, 73), (40, 92), (39, 66), (39, 79), (40, 98), (39, 88), (40, 70), (40, 89), (39, 65), (39, 82), (40, 61), (39, 95), (40, 67), (40, 86), (39, 68), (39, 81), (40, 77), (39, 96), (40, 64), (40, 83), (39, 75), (39, 84), (40, 74), (40, 93), (40, 80), (39, 78), (40, 99), (39, 91), (40, 71), (40, 90), (39, 64), (39, 77), (40, 96), (40, 62), (39, 94), (40, 68), (40, 87), (39, 71), (39, 80), (39, 93), (40, 78), (39, 99), (40, 65), (40, 84), (39, 63), (39, 74), (39, 87), (40, 75), (40, 94), (40, 81), (39, 73), (39, 90), (40, 72), (40, 91), (39, 67), (39, 76), (40, 97), (40, 63), (39, 89), (40, 69)}
    }
    ris= program.es2(2, 'Rettangoli.png')
    check(type(ris),dict, None,"la funzione deve restituire un dizionario")
    check(ris,ris1,None,"il dizionario  restituito   non e' corretto")
    return 3

################################################################################

def test_es3a(lista1, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es3(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1        = albero.fromLista(lista1)
    ris= program.es3(tree1)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista deve contenere triple")
    check(ris, expected ,None,"la lista restituita  non e' corretta")
    return 3

def test_es3a_1():
    '''\nPrimo test della funzione es3 con tree uguale all'albero binario in basso a sinistra
          
          
     0    
    / \   
   5   5  
      /   
     3    
    / \   
   9   7  
          
    '''
    lista1= [0,[5, None, None],[5,[3,[9, None, None],[7, None, None]],None]]  
    lista=[(0, 0, 5), (3, 0, 2), (5, 0, 0), (5, 1, 2), (7, 0, 0), (9, 0, 0)]
    return test_es3a(lista1,lista)
    
def test_es3a_2():
    '''\nSecondo test della funzione es3 con tree uguale all'albero in basso a sinistra
    
                    36              
             _______|______         
            |              |        
            26             10       
         ___|___        ___|__      
        |       |      |      |     
        3       7      3     15     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   2   3   4  5   6  7   8   
                                    

    '''

    lista1=[36,
             [26,
                [3,[1,None,None],[2,None,None]],
                [15,[3,None,None],[4,None,None]],
             ], 
             [10,
                [3,[5,None,None],[6,None,None]],
                [15,[7,None,None],[8,None,None]],
             ]
            ]
    lista=[
           (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 2), (3, 2, 0), (4, 0, 0), (5, 0, 0), 
           (6, 0, 0), (7, 0, 0), (8, 0, 0), (10, 5, 1),(15, 2, 0), (15, 2, 0), (26, 6, 0), (36, 14, 0)
           ]
    return test_es3a(lista1,lista)

def test_es3a_3():
    '''\nTerzo test della funzione es3 con tree uguale all'albero in basso a sinistra
    
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
    '''
    lista1=[76,
              [12,
                 [80,
                    [5,None,None],
                    [19,
                       [181,None,None],
                       [28,None,None],
                    ],
                  ],
                 [15,
                    [47,
                       [94,None,None],
                       [29,None,None],
                    ],
                    [96,None,None],
                  ],
              ],
              [37,
                 [71,
                   [92,None,None],
                   [67,
                      [70,None,None],
                      [8,None,
                         [30,
                           [46,None,None],
                           [21,None,None],
                          ],
                       ],
                   ],
                  ],
                 [100,
                     [23,None,
                        [81,None,None],
                      ],
                     [121,None,
                          [44,None,None],
                      ],
                 ],
               ],
]

    lista=[
    (5, 0, 0), (8, 0, 3), (12, 1, 9), (15, 0, 4), (19, 0, 2), (21, 0, 0), (23, 0, 1), (28, 0, 0), 
    (29, 0, 0), (30, 1, 1), (37, 4, 9), (44, 0, 0), (46, 0, 0), (47, 1, 1), (67, 4, 1), (70, 0, 0), 
    (71, 6, 1), (76, 17, 8), (80, 3, 1), (81, 0, 0), (92, 0, 0), (94, 0, 0), (96, 0, 0), (100, 3, 1),
     (121, 1, 0), (181, 0, 0)]
    return test_es3a(lista1,lista)+1

###############################################################################
def test_es4a(dirname, insieme, expected):
    try:
        isrecursive.decorate_module(program)
        program.es4(dirname,insieme)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es4(dirname,insieme)
    check(type(ris),int,None," bisogna restituire un intero")
    check(ris, expected ,None,"l'intero restituito non e' corretto")
    return 3

def test_es4a_1():
    dirname = 'dir1'
    insieme ={'txt','pdf'}
    expected = 5
    return test_es4a(dirname,insieme, expected)

def test_es4a_2():
    dirname = 'dir2'
    insieme ={'c','py',}
    expected = 7
    return test_es4a(dirname, insieme,  expected)

def test_es4a_3():
    dirname = 'dir3'
    insieme ={'txt','py','png','back'}
    expected=49 
    return test_es4a(dirname,insieme, expected)

###############################################################################

tests = [
    # PER DISATTIVARE ALCUNI TEST BASTA COMMENTARE LE RIGHE CHE SEGUONO
    test_es1a_1, test_es1a_2, test_es1a_3,
    test_es2a_1,  test_es2a_2, test_es2a_3,
    test_es3a_1, test_es3a_2, test_es3a_3,
    test_es4a_1, test_es4a_2, test_es4a_3,
    test_nome_cognome_matricola,
    ]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################


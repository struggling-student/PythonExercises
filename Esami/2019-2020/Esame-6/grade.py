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
    ''' \nPrimo test della funzione es1 con fname='f1.txt'
    '''
    d={25: ['577020', '5624466'], 6: ['6', '677'], 1: ['3122233']}
    ris = program.es1('f1.txt')
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(type(min(ris)),int, None," le chiavi del dizionario devono essere interi")
    check(type(ris[min(ris)]),list, None," gli attributi del dizionario devono essere liste")
    check(ris, d, None, " il dizionario restituito non e' corretto")
    return 2

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con fname='f2.txt'
    '''
    d={
    8: ['1118110'], 
    18: ['2228221'], 
    28: ['3338332'], 
    38: ['4448443'], 
    48: ['5558554'], 
    58: ['6668665'], 
    68: ['7778776'], 
    1: ['1', '221'], 
    0: ['110'], 
    2: ['2', '332'], 
    3: ['3', '443'], 
    4: ['4', '554'], 
    5: ['5', '665'], 
    6: ['6', '776'], 
    7: ['7']
    } 
    ris = program.es1('f2.txt')
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(type(min(ris)),int, None," le chiavi del dizionario devono essere interi")
    check(type(ris[min(ris)]),list, None," gli attributi del dizionario devono essere liste")
    check(ris, d, None, " il dizionario restituito non e' corretto")
    return 2

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con fname='f3.txt'
    '''
    d={
    1: ['1', '10'], 
    234: ['234', '2340'], 
    145: ['12245', '102245', '1022450'], 
    2: ['2', '2', '20', '20', '200', '200'], 
    45: ['45', '450', '4500'], 
    3: ['3', '30', '300'], 
    4: ['3334', '30334', '303340'], 
    6: ['556', '5056', '50560'], 
    0: ['330', '30344', '70788']
    } 
    ris = program.es1('f3.txt')
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(type(min(ris)),int, None," le chiavi del dizionario devono essere interi")
    check(type(ris[min(ris)]),list, None," gli attributi del dizionario devono essere liste")
    check(ris, d, None, " il dizionario restituito non e' corretto")
    return 2

    
################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 sull'immagine   Rettangoli.png e insiemi di colori 
    A={(0,255,0), (255,0,0)}  e B={(0,0,0)}'''
    A,B={(0,255,0), (255,0,0)},{(0,0,0)}
    ris1=([], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 
         55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69])
    ris= program.es2('Rettangoli.png',A,B)
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(type(ris[0]),list, None,"la tupla restituita deve contenere liste ")
    check(type(ris[1]),list, None,"la tupla restituita deve contenere liste ")
    check(ris,ris1,None,"la tupla restituita non e' corretta")
    return 2

def test_es2a_2():
    '''\nSecondo test della funzione es2 sull'immagine   Rettangoli.png e insiemi di colori 
    A={(0,0,0), (255,0,0)}  e B={(0,255,0)}'''
    A,B={(0,0,0), (255,0,0)},{(0,255,0)}
    ris1=([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
           40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], []) 
    ris= program.es2('Rettangoli.png',A,B)
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(type(ris[0]),list, None,"la tupla restituita deve contenere liste ")
    check(type(ris[1]),list, None,"la tupla restituita deve contenere liste ")
    check(ris,ris1,None,"la tupla restituita non e' corretta")
    return 2

def test_es2a_3():
    '''\nTerzo test della funzione es2 sull'immagine   Rettangoli.png e insiemi di colori 
    A={(0,255,0), (255,0,0)}  e B={(0,0,0)}'''
    A,B={(0,0,0)},{(0,0,255)}
    ris1=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
           40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], 
         [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89])
    ris= program.es2('Rettangoli.png',A,B)
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(type(ris[0]),list, None,"la tupla restituita deve contenere liste ")
    check(type(ris[1]),list, None,"la tupla restituita deve contenere liste ")
    check(ris,ris1,None,"la tupla restituita non e' corretta")
    return 3

################################################################################

def test_es3a(lista1,cammini, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es3(tree1,cammini)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1        = albero.fromLista(lista1)
    ris= program.es3(tree1,cammini)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista deve contenere interi")
    check(ris, expected ,None,"la lista restituita  non e' corretta")
    return 3

def test_es3a_1():
    '''\nPrimo test della funzione es3 con tree uguale all'albero binario in basso a sinistra
    e lista dei cammini ['0', '10', '100']
          
          
     0    
    / \   
   5   6  
      /   
     3    
    / \   
   9   7  
          
    '''
    lista1= [0,[5, None, None],[6,[3,[9, None, None],[7, None, None]],None]]  
    lista=[5, 3, 9]
    cammini=['0', '10', '100']
    return test_es3a(lista1,cammini,lista)
    
def test_es3a_2():
    '''\nSecondo test della funzione es3 con tree uguale all'albero in basso a sinistra
    e lista dei cammini ['000', '111', '01','10']
    
                    36              
             _______|______         
            |              |        
            26             10       
         ___|___        ___|__      
        |       |      |      |     
        3       55     3     15     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   2   3   4  5   6  7   8   
                                    
    
    '''

    lista1=[36,
             [26,
                [3,[1,None,None],[2,None,None]],
                [55,[3,None,None],[4,None,None]],
             ], 
             [10,
                [3,[5,None,None],[6,None,None]],
                [15,[7,None,None],[8,None,None]],
             ]
            ]
    lista=[1, 8, 55, 3]
    cammini=['000', '111', '01','10']
    return test_es3a(lista1,cammini,lista)

def test_es3a_3():
    '''\nTerzo test della funzione es3 con tree uguale all'albero in basso a sinistra 
    e lista dei cammini ['0100', '0011', '010','1','11','101','101111','1101']
    
    
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

    lista=lista=[94,28,47,37,100,67,21,81]
    cammini=['0100', '0011', '010','1','11','101','101111','1101']
    return test_es3a(lista1,cammini, lista)+1

###############################################################################
def test_es4a(dirname, expected):
    try:
        isrecursive.decorate_module(program)
        program.es4(dirname)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es4(dirname)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"il dizionario restituito non e' corretto")
    return 3

def test_es4a_1():
    dirname = 'dir1'
    expected = {
    'dir1/stanza1/stanza2': ['png', 'py', 'txt'], 
    'dir1/stanza1': [], 
    'dir1': ['c', 'exe', 'pdf', 'txt']
    } 
    return test_es4a(dirname, expected)

def test_es4a_2():
    dirname = 'dir2'
    expected = {
       'dir2/stanza3/stanza3d': [], 
       'dir2/stanza3/stanza3c/stanza3c1': [], 
       'dir2/stanza3/stanza3c': ['txt'], 
       'dir2/stanza3': [], 
       'dir2/stanza4': ['exe', 'png'], 
       'dir2/stanza2': ['c', 'py'], 
       'dir2/stanza1/stanza1b': ['iii', 'png', 'py', 'txt'], 
       'dir2/stanza1': [], 
       'dir2': ['c']
    }
    return test_es4a(dirname,  expected)

def test_es4a_3():
    dirname = 'dir3'
    expected={
        'dir3/B2': ['txt'], 
        'dir3/B3/C': ['txt'], 
        'dir3/B3': [], 
        'dir3/B4/A3b/B2': ['txt'], 
        'dir3/B4/A3b/B3/C': ['txt'], 
        'dir3/B4/A3b/B3': [], 
        'dir3/B4/A3b/B4': ['txt'], 
        'dir3/B4/A3b/B1/A5/B2': ['txt'], 
        'dir3/B4/A3b/B1/A5/B3/C': ['txt'], 
        'dir3/B4/A3b/B1/A5/B3': [], 
        'dir3/B4/A3b/B1/A5/B4': ['txt'], 
        'dir3/B4/A3b/B1/A5/B1': ['txt'], 
        'dir3/B4/A3b/B1/A5': ['png', 'txt'], 
        'dir3/B4/A3b/B1': ['txt'], 
        'dir3/B4/A3b': ['png', 'txt'], 
        'dir3/B4': ['txt'], 
        'dir3/B1': ['txt'], 
        'dir3': ['png', 'py', 'txt']
    }
    return test_es4a(dirname, expected)

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


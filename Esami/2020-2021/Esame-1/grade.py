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
    ris1=[(7, 8), (11, 30), (8, 8), (6, 8)]
    ris = program.es1('f1.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple, None," gli elementi della lista devono essere tuple")
    check(ris, ris1, None, " la lista restituita non e' corretta")
    return 2

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con fname='f2.txt'
    '''
    ris1=[(4, 1), (3, 1), (1, 1), (8, 16), (10, 32), (12, 64)]
    ris = program.es1('f2.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple, None," gli elementi della lista devono essere tuple")
    check(ris, ris1, None, " la lista restituita  non e' corretta")
    return 2

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con fname='f3.txt'
    '''
    ris1=[(105, 0), (102, 200), (150, 105000), (105, 0), (102, 200), 
    (150, 105000), (105, 0), (102, 200), (150, 105000)]
    ris = program.es1('f3.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple, None," gli elementi della lista devono essere tuple")
    check(ris, ris1, None, " la lista restituita  non e' corretta")
    return 3

    
################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 sull'immagine   fig1.png '''
    ris= program.es2('fig1.png')
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(ris,(3,2),None,"la tupla restituita non e' corretta")
    return 2

def test_es2a_2():
    '''\nSecondo test della funzione es2 sull'immagine   fig2.png'''
    ris= program.es2('fig2.png')
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(ris, (6,8),None,"la tupla restituita non e' corretta")
    return 3

def test_es2a_3():
    '''\nTerzo test della funzione es2 sull'immagine  fig3.png'''
    ris= program.es2('fig3.png')
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(ris, (4,4),None,"la tupla restituita non e' corretta")
    return 3

################################################################################

def test_es3a(lista1,lista2, expected):
    tree1   = albero.fromLista(lista1)
    tree2   = albero.fromLista(lista2)
    try:
        isrecursive.decorate_module(program)
        program.es3(tree1,tree2)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1   = albero.fromLista(lista1)
    tree2   = albero.fromLista(lista2)
    ris= program.es3(tree1,tree2)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista deve contenere coppie")
    check(ris, expected ,None,"la lista restituita  non e' corretta")
    return 3

def test_es3a_1():
    '''\nPrimo test della funzione es3 sui  due  alberi binari: 
                                                                
     0            0                                             
    / \          / \                                            
   5   6        5   1                                           
      /            /                                            
     3            3                                             
    / \          / \                                            
   9   7        2   7                                           
                                                                
    '''                                                         
    lista1= [0,[5, None, None],[6,[3,[9, None, None],[7, None, None]],None]] 
    lista2= [0,[5, None, None],[1,[3,[2, None, None],[7, None, None]],None]] 
    risposta=[(9,2),(6,1)]
    return test_es3a(lista1,lista2,risposta)-1
    
def test_es3a_2():
    '''\nSecondo test della funzione es3 sui due alberi:
    
                    36                                  36              
             _______|______                      _______|______         
            |              |                    |              |        
            26             10                   66             10       
         ___|___        ___|__               ___|___        ___|__      
        |       |      |      |             |       |      |      |     
        3       55     3     15             3       1      3     15     
       _|_     _|_    _|_    _|_           _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |         |   |   |   |  |   |  |   |   
      1   2   3   4  5   6  7   8         1   2   3   4  5   1  1   8   
                                                                        
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
    lista2=[36,
             [66,
                [3,[1,None,None],[2,None,None]],
                [1,[3,None,None],[4,None,None]],
             ], 
             [10,
                [3,[5,None,None],[1,None,None]],
                [15,[1,None,None],[8,None,None]],
             ]
            ]
    
    risposta=[(55, 1), (26, 66), (7, 1), (6, 1)] 
    return test_es3a(lista1,lista2,risposta)

def test_es3a_3():
    '''\nTerzo test della funzione es3 sui due alberi in basso:
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
                                                        
                                                        
                          760                           
            ______________|_______________              
           |                              |             
          120                             37            
    _______|_______              _________|_____        
   |               |            |               |       
   800             15           71              100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
50   190       47      96  92    67         23      121 
   ___|___    __|___         ____|______      \      \  
  |       |  |      |       |           |     81     44 
  1810   280 94     29      70          8               
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
    lista2=[760,
              [120,
                 [800,
                    [50,None,None],
                    [190,
                       [1810,None,None],
                       [280,None,None],
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

    risposta=[(181, 1810), (80, 800), (76, 760), (28, 280), (19, 190), (12, 120), (5, 50)] 
    return test_es3a(lista1,lista2, risposta)

###############################################################################
def test_es4a(dirname,s, expected):
    try:
        isrecursive.decorate_module(program)
        program.es4(dirname,s)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es4(dirname,s)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"il dizionario restituito non e' corretto")
    return 3

def test_es4a_1():
    '''\nPrimo test della funzione es4 con dirname= 'dir1' e s='arco' '''
    dirname = 'dir1'
    s='arco'
    expected = {'parco': 1, 'arco': 3, 'Marco': 1, 'sarcofago': 1}
    return test_es4a(dirname,s, expected)

def test_es4a_2():
    '''\nSecondo test della funzione es4 con dirname= 'dir1' e s='oca' '''
    dirname = 'dir1'
    s='oca'
    expected = {'foca': 1, 'locale': 2, 'ocarina': 1, 'fotocamera': 1, 
    'focalizzatore': 1, 'giocare': 1, 'monolocale': 2} 
    return test_es4a(dirname,s,  expected)

def test_es4a_3():
    '''\nTerzo test della funzione es4 con dirname= 'dir2' e s='occo' '''
    dirname = 'dir2'
    s='occo'
    expected = {'fiocco': 1, 'brocco': 1, 'allocco': 3, 'scroccone': 3, 
    'marocco': 1, 'ritocco': 1, 'tarocco': 1, 'occorrenza': 1, 'cioccolata,': 1, 
    'fiocco,': 1, 'brocco,': 1, 'barocco,': 1, 'blocco,': 1, 'gnocco,': 1, 
    'sbocco,': 1, 'broccoli': 1} 
    return test_es4a(dirname,s,  expected)

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


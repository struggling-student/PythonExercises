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
    ris1=[[8,11,3],[8,9,12]]
    ris = program.es1('f1.txt')
    check(type(ris),list,None," bisogna restituire una lista ")
    check(type(ris[0]),list, None," gli elementi della lista devono essere liste")
    check(ris, ris1, None, " la lista restituita non e' corretta")
    return 2

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con fname='f2.txt'
    '''
    ris1=[[3, 6, 9], [3, 7, 9], [6, 8, 6]]
    ris = program.es1('f2.txt')
    check(type(ris),list,None," bisogna restituire una lista ")
    check(type(ris[0]),list, None," gli elementi della lista devono essere liste")
    check(ris, ris1, None, " la lista restituita  non e' corretta")
    return 2

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con fname='f3.txt'
    '''
    ris1=[[3, 6], [9, 3], [6, 9], [3, 6], [9, 3]]
    ris = program.es1('f3.txt')
    check(type(ris),list,None," bisogna restituire una lista ")
    check(type(ris[0]),list, None," gli elementi della lista devono essere liste")
    check(ris, ris1, None, " la lista restituita  non e' corretta")
    return 3

    
################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 sull'immagine   fig1.png '''
    ris= program.es2('fig1.png')
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(ris,(90,125),None,"la tupla restituita non e' corretta")
    return 2

def test_es2a_2():
    '''\nSecondo test della funzione es2 sull'immagine   fig2.png'''
    ris= program.es2('fig2.png')
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(ris, (20,150),None,"la tupla restituita non e' corretta")
    return 3

def test_es2a_3():
    '''\nTerzo test della funzione es2 sull'immagine  fig3.png'''
    ris= program.es2('fig3.png')
    check(type(ris),tuple, None,"la funzione deve restituire una tupla")
    check(ris, (90,140),None,"la tupla restituita non e' corretta")
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
    
    tree1   = albero.fromLista(lista1)
    ris= program.es3(tree1)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista deve contenere interi")
    check(ris, expected ,None,"la lista restituita  non e' corretta")
    return 3

def test_es3a_1():
    '''\nPrimo test della funzione es3 sui  due  alberi binari: 
     0          
    / \         
   5   6        
      /         
     3          
    / \         
   9   7        
    '''                                                         
    lista1= [0,[5, None, None],[6,[3,[9, None, None],[7, None, None]],None]] 
    risposta=[0, 3]
    return test_es3a(lista1,risposta) - 1
    
def test_es3a_2():
    '''\nSecondo test della funzione es3 sull'albero:
    
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
    
    risposta=[3,15,55] 
    return test_es3a(lista1, risposta)

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
5     19        47      96  92   67          5     121 
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
                     [5,None,
                        [81,None,None],
                      ],
                     [121,None,
                          [44,None,None],
                      ],
                 ],
               ],
]


    risposta=[5, 15, 19, 30, 47, 67, 71, 80, 121] 
    return test_es3a(lista1, risposta)

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
    check(type(ris),list,None," bisogna restituire una lista")
    check(ris, expected ,None,"la lista restituita  non e' corretta")
    return 3

def test_es4a_1():
    '''\nPrimo test della funzione es4 con dirname= 'dir1'  '''
    dirname = 'dir1'
    expected = ['dir1/stanza1/stanza2']
    return test_es4a(dirname, expected)

def test_es4a_2():
    '''\nSecondo test della funzione es4 con dirname= 'dir2'  '''
    dirname = 'dir2'
    expected =['dir2/stanza1/stanza1b', 'dir2/stanza2', 
    'dir2/stanza3/stanza3c/stanza3c1', 'dir2/stanza3/stanza3d', 'dir2/stanza4']  
    return test_es4a(dirname,  expected)

def test_es4a_3():
    '''\nTerzo test della funzione es4 con dirname= 'dir3'  '''
    dirname = 'dir3'
    expected = ['dir3/B1', 'dir3/B2', 'dir3/B3/C', 'dir3/B4/A3b/B1/A5/B1', 'dir3/B4/A3b/B1/A5/B2', 
    'dir3/B4/A3b/B1/A5/B3/C', 'dir3/B4/A3b/B1/A5/B4', 'dir3/B4/A3b/B2', 
    'dir3/B4/A3b/B3/C', 'dir3/B4/A3b/B4']
    return test_es4a(dirname,  expected)

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


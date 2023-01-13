#! /usr/bin/env python3 -B

from testlib import check, runtests, check_text_file, check_img_file, check_json_file
import isrecursive

import tree

import program

###############################################################################
def test_nome_cognome_matricola():
    assert program.nome        != 'NOME',      "ATTENZIONE, NON HAI INSERITO IL TUO NOME NEL FILE program.py !!!"
    assert program.cognome     != 'COGNOME',   "ATTENZIONE, NON HAI INSERITO IL TUO COGNOME NEL FILE program.py !!!"
    assert program.matricola   != 'MATRICOLA', "ATTENZIONE, NON HAI INSERITO LA TUA MATRICOLA NEL FILE program.py !!!"
    return 0

###############################################################################

def test_es1a_1():
    ''' \nPrimo test della funzione es1 con fname='U1.txt'
    '''
    lista1= [5049, 10, 49, 66, 94, 0] 
    ris = program.es1('U1.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int, None," la lista restituita deve contenere interi")
    check(ris, lista1, None, " la lista restituita  non e' corretta")
    return 2

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con fname='U2.txt'
    '''
    lista2= [44444, 1032, 1234, 1302, 3210, 4444, 12, 32]
    ris = program.es1('U2.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista restituita deve contenere interi")
    check(ris, lista2, None, " la lista restituita  non e' corretta")
    return 2

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con fname='U3.txt'
    '''
    lista3= [35406, 1032, 1234, 1234, 1302, 2042, 3210, 3210, 4444, 4444, 4607, 102, 12, 12, 32, 33]
    ris = program.es1('U3.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista restituita deve contenere interi")
    check(ris, lista3, None, " la lista restituita  non e' corretta")
    return 2
    
################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 con f2a.png'''
    P1={(20,10),(20,20),(20,40),(40,40),(50,20),(50,70),(60,20)}
    ris= program.es2(P1,'r2a.png')
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,1,None,"l' intero restituito    non e' corretto")
    check_img_file('r2a.png', 'f2a.png')
    return 2

def test_es2a_2():
    '''\nSecondo test della funzione es2 con f2b.png'''
    P2={(10,10),(20,10),(10,20),(20,20),(20,25),
    (30,30),(40,30),(40,30),(30,35),
    (40,40),(50,40),(60,40),
    (40,50),(50,50),(60,50),
    (50,60),(50,60),(60,60)}
    ris= program.es2(P2, 'r2b.png')
    check(type(ris),int, None,"la funzione deve restituire unintero")
    check(ris,4,None,"l'intero restituito     non e' corretto")
    check_img_file('r2b.png', 'f2b.png')
    return 3

def test_es2a_3():
    '''\nTerzo test della funzione es2 con f2c.png'''
    P3={(20,10),(20,60),(30,20),(30,50),(30,60),(40,30),(40,60),
    (50,20),(50,60),(50,80),(60,40),(60,60),(60,65),(60,70),
    (70,20),(70,40),(70,60),(70,90),(80,40),(80,60),(20,65)
    }
    ris= program.es2(P3,'r2c.png')
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,6,None,"l'intero non e' corretto")
    check_img_file('r2c.png', 'f2c.png')
    return 3

################################################################################

def test_es3a(lista1, expected):
    tree1   = tree.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es3(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1        = tree.fromLista(lista1)
    ris= program.es3(tree1)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"il dizionario restituito non e' corretto")
    return 3

def test_es3a_1():
    '''\nPrimo test della funzione es3 con tree uguale all'albero in basso a sinistra
    
              16                
      ________|_____________   
     |          |           |  
     2          4           5  
     |     _____|______        
     10   |   |  |  |  |       
          1   2  9  8  2       
            __|__              
           |     |             
           3     6             

    '''
    lista1= [16, [[2, [[10, []]]], [4, [[1, []], [2, [[3, []], [6, []]]], [9, []], [8, []],[2, []]]],[5, []]]]    
    d1={3: [16], 1: [2], 0: [1, 2, 3, 5, 6, 8, 9, 10], 5: [4], 2: [2]} 
    return test_es3a(lista1,d1)
    
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
    lista1=[36,[[26,[[3,[[1,[]],
                         [2,[]]]],
                    [7,[[3,[]],
                         [4,[]]]]]],
                [10,[[3,[[5,[]], 
                          [6,[]]]],
                     [15,[[7,[]],
                          [8,[]]]]]]]]
 
    d1={2: [3, 3, 7, 10, 15, 26, 36], 0: [1, 2, 3, 4, 5, 6, 7, 8]} 
    return test_es3a(lista1,d1)

def test_es3a_3():
    '''\nTerzo test della funzione es3 con tree uguale all'albero in basso a sinistra
    
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |      |        |       
   80             15           71     39        100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
5     19        47      96  92   67         23      121 
   ___|___    __|___         ____|______     |      |   
  |       |  |      |       |     |     |    |      |   
  181     28 94     29      70    83    8   81     44   
                                        |               
                                       30               
                                       _|_              
                                      |   |             
                                     46  21             
    '''
    lista1= [76, [[12, [[80, [[5, []], 
                              [19, [[181, []], 
                                    [28, []]]]]], 
                        [15, [[47, [[94, []], 
                                    [29, []]]],
                              [96, []]]]]], 
                  [37, [[71, [[92, []], 
                              [67, [[70, []], 
                                    [83, []], 
                                    [8, [[30, [[46, []], 
                                               [21, []]]]]]]]]], 
                        [39, []], 
                        [100, [[23, [[81, []]]], 
                               [121, [[44, []]]]]]]]]]
    d1={
    2: [12, 15, 19, 30, 47, 71, 76, 80, 100], 
    0: [5, 21, 28, 29, 39, 44, 46, 70, 81, 83, 92, 94, 96, 181], 
    3: [37, 67], 
    1: [8, 23, 121]
    }
    return test_es3a(lista1,d1)

###############################################################################
def test_es4a(dirname,parola, expected):
    try:
        isrecursive.decorate_module(program)
        program.es4(dirname,parola)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es4(dirname,parola)
    check(type(ris),list,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"la lista  non e' corretta")
    return 3

def test_es4a_1():
    dirname = 'dir1'
    parola='angelo'
    expected = [('dir1/st1/st2/1W.txt', 4), ('dir1/st1/st2/Ncn.txt', 5), ('dir1/zzzEFG.txt', 1)]
    return test_es4a(dirname, parola, expected)

def test_es4a_2():
    dirname = 'dir2'
    parola='AndreA'
    expected = [('dir2/st1/st1b/z.txt', 6), ('dir2/st3/st3c/rf1.txt', 1)]
    return test_es4a(dirname, parola,  expected)

def test_es4a_3():
    dirname = 'dir3'
    parola='AngeloS'
    expected = [('dir3/B1/b.txt', 3), ('dir3/B2/ax.txt', 2), 
    ('dir3/B3/C/z.txt', 5), ('dir3/B4/q.txt', 1), ('dir3/a.txt', 1)]
    return test_es4a(dirname,parola, expected)

###############################################################################

tests = [
    # PER DISATTIVARE ALCUNI TEST BASTA COMMENTARE LE RIGHE CHE SEGUONO
    test_es1a_1, test_es1a_2, test_es1a_3,
    test_es2a_1, test_es2a_2, test_es2a_3,
    test_es3a_1, test_es3a_2, test_es3a_3,
    test_es4a_1, test_es4a_2, test_es4a_3,
    test_nome_cognome_matricola,
    ]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################


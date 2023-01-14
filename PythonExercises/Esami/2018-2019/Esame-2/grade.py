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
    ''' \nPrimo test della funzione es1 con lista: [1,10,3,3,2,10,3,8,2,3]
     '''
    lista1=[1,10,3,3,2,10,3,8,2,3]
    lista1b=[1,10,3,3,2,10,3,8,2,3]
    r1=[3,2,10,1,8]
    ris = program.es1(lista1)
    check(type(ris),list ,None," bisogna restituire una lista")
    check(ris, r1, None, " la lista restituita non e' corretta")
    check(lista1, lista1b, None, " la lista di input non va modificata")
    return 1

def test_es1a_2():
    ''' \nsecondo test della funzione es1 con lista: 
    [1,2,2,3,4,5,5,5,6,6,6,6,7,7,7,8,9,8]
     '''
    lista1=[1,2,2,3,4,5,5,5,6,6,6,6,7,7,7,8,9,8]
    lista1b=[1,2,2,3,4,5,5,5,6,6,6,6,7,7,7,8,9,8]
    r1=[6, 5, 7, 2, 8, 1, 3, 4, 9]
    ris = program.es1(lista1)
    check(type(ris),list ,None," bisogna restituire una lista")
    check(ris, r1, None, " la lista restituita non e' corretta")
    check(lista1, lista1b, None, " la lista di input non va modificata")
    return 1

def test_es1a_3():
    ''' \nterzo test della funzione es1 con lista: 
    [1,10,0,2,20,2,20,3,0,30,3,30,3,30,4,0,4,4,0,4,40,40,40,0,40]
     '''
    lista1=[1,10,0,2,20,2,20,3,0,30,3,30,3,30,4,0,4,4,0,4,40,40,40,0,40]
    lista1b=[1,10,0,2,20,2,20,3,0,30,3,30,3,30,4,0,4,4,0,4,40,40,40,0,40]
    r1=[0, 4, 40, 3, 30, 2, 20, 1, 10]
    ris = program.es1(lista1)
    check(type(ris),list ,None," bisogna restituire una lista")
    check(ris, r1, None, " la lista restituita non e' corretta")
    check(lista1, lista1b, None, " la lista di input non va modificata")
    return 1

##########################################################################################

def test_es2a_1():
    ''' \nPrimo test della funzione es2 con lista= ['lucio', 'anna', 'federico', 'roberto']
    '''
    lista1= ['lucio', 'anna', 'federico', 'roberto']
    lista1b=['l**io','****','fede*i*o','ro*er*o']
    ris = program.es2(lista1)
    check(type(ris),list,None," bisogna restituire una lista")
    check(ris, lista1b, None, " la lista restituita  non e' corretta")
    return 1

def test_es2a_2():
    ''' \nSecondo test della funzione es2 con 
    lista= ['zero','uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto','nove']
    '''
    lista2= ['zero','uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto','nove']
    lista2b=['**ro', '**o', '**e', '*r*', 'q**ttro', '*inq*e', '**i', 's****', '****', 'no**']
    ris = program.es2(lista2)
    check(type(ris),list,None," bisogna restituire una lista")
    check(ris, lista2b, None, " la lista restituita  non e' corretta")
    return 1

def test_es2a_3():
    ''' \nTerzo test della funzione es2 con 
    lista= ['fondamenti', 'calcolo', 'metodi', 'metodologie', 'architetture', 'progettazione']
    '''
    lista3= ['fondamenti', 'calcolo', 'metodi', 'metodologie', 'architetture', 'progettazione']
    lista3b=['fond*men*i', 'c*lc*l*', 'me*o*i', 'me*o*ologie', '*rchitett*re', 'progett**ione']
    ris = program.es2(lista3)
    check(type(ris),list,None," bisogna restituire una lista")
    check(ris, lista3b, None, " la lista restituita  non e' corretta")
    return 1
    
################################################################################

def test_es3a_1():
    '''\nPrimo test della funzione es3 sul file f3a.txt'''
    lista1=[8,-2,-60,5]
    ris= program.es3('f3a.txt')
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,lista1,None,"la lista  non e' corretta")
    return 1

def test_es3a_2():
    '''\nSecondo test della funzione es3 sul file f3b.txt'''
    lista1=[1, -3, -1, 3, 1, -3, -1, 3]
    ris= program.es3('f3b.txt')
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,lista1,None,"la lista  non e' corretta")
    return 1

def test_es3a_3():
    '''\nTerzo test della funzione es3 sul file f3c.txt'''
    lista1=[-4, -4, -4, -6, -6, -6, -5, -5,-5]
    ris= program.es3('f3c.txt')
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,lista1,None,"la lista  non e' corretta")
    return 2
    
################################################################################
def test_es4a_1():
    '''\nPrimo test della funzione es4 con f4.png  e pixel (20,20)'''
    ris1=80
    ris= program.es4('f4.png',20,20)
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,ris1,None,"il valore non e' corretto")
    return 1

def test_es4a_2():
    '''\nSecondo test della funzione es4 con f4.png e pixel (40,20)'''
    ris2=80
    ris= program.es4('f4.png',40,20)
    check(type(ris),int,None,"la funzione deve restituire un intero")
    check(ris,ris2,None,"il valore non e' corretto")
    return 1

def test_es4a_3():
    '''\nTerzo test della funzione es4 con f4.png e pixel (60,40)'''
    ris3=61
    ris= program.es4('f4.png',60,40)
    check(type(ris),int ,None,"la funzione deve restituire un intero")
    check(ris,ris3,None,"il valore restituito non e' corretto")
    return 2
################################################################################

def test_es5a(lista1, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es5(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1   = albero.fromLista(lista1)
    ris= program.es5(tree1)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"il dizionario restituito non e' corretto")
    return 2


def test_es5a_1():
    '''\nPrimo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
                    10                 
             _______|______            
            |              |           
            3              7           
         ___|___        ___|__         
        |       |      |      |        
        1       2      3      4        
                                       
    '''
    lista1=[10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]]
    d1={0: {1, 2, 3, 4}, 2: {10, 3, 7}}
    return test_es5a(lista1,d1)
    
def test_es5a_2():
    '''\nTerzo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
                    36              
             _______|______         
            |              |        
            10             26       
         ___|___        ___|__      
        |       |      |      |     
        3       7     11     15     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   2   3   4  5   6  7   8   
                                    

    '''
    lista2=[36,[[10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]],[26,[[11,[[5,[]],
    [6,[]]]],[15,[[7,[]],[8,[]]]]]]]]
    d2={0: {1, 2, 3, 4, 5, 6, 7, 8}, 2: {3, 26, 36, 7, 10, 11, 15}} 
    return test_es5a(lista2,d2)


def test_es5a_3():
    '''\nTerzo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |      |        |       
   15             80           71     39        100     
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
    listaA3= [76, [[12, [[15, [[5, []], [19, [[181, []], [28, []]]]]],
    [80, [[47, [[94, []], [29, []]]],[96, []]]]]], [37, [[71, [[92, []], 
    [67, [[70, []], [83, []], [8, [[30, [[46, []], [21, []]]]]]]]]],
    [39, []], [100, [[23, [[81, []]]], [121, [[44, []]]]]]]]]]
    d3={
     0: {96, 5, 70, 39, 44, 46, 92, 81, 83, 181, 21, 28, 29, 94}, 
     1: {8, 121, 23}, 3: {67, 37},
     2: {100, 71, 12, 76, 15, 80, 47, 19, 30} 
    }
    return test_es5a(listaA3,d3)

################################################################################

def test_es6a(indirizzo,cartella, expected):
    try:
        isrecursive.decorate_module(program)
        program.es6(indirizzo,cartella)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es6(indirizzo,cartella)
    check(type(ris),str,None,"bisogna restituire una stringa")
    check(ris,expected,None,"la stringa  restituita non e' corretta")
    return 2


def test_es6a_1():
    '''\nPrimo test della funzione es6 con indirizzo cartella ='Informatica' e 
    seconda cartella = 'RISC'
    '''
    return test_es6a('Informatica','RISC','Informatica/Hardware/Architetture/Processori/RISC')

def test_es6a_2():
    '''\nPrimo test della funzione es6 con indirizzo cartella ='Informatica' e 
    seconda cartella = 'Basi'
    '''
    return test_es6a('Informatica','Basi','')

def test_es6a_3():
    '''\nPrimo test della funzione es6 con indirizzo cartella ='Informatica/Software' e 
    seconda cartella = 'ManualeMac'
    '''
    return test_es6a('Informatica/Software','ManualeMac','Informatica/Software/SistemiOperativi/OSX/ManualeMac')

###############################################################################
def test_es7a(lista1, expected, expectedList):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es7(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1        = albero.fromLista(lista1)
    ris= program.es7(tree1)
    resultingList= albero.toLista(tree1)
    check(type(ris),int,None," bisogna restituire un intero")
    check(ris, expected ,None,"il numero di nodi modificati non e' corretto")
    check(resultingList, expectedList, None, "L'albero risultante non è corretto")
    return 2

def test_es7a_1():
    '''\nPrimo test della funzione es7 con tree uguale all'albero in basso a sinistra
    
                    10                 
             _______|______            
            |              |           
            3              7           
         ___|___        ___|__         
        |       |      |      |        
        1       2      3      4        
                                       
    '''
    lista1=[10,[[3,[[1,[]],
                    [2,[]]]],
                [7,[[3,[]],
                    [4,[]]]]]]
    N     = 2
    lista2=[10, [[3, [[2, []], 
                      [1, []]]], 
                 [7, [[4, []], 
                      [3, []]]]]]
    return test_es7a(lista1,N,lista2)
    
def test_es7a_2():
    '''\nTerzo test della funzione es7 con tree uguale all'albero in basso a sinistra
    
                    36              
             _______|______         
            |              |        
            10             26       
         ___|___        ___|__      
        |       |      |      |     
        3       7     11     15     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   2   3   4  5   6  7   8   
                                    

    '''
    lista1=[36,[[10,[[3,[[1,[]],
                         [2,[]]]],
                [7,[[3,[]],
                    [4,[]]]]]],
                [26,[[11,[[5,[]], 
                          [6,[]]]],
                     [15,[[7,[]],
                          [8,[]]]]]]]]
    N     = 2
    lista2=[36, [[10, [[7, [[3, []], 
                            [4, []]]], 
                       [3, [[1, []], 
                            [2, []]]]]], 
                 [26, [[15, [[7, []], 
                             [8, []]]], 
                       [11, [[5, []], 
                             [6, []]]]]]]]
    return test_es7a(lista1,N,lista2)

def test_es7a_3():
    '''\nTerzo test della funzione es7 con tree uguale all'albero in basso a sinistra
    
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |      |        |       
   15             80           71     39        100     
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
    lista1= [76, [[12, [[15, [[5, []], 
                              [19, [[181, []], 
                                    [28, []]]]]], 
                        [80, [[47, [[94, []], 
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
    N     = 6
    lista2=[76, [[12, [[80, [[47, [[29, []], 
                                   [94, []]]], 
                             [96, []]]], 
                       [15, [[5, []], 
                             [19, [[28, []], 
                                   [181, []]]]]]]], 
                 [37, [[39, []], 
                       [100, [[23, [[81, []]]], 
                              [121, [[44, []]]]]], 
                       [71, [[92, []], 
                             [67, [[83, []], 
                                   [8, [[30, [[21, []], 
                                              [46, []]]]]], 
                                   [70, []]]]]]]]]]
    return test_es7a(lista1,N,lista2)

###############################################################################

tests = [
    test_nome_cognome_matricola,
    test_es1a_1, test_es1a_2, test_es1a_3,
    test_es2a_1, test_es2a_2, test_es2a_3,
    test_es3a_1, test_es3a_2, test_es3a_3,
    test_es4a_1, test_es4a_2, test_es4a_3,
    test_es5a_1, test_es5a_2, test_es5a_3,
    test_es6a_1, test_es6a_2, test_es6a_3,
    test_es7a_1, test_es7a_2, test_es7a_3,
    ]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################


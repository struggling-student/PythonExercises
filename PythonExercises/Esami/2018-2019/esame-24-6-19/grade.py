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
    ''' \nPrimo test della funzione es1 con lista=[5,2,5,5,2,3,5,3,2,5,1,1]'''
    lista1=[5,2,5,5,2,3,5,3,2,5,1,1]
    listar=[5,2,3,1]
    risp= program.es1(lista1)
    check(type(risp),int,None,"la funzione deve restituire un intero")
    check(risp,8,None,"l'intero restituito non e' corretto")
    check(lista1,listar,None, "la lista non e' stata modificata correttamente")
    return 1

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con lista=[1,1,2,2,3,3,3,3,2,2,1,1]'''
    lista2=[1,1,2,2,3,3,3,3,2,2,1,1]
    listar=[1,2,3]
    risp= program.es1(lista2)
    check(type(risp),int,None,"la funzione deve restituire un intero")
    check(risp,9,None,"l'intero restituito non e' corretto")
    check(lista2,listar,None, "la lista non e' stata modificata correttamente")
    return 1
    
def test_es1a_3():
    ''' \nTerzo test della funzione es1 con lista=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]'''
    lista3=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]
    listar=[1,2,3,4,5,6]
    risp= program.es1(lista3)
    check(type(risp),int,None,"la funzione deve restituire un intero")
    check(risp,10,None,"l'intero restituito non e' corretto")
    check(lista3,listar,None, "la lista non e' stata modificata correttamente")
    return 1

##########################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 con matrice
      9,2,3,4,4,3
      3,8,4,8,1,5
      3,3,4,1,2,6
      9,5,7,6,4,6
    '''
    mat1=[[9,2,3,4,4,3],[3,8,4,8,1,5],[3,3,4,1,2,6],[9,5,7,6,4,6]]
    ris1=([1, 8], [5, 6, 7, 9])
    risp= program.es2(mat1)
    check(type(risp),tuple,None,"la funzione deve restituire una tupla")
    check(type(risp[0]),list,None,"la prima componente della tupla deve essere una lista")
    check(type(risp[1]),list,None,"la seconda  componente della tupla deve essere una lista")
    check(risp,ris1,None,"la tupla restituita non e' corretta")
    return 1

    
def test_es2a_2():
    '''\nSecondo test della funzione es2 con matrice
       1,1,1
       1,0,1
       1,1,1 
    '''
    mat2=[[1,1,1],[1,0,1],[1,1,1],]
    ris2=([0],[1])
    risp= program.es2(mat2)
    check(type(risp),tuple,None,"la funzione deve restituire una tupla")
    check(type(risp[0]),list,None,"la prima componente della tupla deve essere una lista")
    check(type(risp[1]),list,None,"la seconda  componente della tupla deve essere una lista")
    check(risp,ris2,None,"la tupla restituita non e' corretta")
    return 1


def test_es2a_3():
    '''\nTerzo test della funzione es2 con mat=
      1,1,1,1 
      1,1,2,1
      2,2,2,2
    '''
    mat3=[[1,1,1,1],[1,1,2,1],[2,2,2,2]]
    ris3=([],[])
    risp= program.es2(mat3)
    check(type(risp),tuple,None,"la funzione deve restituire una tupla")
    check(type(risp[0]),list,None,"la prima componente della tupla deve essere una lista")
    check(type(risp[1]),list,None,"la seconda  componente della tupla deve essere una lista")
    check(risp,ris3,None,"la tupla restituita non e' corretta")
    return 1
    
################################################################################

def test_es3a_1():
    '''\nPrimo test della funzione es3 sul file f3a.txt'''
    ris1=(2,-3)
    ris= program.es3('f3a.txt')
    check(type(ris),tuple,None,"la funzione deve restituire una tupla")
    check(ris,ris1,None,"la tupla  non e' corretta")
    return 1
    
def test_es3a_2():
    '''\nSecondo test della funzione es3 sul file f3b.txt'''
    ris2=(0,1)
    ris= program.es3('f3b.txt')
    check(type(ris),tuple,None,"la funzione deve restituire una tupla")
    check(ris,ris2,None,"la tupla  non e' corretta")
    return 1
    
def test_es3a_3():
    '''\nTerzo test della funzione es3 sul file f3c.txt'''
    ris3=(-1,-1)
    ris= program.es3('f3c.txt')
    check(type(ris),tuple,None,"la funzione deve restituire una tupla")
    check(ris,ris3,None,"la tupla  non e' corretta")
    return 1
    
################################################################################
def test_es4a(lista1, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es4(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1   = albero.fromLista(lista1)
    ris= program.es4(tree1)
    check(type(ris),list,None,"bisogna restituire una lista")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 2


def test_es4a_1():
    '''\nPrimo test della funzione es4 con tree uguale all'albero in basso a sinistra
                                  
               5                  
      ________|_____________      
     |          |           |     
     20         4           6     
     |     _____|______           
     12   |   |  |  |  |          
          10  2  9  8  7          
            __|__                 
           |     |                
           30   22               

    '''
    listaA1= [5, [[20, [[12, []]]], [4, [[10, []], [2, [[30, []], [22, []]]], 
    [9, []], [8, []],[7, []]]],[6, []]]]
    #tree1   = albero.fromLista(listaA1)
    lista1=[1, 2, 3]
    return test_es4a(listaA1,lista1)
   
def test_es4a_2():
    '''\nSecondo test della funzione es4 con tree uguale all'albero in basso a sinistra
    
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
    listaA2=[36,[[10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]],[26,[[11,[[5,[]],
    [6,[]]]],[15,[[7,[]],[8,[]]]]]]]]
    lista2=[3]
    return test_es4a(listaA2,lista2)


def test_es4a_3():
    '''\nTerzo test della funzione es4 con tree uguale all'albero in basso a sinistra
    
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
    lista3=[2, 3, 4, 6] 
    return test_es4a(listaA3,lista3)
    
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
    check(type(ris),list,None,"bisogna restituire una lista")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 3


def test_es5a_1():
    '''\nPrimo test della funzione es5 con tree uguale all'albero in basso a sinistra
                                  
               5                  
      ________|_____________      
     |          |           |     
     20         4           6     
     |     _____|______           
     12   |   |  |  |  |          
          10  2  9  8  7          
            __|__                 
           |     |                
           30   22               

    '''
    listaA1= [5, [[20, [[12, []]]], [4, [[10, []], [2, [[30, []], [22, []]]], 
    [9, []], [8, []],[7, []]]],[6, []]]]
    lista1=[ 2, 4, 5]
    return test_es5a(listaA1,lista1)
   
def test_es5a_2():
    '''\nSecondo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
                    36              
             _______|______         
            |              |        
            10             26       
         ___|___        ___|__      
        |       |      |      |     
        3       7     11     15     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      6   2   3   4  5   1  7   8   
                                    

    '''
    listaA2=[36,[[10,[[3,[[6,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]],[26,[[11,[[5,[]],
    [1,[]]]],[15,[[7,[]],[8,[]]]]]]]]
    lista2=[1,11,26,36]
    return test_es5a(listaA2,lista2)


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
50     19        47      96  92   67         23      121 
   ___|___    __|___         ____|______     |      |   
  |       |  |      |       |     |     |    |      |   
  181     28 94     5      70     83    8   81     44   
                                        |               
                                       30               
                                       _|_              
                                      |   |             
                                     46  21             
    '''
    listaA3= [76, [[12, [[15, [[50, []], [19, [[181, []], [28, []]]]]],
    [80, [[47, [[94, []], [5, []]]],[96, []]]]]], [37, [[71, [[92, []], 
    [67, [[70, []], [83, []], [8, [[30, [[46, []], [21, []]]]]]]]]],
    [39, []], [100, [[23, [[81, []]]], [121, [[44, []]]]]]]]]]
    lista3=[5, 47, 80, 12, 76]
    return test_es5a(listaA3,lista3)

################################################################################

def test_es6a_1():
    '''\nPrimo test della funzione es6 con f6.png  e (20,20)'''
    ris1=80
    ris= program.es6('f6.png',20,20)
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,ris1,None,"il valore non e' corretto")
    return 2

def test_es6a_2():
    '''\nSecondo test della funzione es6 con f6.png e (20,50)'''
    ris2=191
    ris= program.es6('f6.png',20,50)
    check(type(ris),int,None,"la funzione deve restituire un intero")
    check(ris,ris2,None,"il valore non e' corretto")
    return 2

def test_es6a_3():
    '''\nTerzo test della funzione es2 con f6.png e (30,60)'''
    ris3=91
    ris= program.es6('f6.png',30,60)
    check(type(ris),int ,None,"la funzione deve restituire un intero")
    check(ris,ris3,None,"il valore restituito non e' corretto")
    return 2

###############################################################################

def test_es7a_1():
    '''\nPrimo test della funzione es6 con k=3 e
    stringa1='uoccazaodaaaoboccbnzbnznbz' 
    stringa2='aaaobnzazaodnbzocc'
    '''
    stringa1='uoccazaodaaaoboccbnzbnznbz' 
    stringa2='aaaobnzazaodnbzocc'
    ris1=['bnz', 'nbz', 'aaa', 'aza', 'occ', 'aao', 'aob', 'aod', 'zao']
    ris= program.es7(stringa1,stringa2,3)
    check(type(ris),list, None,"la funzione deve restituire una lista")
    check(ris,ris1,None,"la lista restituita non e' corretta")
    return 1

def test_es7a_2():
    '''\nSecondo test della funzione es6 con k=3 e
    stringa1='uoccazaodaaaoboccbnzbnznbz' 
    stringa2='aaaobnzazaodnbzocc'
    '''
    stringa1='uoccazaodaaaoboccbnzbnznbz' 
    stringa2='aaaobnzazaodnbzocc'
    ris2=['aaao', 'aaob', 'azao', 'zaod']
    ris= program.es7(stringa1,stringa2,4)
    check(type(ris),list, None,"la funzione deve restituire una lista")
    check(ris,ris2,None,"la lista restituita non e' corretta")
    return 1

def test_es7a_3():
    '''\nTerzo test della funzione es2 con con k=1 e
    stringa1='uoccazaodaaaoboccbnzbnznbz' 
    stringa2='aaaobnzazaodnbzocc'
    '''
    stringa1='uoccazaodaaaoboccbnzbnznbz' 
    stringa2='aaaobnzazaodnbzocc'
    ris3=['b', 'c', 'd', 'n', 'z', 'a', 'o']
    ris= program.es7(stringa1,stringa2,1)
    check(type(ris),list, None,"la funzione deve restituire una lista")
    check(ris,ris3,None,"la lista restituita non e' corretta")
    return 1


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


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
    ''' \nPrimo test della funzione es1 con s='aaxbaaxb' e k=3
     '''
    lista1=[('aax', 2), ('axb', 2), ('baa', 1), ('xba', 1)]
    ris = program.es1('aaxbaaxb',3)
    check(type(ris),list ,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista restituita deve contenere tuple")
    check(ris, lista1, None, " la lista restituita non e' corretta")
    return 1

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con s='aaxbaaxb' e k=3
     '''
    lista2=[('aa', 2), ('zz', 2), ('za', 1)]
    ris = program.es1('zzzaaa',2)
    check(type(ris),list ,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista restituita deve contenere tuple")
    check(ris, lista2, None, " la lista restituita non e' corretta")
    return 1
    
def test_es1a_3():
    ''' \nTerzo test della funzione es1 con s='abcdefgabcdefgabcdefg' e k=5
     '''
    lista3=[('edcba', 3), ('fedcb', 3), ('gfedc', 3), ('agfed', 2), 
    ('bagfe', 2), ('cbagf', 2), ('dcbag', 2)]
    ris = program.es1('gfedcbagfedcbagfedcba',5)
    check(type(ris),list ,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista restituita deve contenere tuple")
    check(ris, lista3, None, " la lista restituita non e' corretta")
    return 1
##########################################################################################

def test_es2a_1():
    ''' \nPrimo test della funzione es2 con 
    lista1= [(10,20,40),(60,30,20),(20,30,20),(70,40,20),(50,60,10)]
    '''
    lista1= [(10,20,40),(60,30,20),(20,30,20),(70,40,20),(50,60,10)]
    lista2=[(10,20,40),(20,30,20),(50,60,10)]
    ris = program.es2(lista1)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista restituita deve contenere tuple")
    check(ris, lista2, None, " la lista restituita  non e' corretta")
    return 1

def test_es2a_2():
    ''' \nSecondo test della funzione es2 con 
    lista1=[(60,30,20),(50,60,10),(10,20,40),(20,30,20),(70,40,20)]
    '''
    lista1=[(60,30,20),(50,60,10),(10,20,40),(20,30,20),(70,40,20)]
    lista2=[(60,30,20),(70,40,20)]
    ris = program.es2(lista1)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista restituita deve contenere tuple")
    check(ris, lista2, None, " la lista restituita  non e' corretta")
    return 1

def test_es2a_3():
    ''' \nTerzo test della funzione es2 con 
    lista1= [(10,10,5),(20,20,5),(30,30,5),(40,40,5),(12,12,10)]
    '''
    lista1= [(10,10,5),(20,20,5),(30,30,5),(40,40,5),(12,12,10)]
    lista2=[(10, 10, 5), (12, 12, 10)]
    ris = program.es2(lista1)
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),tuple,None," la lista restituita deve contenere tuple")
    check(ris, lista2, None, " la lista restituita  non e' corretta")
    return 2
    
################################################################################

def test_es3a_1():
    '''\nPrimo test della funzione es3 sul file f3a.png'''
    lista1=[(0, 0, 0), (255, 0, 0)]
    ris= program.es3('f3a.png')
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,lista1,None,"la lista  non e' corretta")
    return 1

def test_es3a_2():
    '''\nSecondo test della funzione es3 sul file f3b.png'''
    lista2=[(0, 255, 0), (0, 0, 0), (255, 0, 0), (0, 0, 255)]
    ris= program.es3('f3b.png')
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,lista2,None,"la lista  non e' corretta")
    return 1

def test_es3a_3():
    '''\nTerzo test della funzione es3 sul file f3c.png'''
    lista3=[(75, 74, 60), (235, 186, 140), (215, 172, 130), 
            (195, 158, 120), (175, 144, 110), (155, 130, 100), 
            (135, 116, 90), (115, 102, 80), (95, 88, 70)]
    ris= program.es3('f3c.png')
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,lista3,None,"la lista  non e' corretta")
    return 1
    
################################################################################
def test_es4a_1():
    '''\nPrimo test della funzione es4 con f4a.png'''
    ris1=60
    ris= program.es4('f4a.png')
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,ris1,None,"il valore non e' corretto")
    return 2

def test_es4a_2():
    '''\nSecondo test della funzione es4 con f4b.png'''
    ris1=100
    ris= program.es4('f4b.png')
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,ris1,None,"il valore non e' corretto")
    return 2

def test_es4a_3():
    '''\nTerzo test della funzione es4 con f4c.png'''
    ris1=191
    ris= program.es4('f4c.png')
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,ris1,None,"il valore non e' corretto")
    return 2
################################################################################

def test_es5a(lista1, expected, expectedList):
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
    
    tree1        = albero.fromLista(lista1)
    ris= program.es5(tree1)
    resultingList= albero.toLista(tree1)
    check(type(ris),int,None," bisogna restituire un intero")
    check(ris, expected ,None,"il valore estituito non e' corretto")
    check(resultingList, expectedList, None, "L'albero risultante non è corretto")
    return 1



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
    lista2=[10, [[6, []], [14, []]]]
    return test_es5a(lista1,10, lista2) +1
    
def test_es5a_2():
    '''\nSecondo test della funzione es5 con tree uguale all'albero in basso a sinistra
    che dovra' restituire l'albero alla destra
    
              5                                    11             
      ________|_____________                _______|______         
     |          |           |              |              |        
     20         4           6              31             38        
     |     _____|______                                   |            
     11   |   |  |  |  |                                  6 
          10  2  9  8  7                                 
            __|__                                  
           |     |                                 
           3     1                                   
                                    

    '''
    lista1= [5, [[20, [[11, []]]], [4, [[10, []], [2, [[3, []], [1, []]]], [9, []], [8, []],[7, []]]],[6, []]]] 
    lista2=[11, [[31, []], [38, [[6, []]]]]]
    return test_es5a(lista1,55,lista2)+2


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
    lista1= [76, [[12, [[15, [[5, []], [19, [[181, []], [28, []]]]]],
    [80, [[47, [[94, []], [29, []]]],[96, []]]]]], [37, [[71, [[92, []], 
    [67, [[70, []], [83, []], [8, [[30, [[46, []], [21, []]]]]]]]]],
    [39, []], [100, [[23, [[81, []]]], [121, [[44, []]]]]]]]]]
    lista3=[76, [[12, [[20, [[228, []]]], [176, [[170, []]]]]], 
    [76, [[163, [[220, [[8, [[97, []]]]]]]], [100, [[104, []], [165, []]]]]]]]
    return test_es5a(lista1,909,lista3) +2

################################################################################

def test_es6a(indirizzo, expected):
    try:
        isrecursive.decorate_module(program)
        program.es6(indirizzo)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es6(indirizzo)
    check(type(ris),list,None,"bisogna restituire una lista")
    check(type(ris[0]),tuple,None,"la liste deve contenere tuple")
    check(ris,expected,None,"lista  restituita non e' corretta")
    return 1


def test_es6a_1():
    '''\nPrimo test della funzione es6 con indirizzo cartella ='Informatica/Software'
    '''
    risposta=[('BasiDati', 0, 0), ('ManualeMac', 0, 0), ('OSX', 1, 1), 
    ('Software', 2, 2), ('SistemiOperativi', 4, 1)]
    return test_es6a('Informatica/Software',risposta) +1

def test_es6a_2():
    '''\nPrimo test della funzione es6 con indirizzo cartella ='Informatica/Hardware'
    '''
    risposta=[('Hardware', 0, 1), ('Processori', 0, 1), ('RISC', 2, 0), ('Architetture', 3, 1)]
    return test_es6a('Informatica/Hardware',risposta) +2

def test_es6a_3():
    '''\nTerzo test della funzione es6 con indirizzo cartella ='Informatica'
    '''
    risposta=[('BasiDati', 0, 0), ('ManualeMac', 0, 0), ('Hardware', 0, 1), 
    ('Processori', 0, 1), ('OSX', 1, 1), ('RISC', 2, 0), ('Architetture', 3, 1), 
    ('Informatica', 2, 2), ('Software', 2, 2), ('SistemiOperativi', 4, 1)]
    return test_es6a('Informatica',risposta) +2

###############################################################################

tests = [
    test_nome_cognome_matricola,
    test_es1a_1, test_es1a_2, test_es1a_3,
    test_es2a_1, test_es2a_2, test_es2a_3,
    test_es3a_1, test_es3a_2, test_es3a_3,
    test_es4a_1, test_es4a_2, test_es4a_3,
    test_es5a_1,  test_es5a_2, test_es5a_3,
    test_es6a_1, test_es6a_2, test_es6a_3,
    ]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################


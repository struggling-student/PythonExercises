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
    ''' \nPrimo test della funzione es1 con liste:
    lista1=['caso','melo','puri','pero','rana']
    lista2=['velo','volo','viso', 'vaso', 'dado','dito']
     '''
    l1=['caso','melo','puri','pero','rana']
    l1b=['velo','volo','viso', 'vaso', 'dado','dito']
    ris = program.es1(l1,l1b)
    check(type(ris),dict ,None," bisogna restituire un dizionario")
    d1={'caso': 'vaso', 'melo': 'velo', 'puri': 'dado', 'pero': 'velo', 'rana': 'dado'}
    check(ris, d1, None, " la risposta non e' corretta")
    return 1

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con liste
    lista1=['carbone', 'canotto', sultani', 'caviale', 'bacillo', 'palmare']
    lista2=['declino', 'granito', 'sovrani', 'castano', 'criceto', 'polenta']
     '''
    l2=['carbone', 'canotto', 'sultani', 'caviale', 'bacillo', 'palmare']
    l2b=['declino', 'granito', 'sovrani', 'castano', 'criceto', 'polenta']
    ris = program.es1(l2,l2b)
    d2={'carbone': 'castano', 'canotto': 'castano', 'sultani': 'sovrani', 
    'caviale': 'castano', 'bacillo': 'castano', 'palmare': 'castano'}
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, d2, None, " la risposta non e' corretta")
    return 1

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con liste
    lista1=['zvutsr','abcdef', fedcba','fghilm','mlihgf','rstuvz']
    lista2=['hbhdhf', 'gbgdgf','federa', 'fghilm', 'alihaa']
    '''
    l3=['zvutsr','abcdef', 'fedcba','fghilm','mlihgf','rstuvz']
    l3b=['hbhdhf', 'gbgdgf','federa', 'fghilm', 'alihaa']
    ris = program.es1(l3,l3b)
    d3={'zvutsr': 'alihaa', 'abcdef': 'gbgdgf', 
    'fedcba': 'federa', 'fghilm': 'fghilm', 'mlihgf': 'alihaa', 
    'rstuvz': 'alihaa'} 
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, d3, None, " la risposta non e' corretta")
    return 1

##########################################################################################

def test_es2a_1():
    ''' \nPrimo test della funzione es2 con 
    lista= ['amare', 'cannone', 'cantare', 'dormire',  'gommone', 'torrone', 
            'burrone', 'partire', 'estate', 'morire', 'fiorire']
    '''
    lista1= ['amare', 'cannone', 'cantare', 'dormire',  'gommone', 'torrone', 'burrone', 
    'partire','estate','morire', 'fiorire']
    d1={'are': ['cantare', 'amare'], 'one': ['burrone', 'cannone', 'gommone', 'torrone'], 
    'ire': ['dormire', 'fiorire', 'partire', 'morire'], 'ate': ['estate']}
    ris = program.es2(lista1)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, d1, None, " la risposta non e' corretta")
    return 1

def test_es2a_2():
    ''' \nSecondo test della funzione es2 con
    lista=['cono', 'cattivo', 'vino', 'prato', 'lato',
           'camino', 'cammino', 'fiato', 'buono', 'ulivo']
    '''
    lista2=['cono', 'cattivo', 'vino', 'prato', 'lato',
    'camino', 'cammino', 'fiato', 'buono', 'ulivo']
    d2={'ono': ['buono', 'cono'], 
        'ivo': ['cattivo', 'ulivo'], 
        'ino': ['cammino', 'camino', 'vino'], 
        'ato': ['fiato', 'prato', 'lato']} 
    ris = program.es2(lista2)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, d2, None, " la risposta non e' corretta")
    return 1

def test_es2a_3():
    ''' \nTerzo test della funzione es2 con
    lista3=[ 'aaa', 'xxy', 'aaaa', 'axxy', 'sst', 
             'baaa', 'ccaaa', 'zxxxy', 'xxxy', 'zsst']
    '''
    lista3=[ 'aaa','xxy','aaaa','axxy','sst','baaa', 'ccaaa','zxxxy','xxxy', 'zsst']
    ris = program.es2(lista3)
    d3={'aaa': ['ccaaa', 'aaaa', 'baaa', 'aaa'], 
        'xxy': ['zxxxy', 'axxy', 'xxxy', 'xxy'], 
        'sst': ['zsst', 'sst']}
    check(type(ris),dict,None," bisogna restituire un dizionario") 
    check(ris, d3, None, " la risposta non e' corretta")
    return 1
    
################################################################################

def test_es3a_1():
    ''' \nPrimo test della funzione es3 con 
    ftesto1='f3a.txt', ftesto2='rf3a.txt', s1=2, s2=5.
    Il file rf3a.txt deve coincidere col file RISf6a.txt'''
    ris = program.es3('f3a.txt','rf3a.txt',2,5)
    check_text_file('rf3a.txt','RISf3a.txt')
    check(ris, 5, None, " la risposta non e' corretta")
    return 1

def test_es3a_2():
    ''' \nSecondo test della funzione es3 con 
    ftesto1='f3a.txt', ftesto2='rf3b.txt', s1=20, s2=25.
    Il file rf3b.txt deve coincidere col file RISf3b.txt'''
    ris = program.es3('f3a.txt','rf3b.txt',20,25)
    check_text_file('rf3b.txt','RISf3b.txt')
    check(ris, 0, None, " la risposta non e' corretta")
    return 1

def test_es3a_3():
    ''' \nTerzo test della funzione es3 con 
    ftesto1='f3a.txt', ftesto2='rf3c.txt', s1=11, s2=12.
    Il file rf3c.txt deve coincidere col file RISf3c.txt'''
    ris = program.es3('f3a.txt','rf3c.txt',11,12)
    check_text_file('rf3c.txt','RISf3c.txt')
    check(ris, 0, None, " la risposta non e' corretta")
    return 1
    
################################################################################
def test_es4a_1():
    '''\nPrimo test della funzione es4 con f4a.png  '''
    ris1=2
    ris= program.es4('f4a.png')
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,ris1,None,"il valore non e' corretto")
    return 2

def test_es4a_2():
    '''\nSecondo test della funzione es4 con f4b.png '''
    ris2=10
    ris= program.es4('f4b.png')
    check(type(ris),int,None,"la funzione deve restituire un intero")
    check(ris,ris2,None,"il valore non e' corretto")
    return 2

def test_es4a_3():
    '''\nTerzo test della funzione es4 con f4c.png '''
    ris3=3
    ris= program.es4('f4c.png')
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
    check(type(ris),list,None,"bisogna restituire una lista")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 1


   

def test_es5a_1():
    '''\nPrimo test della funzione es5 con  albero:
    
               5
      ________|_____________
     |          |           |
     20         4           6
     |     _____|______  
     11   |   |  |  |  |
          10  2  9  8  7
            __|__   
           |     |
           3     1 

    '''
    listaA1= [5, [[20, [[11, []]]], [4, [[10, []], [2, [[3, []], [1, []]]], [9, []], 
    [8, []],[7, []]]],[6, []]]]
    #tree1   = albero.fromLista(listaA1)
    lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20] 
    return test_es5a(listaA1,lista1)


def test_es5a_2():
    '''\nSecondo test della funzione es5 con  albero:
    
                    7               
             _______|______         
            |              |        
            5              9        
         ___|___        ___|__      
        |       |      |      |     
        10      8      3      1     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   2   12  13 15  6  4   0   
                                     
 
    '''
    listaA2=[7,[[5,[[10,[[1,[]],[2,[]]]],[8,[[12,[]],[13,[]]]]]],[9,[[3,[[15,[]],[6,[]]]],
    [1,[[4,[]],[0,[]]]]]]]]
    lista2=[0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15] 
    return test_es5a(listaA2,lista2)

def test_es5a_3():
    '''\nTerzo test della funzione es5 con  albero:
    
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
    lista3=[5, 8, 12, 15, 19, 21, 23, 28, 29, 30, 37, 39, 44, 46, 47, 67, 70, 71, 76, 
            80, 81, 83, 92, 94, 96, 100, 121, 181]
    return test_es5a(listaA3,lista3)


################################################################################

def test_es6a(lista1, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program)
        program.es6(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    tree1   = albero.fromLista(lista1)
    ris= program.es6(tree1)
    check(type(ris),list,None,"bisogna restituire una lista")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 2



def test_es6a_1():
    '''\nPrimo test della funzione es6 con tree uguale all'albero in basso a sinistra
                                  
               5                  
      ________|_____________      
     |          |           |     
     20         4           6     
     |     _____|______           
     11   |   |  |  |  |          
          10  2  9  8  7          
            __|__                 
           |     |                
           3     1                

    '''
    listaA1= [5, [[20, [[12, []]]], [4, [[10, []], [2, [[30, []], [22, []]]], 
    [9, []], [8, []],[7, []]]],[6, []]]]
    lista1=[4, 5, 20]
    return test_es6a(listaA1,lista1)
    
def test_es6a_2():
    '''\nSecondo test della funzione es6 con tree uguale all'albero in basso a sinistra
    
                  7               
           _______|______         
          |              |        
          5              9        
       ___|___        ___|__      
      |       |      |      |     
      10      8      3      1     
     _|_     _|_    _|_    _|_    
    |   |   |   |  |   |  |   |   
    1   2   12  13 15  6  4   0   
                                  

    '''
    listaA2=[7,[[5,[[10,[[1,[]],[2,[]]]],[8,[[12,[]],[13,[]]]]]],[9,[[3,[[15,[]],[6,[]]]],
    [1,[[4,[]],[0,[]]]]]]]]
    lista2=[]
    return test_es6a(listaA2,lista2)


def test_es6a_3():
    '''\nTerzo test della funzione es6 con tree uguale all'albero in basso a sinistra
    
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
    lista3=[8, 23, 37, 76, 121]
    return test_es6a(listaA3,lista3)


###############################################################################
def test_es7a(dirname, expected):
    try:
        isrecursive.decorate_module(program)
        program.es7(dirname)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es7(dirname)
    check(type(ris),dict,None,"bisogna restituire un dizionario")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 3


def test_es7a_1():
    dirname = 'd1'
    #expected= {'f11': 23, 'd11': 4, 'f2': 2550, 'd1': 5, 'f1': 20200, 'd3': 110}
    expected= {'f11': 23, 'd11': 4, 'f2': 2550, 'd1': 8, 'f1': 20200, 'd3': 3}
    return test_es7a(dirname, expected)

def test_es7a_2():
    dirname = 'd2'
    #expected= {'f0': 33, 'f4': 21, 'f3': 7, 'f2': 7, 'd2': 21, 'd3': 3}
    expected= {'f0': 33, 'f4': 21, 'f3': 7, 'f2': 7, 'd2': 2, 'd3': 3}
    return test_es7a(dirname, expected)

def test_es7a_3():
    dirname = 'd3'
    #expected= {'d3': 60, 'f11': 37, 'f6': 0, 'f4': 0, 'd2': 5}
    expected= {'d3': 3, 'f11': 37, 'f6': 0, 'f4': 0, 'd2': 5, 'd1': 4}
    return test_es7a(dirname, expected)

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


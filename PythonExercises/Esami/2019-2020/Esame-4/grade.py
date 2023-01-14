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
    ''' \nPrimo test della funzione es1 con fname='uguaglianze1.txt'
    '''
    lista1= [1,0,1,0] 
    ris = program.es1('uguaglianze1.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int, None," la lista restituita deve contenere interi")
    check(ris, lista1, None, " la lista restituita  non e' corretta")
    return 2

def test_es1a_2():
    ''' \nSecondo test della funzione es1 con fname='uguaglianze2.txt'
    '''
    lista2= [0,1,0,0,1]
    ris = program.es1('uguaglianze2.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista restituita deve contenere interi")
    check(ris, lista2, None, " la lista restituita  non e' corretta")
    return 3

def test_es1a_3():
    ''' \nTerzo test della funzione es1 con fname='uguaglianze3.txt'
    '''
    lista3= [1,0,1,0,0,1]
    ris = program.es1('uguaglianze3.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista restituita deve contenere interi")
    check(ris, lista3, None, " la lista restituita  non e' corretta")
    return 3
    
################################################################################

def test_es2a_1():
    '''\nPrimo test della funzione es2 sull'immagine Rettiangoli.png e pixel (20,20)'''
    ris= program.es2('Rettangoli.png',20,20)
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,4200,None,"l' intero restituito    non e' corretto")
    return 2

def test_es2a_2():
    '''\nSecondo test della funzione es2 sull'immagine Rettiangoli.png e pixel (80,90)'''
    ris= program.es2('Rettangoli.png',80,90)
    check(type(ris),int, None,"la funzione deve restituire unintero")
    check(ris,2400,None,"l'intero restituito     non e' corretto")
    return 2

def test_es2a_3():
    '''\nTerzo test della funzione es2 sull'immagine Rettiangoli.png e pixel (0,90)'''
    ris= program.es2('Rettangoli.png',0,90)
    check(type(ris),int, None,"la funzione deve restituire un intero")
    check(ris,1600,None,"l'intero non e' corretto")
    return 2

################################################################################

def test_es3a(n, expected):
    try:
        isrecursive.decorate_module(program)
        program.es3(n)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    ris= program.es3(n)
    check(type(ris),type(albero.Nodo(1)),None," bisogna restituire un oggetto di tipo nodo")
    check(albero.toLista(ris), expected ,None,"l'albero restituito non e' corretto")
    return 3

  
def test_es3a_1():
    '''\nPrimo test della funzione es3 con n=8, la funzione deve restituire la radice dell'albero:  
             8   
            _|_  
           |   |
           2   4 
               | 
               2 
    '''
    return test_es3a(8,[8, [[2, []], [4, [[2, []]]]]])

def test_es3a_2():
    '''\nSecondo  test della funzione es3 con n=12, la funzione deve restituire la radice dell'albero:  
                12         
            _____|_____    
           |  |  |     | 
            2  3 4     6 
                 |    _|_
                 2   |   |
                     2   3
    '''
    lista=[12, [[2, []], [3, []], [4, [[2, []]]], [6, [[2, []], [3, []]]]]]
    return test_es3a(12,lista)


def test_es3a_3():
    '''\nTerzo test della funzione es3 con n=125, la funzione deve restituire la radice dell'albero:
        
           125     
           _|_    
          |   |     
          5   25    
              |     
              5     
    '''
    lista=[125, [[5, []], [25, [[5, []]]]]]
    return test_es3a(125,lista)

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
    check(ris, expected ,None,"il dizionario  restituito non e' corretto")
    return 3

def test_es4a_1():
    dirname = 'dir1'
    expected = {
    'esercizio5': {'dir1/st1/st3/esercizio5.txt', 'dir1/st2/esercizio5.txt'}, 
    'esercizio1': {'dir1/esercizio1.txt', 'dir1/st1/st3/esercizio1.txt', 'dir1/st1/esercizio1.txt'}
    }
    return test_es4a(dirname, expected)

def test_es4a_2():
    dirname = 'dir2'
    expected = {
    'z': {'dir2/st3/st3d/z.txt', 'dir2/st1/st1b/z.txt', 'dir2/z.txt'}, 
    'b': {'dir2/st3/st3d/b.txt', 'dir2/st3/st3c/stanza3c1/b.txt'}, 
    'a': {'dir2/st3/st3c/a.txt', 'dir2/st3/st3c/stanza3c1/a.txt', 'dir2/st2/a.txt', 'dir2/st1/st1b/a.txt'}
    } 
    return test_es4a(dirname,  expected)

def test_es4a_3():
    dirname = 'dir3'
    expected = {
    'z': {'dir3/B4/A3b/B3/C/z.txt', 'dir3/B3/C/z.txt', 'dir3/B4/A3b/B1/A5/B3/C/z.txt'}, 
    'a': {'dir3/B4/A3b/B4/a.txt', 'dir3/B3/C/a.txt', 'dir3/B4/A3b/B1/A5/B4/a.txt', 'dir3/B4/A3b/B1/A5/a.txt', 'dir3/B4/A3b/B1/a.txt', 'dir3/B1/a.txt'}, 
    'r': {'dir3/B4/A3b/B1/A5/B3/C/r.txt', 'dir3/B4/A3b/B3/C/r.txt', 'dir3/B3/C/r.txt'}, 
    'q': {'dir3/B4/A3b/B1/A5/B4/q.txt', 'dir3/B4/q.txt', 'dir3/B4/A3b/B1/A5/B3/C/q.txt', 'dir3/B4/A3b/B4/q.txt', 'dir3/B3/C/q.txt', 'dir3/B4/A3b/B3/C/q.txt'}, 
    'b': {'dir3/B4/A3b/B4/b.txt', 'dir3/B4/A3b/B2/b.txt', 'dir3/B4/A3b/B1/A5/b.txt', 'dir3/B4/A3b/B1/A5/B1/b.txt', 'dir3/B4/A3b/B1/A5/B2/b.txt', 'dir3/B1/b.txt', 'dir3/B4/A3b/B1/b.txt', 'dir3/B4/A3b/b.txt', 'dir3/B4/A3b/B1/A5/B4/b.txt', 'dir3/B4/b.txt', 'dir3/b.txt'}, 
    'd': {'dir3/B4/A3b/B4/d.txt', 'dir3/B4/A3b/B1/A5/B4/d.txt', 'dir3/B4/d.txt'}, 
    'c': {'dir3/B4/A3b/B1/A5/c.txt', 'dir3/c.txt', 'dir3/B4/A3b/c.txt'}
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


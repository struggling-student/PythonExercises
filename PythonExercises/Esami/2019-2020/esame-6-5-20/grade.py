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

def test_es2a_1():
    ''' \nPrimo test della funzione es2 con fname='expressioni0.txt'
    '''
    lista1=[78]
    ris = program.es2('expressioni0.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int, None," la lista restituita deve contenere interi")
    check(ris, lista1, None, " la lista restituita  non e' corretta")
    return 1

def test_es2a_2():
    ''' \nSecondo test della funzione es2 con fname='expressioni1.txt'
    '''
    #lista1=[200, 10000, 10, 0, 10001, 10000]
    #ris = program.es2('f2.txt')
    lista1= [370944104397271266530, 744446970798550722708, 2379237618858967013923674, 682592962108239278, 
             120096990261873938567, 1188935186355062021134908, 2749828376010] 
    ris = program.es2('expressioni1.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int, None," la lista restituita deve contenere interi")
    check(ris, lista1, None, " la lista restituita  non e' corretta")
    return 2

def test_es2a_3():
    ''' \nTerzo test della funzione es2 con fname='expressioni2.txt'
    '''
    #lista1= [2, 1, 2, 5, 25, 250000000000]
    #ris = program.es2('f3.txt')
    lista1= [34508444913270027787008888, 247404829429395402898887163655983667049240, 32838693356895549994904854291200, 
             4854169842442699535194830157114571, 11044232069001852585327523651645997650942643, 
             42148207137271066989500227233860682608376102, 109181918889267278641671147145220084638993456, 
             1816543370207524729902419019927158304053855200, 341171516138910779676699513764518967284783, 
             139216716146485082014258400640500361781588658, 110410218155043491848529431980702657103682688, 
             12228038071020391116797342233023564075642571, 161798204850150069891726860378315067399018, 
             12229138682402224636657274537038373352628173]
    ris = program.es2('expressioni2.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista restituita deve contenere interi")
    check(ris, lista1, None, " la lista restituita  non e' corretta")
    return 2

def test_es2a_4():
    ''' \nQuarto test della funzione es2 con fname='expressioni3.txt'
    '''
    #lista1= [2, 1, 2, 5, 25, 250000000000]
    #ris = program.es2('f3.txt')
    lista1= [19661368435458163839331748897617724430996807177983525720991271, 
             31026332138527539406699652745454319753717145853271103897600, 
             6449724454817059516126369853055784785651215480760637442280363961, 
             64717211113126938711488526323893180532605325160348099236421264278, 
             98813982816541446521861447524436553996020667560637251409718683, 
             219127136711509187439250881645749146454562922726535852904746289, 
             9745288953771206799544889425409528370714199140433920000, 
             864081940956800868970674859199658640967409540154982400, 
             2516882367528869890338451152242855307817494599888484480, 
             1376955410756949564864779605706427392785748925525786624000,
             814778334237857042884671356399960269048560173624035655151947625, 
             18711997740530882382143493492758228573933566214593839173564, 
             502416228970602883455507550149365111409001677251189341849590,
             13201902014456945122430668055504578783925911051821662760, 
             69030204161128546320901364913564024993219922095217157544, 
             185803031057321977560981948501112541167322765153989522639082773, 
             120911751472012533259987418793667839026831263621218142572062144, 
             87749619206528446568547211265011225508773097040892561892264652140,
             153318795851699978597773261518561077460174507135839082240, 
             54394845526607762731279321454819777731468111570318, 
             109574614232340958820682596695947164112655622468852646484237867780]
    ris = program.es2('expressioni3.txt')
    check(type(ris),list,None," bisogna restituire una lista")
    check(type(ris[0]),int,None," la lista restituita deve contenere interi")
    check(ris, lista1, None, " la lista restituita  non e' corretta")
    return 2
    
################################################################################

def test_es4a_1():
    '''\nPrimo test della funzione es4 con f4a.png'''
    ris1={(30, 50, 30, 69), (50, 50, 50, 69), (20, 40, 79, 40), (20, 50, 20, 69), 
    (20, 30, 79, 30), (60, 50, 60, 69), (20, 20, 79, 20), (80, 50, 80, 69), 
    (70, 50, 70, 69), (40, 50, 40, 69)}
    ris= program.es4('f4a.png')
    check(type(ris),set, None,"la funzione deve restituire un insieme")
    check(ris,ris1,None,"l'insieme  restituito  non e' corretto")
    return 3

def test_es4a_2():
    '''\nSecondo test della funzione es4 con f4b.png'''
    ris1={(0, 20, 99, 20), (50, 50, 50, 98)}
    ris= program.es4('f4b.png')
    check(type(ris),set, None,"la funzione deve restituire un insieme")
    check(ris,ris1,None,"l'insieme  restituito  non e' corretto")
    return 3

def test_es4a_3():
    '''\nTerzo test della funzione es4 con f4c.png'''
    ris1={(20, 20, 99, 20), (20, 40, 20, 50), (30, 60, 70, 70)} 
    ris= program.es4('f4c.png')
    check(type(ris),set, None,"la funzione deve restituire un insieme")
    check(ris,ris1,None,"l'insieme  restituito  non e' corretto")
    return 3

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
    
    tree1        = albero.fromLista(lista1)
    ris= program.es5(tree1)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"il dizionario restituito non e' corretto")
    return 2

def test_es5a_1():
    '''\nPrimo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
                    10                 
             _______|______            
            |              |           
            3              3           
         ___|___        ___|__         
        |       |      |      |        
        2       1      8      4        
                                       
    '''
    lista1=[10,[[3,[[2,[]],
                    [1,[]]]],
                [3,[[8,[]],
                    [1,[]]]]]]
    d1={0:[10], 1:[3],2:[1,2,8]}
    return test_es5a(lista1,d1)
    
def test_es5a_2():
    '''\nSecondo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
                    36              
             _______|______         
            |              |        
            26             10       
         ___|___        ___|__      
        |       |      |      |     
        3       7      3     15     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   8   8   4  8   6  7   8   
                                    

    '''
    lista1=[36,[[26,[[3,[[1,[]],
                         [8,[]]]],
                [7,[[8,[]],
                    [4,[]]]]]],
                [10,[[3,[[8,[]], 
                          [6,[]]]],
                     [15,[[7,[]],
                          [8,[]]]]]]]]
    d1={0: [36], 1: [10, 26], 2: [3, 7, 15], 3: [1, 4, 6, 7, 8]} 
    return test_es5a(lista1,d1)

def test_es5a_3():
    '''\nTerzo test della funzione es5 con tree uguale all'albero in basso a sinistra
    
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
    d1={0: [76], 1: [12, 37], 2: [15, 39, 71, 80, 100], 3: [5, 19, 23, 47, 67, 92, 96, 121], 
    4: [8, 28, 29, 44, 70, 81, 83, 94, 181], 5: [30], 6: [21, 46]} 
    return test_es5a(lista1,d1)+1

###############################################################################
def test_es7a(dirname, ext, expected):
    try:
        isrecursive.decorate_module(program)
        program.es7(dirname, ext)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program)
    
    ris= program.es7(dirname, ext)
    check(type(ris),dict,None," bisogna restituire un dizionario")
    check(ris, expected ,None,"il dizionario non e' corretto")
    return 3

def test_es7a_1():
    dirname = 'dir1'
    ext = 'pPp'
    expected = {'dir1/IXId6UiSY3.ppp': 'yIkzrn5vCh'}
    return test_es7a(dirname, ext, expected)

def test_es7a_2():
    dirname = 'dir2'
    ext = 'QQq'
    expected = {'dir2/e7JHlEUADv/BWebVRf7PJ/E1yvRzuUmN.QQQ': 'OADYGzTJaJ', 
                'dir2/EsNYG8Yx1i/btLfEdjc3g.QQQ': 'Vtclr2lqj1', 
                'dir2/EsNYG8Yx1i/Ebp6uI82ja/eyDiIS8wtY/VgwcGxEuji.QQQ': 'kQ7PnCvGKZ', 
                'dir2/EsNYG8Yx1i/Ebp6uI82ja/mscAu8GPGo.QQQ': '5yXYazETTJ', 
                'dir2/EsNYG8Yx1i/jYjpse4Tod/5pXG2Lc3jZ/2lXCxxkFNC/Udn0pLVUlb.QQQ': 'RVu7doKHdD', 
                'dir2/EsNYG8Yx1i/yvC2O0QZ8I/2TxSXlpdMy.QQQ': 'FJUirOQ4Hp', 
                'dir2/EsNYG8Yx1i/yvC2O0QZ8I/GTdgLPC3ER.QQQ': 'c0x9mNjo6d', 
                'dir2/EsNYG8Yx1i/yvC2O0QZ8I/kttLz7uuLP/aLgvCn6KdT/ekgUGO9oAd.QQQ': 'f4zejC2Xqu', 
                'dir2/EsNYG8Yx1i/yvC2O0QZ8I/kttLz7uuLP/xzLmYweT8I/hFHeHlrw1U.QQQ': 'arfIvkob8L', 
                'dir2/EsNYG8Yx1i/yvC2O0QZ8I/ZFozUF48dm.QQQ': 'gvs5GFb3dl', 
                'dir2/lDGUnBxGqX.QQQ': 'YUMRf4kFLp', 
                'dir2/OvQ0cUzDda/0WQq11NTKn/jPTNmBhK5G.QQQ': '02JPoI84Bt', 
                'dir2/OvQ0cUzDda/0WQq11NTKn/TJemF49wA9/lQ66WbWfhW/qjlo5Wg4fy.QQQ': 'DfreoJ3NHo', 
                'dir2/OvQ0cUzDda/8tJLc4WnvX/1hHL7zoVIV.QQQ': 'Lw16dhRr2A', 
                'dir2/OvQ0cUzDda/8tJLc4WnvX/ys07YAZSpX/XMTF0DbUmH/NxiCVIzdWl.QQQ': 'hDjQBMRR21'}
    return test_es7a(dirname, ext, expected)

def test_es7a_3():
    dirname = 'dir3'
    ext = 'BbB'
    expected = {'dir3/m7bTC7N76Q/CWGrhIKCux/i8ag7JSJBI/LtRo3CQS1h/etYdlTkiUV/yG3WJx1e7q/OSlm79r9pq.bbb': 'OCdxoUIWML', 
                'dir3/m7bTC7N76Q/CWGrhIKCux/i8ag7JSJBI/LtRo3CQS1h/UJXJY0dsWT.bbb': 'j2PhySenRL', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/919oA90zDP.bbb': '9JNPsro29P', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/H046wyhgk0/poW3iMVgX8/YbXQaaXjR9.bbb': 'dWVMUBhWpE', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/H046wyhgk0/ZS9dNqJHv1/c2GMXMmYwv/ObXnUneVoK.bbb': 'TmtlnKoZhz', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/H046wyhgk0/ZS9dNqJHv1/cSDJtTnRvG/NPwJP8Z3sY.bbb': 'xajqhfUAFd', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/vDU8bkk3HL/FrjcAUTPRb/vm6oAKmWai/hjbOT58ejo.bbb': 'Nb5MBDYkYo', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/vDU8bkk3HL/VbjCuEpC9O/HlHOFXEyIP/w30tXwvlgl.bbb': 'OVKB6wSSZd', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/3S4ncY8Thj/vDU8bkk3HL/wBSK3KEi3c/cY1vQ2IXqH/FB5a9m9JSZ.bbb': 'V4wfxJF2dg', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/AYijAoDHAE/fwuKGx1Nww/HB465z1itY/TAwaJTdTyQ.bbb': 'HzQIi1Zcvn', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/AYijAoDHAE/fwuKGx1Nww/qmAed7BWiI/54Huw2oJgu.bbb': '3xAiNHeSBN', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/r9C9QhobKc/FpuIRYkfmP/gsWBvmblg1.bbb': 'vPsXYCjrCg', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/r9C9QhobKc/FpuIRYkfmP/jv3bKwohWQ.bbb': 'RYGZ2gmpFC', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/r9C9QhobKc/FpuIRYkfmP/QDsr0EYVko.bbb': 'UaUpx569sP', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/r9C9QhobKc/FpuIRYkfmP/yMzzPhJgcD.bbb': 'XzLyhqNfkJ', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/r9C9QhobKc/Z29IjE5Az3/vNLe8Hia5t/Og7vm15prN.bbb': 'pEURxZj3Iy', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/DbCNC50FdV/r9C9QhobKc/zSyiZYdld8.bbb': 'HSBJgo4vsW', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/PmMPBsH6QA/nJGsDYcMtO/0Wrga4UWmL/GkMeIfSDST/hP9AABjkUS.bbb': 'wrM06zO7ZW', 
                'dir3/m7bTC7N76Q/QcPvpGgLe3/PmMPBsH6QA/nJGsDYcMtO/0Wrga4UWmL/RJ1zR2KdzJ.bbb': 'RUmCFaXnQK', 
                'dir3/m7bTC7N76Q/UoxbO5zBAq/tA7ObvrUti/jLHAn89PIk/iekQFTpHGS/MWvMCgcMFk/qBq4leBS0j.bbb': 'C2Bodh3GFh'} 
    return test_es7a(dirname, ext, expected)

###############################################################################

tests = [
    # PER DISATTIVARE ALCUNI TEST BASTA COMMENTARE ALCUNE DELLE LE RIGHE CHE SEGUONO
    test_es2a_1, test_es2a_2, test_es2a_3, test_es2a_4,      # 7 punti
    test_es4a_1,  test_es4a_2, test_es4a_3,     # 9 punti
    
    test_es5a_1, test_es5a_2, test_es5a_3,      # 7 punti
    test_es7a_1, test_es7a_2, test_es7a_3,      # 9 punti
    test_nome_cognome_matricola,
    ]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################


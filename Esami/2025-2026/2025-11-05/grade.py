# -*- coding: utf-8 -*-
from testlib import (my_print as print, COL, runtests,
                     check_expected, check_text_file, check_img_file, check)
import isrecursive
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

def test_personal_data_entry(run=None):
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 0

###############################################################################

# ----------------------------------- Func.1 ----------------------------------- #

def do_func1_tests(string_list, word, expected, N):
    res = program.func1(string_list, word)
    if res != N:
        print(f'''{'*'*50}\n[ERROR] Il numero di stringhe rimosse e' {N} e non {res}. / Removed strings is {N}, but {res} were expected.\n {'*'*50}''')
        return 0
    if string_list != expected:
        print(f'''{'*'*50}\n[ERROR] La lista string_list non è stata modificata correttamente: vale {string_list} invece dovrebbe essere {expected}.\n
              string_list has not been correctly modified: it is {string_list}, but it should be {expected} {'*'*50}''')
        return 0
    return 2/3


def test_func1_1(run=None):
    '''
    string_list = ['cocacola','fanta', 'assenzio', 'Minosse', 'sinfonie']
    word = 'saponette'
    expected = ['cocacola','fanta', 'sinfonie']
    N = 2
    '''
    string_list = ['cocacola','fanta', 'assenzio', 'Minosse', 'sinfonie']
    expected = ['cocacola','fanta', 'sinfonie']
    word = 'saponette'
    N = 2
    return do_func1_tests(string_list, word, expected, N)

def test_func1_2(run=None):
    '''
    'Francesco è eliminato da MasterChef 12. L’attacco ai giudici: Ricordatevi che siamo persone'
    '''
    string_list = 'Francesco è eliminato da MasterChef 12. L’attacco ai giudici: Ricordatevi che siamo persone'.split()
    word = 'donna'
    expected = ['Francesco', 'è', 'eliminato', 'MasterChef', '12.', 'L’attacco', 'ai', 'giudici:', 'che', 'siamo', 'persone']
    N = 2
    return do_func1_tests(string_list, word, expected, N)

def test_func1_3(run=None):
    '''
    'Lotteria Italia, questa sera l’estrazione dei biglietti vincenti: nel Lazio venduto il maggior numero di tagliandi'
    '''
    string_list = 'Lotteria Italia, questa sera l’estrazione dei biglietti vincenti: nel Lazio venduto il maggior numero di tutti i tagliandi'.split()
    word = 'tot'
    expected = ['Italia,', 'questa', 'sera', 'l’estrazione', 'dei', 'vincenti:', 'nel', 'Lazio', 'venduto', 'il', 'maggior', 'numero', 'di', 'i', 'tagliandi']
    N = 3
    return do_func1_tests(string_list, word, expected, N)

# ----------------------------------- Func.2 ----------------------------------- #

def do_func2_tests(pathname, expected):
    pathname = 'func2/'+pathname

    res = program.func2(pathname)

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        keys_ex = set(expected.keys())
        keys_rez = set(res.keys())
        if keys_ex == keys_rez:
            for k in expected:
                if expected[k] != res[k]:
                    print(f'''[ERROR] Ad esempio, la matricola {k} dovrebbe avere una il valore {expected[k]} invece che {res[k]}.''')
                    print(f'''[ERROR] For example, matr {k} should have a value of {expected[k]} instead of {res[k]}.''')
                    return 0
                else:
                    pass
        else:
            diff_ex = keys_ex - keys_rez
            if diff_ex:
                print(f'''[ERROR] Le chiavi nei dizionari non sono uguali: al tuo dizionario mancano le matricole {diff_ex}''')
                print(f'''[ERROR] Keys in the dictionaries are not equal: your dictionary misses the following matr  {diff_ex}''')
            diff_rez = keys_rez - keys_ex
            if diff_rez:
                print(f'''[ERROR] Le chiavi nei dizionari non sono uguali: il tuo ha in piu le seguenti matricole {diff_rez}''')
                print(f'''[ERROR] Keys in the dictionaries are not equal: the following matr are not necessary {diff_rez}''')
            return 0
    return 2/3


def test_func2_1(run=None):
    '''
    func2_test_1.txt
    '''
    pathname = 'func2_test_1.txt'
    expected = {'123456': 26.5, '121212': 78.5, '111111': 90.5}
    return do_func2_tests(pathname, expected)

def test_func2_2(run=None):
    '''
    func2_test_2.txt
    '''
    pathname = 'func2_test_2.txt'
    expected = {'858567': 55.0, '944686': 49.5, '502665': 46.0, '922651': 50.0, '669985': 84.0, '708542': 56.5,
                '190832': 61.0, '446778': 13.5, '715822': 51.0, '496949': 36.0, '855338': 31.5, '654439': 41.5,
                '286452': 51.5, '386087': 50.5, '066402': 19.0, '862915': 29.0, '715947': 51.5, '253929': 25.5,
                '647445': 42.5, '481654': 88.0}
    return do_func2_tests(pathname, expected)

def test_func2_3(run=None):
    '''
    func2_test_3.txt
    '''
    pathname = 'func2_test_3.txt'
    expected = {'1615350266': 17.0, '6153502665': 5.0, '1535026650': 38.5, '5350266507': 2.0, '3502665073': 91.0,
                '5026650732': 67.0, '2797404044': 35.75, '6507329068': 30.0, '5073290685': 31.0, '0732906855': 89.0,
                '7329068553': 66.0, '3290685533': 54.0, '2906855338': 33.0, '9068553381': 34.0, '0685533818': 88.0,
                '6855338182': 33.0, '8553381822': 86.0, '5338182224': 50.8, '1822242797': 82.0, '8222427974': 86.0,
                '2224279740': 58.0, '2242797404': 14.0, '2427974040': 99.0, '7974040442': 38.0}
    return do_func2_tests(pathname, expected)

# ----------------------------------- Func.3 ----------------------------------- #

def do_func3_tests(listA, expected, outpath):
    outpath = 'func3/' + outpath
    actual_out_path = outpath.replace('!!TMP!!', 'out')
    expected_path = outpath.replace('!!TMP!!', 'exp')
    # before running anything remove if any
    if os.path.exists(actual_out_path):
        os.remove(actual_out_path)
    # now running
    res = program.func3(listA, actual_out_path)

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] Il numero di caratteri ritornato non è corretto / The number of characters is incorrect\n[ERROR] expected={expected} returned={res}.\n {'*'*50}''')
        return 0

    if os.path.isfile(actual_out_path):
        try:
            check_text_file(actual_out_path,
                                    expected_path)
        except:
            print(f"{'*'*50}\n[ERROR] Il tuo file è\n --> {actual_out_path} \n VS. il file atteso\n --> {expected_path}\n {'*'*50}", end='\n')
            return 0
        else:
            print("Output file OK", end=' ') # all goo dwe proceed
    else:
        print(f"{'*'*50}\n[ERROR] Impossibile trovare il file di output {actual_out_path} / Output file not found {actual_out_path}\n {'*'*50}", end=' ')
        return 0

    return 2/3


def test_func3_1(run=None):
    '''
    lista = ['ananas', 'Banana', 'pluto', 'zoroastro', 'marx', 'socrate', 'PLATO']
    expected = 42
    '''
    lista = ['ananas', 'Banana', 'pluto', 'zoroastro', 'marx', 'socrate', 'PLATO']
    expected = 42
    return do_func3_tests(lista, expected, 'func3_1_!!TMP!!.txt')

def test_func3_2(run=None):
    '''
    listaA = ['A', 'survey', 'of', 'user', 'Opinion', 'of', 'Computer', 'system', 'response', 'time']
'''
    lista = "A survey of user Opinion of Computer system response time".split()
    expected = 48
    return do_func3_tests(lista, expected, 'func3_2_!!TMP!!.txt')

def test_func3_3(run=None):
    '''
    listA = ['HdzCZJ', 'dzCZJy', 'zCZJyg', 'CZJygW', 'ZJygWo', 'Jy.....
    '''
    lista = ['HdzCZJ', 'dzCZJy', 'zCZJyg', 'CZJygW', 'ZJygWo', 'JygWoE', 'ygWoEM', 'gWoEMw', 'WoEMwQ', 'oEMwQz', 'EMwQzY', 'MwQzYr', 'wQzYrb', 'QzYrbl', 'zYrblN', 'YrblNv', 'rblNvK', 'blNvKs', 'lNvKsy', 'NvKsyd', 'vKsydc', 'Ksydcp', 'sydcpO', 'ydcpOm', 'dcpOmB', 'cpOmBC', 'pOmBCF', 'OmBCFo', 'mBCFoe', 'BCFoeV', 'CFoeVK', 'FoeVKF', 'oeVKFp', 'eVKFpe', 'VKFpeI', 'KFpeIo', 'FpeIot', 'peIotw', 'eIotwr', 'Iotwrq', 'otwrqJ', 'twrqJK', 'wrqJKS']
    expected = 258
    return do_func3_tests(lista, expected, 'func3_3_!!TMP!!.txt')

# ----------------------------------- Func.4 ----------------------------------- #

def do_func4_tests(S, expected):
    res = program.func4(S)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The histogram string should be \n{expected}\nCodified as a string={repr(expected)}\n instead of\n{res}\nCodified as a string={repr(res)}\n'''
              f'''[ERROR] L'istogramma stringa deve essere \n{expected}\nCodificato come stringa={repr(expected)}\n  invece che\n{res}.\nCodificato come stringa={repr(res)}\n {'*'*50}''')
        return 0
    return 2


def test_func4_1(run=None):
    '''
    S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era scordato di chiamare Paperino'
    '''
    S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era scordato di chiamare Paperino'
    expected = '      una *\n topolino **\n     sono *\n       si *\n scordato *\npurtroppo *\n    prima *\n    pippo *\n    pesce *\n  pescato *\n    pasta *\n paperino *\n     mare **\n mangiato *\n       ma *\n       in *\n       il *\n    hanno *\n   giorno *\n      era *\n        e *\n       di *\n chiamare *\n    bella *\n   andati *\n       al **\n'
    return do_func4_tests(S, expected)

def test_func4_2(run=None):
    '''
    S = 'From: mathew <mathew@mantis.co.uk>\nSubject: Re: university violating separation of church/state?\nOrganiz...
    '''
    S = 'From: mathew <mathew@mantis.co.uk>\nSubject: Re: university violating separation of church/state?\nOrganization: Mantis Consultants, Cambridge. UK.\nX-Newsreader: rusnews v1.01\nLines: 29\n\ndmn@kepler.unh.edu (...until kings become philosophers or philosophers become kings) writes:\n>'
    expected = '           x *\n      writes *\n   violating *\n           v *\n       until *\n  university *\n         unh *\n          uk **\n     subject *\n       state *\n  separation *\n     rusnews *\n          re *\nphilosophers **\norganization *\n          or *\n          of *\n  newsreader *\n      mathew **\n      mantis **\n       lines *\n       kings **\n      kepler *\n        from *\n         edu *\n         dmn *\n consultants *\n          co *\n      church *\n   cambridge *\n      become **\n'
    return do_func4_tests(S, expected)


def test_func4_3(run=None):
    '''
    S = 'Re: <<Pompous ass\nOrganization: Tektronix Inc., Beaverto ......
    '''

    S = 'Re: <<Pompous ass\nOrganization: Tektronix Inc., Beaverton, Or.\nLines: 20\n\nIn article <1ql6jiINN5df@gap.caltech.edu> keith@cco.caltech.edu (Keith Allan Schneider) writes:\n>\n>The "`little\' things" above were in reference to Germany, clearly.  People\n>said that there were similar things in Germany, but no one could name any.\n>They said that these were things that everyone should know, and that they\n>weren\'t going to waste their time repeating them.  Sounds to me like no one\n>knew, either.  I looked in some books, but to no avail.\n\n  If the Anne Frank exhibit makes it to your small little world,\n  take an afternoon to go see it.  \n\n\n/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\ \n\nBob Beauchaine bobbe@vice.ICO.TEK.COM \n\nThey said that Queens could stay, they blew the Bronx away,\nand sank Manhattan out at sea.\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
    expected = '        your *\n      writes *\n       world *\n       weren *\n        were ***\n       waste *\n        vice *\n          to ******\n        time *\n      things ***\n        they ****\n       these *\n       there *\n        them *\n       their *\n         the ***\n        that *****\n   tektronix *\n         tek *\n        take *\n           t *\n        stay *\n      sounds *\n        some *\n       small *\n     similar *\n      should *\n         see *\n         sea *\n   schneider *\n        sank *\n        said ***\n   repeating *\n   reference *\n          re *\n      queens *\n          ql *\n     pompous *\n      people *\n         out *\norganization *\n          or *\n         one **\n          no ***\n        name *\n          me *\n   manhattan *\n       makes *\n      looked *\n      little **\n       lines *\n        like *\n        know *\n        knew *\n       keith **\n       jiinn *\n          it **\n         inc *\n          in ****\n          if *\n         ico *\n           i *\n       going *\n          go *\n     germany **\n         gap *\n       frank *\n     exhibit *\n    everyone *\n      either *\n         edu **\n          df *\n       could **\n         com *\n     clearly *\n         cco *\n     caltech **\n         but **\n       bronx *\n       books *\n       bobbe *\n         bob *\n        blew *\n   beaverton *\n  beauchaine *\n        away *\n       avail *\n          at *\n         ass *\n     article *\n         any *\n        anne *\n         and **\n          an *\n       allan *\n   afternoon *\n       above *\n'
    return do_func4_tests(S, expected)

# ----------------------------------- Func.5 ----------------------------------- #

import images

def do_test_func5(ID, expected):
    img_in  = f'func5/image0{ID}.png'
    img_out = f'func5/your_image0{ID}.png'
    img_exp = f'func5/expected0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(images.load(img_in), img_out)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The rotated image dimensions should be {expected} instead of {res}.\n'''
              f'''[ERROR] Le dimensioni dell'immagine ruotata devono essere {expected} invece che {res}.\n{'*'*50}''')
        return 0
    check_img_file(img_out, img_exp)
    return 2


def test_func5_1(run=None):
    '''imm_in = func5/image01.png
    imm_out = func5/expected01.png
    expected = (256, 256)
    '''
    ID = 1
    expected = (256, 256)
    return do_test_func5(ID, expected)


def test_func5_2(run=None):
    '''imm_in = func5/image02.png
    imm_out = func5/expected02.png
    expected = 3
    '''
    ID = 2
    expected = (256, 128)
    return do_test_func5(ID, expected)


def test_func5_3(run=None):
    '''imm_in = func5/image03.png
    imm_out = func5/expected03.png
    expected = (645, 800)
    '''
    ID = 3
    expected = (323, 400)
    return do_test_func5(ID, expected)


# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(directory, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(directory)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(directory)
    check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
    return 2


def test_ex1_1(run=None):
    '''
    directory = 'ex1/A'
    '''
    directory = 'ex1/A'
    expected = {'ex1/A': 'KTTISLJL', 'ex1/A/bkLbD': 'ĳŜǖA\x9eŻĂ'}
    return do_test_ex1(directory, expected)


def test_ex1_2(run=None):
    '''directory = 'ex1/B'
    '''
    directory = 'ex1/B'
    expected = {'ex1/B': '\x83ÔǄď¶\x9d', 'ex1/B/vWHJp': '\x85¹ƖƕƢÒ~ǀďIřǱāƁ', 'ex1/B/stSOl': 'ÁƭĉǌǀàWŰĦ'}
    return do_test_ex1(directory, expected)


def test_ex1_3(run=None):
    '''directory = 'ex1/C'
    '''
    directory = 'ex1/C'
    expected = {'ex1/C': 'ņĞö\x88ŭ', 'ex1/C/Lospm': 'Ơ\\', 'ex1/C/Lospm/TTINY': 'ĮĊvƅĕŒŇTƑǁ®ªÖ',
                'ex1/C/Lospm/wGuOG': '³¨ŖõƙċƂ', 'ex1/C/Lospm/vcynO': '²qŐŎ«\x83ı',
                'ex1/C/Lospm/nghch': 'ƍōWŚŽêíØÜÄe', 'ex1/C/Lospm/Khvrj': 'MǇǧƴĈª\x84ĵķƉðĔ',
                'ex1/C/MfzQL': 'Űťǋ\xad²\x9aœŕ', 'ex1/C/MfzQL/fNcLp': '\x81wĥ¿ŷ',
                'ex1/C/MfzQL/eiKqi': 'þǟL¿Üw', 'ex1/C/MfzQL/rtGJs': 'Ƃ\x84ƬƁ\x9fſŻÑǙ³',
                'ex1/C/sOsTK/Ffufy': '\x97ņíƢ', 'ex1/C/sOsTK/IpUQx': 'ƼŦĲűų', 'ex1/C/sOsTK/pjDEZ': '^ǃuŽ»ų'}
    return do_test_ex1(directory, expected)+1
# ----------------------------------- EX. 2----------------------------------- #

def do_ex2_test(strings, n, expected, score=2):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(strings, n)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(strings, n)
    if not isinstance(res, (set)):
        check(type(res), set, None, f"Wrong return type! Returned={type(res)}, expected= set / Il tipo ritornato non è corretto! Ritornato={type(res)}, atteso= set")
    p=0
    if type(res) == set:
        check(res, set(expected), None, f"Wrong set returned! Returned={res}, expected={expected} / Il set ritornato non è corretto! Ritornato={res}, atteso ={expected}")
        print("Correct set returned", end=' ')
        p = score
    return p

def test_ex2_1(run=None):
    '''
    nums = [5, 0, 5]; ops = ['+', '*', '+']
    '''
    nums = [5, 0, 5]; ops = ['+', '*', '+']
    expected = {'0+5+5', '5*5+0', '0*5+5', '5+5*0', '5+0*5', '5*0+5', '5+0+5', '5+5+0', '0+5*5'}
    return do_ex2_test(nums, ops, expected)

def test_ex2_2(run=None):
    '''
    nums = [99, 99, 100, 100]; ops = ['+', '*', '*']
    '''
    nums = [99, 99, 100, 100]; ops = ['*', '+']
    expected =  {'99*100+99', '99+100*100', '100+100*99', '99*99+100', '99+99*100', '100*99+100', '100+99*99',
                 '100*99+99', '99*100+100', '99+100*99', '100+99*100', '100*100+99'}
    return do_ex2_test(nums, ops, expected)

def test_ex2_3(run=None):
    '''
    nums = [1, 100000, 1000]; ops = ['+', '*', '-', '/', '@', '||']
    '''
    nums = [1, 100000, 1000]; ops = ['+', '*', '-', '/', '@', '||']
    expected = {'100000/1*1000', '1||1000*100000', '1-1000||100000', '100000||1000/1', '100000*1000+1',
                '1*100000||1000', '1-100000+1000', '100000*1@1000', '1||1000-100000', '1000-100000||1', '1000/1*100000',
                '1@100000*1000', '1000/1@100000', '1@1000||100000', '100000||1-1000', '1*1000||100000', '1000/1+100000',
                '100000/1-1000', '1000*1@100000', '1-100000/1000', '1000+1-100000', '1000*1+100000', '1000+100000||1',
                '1/1000*100000', '100000+1000*1', '1000/100000+1', '100000/1||1000', '1000||1+100000', '1+100000@1000',
                '1000||1@100000', '100000||1000*1', '100000*1000@1', '100000/1000-1', '1000||1*100000', '1/100000+1000',
                '1/100000||1000', '1||100000*1000', '1000@1*100000', '1+100000*1000', '1/1000||100000', '1-1000*100000',
                '1*1000-100000', '1000||100000*1', '1||100000@1000', '100000||1*1000', '100000*1-1000',
                '1000/1||100000', '100000@1000/1', '1000/100000-1', '1*100000@1000', '1000+100000@1', '1/1000-100000',
                '1000*100000+1', '1-100000||1000', '1000-100000+1', '100000*1000||1', '1000/100000*1', '100000@1||1000',
                '1+1000||100000', '1000*100000||1', '1000*1||100000', '1000*1/100000', '1000-1||100000',
                '1000||100000-1', '1000||100000/1', '1000+1||100000', '100000/1@1000', '1@1000*100000', '1/1000@100000',
                '1000/100000@1', '1||100000-1000', '100000-1000+1', '1@1000+100000', '100000@1000*1', '100000-1000/1',
                '1000+1@100000', '1*100000+1000', '100000-1+1000', '1@100000/1000', '1000-1/100000', '1*100000/1000',
                '1||1000/100000', '100000-1000@1', '100000+1000||1', '100000@1000+1', '1+1000@100000', '100000+1||1000',
                '100000/1000*1', '1000+100000-1', '1000@100000||1', '100000@1-1000', '1*1000+100000', '1@100000-1000',
                '1/100000-1000', '1000*100000/1', '100000+1000/1', '100000@1*1000', '100000+1@1000', '1-100000*1000',
                '1000+1/100000', '100000@1/1000', '100000-1000||1', '1000@100000-1', '100000||1000-1', '100000-1*1000',
                '100000-1000*1', '100000/1000||1', '100000||1/1000', '100000*1000-1', '1000||100000+1', '100000/1000@1',
                '1*1000/100000', '100000+1*1000', '1-1000/100000', '100000@1+1000', '1-1000@100000', '1000||1/100000',
                '1000@1||100000', '100000+1000@1', '1@100000+1000', '100000*1/1000', '1000-100000@1', '1000-100000/1',
                '1+1000/100000', '1||100000+1000', '1000+100000/1', '1000*100000-1', '1@1000-100000', '1/1000+100000',
                '1+1000*100000', '1000@1+100000', '1*100000-1000', '1@100000||1000', '100000-1/1000', '100000||1+1000',
                '100000/1+1000', '1000/100000||1', '1000*100000@1', '100000-1@1000', '100000+1000-1', '100000+1-1000',
                '100000/1000+1', '1-1000+100000', '1000+1*100000', '100000*1000/1', '1000||100000@1', '1000+100000*1',
                '1+100000/1000', '1000@100000*1', '100000-1||1000', '1-100000@1000', '1||1000+100000', '1/100000*1000',
                '1+100000||1000', '1000-100000*1', '1@1000/100000', '100000*1+1000', '1000@100000+1', '1+100000-1000',
                '100000||1@1000', '100000@1000||1', '100000||1000@1', '1||1000@100000', '1000@100000/1',
                '100000||1000+1', '1000-1+100000', '1000@1/100000', '1000||1-100000', '100000*1||1000', '1000*1-100000',
                '1*1000@100000', '100000+1/1000', '1000-1@100000', '1||100000/1000', '1000-1*100000', '1000/1-100000',
                '1000@1-100000', '100000@1000-1', '1/100000@1000', '1+1000-100000'}
    return do_ex2_test(nums, ops, expected, score=3)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3,
    test_func2_1, test_func2_2, test_func2_3,
    test_func3_1, test_func3_2, test_func3_3,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3,
    test_ex1_1,   test_ex1_2,  test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
]


if __name__ == '__main__':
    test_personal_data_entry()
    check_expected()
    runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    grades = {}
    total  = 0
    with open('grade.csv') as F:
        for line in F:
            test, points = line.split(',')
            _, name, *_ = test.split('_')
            if name == 'personal': continue
            total += float(points)
            grades[name] = grades.get(name, 0) + float(points)
    #%% Constraint for the exam
    if not total >= 18:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['GREEN']}{total}{COL['RST']} POINTS")
################################################################################

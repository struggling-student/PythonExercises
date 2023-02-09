# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program


def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['RED']
        return func(f'{COL["BOLD"]}{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
    return wrapped_func

print = my_decorator(print)

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

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m',
       'BOLD' : '\033[1m',
       'ENDC' : '\033[0m'}


def test_personal_data_entry():
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


def test_func1_1():
    '''
    ['cocacola','fanta', 'sprite', 'lambdala']
    '''
    string_list = ['cocacola', 'fanta', 'sprite', 'lambdala']
    expected = ['fanta', 'sprite']
    word = 'la'
    N = 2
    return do_func1_tests(string_list, word, expected, N)

def test_func1_2():
    '''
    'Francesco è eliminato da MasterChef 12. L’attacco ai giudici: Ricordatevi che siamo persone'
    '''
    string_list = 'Francesco è eliminato da MasterChef 12. L’attacco ai giudici: Ricordatevi che siamo persone'.split()
    word = 'e'
    expected = ['è', 'da', '12.', 'L’attacco', 'ai', 'giudici:', 'siamo']
    N = 6
    return do_func1_tests(string_list, word, expected, N)

def test_func1_3():
    '''
    'Lotteria Italia, questa sera l’estrazione dei biglietti vincenti: nel Lazio venduto il maggior numero di tagliandi'
    '''
    string_list = 'Lotteria Italia, questa sera l’estrazione dei biglietti vincenti: nel Lazio venduto il maggior numero di tutti i tagliandi'.split()
    word = 'tt'
    expected = ['Italia,', 'questa', 'sera', 'l’estrazione', 'dei', 'vincenti:', 'nel', 'Lazio', 'venduto', 'il', 'maggior', 'numero', 'di', 'i', 'tagliandi']
    N = 3
    return do_func1_tests(string_list, word, expected, N)


def do_func2_tests(pathname, expected):
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


def test_func2_1():
    '''
    func2_test_1.txt
    '''
    pathname = 'func2_test_1.txt'
    expected = {'123456': 27, '121212': 79, '111111': 91}
    return do_func2_tests(pathname, expected)

def test_func2_2():
    '''
    func2_test_2.txt
    '''
    pathname = 'func2_test_2.txt'
    expected = {'858567': 70, '944686': 65, '502665': 61, '922651': 98, '669985': 99, '708542': 66, '190832': 92, '446778': 16, '715822': 58, '496949': 60, '855338': 51, '654439': 66, '286452': 53, '386087': 82, '066402': 22, '862915': 58, '715947': 81, '253929': 30, '647445': 76, '481654': 90}
    return do_func2_tests(pathname, expected)

def test_func2_3():
    '''
    func2_test_3.txt
    '''
    pathname = 'func2_test_3.txt'
    expected = {'1615350266': 17, '6153502665': 5, '1535026650': 42, '5350266507': 2, '3502665073': 91, '5026650732': 67, '0266507329': 32, '2665073290': 68, '6650732906': 33, '6507329068': 30, '5073290685': 31, '0732906855': 89, '7329068553': 97, '3290685533': 54, '2906855338': 33, '9068553381': 34, '0685533818': 88, '6855338182': 33, '8553381822': 86, '5533818222': 35, '5338182224': 77, '3381822242': 86, '3818222427': 67, '8182224279': 20, '1822242797': 82, '8222427974': 86, '2224279740': 58, '2242797404': 14, '2427974040': 99, '4279740404': 35, '2797404044': 10, '7974040442': 38, '9740404427': 4}
    return do_func2_tests(pathname, expected)


def do_func3_tests(listA, expected, outpath):
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
            testlib.check_text_file(actual_out_path,
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


def test_func3_1():
    '''
    listaA = ['ananas', 'banana', 'pluto', 'zoroastro', 'marx', 'socrate', 'PLATO']
    '''
    lista = ['ananas', 'banana', 'pluto', 'zoroastro', 'marx', 'socrate', 'PLATO']
    expected = 42
    return do_func3_tests(lista, expected, 'func3_1_!!TMP!!.txt')

def test_func3_2():
    '''
    listaA = ['A', 'survey', 'of', 'user', 'opinion', 'of', 'computer', 'system', 'response', 'time']
'''
    lista = "A survey of user opinion of computer system response time".split()
    expected = 48
    return do_func3_tests(lista, expected, 'func3_2_!!TMP!!.txt')

def test_func3_3():
    '''
    listA = ['HdzCZJ', 'dzCZJy', 'zCZJyg', 'CZJygW', 'ZJygWo', 'Jy.....
    '''
    lista = ['HdzCZJ', 'dzCZJy', 'zCZJyg', 'CZJygW', 'ZJygWo', 'JygWoE', 'ygWoEM', 'gWoEMw', 'WoEMwQ', 'oEMwQz', 'EMwQzY', 'MwQzYr', 'wQzYrb', 'QzYrbl', 'zYrblN', 'YrblNv', 'rblNvK', 'blNvKs', 'lNvKsy', 'NvKsyd', 'vKsydc', 'Ksydcp', 'sydcpO', 'ydcpOm', 'dcpOmB', 'cpOmBC', 'pOmBCF', 'OmBCFo', 'mBCFoe', 'BCFoeV', 'CFoeVK', 'FoeVKF', 'oeVKFp', 'eVKFpe', 'VKFpeI', 'KFpeIo', 'FpeIot', 'peIotw', 'eIotwr', 'Iotwrq', 'otwrqJ', 'twrqJK', 'wrqJKS']
    expected = 258
    return do_func3_tests(lista, expected, 'func3_3_!!TMP!!.txt')

# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(S, expected):
    res = program.func4(S)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The histogram string should be \n{expected}\nCodified as a string={repr(expected)}\n instead of\n{res}\nCodified as a string={repr(res)}\n'''
              f'''[ERROR] L'istogramma stringa deve essere \n{expected}\nCodificato come stringa={repr(expected)}\n  invece che\n{res}.\nCodificato come stringa={repr(res)}\n {'*'*50}''')
        return 0
    return 2


def test_func4_1():
    '''
    S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era scordato di chiamare Paperino'
    '''
    S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era scordato di chiamare Paperino'
    expected = 'al        **\nandati    *\nbella     *\nchiamare  *\ndi        *\ne         *\nera       *\ngiorno    *\nhanno     *\nil        *\nin        *\nma        *\nmangiato  *\nmare      **\npaperino  *\npasta     *\npescato   *\npesce     *\npippo     *\nprima     *\npurtroppo *\nscordato  *\nsi        *\nsono      *\ntopolino  **\nuna       *\n'
    return do_func4_tests(S, expected)

def test_func4_2():
    '''
    S = 'From: mathew <mathew@mantis.co.uk>\nSubject: Re: university violating separation of church/state?\nOrganiz...
    '''
    S = 'From: mathew <mathew@mantis.co.uk>\nSubject: Re: university violating separation of church/state?\nOrganization: Mantis Consultants, Cambridge. UK.\nX-Newsreader: rusnews v1.01\nLines: 29\n\ndmn@kepler.unh.edu (...until kings become philosophers or philosophers become kings) writes:\n>'
    expected = 'become       **\ncambridge    *\nchurch       *\nco           *\nconsultants  *\ndmn          *\nedu          *\nfrom         *\nkepler       *\nkings        **\nlines        *\nmantis       **\nmathew       **\nnewsreader   *\nof           *\nor           *\norganization *\nphilosophers **\nre           *\nrusnews      *\nseparation   *\nstate        *\nsubject      *\nuk           **\nunh          *\nuniversity   *\nuntil        *\nv            *\nviolating    *\nwrites       *\nx            *\n'
    return do_func4_tests(S, expected)


def test_func4_3():
    '''
    S = 'Re: <<Pompous ass\nOrganization: Tektronix Inc., Beaverto ......
    '''

    S = 'Re: <<Pompous ass\nOrganization: Tektronix Inc., Beaverton, Or.\nLines: 20\n\nIn article <1ql6jiINN5df@gap.caltech.edu> keith@cco.caltech.edu (Keith Allan Schneider) writes:\n>\n>The "`little\' things" above were in reference to Germany, clearly.  People\n>said that there were similar things in Germany, but no one could name any.\n>They said that these were things that everyone should know, and that they\n>weren\'t going to waste their time repeating them.  Sounds to me like no one\n>knew, either.  I looked in some books, but to no avail.\n\n  If the Anne Frank exhibit makes it to your small little world,\n  take an afternoon to go see it.  \n\n\n/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\ \n\nBob Beauchaine bobbe@vice.ICO.TEK.COM \n\nThey said that Queens could stay, they blew the Bronx away,\nand sank Manhattan out at sea.\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
    expected = 'above        *\nafternoon    *\nallan        *\nan           *\nand          **\nanne         *\nany          *\narticle      *\nass          *\nat           *\navail        *\naway         *\nbeauchaine   *\nbeaverton    *\nblew         *\nbob          *\nbobbe        *\nbooks        *\nbronx        *\nbut          **\ncaltech      **\ncco          *\nclearly      *\ncom          *\ncould        **\ndf           *\nedu          **\neither       *\neveryone     *\nexhibit      *\nfrank        *\ngap          *\ngermany      **\ngo           *\ngoing        *\ni            *\nico          *\nif           *\nin           ****\ninc          *\nit           **\njiinn        *\nkeith        **\nknew         *\nknow         *\nlike         *\nlines        *\nlittle       **\nlooked       *\nmakes        *\nmanhattan    *\nme           *\nname         *\nno           ***\none          **\nor           *\norganization *\nout          *\npeople       *\npompous      *\nql           *\nqueens       *\nre           *\nreference    *\nrepeating    *\nsaid         ***\nsank         *\nschneider    *\nsea          *\nsee          *\nshould       *\nsimilar      *\nsmall        *\nsome         *\nsounds       *\nstay         *\nt            *\ntake         *\ntek          *\ntektronix    *\nthat         *****\nthe          ***\ntheir        *\nthem         *\nthere        *\nthese        *\nthey         ****\nthings       ***\ntime         *\nto           ******\nvice         *\nwaste        *\nwere         ***\nweren        *\nworld        *\nwrites       *\nyour         *\n'
    return do_func4_tests(S, expected)

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
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''imm_in = func5/image01.png
    imm_out = func5/expected01.png
    expected = (256, 256)
    '''
    ID = 1
    expected = (256, 256)
    return do_test_func5(ID, expected)


def test_func5_2():
    '''imm_in = func5/image02.png
    imm_out = func5/expected02.png
    expected = 3
    '''
    ID = 2
    expected = (256, 128)
    return do_test_func5(ID, expected)


def test_func5_3():
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
    testlib.check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
    return 2


def test_ex1_1():
    '''
    directory = 'ex1_A'
    '''
    directory = 'ex1_A'
    expected = {'ex1_A/bkLbD': 'A\x9eŻĂĳŜǖ', 'ex1_A': 'KTTISLJL'}
    return do_test_ex1(directory, expected)


def test_ex1_2():
    '''directory = 'ex1_B'
    '''
    directory = 'ex1_B'
    expected = {'ex1_B/stSOl': 'àWŰĦÁƭĉǌǀ', 'ex1_B/vWHJp': 'IřǱāƁƢÒ~ǀď\x85¹Ɩƕ', 'ex1_B': '¶\x9d\x83ÔǄď'}
    return do_test_ex1(directory, expected)


def test_ex1_3():
    '''directory = 'ex1_C'
    '''
    directory = 'ex1_C'
    expected = {'ex1_C/Lospm/Khvrj': 'ª\x84ĵķƉðĔMǇǧƴĈ', 'ex1_C/Lospm/TTINY': '®ªÖŇTƑǁĮĊvƅĕŒ', 'ex1_C/Lospm/nghch': 'ØÜÄeŽêíƍōWŚ', 'ex1_C/Lospm/vcynO': 'Ŏ«\x83ı²qŐ', 'ex1_C/Lospm/wGuOG': 'ŖõƙċƂ³¨', 'ex1_C/Lospm': 'Ơ\\', 'ex1_C/MfzQL/eiKqi': '¿ÜwþǟL', 'ex1_C/MfzQL/fNcLp': 'wĥ¿ŷ\x81', 'ex1_C/MfzQL/rtGJs': 'ſŻÑǙ³Ƃ\x84ƬƁ\x9f', 'ex1_C/MfzQL': 'ŕŰťǋ\xad²\x9aœ', 'ex1_C/sOsTK/Ffufy': '\x97ņíƢ', 'ex1_C/sOsTK/IpUQx': 'ƼŦĲűų', 'ex1_C/sOsTK/pjDEZ': '^ǃuŽ»ų', 'ex1_C': 'ņĞö\x88ŭ'}
    return do_test_ex1(directory, expected)
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
        testlib.check(type(res), set, None, f"Wrong return type! Returned={type(res)}, expected= set / Il tipo ritornato non è corretto! Ritornato={type(res)}, atteso= set")
    p=0
    if type(res) == set:
        testlib.check(res, set(expected), None, f"Wrong set returned! Returned={res}, expected={expected} / Il set ritornato non è corretto! Ritornato={res}, atteso ={expected}")
        print("Correct set returned", end=' ')
        p = score
    return p


def test_ex2_1():
    '''
    nums = {5, 8, 0}; ops=['+', '*']
    '''
    nums = {5, 8, 0}; ops = ['+', '*']
    expected = ['8+5+0', '8+0+5', '5+8+0', '5+0+8', '0+8+5', '0+5+8', '8+5*0',
                '8+0*5', '8*5+0', '8*0+5', '5+8*0', '5+0*8', '5*8+0', '5*0+8',
                '0+8*5', '0+5*8', '0*8+5', '0*5+8', '8*5*0', '8*0*5', '5*8*0',
                '5*0*8', '0*8*5', '0*5*8']
    return do_ex2_test(nums, ops, expected)

def test_ex2_2():
    '''
    nums = {99, 88, 100}; ops=['+', '*', '-']
    '''
    nums = {99, 88, 100}; ops = ['+', '*', '-']
    expected =  ['99+88+100', '99+100+88', '88+99+100', '88+100+99', '100+99+88', '100+88+99', '99+88*100', '99+100*88', '99*88+100', '99*100+88', '88+99*100', '88+100*99', '88*99+100', '88*100+99', '100+99*88', '100+88*99', '100*99+88', '100*88+99', '99-88+100', '99-100+88', '99+88-100', '99+100-88', '88-99+100', '88-100+99', '88+99-100', '88+100-99', '100-99+88', '100-88+99', '100+99-88', '100+88-99', '99*88*100', '99*100*88', '88*99*100', '88*100*99', '100*99*88', '100*88*99', '99-88*100', '99-100*88', '99*88-100', '99*100-88', '88-99*100', '88-100*99', '88*99-100', '88*100-99', '100-99*88', '100-88*99', '100*99-88', '100*88-99', '99-88-100', '99-100-88', '88-99-100', '88-100-99', '100-99-88', '100-88-99']
    return do_ex2_test(nums, ops, expected, score=3)


def test_ex2_3():
    '''
    nums = {1, 100000, 1000}; ops = ['+', '*', '-', '/', '@', '||']
    '''
    nums = {1, 100000, 1000}; ops = ['+', '*', '-', '/', '@', '||']
    expected = ['100000+1000+1', '100000+1+1000', '1000+100000+1', '1000+1+100000', '1+100000+1000', '1+1000+100000', '100000+1000*1', '100000+1*1000', '100000*1000+1', '100000*1+1000', '1000+100000*1', '1000+1*100000', '1000*100000+1', '1000*1+100000', '1+100000*1000', '1+1000*100000', '1*100000+1000', '1*1000+100000', '100000-1000+1', '100000-1+1000', '100000+1000-1', '100000+1-1000', '1000-100000+1', '1000-1+100000', '1000+100000-1', '1000+1-100000', '1-100000+1000', '1-1000+100000', '1+100000-1000', '1+1000-100000', '100000/1000+1', '100000/1+1000', '100000+1000/1', '100000+1/1000', '1000/100000+1', '1000/1+100000', '1000+100000/1', '1000+1/100000', '1/100000+1000', '1/1000+100000', '1+100000/1000', '1+1000/100000', '1@100000+1000', '1@1000+100000', '1000@100000+1', '1000@1+100000', '100000@1000+1', '100000@1+1000', '100000+1@1000', '100000+1000@1', '1000+1@100000', '1000+100000@1', '1+1000@100000', '1+100000@1000', '1||100000+1000', '1||1000+100000', '1000||100000+1', '1000||1+100000', '100000||1000+1', '100000||1+1000', '100000+1||1000', '100000+1000||1', '1000+1||100000', '1000+100000||1', '1+1000||100000', '1+100000||1000', '100000*1000*1', '100000*1*1000', '1000*100000*1', '1000*1*100000', '1*100000*1000', '1*1000*100000', '100000-1000*1', '100000-1*1000', '100000*1000-1', '100000*1-1000', '1000-100000*1', '1000-1*100000', '1000*100000-1', '1000*1-100000', '1-100000*1000', '1-1000*100000', '1*100000-1000', '1*1000-100000', '100000/1000*1', '100000/1*1000', '100000*1000/1', '100000*1/1000', '1000/100000*1', '1000/1*100000', '1000*100000/1', '1000*1/100000', '1/100000*1000', '1/1000*100000', '1*100000/1000', '1*1000/100000', '1@100000*1000', '1@1000*100000', '1000@100000*1', '1000@1*100000', '100000@1000*1', '100000@1*1000', '100000*1@1000', '100000*1000@1', '1000*1@100000', '1000*100000@1', '1*1000@100000', '1*100000@1000', '1||100000*1000', '1||1000*100000', '1000||100000*1', '1000||1*100000', '100000||1000*1', '100000||1*1000', '100000*1||1000', '100000*1000||1', '1000*1||100000', '1000*100000||1', '1*1000||100000', '1*100000||1000', '100000-1000-1', '100000-1-1000', '1000-100000-1', '1000-1-100000', '1-100000-1000', '1-1000-100000', '100000/1000-1', '100000/1-1000', '100000-1000/1', '100000-1/1000', '1000/100000-1', '1000/1-100000', '1000-100000/1', '1000-1/100000', '1/100000-1000', '1/1000-100000', '1-100000/1000', '1-1000/100000', '1@100000-1000', '1@1000-100000', '1000@100000-1', '1000@1-100000', '100000@1000-1', '100000@1-1000', '100000-1@1000', '100000-1000@1', '1000-1@100000', '1000-100000@1', '1-1000@100000', '1-100000@1000', '1||100000-1000', '1||1000-100000', '1000||100000-1', '1000||1-100000', '100000||1000-1', '100000||1-1000', '100000-1||1000', '100000-1000||1', '1000-1||100000', '1000-100000||1', '1-1000||100000', '1-100000||1000', '100000/1000/1', '100000/1/1000', '1000/100000/1', '1000/1/100000', '1/100000/1000', '1/1000/100000', '1@100000/1000', '1@1000/100000', '1000@100000/1', '1000@1/100000', '100000@1000/1', '100000@1/1000', '100000/1@1000', '100000/1000@1', '1000/1@100000', '1000/100000@1', '1/1000@100000', '1/100000@1000', '1||100000/1000', '1||1000/100000', '1000||100000/1', '1000||1/100000', '100000||1000/1', '100000||1/1000', '100000/1||1000', '100000/1000||1', '1000/1||100000', '1000/100000||1', '1/1000||100000', '1/100000||1000', '1@1000@100000', '1@100000@1000', '1000@1@100000', '1000@100000@1', '100000@1@1000', '100000@1000@1', '1||1000@100000', '1||100000@1000', '1@1000||100000', '1@100000||1000', '1000||1@100000', '1000||100000@1', '1000@1||100000', '1000@100000||1', '100000||1@1000', '100000||1000@1', '100000@1||1000', '100000@1000||1', '1||1000||100000', '1||100000||1000', '1000||1||100000', '1000||100000||1', '100000||1||1000', '100000||1000||1']
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
    test_ex1_1,  test_ex1_2,  test_ex1_3,
    test_ex2_1,    test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
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
    constraint1 = len([name for name,grade in grades.items() if grade>0 and name.startswith('func')]) >= 3
    constraint2 = len([name for name,grade in grades.items() if grade>0 and name.startswith('ex')]) >= 1
    constraint3 = total >= 18
    constraint4 = all((constraint1, constraint2, constraint3))
    if not constraint1:
        print(f'YOU HAVE NOT PASSED AT LEAST 3 FUNC EXERCISES: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint2:
        print(f'YOU HAVE NOT PASSED AT LEAST 1 RECURSIVE EXERCISE: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint3:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
################################################################################

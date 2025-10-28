# -*- coding: utf-8 -*-
import testlib
from testlib import my_print, COL, check_expected

import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
# %% ---------------------- DEBUG VARIABLE -------------------
#DEBUG = True    # with    stack trace of errors
DEBUG = False   # without stack trace of errors

#############################################################################
# %% ---------------------- TEST SECTION -------------------
#############################################################################

def test_personal_data_entry():
    assert program.nome      != 'NOME',      f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME',   f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9

###########################################################################################################################

def do_func1_tests(ID, expected):
    input_filename  = f'txt/in_0{ID}.txt'
    res = program.func1(input_filename)
    testlib.checkList(res, expected)
    return 1.5

def test_func1_1():
    ID = 1
    expected = ['bat', 'car', 'cat', 'condor', 'rat']
    return do_func1_tests(ID, expected)

def test_func1_2():
    ID = 2
    expected = ['absurdly', 'actuator', 'ai', 'anus', 'aqdb', 'b', 'bc', 'c', 'd', 'defectors', 'disadvantage', 'doormen', 'expected', 'f', 'fit', 'fitb', 'gbe', 'h', 'ih', 'j', 'm', 'od', 'pg', 'qi', 's', 't', 'vmn', 'wa', 'yvbo']
    return do_func1_tests(ID, expected)

def test_func1_3():
    ID = 3
    expected = ['adduced', 'analytics', 'crapshooter', 'decreer', 'deprivations', 'develops', 'drastic', 'establishes', 'griding', 'humanistic', 'lubricative', 'noggins', 'overtire', 'panoramic', 'penthouses', 'percolating', 'supportability', 'tachometer', 'unharvested', 'wintertime']
    return do_func1_tests(ID, expected)

def test_func1_4():
    ID = 4
    expected = ['a', 'abbandonai', 'acciò', 'acqua', 'acquista', 'aere', 'affannata', 'ahi', 'aiutami', 'al', 'alighieri', 'allor', 'alta', 'altezza', 'alto', 'altre', 'altri', 'altro', 'altrui', 'amara', 'ambedui', 'ammoglia', 'amor', 'amore', 'anchise', 'ancor', 'ancora', 'anima', 'animali', 'animo', 'antichi', 'anzi', 'apparve', 'aspra', 'attrista', 'augusto', 'autore', 'avea', 'avrà', 'basso', 'beate', 'belle', 'bello', 'ben', 'bene', 'bestia', 'brame', 'bramosa', 'bugiardi', 'buono', 'caccerà', 'cagion', 'cagione', 'calle', 'cammilla', 'cammin', 'cammino', 'campar', 'cantai', 'canto', 'carca', 'cercar', 'certo', 'ch', 'che', 'chi', 'ché', 'ciascun', 'ciberà', 'città', 'ciò', 'colle', 'color', 'colui', 'com', 'combusto', 'come', 'cominciar', 'commedia', 'compunto', 'con', 'conoscesti', 'contenti', 'contra', 'convien', 'cor', 'corpo', 'cosa', 'cose', 'costui', 'così', 'cotanto', 'coverta', 'cu', 'cui', 'd', 'da', 'dal', 'dante', 'de', 'degna', 'del', 'desse', 'di', 'dicesti', 'dietro', 'dilettoso', 'dinanzi', 'dio', 'dipartilla', 'dir', 'diritta', 'dirò', 'discerno', 'diserta', 'diserto', 'disperate', 'divina', 'divino', 'doglia', 'dolce', 'dolenti', 'dopo', 'dov', 'dove', 'dritto', 'dura', 'durata', 'dèi', 'e', 'ecco', 'ed', 'elegge', 'ella', 'empie', 'era', 'eran', 'erta', 'esta', 'esto', 'etterno', 'eurialo', 'fa', 'face', 'fai', 'falsi', 'fame', 'famoso', 'farà', 'fatto', 'fece', 'felice', 'feltro', 'fermo', 'ferute', 'fia', 'fiera', 'figliuol', 'fin', 'fioco', 'fiume', 'foco', 'fonte', 'forte', 'fosse', 'fronte', 'fu', 'fugga', 'fuggiva', 'fui', 'fuor', 'furon', 'fé', 'gaetta', 'genti', 'gioia', 'giugne', 'giunto', 'giusto', 'già', 'grame', 'gran', 'grande', 'gravezza', 'grida', 'gridai', 'gride', 'guardai', 'guata', 'guida', 'ha', 'ho', 'i', 'il', 'ilión', 'impera', 'imperador', 'in', 'inferno', 'infin', 'intrai', 'io', 'italia', 'iulio', 'ivi', 'l', 'la', 'lago', 'lagrimar', 'largo', 'lascerò', 'lascia', 'lasciò', 'lasso', 'le', 'legge', 'leggera', 'lei', 'lena', 'leone', 'li', 'lo', 'loco', 'lombardi', 'lonza', 'lui', 'lume', 'lungo', 'lupa', 'là', 'm', 'ma', 'macolato', 'maestro', 'magrezza', 'mai', 'male', 'malvagia', 'mantoani', 'mattino', 'me', 'mena', 'meni', 'mentre', 'mesti', 'mezzo', 'mi', 'miei', 'mio', 'miserere', 'molte', 'molti', 'molto', 'montava', 'monte', 'morir', 'morte', 'morì', 'mosse', 'mpedisce', 'mpediva', 'n', 'nacqui', 'natura', 'nazion', 'ncontro', 'ne', 'nel', 'nferno', 'niso', 'noia', 'non', 'nostra', 'notte', 'nvidia', 'né', 'o', 'occhi', 'od', 'offerto', 'ogne', 'oh', 'ombra', 'omo', 'ond', 'onde', 'onore', 'or', 'ora', 'oscura', 'ove', 'pace', 'parea', 'parenti', 'parlar', 'parti', 'partia', 'partire', 'passai', 'passar', 'passo', 'pasto', 'patria', 'paura', 'peggio', 'pel', 'pelago', 'pelle', 'peltro', 'pensier', 'penso', 'per', 'perch', 'perché', 'perdei', 'perder', 'perigliosa', 'persona', 'piaggia', 'pianeta', 'piange', 'pien', 'pieta', 'pietro', 'piè', 'più', 'poco', 'poeta', 'poeti', 'poi', 'polsi', 'porse', 'porta', 'posato', 'presta', 'pria', 'prima', 'principio', 'punto', 'quai', 'qual', 'quando', 'quanto', 'quasi', 'quei', 'quel', 'quella', 'quelle', 'quello', 'questa', 'questi', 'questo', 'queta', 'qui', 'quivi', 'rabbiosa', 'raggi', 'regge', 'regna', 'retro', 'ria', 'ribellante', 'richeggio', 'ridir', 'rimessa', 'rimirar', 'rinova', 'ripigneva', 'ripresi', 'rispuos', 'rispuose', 'rispuosemi', 'ritornar', 'ritorni', 'ritrovai', 'riva', 'roma', 'rovinava', 's', 'saggio', 'sali', 'salire', 'salute', 'san', 'sanza', 'sapienza', 'saranno', 'sarà', 'sarò', 'scorte', 'se', 'seconda', 'seggio', 'segui', 'selva', 'selvaggia', 'selvaggio', 'sembiava', 'sempre', 'si', 'sia', 'sii', 'silenzio', 'smarrita', 'so', 'sol', 'solo', 'son', 'sonno', 'sotto', 'spalle', 'spandi', 'speran', 'speranza', 'sperar', 'spiriti', 'stagione', 'stelle', 'stilo', 'strida', 'studio', 'sua', 'sub', 'sue', 'suoi', 'superbo', 'sì', 'sù', 'tace', 'tal', 'tant', 'tanta', 'tanto', 'tardi', 'te', 'temp', 'tempo', 'tenere', 'tenni', 'terminava', 'terra', 'test', 'ti', 'tolsi', 'tra', 'trarrotti', 'trattar', 'tremar', 'tremesse', 'troia', 'trovai', 'tu', 'tua', 'tuo', 'turno', 'tutt', 'tutta', 'tutte', 'uccide', 'udirai', 'umile', 'un', 'una', 'uscia', 'uscito', 'v', 'vagliami', 'valle', 'vederai', 'vedi', 'vedrai', 'veggia', 'vegna', 'veltro', 'vene', 'venendomi', 'venire', 'venisse', 'venne', 'verace', 'vergine', 'vergognosa', 'verrà', 'vestite', 'vi', 'via', 'viaggio', 'vide', 'vidi', 'villa', 'virgilio', 'virtute', 'vissi', 'vista', 'vita', 'viva', 'viver', 'voglia', 'volge', 'volontieri', 'volse', 'volsi', 'volte', 'volto', 'volume', 'vorrai', 'vuo', 'vuol', 'vòlto', 'è', 'èi']
    return do_func1_tests(ID, expected)


###########################################################################################################################

def do_func2_tests(ID1, ID2, expected):
    input_filename  = f'txt/in_0{ID1}.txt'
    input_filename_b  = f'txt/in_0{ID2}.txt'
    res = program.func2(input_filename, input_filename_b)
    testlib.checkList(res, expected)
    return 1.5

def test_func2_1():
    IDa = 1
    IDb = 3
    expected = ['B', 'D', 'E', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'S', 'U', 'V', 'Y', 'e', 'g', 'h', 'i', 'l', 'm', 'p', 's', 'u', 'v', 'w', 'y', '😌']
    return do_func2_tests(IDa, IDb, expected)


def test_func2_2():
    IDa = 1
    IDb = 1
    expected = []
    return do_func2_tests(IDa, IDb, expected)


def test_func2_3():
    IDa = 2
    IDb = 3
    expected = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'F', 'X', 'f', 'j', 'q', 'x', 'H', 'Y', 'l', '😌']
    return do_func2_tests(IDa, IDb, expected)


def test_func2_4():
    IDa = 4
    IDb = 3
    expected = ['!', '"', "'", ',', '.', ':', ';', '?', 'F', 'Q', 'f', 'q', 'z', 'à', 'è', 'é', 'ì', 'ò', 'ó', 'ù', 'B', 'G', 'H', 'S', 'U', 'Y', 'w', 'y', '😌']
    return do_func2_tests(IDa, IDb, expected)



###########################################################################################################################

def do_func3_tests(ID, a_list, listi, expected):
    output_filename = f'txt/out_0{ID}.txt'
    expected_filename = f'txt/exp_0{ID}.txt'
    res = program.func3(a_list, listi, output_filename)
    testlib.check_text_file(output_filename, expected_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}\nexpected={expected}.\n{'*'*50}''')
        return 0
    return 1.5


def test_func3_1():
    ID = 0
    lists = [["monkey", "cat",], ["panda", "alligator"], ["zoo", 'zuu', 'zotero']]
    listi= [[1, 0], [0, 1], [2, 1, 0]]
    expected = 7
    return do_func3_tests(ID, lists, listi, expected)


def test_func3_2():
    ID = 1
    lists = [
        ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"],
        ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown", "black"],
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    ]
    listi = [
        [9, 0, 1, 4, 3, 7, 2, 5, 8, 6],
        [3, 2, 6, 4, 9, 5, 1, 0, 8, 7],
        [1, 3, 0, 7, 9, 5, 4, 6, 2, 8]
    ]
    expected = 30
    return do_func3_tests(ID, lists, listi, expected)


def test_func3_3():
    ID = 2
    lists = [
        ["car", "bus", "bike", "train", "plane", "boat"],  # 6 elements
        ["apple", "banana", "cherry", "date"],             # 4 elements
        ["red", "blue", "green", "yellow", "purple"],      # 5 elements
        ["one", "two", "three", "four", "five", "six", "seven"]  # 7 elements
    ]
    listi = [
        [5, 2, 0, 3, 1, 4],  # Permutation for the 6-element list
        [1, 3, 2, 0],        # Permutation for the 4-element list
        [4, 0, 3, 1, 2],     # Permutation for the 5-element list
        [6, 5, 3, 1, 4, 0, 2]  # Permutation for the 7-element list
    ]
    expected = 22
    return do_func3_tests(ID, lists, listi, expected)


def test_func3_4():
    ID = 3
    lists = [
        ["jazz", "rock", "pop", "blues", "classical", "hip-hop", "metal"],  # 7 elements
        ["paris", "london", "rome", "berlin", "madrid"],                   # 5 elements
        ["jupiter", "saturn", "neptune"],                                  # 3 elements
        ["north", "south", "east", "west"]                                 # 4 elements
    ]
    listi = [
        [6, 4, 3, 1, 0, 5, 2],  # Permutation for the 7-element music genre list
        [1, 3, 4, 0, 2],        # Permutation for the 5-element cities list
        [2, 0, 1],              # Permutation for the 3-element planets list
        [3, 1, 2, 0]            # Permutation for the 4-element directions list
    ]
    expected = 19
    return do_func3_tests(ID, lists, listi, expected)


def do_func4_tests(ID, expected, score=2):
    input_file = f'func4/func4_test{ID}.txt'
    output_file= f'func4/func4_out{ID}.txt'
    expected_file=f'func4/func4_exp{ID}.txt'
    res = program.func4(input_file, output_file)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è corretto! / Returned value is incorrect!\n'''
              f'''[ERROR] Expected {expected} returne {res}\n {'*'*50}''')
        return 0
    testlib.check_text_file(output_file, expected_file)
    return score

###########################################################################################################################

def test_func4_1():
    '''
    input_file = func4/func4_test1.txt
    output_file = func4/func4_out1.txt
    '''
    ID = 1
    expected = 6
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_file = func4/func4_test2.txt
    output_file = func4/func4_out2.txt
    '''
    ID = 2
    expected = 15
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_file = func4/func4_test3.txt
    output_file = func4/func4_out3.txt
    '''
    ID = 3
    expected = 20
    return do_func4_tests(ID, expected)

###########################################################################################################################
def do_func5_tests(ID, length, expected):
    input_filename  = f'func5/func5_test{ID}.txt'
    output_filename = f'func5/func5_out{ID}.txt'
    expected_filename = f'func5/func5_exp{ID}.txt'
    res = program.func5(input_filename, output_filename, length)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di righe ritornato è sbagliato! / The number of written rows is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func5_1():
    '''
    input_filename = 'func5/func5_test1.txt'
    expected = 7
    '''
    ID = 1
    length = 3
    expected = 7
    return do_func5_tests(ID, length, expected)

def test_func5_2():
    '''
    input_filename = 'func5/func5_test2.txt'
    '''
    ID = 2
    length = 8
    expected = 5
    return do_func5_tests(ID, length, expected)


def test_func5_3():
    '''
    input_filename = 'func5/func5_test3.txt'
    '''

    ID = 3
    length = 7
    expected = 20
    return do_func5_tests(ID, length, expected)


tests = [
    # TO DISABLE SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1 ,  test_func1_2, test_func1_3, test_func1_4, # OK 6
    test_func2_1,  test_func2_2, test_func2_3, test_func2_4, # OK 6
    test_func3_1,  test_func3_2, test_func3_3, test_func3_4, # OK 6
    test_func4_1, test_func4_2, test_func4_3, # OK 6
    test_func5_1, test_func5_2, test_func5_3, # OK 6
    test_personal_data_entry,
]

if __name__ == '__main__':
    import sys
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################

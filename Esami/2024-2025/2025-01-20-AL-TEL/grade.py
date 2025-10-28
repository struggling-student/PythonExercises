# -*- coding: utf-8 -*-

import testlib
import isrecursive2
import os
import sys

import nary_tree, tree
from testlib import my_print, COL, check_expected

#############################################################################
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = True
DEBUG = False
#############################################################################

################################################################################
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print(  'WARNING: Save program.empty.py as program.py\n'
            'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################
if DEBUG:
    # import classico senza decorazioni
    import program
else:
    # import del file decorato in modo che possa accorgersi della ricorsione
    modulename = 'program'
    decorated_code = isrecursive2.decorate_file(f"{modulename}.py")
    program = isrecursive2.import_from_string(modulename, decorated_code)

################################################################################

def test_personal_data_entry(run=True):
    assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

###############################################################################
# ----------------------------------- FUNC. 1----------------------------------- #
def do_func1_test(testo,expected):
    res = program.func1(testo)
    if res != expected:
        my_print(
            f'''{'*' * 50}\n[ERROR]Il valore ritornato non è corretto!\nReturned={res}\nExpected={expected}''')
        return 0
    return 1

def test_func1_1(run=True):
    testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
    expected = {'s': [0, 31], 'o': [1, 32, 35], 'p': [2, 9, 20, 27, 40, 51, 58], 'r': [3, 21, 52, 56],
                'a': [4, 7, 10, 13, 16, 19, 22, 25, 28, 38, 41, 44, 47, 50, 53, 59], 'l': [6, 15, 37, 46],
                'n': [11, 42], 'c': [12, 18, 24, 43, 49, 55], 'm': [26], 't': [33, 34], 'e': [57]}
    return do_func1_test(testo,expected)

def test_func1_2(run=True):
    testo = '''essere o non essere, questo è il dilemma: 
               se sia più nobile nella mente soffrire colpi di fionda e dardi d’atroce fortuna 
               o prender armi contro un mare d’affanni e, opponendosi, por loro fine? 
               morire, dormire; nient’altro; e con un sonno dire che poniamo fine al dolore 
               del cuore e ai mille tumulti naturali di cui è erede la carne: 
               è una conclusione da desiderarsi devotamente'''
    expected = {
        'e': [0, 3, 5, 13, 16, 18, 23, 36, 59, 74, 77, 83, 86, 95, 113, 128, 158, 161, 182, 194, 202, 222, 246, 255,
              260, 271, 289, 293, 306, 316, 335, 342, 344, 353, 381, 383, 385, 394, 429, 435, 439, 447, 453, 456],
        's': [1, 2, 14, 15, 24, 58, 61, 88, 206, 280, 425, 436, 443],
        'r': [4, 17, 92, 94, 117, 125, 132, 157, 162, 165, 173, 181, 212, 216, 243, 245, 251, 254, 267, 288, 315, 341,
              367, 382, 392, 440, 442],
        'o': [7, 10, 26, 70, 89, 98, 108, 126, 131, 154, 170, 174, 197, 200, 205, 211, 215, 217, 242, 250, 268, 274,
              281, 284, 296, 301, 312, 314, 340, 420, 427, 449],
        'n': [9, 11, 69, 76, 84, 109, 135, 159, 171, 177, 190, 191, 201, 203, 221, 258, 261, 275, 278, 282, 283, 297,
              305, 363, 393, 416, 421, 428, 454], 'q': [21],
        'u': [22, 134, 176, 277, 339, 356, 358, 366, 376, 415, 424],
        't': [25, 85, 124, 133, 172, 262, 266, 355, 360, 365, 450, 455], 'è': [28, 379, 413],
        'i': [30, 34, 62, 66, 72, 93, 101, 104, 107, 119, 167, 192, 207, 220, 244, 253, 259, 287, 298, 304, 347, 350,
              361, 370, 373, 377, 426, 437, 444],
        'l': [31, 35, 73, 78, 79, 99, 214, 265, 309, 313, 336, 351, 352, 359, 369, 387, 423],
        'd': [33, 103, 110, 115, 118, 121, 160, 184, 204, 249, 286, 311, 334, 372, 384, 431, 434, 438, 446],
        'm': [37, 38, 82, 166, 179, 241, 252, 300, 349, 357, 452],
        'a': [39, 63, 80, 111, 116, 123, 136, 164, 180, 186, 189, 264, 299, 308, 346, 364, 368, 388, 391, 417, 432, 441,
              451], 'p': [65, 100, 156, 198, 199, 210, 295], 'ù': [67], 'b': [71],
        'f': [90, 91, 106, 130, 187, 188, 219, 303], 'c': [97, 127, 169, 273, 291, 338, 375, 390, 419, 422], 'h': [292],
        'v': [448]}
    return do_func1_test(testo,expected)

# ----------------------------------- FUNC. 2----------------------------------- #
def do_func2_test(D1,D2,expected):
    res = program.func2(D1,D2)
    if res != expected:
        my_print(
            f'''{'*' * 50}\n[ERROR]Il valore ritornato non è corretto!\nReturned={res}, expected={expected}''')
        return 0
    return 1/2

def test_func2_1(run=True):
    D1 = {'a':[1,2,3], 'b':[3,4,5,6], 'c':[6,7,8]}
    D2 = {1:'ccc', 3:'qq', 4:'z', 5:'fff', 2:'zz'}
    expected = {'a': ['ccc', 'qq', 'zz'], 'b': ['fff', 'qq', 'z']}
    return do_func2_test(D1,D2,expected)

def test_func2_2(run=True):
    D1 = {'lye': [9, 8, 5, 7, 3, 1], 'blade': [9, 3, 4, 4, 4, 2, 8, 9, 1, 4], 'lay': [4, 5, 7, 9, 4, 3, 2, 5, 2, 4],
          'size': [7, 5, 5, 1, 4, 2, 5, 4], 'wise': [1, 2], 'alias': [3, 6, 6, 8, 9, 4, 5, 5], 'dot': [5, 6, 5, 6],
          'cod': [4, 6, 2, 2, 7, 8, 2, 9, 9, 8], 'bee': [8, 7, 1, 9, 9, 4, 8], 'itch': [8, 2, 8, 4, 5, 3, 6, 2]}
    D2 = {4: 'porcupine', 2: 'connect', 3: 'chipmunk', 7: 'node', 1: 'continue', 5: 'violence'}
    expected = {'lye': ['chipmunk', 'continue', 'violence', 'node'],
                'blade': ['porcupine', 'porcupine', 'porcupine', 'porcupine', 'chipmunk', 'continue', 'connect'],
                'lay': ['porcupine', 'porcupine', 'porcupine', 'chipmunk', 'violence', 'violence', 'connect', 'connect',
                        'node'],
                'size': ['porcupine', 'porcupine', 'continue', 'violence', 'violence', 'violence', 'connect', 'node'],
                'wise': ['continue', 'connect'], 'alias': ['porcupine', 'chipmunk', 'violence', 'violence'],
                'dot': ['violence', 'violence'], 'cod': ['porcupine', 'connect', 'connect', 'connect', 'node'],
                'bee': ['porcupine', 'continue', 'node'],
                'itch': ['porcupine', 'chipmunk', 'violence', 'connect', 'connect']}
    return do_func2_test(D1, D2, expected)

def test_func2_3(run=True):
    D1 = {'ash': [10, 4, 13, 14, 1, 14, 4, 6, 7], 'hope': [7, 5, 4, 4, 13, 12],
          'persuade': [14, 2, 2, 7, 4, 5, 6, 11, 12, 10, 7, 1, 4], 'cow': [3, 3, 3],
          'barber': [9, 1, 3, 5, 11, 8, 12, 1, 5, 12, 8, 7, 9], 'talent': [5, 1], 'poised': [13, 7, 7, 11, 8],
          'husky': [8, 5, 7, 9, 13, 5, 12], 'dive': [13, 11], 'spoon': [9, 9, 1, 4, 2, 12], 'bet': [3, 11],
          'lie': [11, 9, 10, 7, 13, 10, 9, 5, 9, 6, 11, 7, 13, 6, 8], 'chopstick': [4, 6, 2, 9],
          'grind': [5, 6, 11, 13, 11, 3, 14, 4, 6, 9]}
    D2 = {3: 'headrest', 13: 'butterfly', 11: 'trellis', 2: 'terrarium', 1: 'nickname', 9: 'border', 7: 'fascinated',
          6: 'cloakroom'}
    expected = {'ash': ['fascinated', 'butterfly', 'cloakroom', 'nickname'], 'hope': ['fascinated', 'butterfly'],
                'persuade': ['fascinated', 'fascinated', 'cloakroom', 'terrarium', 'terrarium', 'nickname', 'trellis'],
                'cow': ['headrest', 'headrest', 'headrest'],
                'barber': ['fascinated', 'headrest', 'nickname', 'nickname', 'trellis', 'border', 'border'],
                'talent': ['nickname'], 'poised': ['fascinated', 'fascinated', 'butterfly', 'trellis'],
                'husky': ['fascinated', 'butterfly', 'border'], 'dive': ['butterfly', 'trellis'],
                'spoon': ['terrarium', 'nickname', 'border', 'border'], 'bet': ['headrest', 'trellis'],
                'lie': ['fascinated', 'fascinated', 'butterfly', 'butterfly', 'cloakroom', 'cloakroom', 'trellis',
                        'trellis', 'border', 'border', 'border'], 'chopstick': ['cloakroom', 'terrarium', 'border'],
                'grind': ['butterfly', 'cloakroom', 'cloakroom', 'headrest', 'trellis', 'trellis', 'border']}
    return do_func2_test(D1, D2, expected)

def test_func2_4(run=True):
    D1 = {'black': [19, 17, 13, 1, 4, 21, 18, 7, 2, 8, 13, 8, 19, 9, 4, 19, 5],
          'bumper': [11, 24, 4, 20, 22, 10, 6, 9, 16, 1, 3, 2, 16, 5, 17, 11, 22, 23, 23, 5, 22, 3],
          'leprosy': [7, 4, 13, 20, 15, 16, 2, 12, 4, 24, 22, 12, 15, 13, 4, 4, 13, 7, 12, 1, 3],
          'follow': [4, 23, 24, 15, 24, 24, 11, 20, 17, 19, 5, 4, 24, 11],
          'grub': [15, 2, 14, 22, 15, 4, 24, 3, 14, 18, 6, 4, 17, 24, 5, 23, 23, 7, 1, 5, 22, 14],
          'tog': [14, 12, 22, 19, 13, 8, 13, 6, 3, 19, 8, 8, 1, 11, 3, 19, 15, 15, 9, 23, 2, 12, 2], 'sand': [6, 24, 6],
          'jug': [7, 20, 2, 16, 3, 5, 22, 7, 15, 20, 19, 16, 5, 14, 15, 3, 22, 11, 24, 14, 15, 14, 6],
          'life': [5, 24, 21, 8, 1], 'output': [2, 14, 19, 1, 4, 15, 23, 23, 2, 3, 13, 14, 9, 9, 24, 10, 20],
          'selfish': [4, 20], 'adoption': [15, 16, 20, 21, 7, 6, 4, 16, 10, 5, 21, 5, 20, 23, 4, 15, 9, 16],
          'prow': [8, 12, 10, 21, 12, 11, 2, 21, 12, 6, 11, 19, 12, 10, 24, 15, 11, 16, 14, 18, 24, 7, 18, 13],
          'pod': [8, 1, 11, 9, 21, 23, 11, 14, 7, 18, 19, 12, 8, 10, 7, 16, 14, 10, 24, 23],
          'SUV': [19, 23, 19, 14, 3, 5, 7, 2, 3, 19, 19, 13, 21, 22, 23, 15, 21, 10, 11, 2, 3, 9, 7, 2, 17],
          'pork': [23, 15, 12, 12, 23, 3, 10, 24, 12, 23, 21], 'strand': [18], 'guy': [22, 13, 19, 16, 11, 10, 16],
          'dizzy': [24, 22, 20, 17, 11, 1, 16, 1, 9, 18, 9, 10, 3, 23, 10, 17, 10, 18, 15], 'sink': [13, 7, 2, 6],
          'smog': [9, 7, 22, 17, 20, 7], 'peer': [22, 9, 18, 5, 4, 14, 1, 17, 7, 16, 7, 4, 7, 17, 22, 6, 9],
          'samurai': [13, 23, 8, 6, 5, 23, 23, 8, 4, 16, 10, 18, 3, 2, 11, 3, 7, 16, 10, 20],
          'lad': [7, 7, 22, 17, 9, 23, 20, 9, 1, 11, 16, 16, 12, 12, 6, 22, 7, 10, 10, 24, 19, 9, 11, 5, 9],
          'type': [4, 16, 19, 1, 1, 9, 8, 6, 6, 16, 1, 13, 9, 3, 11, 12, 16, 17, 17]}
    D2 = {11: 'macaroni', 19: 'classy', 21: 'machine', 6: 'enlist', 5: 'systemize', 17: 'archaeology',
          24: 'enthusiastic', 13: 'spatula', 2: 'embryo', 8: 'harpooner', 9: 'extract', 20: 'complaint',
          10: 'toothbrush', 15: 'extent', 7: 'cantaloupe', 18: 'return', 22: 'parsley', 4: 'documentary'}
    expected = {
        'black': ['archaeology', 'documentary', 'documentary', 'cantaloupe', 'harpooner', 'harpooner', 'systemize',
                  'extract', 'machine', 'spatula', 'spatula', 'classy', 'classy', 'classy', 'embryo', 'return'],
        'bumper': ['enthusiastic', 'archaeology', 'documentary', 'toothbrush', 'complaint', 'systemize', 'systemize',
                   'macaroni', 'macaroni', 'extract', 'parsley', 'parsley', 'parsley', 'embryo', 'enlist'],
        'leprosy': ['enthusiastic', 'documentary', 'documentary', 'documentary', 'documentary', 'cantaloupe',
                    'cantaloupe', 'complaint', 'parsley', 'spatula', 'spatula', 'spatula', 'embryo', 'extent',
                    'extent'],
        'follow': ['enthusiastic', 'enthusiastic', 'enthusiastic', 'enthusiastic', 'archaeology', 'documentary',
                   'documentary', 'complaint', 'systemize', 'macaroni', 'macaroni', 'classy', 'extent'],
        'grub': ['enthusiastic', 'enthusiastic', 'archaeology', 'documentary', 'documentary', 'cantaloupe', 'systemize',
                 'systemize', 'parsley', 'parsley', 'embryo', 'enlist', 'extent', 'extent', 'return'],
        'tog': ['harpooner', 'harpooner', 'harpooner', 'macaroni', 'extract', 'parsley', 'spatula', 'spatula', 'classy',
                'classy', 'classy', 'embryo', 'embryo', 'enlist', 'extent', 'extent'],
        'sand': ['enthusiastic', 'enlist', 'enlist'],
        'jug': ['enthusiastic', 'cantaloupe', 'cantaloupe', 'complaint', 'complaint', 'systemize', 'systemize',
                'macaroni', 'parsley', 'parsley', 'classy', 'embryo', 'enlist', 'extent', 'extent', 'extent'],
        'life': ['enthusiastic', 'harpooner', 'systemize', 'machine'],
        'output': ['enthusiastic', 'documentary', 'toothbrush', 'complaint', 'extract', 'extract', 'spatula', 'classy',
                   'embryo', 'embryo', 'extent'], 'selfish': ['documentary', 'complaint'],
        'adoption': ['documentary', 'documentary', 'cantaloupe', 'toothbrush', 'complaint', 'complaint', 'systemize',
                     'systemize', 'extract', 'machine', 'machine', 'enlist', 'extent', 'extent'],
        'prow': ['enthusiastic', 'enthusiastic', 'cantaloupe', 'toothbrush', 'toothbrush', 'harpooner', 'macaroni',
                 'macaroni', 'macaroni', 'machine', 'machine', 'spatula', 'classy', 'embryo', 'enlist', 'extent',
                 'return', 'return'],
        'pod': ['enthusiastic', 'cantaloupe', 'cantaloupe', 'toothbrush', 'toothbrush', 'harpooner', 'harpooner',
                'macaroni', 'macaroni', 'extract', 'machine', 'classy', 'return'],
        'SUV': ['archaeology', 'cantaloupe', 'cantaloupe', 'toothbrush', 'systemize', 'macaroni', 'extract', 'machine',
                'machine', 'parsley', 'spatula', 'classy', 'classy', 'classy', 'classy', 'embryo', 'embryo', 'embryo',
                'extent'], 'pork': ['enthusiastic', 'toothbrush', 'machine', 'extent'], 'strand': ['return'],
        'guy': ['toothbrush', 'macaroni', 'parsley', 'spatula', 'classy'],
        'dizzy': ['enthusiastic', 'archaeology', 'archaeology', 'toothbrush', 'toothbrush', 'toothbrush', 'complaint',
                  'macaroni', 'extract', 'extract', 'parsley', 'extent', 'return', 'return'],
        'sink': ['cantaloupe', 'spatula', 'embryo', 'enlist'],
        'smog': ['archaeology', 'cantaloupe', 'cantaloupe', 'complaint', 'extract', 'parsley'],
        'peer': ['archaeology', 'archaeology', 'documentary', 'documentary', 'cantaloupe', 'cantaloupe', 'cantaloupe',
                 'systemize', 'extract', 'extract', 'parsley', 'parsley', 'enlist', 'return'],
        'samurai': ['documentary', 'cantaloupe', 'toothbrush', 'toothbrush', 'complaint', 'harpooner', 'harpooner',
                    'systemize', 'macaroni', 'spatula', 'embryo', 'enlist', 'return'],
        'lad': ['enthusiastic', 'archaeology', 'cantaloupe', 'cantaloupe', 'cantaloupe', 'toothbrush', 'toothbrush',
                'complaint', 'systemize', 'macaroni', 'macaroni', 'extract', 'extract', 'extract', 'extract', 'parsley',
                'parsley', 'classy', 'enlist'],
        'type': ['archaeology', 'archaeology', 'documentary', 'harpooner', 'macaroni', 'extract', 'extract', 'spatula',
                 'classy', 'enlist', 'enlist']}
    return do_func2_test(D1, D2, expected)

# ----------------------------------- FUNC. 3----------------------------------- #
def do_func3_test(parole,k,S,expected):
    res = program.func3(parole,k,S)
    testlib.check_dict(res, expected)
    return 2/3

def test_func3_1(run=True):
    parole = ['ciao', 'come', 'stai', 'bene', 'cane', 'gatto', 'topo', 'elefante', 'giraffa']
    k = 3
    S = {'a','e','i','o','u'}
    expected = {'ciao': 3, 'elefante': 4, 'giraffa': 3}
    return do_func3_test(parole,k,S,expected)

def test_func3_2(run=True):
    parole = ['mint', 'coal', 'torpid', 'bonsai', 'clutch', 'nappy', 'sprinkles', 'trailer', 'chutney', 'manager']
    k = 2
    S = {'a', 'v', 'y', 'w'}
    expected = {'nappy': 2, 'manager': 2}
    return do_func3_test(parole,k,S,expected)

def test_func3_3(run=True):
    parole = ['tankful', 'conclude', 'communicant', 'spine', 'morphology', 'console', 'kielbasa', 'letter', 'eel', 'eat', 'tuxedo', 'oats', 'pigpen', 'grenade', 'electrocardiogram', 'pardon', 'ramen', 'channel', 'receive', 'white', 'trinket', 'suppression', 'tire', 'leptocephalus', 'drip', 'hill', 'neglect', 'walkway', 'hurricane', 'exposition', 'blouse', 'supplement', 'tavern', 'buying', 'vet', 'commercial', 'circle', 'retrospectivity', 'marketer', 'spotlight', 'marsh', 'dagger', 'mailbox', 'interval', 'suet', 'necessity', 'networking', 'emphasis', 'agonizing', 'scallion']
    k = 5
    S = {'j', 'a', 'h', 'n', 'l', 'r', 'w', 'z'}
    expected = {'electrocardiogram': 6, 'channel': 5, 'walkway': 5, 'hurricane': 5}
    return do_func3_test(parole,k,S,expected)
# ----------------------------------- FUNC. 4----------------------------------- #
def do_func4_test(ID,k,expected):
    path_in  = f"func4/in_{ID}.txt"
    path_out = f"func4/out_{ID}.txt"
    path_exp = f"func4/expected_{ID}.txt"

    if os.path.exists(path_out):
        os.remove(path_out)

    res = program.func4(path_in,path_out,k)
    testlib.check_dict(res, expected)
    my_print(f"[OK]: Il dizionario è corretto")
    try:
        testlib.check_text_file(path_out,path_exp)
    except:
        my_print(f"[ERRORE]: Il file di output non è corretto")
        return 4/4
    my_print(f"[OK]: Il file di output è corretto")
    return 7/4

def test_func4_1(run=True):
    ID = 1
    k = 2
    expected = {'a': {(0, 3), (2, 1)}, 'b': {(0, 2), (2, 1), (3, 1)}, 'aa': {(1, 2), (3, 1)}}
    return do_func4_test(ID,k,expected)

def test_func4_2():
    ID = 2
    K = 3
    expected = {'suitcase': {(0, 1), (7, 1), (10, 1)}, 'hydrocarbon': {(0, 1), (4, 1), (18, 1)},
                'photodiode': {(0, 1), (5, 1), (7, 1), (20, 1), (23, 1)}, 'famous': {(0, 1), (9, 1), (18, 1), (24, 1)},
                'grief': {(0, 1), (4, 1), (18, 1)}, 'scissors': {(0, 1), (19, 1), (21, 1), (26, 1)},
                'calculator': {(0, 1), (3, 1), (9, 1), (15, 1), (28, 1)},
                'airbus': {(0, 1), (19, 1), (21, 1), (23, 1), (27, 1)}, 'risk': {(0, 1), (22, 1), (28, 1)},
                'mow': {(1, 1), (19, 1), (21, 1), (29, 1)}, 'cross': {(1, 1), (9, 1), (21, 1)},
                'locust': {(1, 1), (7, 1), (9, 1)}, 'fisting': {(1, 1), (5, 1), (18, 1), (22, 1), (28, 1)},
                'engineer': {(2, 1), (4, 1), (8, 1), (15, 1), (19, 1)},
                'aunt': {(2, 1), (4, 1), (8, 1), (18, 1), (25, 1)}, 'effort': {(2, 1), (7, 1), (10, 1), (12, 1)},
                'paragraph': {(2, 1), (6, 1), (8, 1), (29, 1)}, 'heifer': {(2, 1), (15, 1), (22, 1)},
                'pagan': {(2, 1), (6, 1), (11, 1)}, 'warfare': {(2, 1), (18, 1), (26, 1)},
                'nonsense': {(2, 1), (3, 1), (26, 1), (29, 1)}, 'chops': {(2, 1), (4, 1), (9, 1), (15, 1)},
                'aspect': {(2, 1), (7, 1), (28, 1)}, 'carport': {(2, 1), (8, 1), (9, 1), (11, 1), (14, 1)},
                'bronze': {(2, 1), (3, 1), (22, 1)}, 'ill': {(2, 1), (18, 1), (19, 1)},
                'epoch': {(3, 1), (5, 1), (29, 1)}, 'strength': {(3, 1), (20, 1), (23, 1)},
                'hip': {(3, 1), (11, 1), (19, 1), (22, 1)}, 'wild': {(3, 1), (5, 1), (8, 1)},
                'fix': {(3, 1), (13, 1), (21, 1), (29, 1)}, 'average': {(4, 1), (5, 1), (9, 1)},
                'grin': {(4, 1), (6, 1), (8, 1), (20, 1), (23, 1)}, 'reputation': {(4, 1), (5, 1), (9, 1), (18, 1)},
                'inconvenience': {(4, 1), (22, 1), (23, 1)}, 'attention': {(4, 1), (8, 1), (24, 1)},
                'cue': {(5, 1), (15, 1), (18, 1), (24, 1)}, 'sweltering': {(5, 1), (12, 1), (21, 1)},
                'sea': {(5, 1), (21, 1), (29, 1)}, 'quince': {(5, 1), (6, 1), (22, 1)},
                'brother': {(5, 1), (19, 1), (22, 1)}, 'training': {(5, 1), (9, 1), (11, 1)},
                'ceaseless': {(5, 1), (19, 1), (20, 1)}, 'tactile': {(5, 1), (23, 1), (26, 1)},
                'poison': {(5, 1), (18, 1), (21, 1)}, 'testy': {(6, 1), (7, 1), (18, 1), (19, 1), (21, 1)},
                'netbook': {(6, 1), (7, 1), (22, 1), (24, 1)}, 'extend': {(6, 1), (10, 1), (15, 1)},
                'precision': {(7, 1), (9, 1), (28, 1)}, 'laparoscope': {(7, 1), (22, 1), (26, 1)},
                'decongestant': {(7, 1), (9, 1), (14, 1), (20, 1), (26, 1)}, 'optimisation': {(8, 1), (19, 1), (28, 1)},
                'spectrograph': {(8, 1), (9, 1), (24, 1)}, 'ashram': {(8, 1), (12, 1), (21, 1)},
                'gator': {(8, 1), (11, 1), (21, 1)}, 'termination': {(9, 1), (18, 1), (22, 1), (25, 1)},
                'sepal': {(9, 1), (11, 1), (18, 1), (21, 1), (22, 1)}, 'spud': {(10, 1), (11, 1), (19, 1), (20, 1)},
                'condor': {(14, 1), (21, 1), (29, 1)}, 'sorrow': {(15, 1), (18, 1), (19, 1)},
                'incarnation': {(18, 1), (20, 1), (22, 1)}, 'charset': {(19, 1), (20, 1), (22, 1), (25, 1)}}
    return do_func4_test(ID, K, expected)


def test_func4_3():
    ID = 3
    K = 5
    expected = {'synergy': {(0, 1), (2, 1), (7, 1), (22, 1), (23, 1), (25, 1), (34, 1), (35, 1), (38, 1)},
                'depend': {(0, 1), (19, 1), (25, 1), (45, 1), (48, 1), (49, 1)},
                'garter': {(0, 1), (6, 1), (7, 1), (34, 1), (40, 1)},
                'gamma-ray': {(0, 1), (13, 1), (22, 1), (32, 1), (35, 1)},
                'bug': {(0, 1), (8, 1), (19, 1), (21, 1), (34, 1), (39, 1)},
                'godly': {(0, 1), (1, 1), (3, 1), (30, 1), (38, 1)},
                'anybody': {(0, 1), (33, 1), (37, 1), (43, 1), (47, 1)},
                'tell': {(0, 1), (20, 1), (33, 1), (39, 1), (43, 1)},
                'array': {(0, 1), (5, 1), (13, 1), (32, 1), (40, 1), (43, 1)},
                'damaging': {(1, 1), (9, 1), (34, 1), (39, 1), (43, 1)},
                'sepal': {(1, 1), (21, 1), (23, 1), (36, 1), (44, 1)},
                'fixture': {(2, 1), (21, 1), (40, 1), (41, 1), (46, 1)},
                'teriyaki': {(2, 1), (5, 1), (24, 1), (30, 1), (34, 1), (41, 1), (48, 1)},
                'rider': {(2, 1), (34, 1), (39, 1), (44, 1), (48, 1)},
                'chromolithograph': {(2, 1), (9, 1), (33, 1), (45, 1), (48, 1)},
                'brain': {(2, 1), (19, 1), (22, 1), (23, 1), (24, 1)},
                'affidavit': {(2, 1), (5, 1), (19, 1), (40, 1), (42, 1), (49, 1)},
                'mat': {(2, 1), (5, 1), (16, 1), (28, 1), (49, 1)},
                'modification': {(2, 1), (15, 1), (17, 1), (22, 1), (29, 1), (32, 1), (40, 1), (45, 1)},
                'knit': {(2, 1), (15, 1), (16, 1), (22, 1), (40, 1)},
                'blackberry': {(2, 1), (7, 1), (30, 1), (32, 1), (39, 1)},
                'scary': {(2, 1), (8, 1), (15, 1), (28, 1), (39, 1)},
                'walrus': {(2, 1), (15, 1), (24, 1), (38, 1), (45, 1), (49, 1)},
                'lamp': {(3, 1), (13, 1), (22, 1), (29, 1), (32, 1), (35, 1), (37, 1)},
                'wake': {(5, 1), (22, 1), (23, 1), (41, 1), (48, 1)},
                'blowhole': {(5, 1), (16, 1), (22, 1), (32, 1), (37, 1), (45, 1)},
                'strife': {(5, 1), (15, 1), (17, 1), (19, 1), (34, 1), (37, 1)},
                'binoculars': {(5, 1), (8, 1), (9, 1), (25, 1), (33, 1), (34, 1)},
                'cathedral': {(5, 1), (19, 1), (26, 1), (32, 1), (48, 1)},
                'valance': {(5, 1), (28, 1), (31, 1), (37, 1), (38, 1), (41, 1)},
                'fright': {(5, 1), (15, 1), (34, 1), (35, 1), (44, 1), (48, 1)},
                'echidna': {(7, 1), (22, 1), (33, 1), (39, 1), (45, 1), (46, 1)},
                'dissect': {(8, 1), (17, 1), (28, 1), (32, 1), (41, 1)},
                'snore': {(9, 1), (24, 1), (34, 1), (38, 1), (42, 1)},
                'fearless': {(9, 1), (31, 1), (39, 1), (44, 1), (45, 1)},
                'pool': {(9, 1), (28, 1), (30, 1), (32, 1), (35, 1), (37, 1), (40, 1)},
                'briefing': {(11, 1), (15, 1), (32, 1), (34, 1), (38, 1), (42, 1)},
                'receipt': {(11, 1), (15, 1), (24, 1), (35, 1), (48, 1)},
                'sill': {(12, 1), (22, 1), (24, 1), (38, 1), (43, 1)},
                'engagement': {(12, 1), (15, 1), (17, 1), (34, 1), (35, 1), (40, 1)},
                'derby': {(13, 1), (20, 1), (38, 1), (41, 1), (47, 1)},
                'captain': {(15, 1), (28, 1), (32, 1), (39, 1), (47, 1)},
                'gran': {(15, 1), (19, 1), (23, 1), (46, 1), (48, 1)},
                'poker': {(15, 1), (22, 1), (34, 1), (37, 1), (42, 1), (49, 1)},
                'headline': {(15, 1), (17, 1), (28, 1), (32, 1), (43, 1)},
                'texture': {(15, 1), (20, 1), (29, 1), (33, 1), (41, 1)},
                'champagne': {(15, 1), (23, 1), (30, 1), (34, 1), (37, 1)},
                'angry': {(17, 1), (24, 1), (26, 1), (44, 1), (49, 1)},
                'wire': {(18, 1), (22, 1), (23, 1), (33, 1), (34, 1)},
                'stepping-stone': {(19, 1), (30, 1), (33, 1), (42, 1), (47, 1)},
                'enchanting': {(20, 1), (22, 1), (27, 1), (37, 1), (47, 1), (48, 1)},
                'inside': {(20, 1), (25, 1), (31, 1), (34, 1), (44, 1)},
                'cherry': {(22, 1), (36, 1), (37, 1), (38, 1), (49, 1)},
                'wafer': {(33, 1), (39, 1), (43, 1), (45, 1), (48, 1)}}
    return do_func4_test(ID, K, expected)


def test_func4_4():
    ID       = 4
    K        = 10
    expected = {
        'snowstorm': {(1, 1), (11, 1), (19, 1), (21, 1), (31, 1), (49, 1), (50, 1), (71, 1), (74, 1), (75, 1), (76, 1)},
        'summit': {(1, 1), (11, 1), (21, 1), (37, 1), (43, 1), (49, 1), (52, 1), (55, 1), (68, 1), (74, 1), (94, 1)},
        'charm': {(2, 1), (6, 1), (22, 1), (25, 1), (29, 1), (34, 1), (47, 1), (66, 1), (73, 1), (78, 1), (92, 1)},
        'litter': {(2, 1), (7, 1), (10, 1), (16, 1), (29, 1), (45, 1), (53, 1), (65, 1), (68, 1), (83, 1), (94, 1)},
        'wardrobe': {(2, 1), (10, 1), (12, 1), (37, 1), (48, 1), (50, 1), (51, 1), (66, 1), (77, 1), (95, 1)},
        'reading': {(2, 1), (10, 1), (18, 1), (23, 1), (24, 1), (26, 1), (27, 1), (56, 1), (78, 1), (97, 1)},
        'injury': {(2, 1), (7, 1), (8, 1), (10, 1), (38, 1), (52, 1), (74, 1), (83, 1), (89, 1), (95, 1)},
        'mallard': {(2, 1), (7, 1), (9, 1), (22, 1), (27, 1), (33, 1), (35, 1), (43, 1), (68, 1), (83, 1)},
        'slash': {(2, 1), (11, 1), (19, 1), (27, 1), (45, 1), (47, 1), (50, 1), (65, 1), (87, 1), (90, 1)},
        'glut': {(2, 1), (4, 1), (22, 1), (27, 1), (31, 1), (43, 1), (48, 1), (53, 1), (66, 1), (84, 1)},
        'plug': {(3, 1), (4, 1), (7, 1), (12, 1), (24, 1), (39, 1), (46, 1), (53, 1), (82, 1), (84, 1), (95, 1)},
        'dwell': {(3, 1), (8, 1), (11, 1), (30, 1), (38, 1), (65, 1), (70, 1), (77, 1), (93, 1), (95, 1)},
        'bongo': {(3, 1), (5, 1), (16, 1), (18, 1), (19, 1), (20, 1), (33, 1), (51, 1), (84, 1), (89, 1)},
        'respect': {(3, 1), (21, 1), (35, 1), (66, 1), (69, 1), (71, 1), (82, 1), (85, 1), (87, 1), (88, 1), (94, 1)},
        'devastation': {(4, 1), (13, 1), (29, 1), (33, 1), (49, 1), (50, 1), (88, 1), (93, 1), (95, 1), (99, 1)},
        'house': {(4, 1), (12, 1), (19, 1), (33, 1), (37, 1), (67, 1), (74, 1), (79, 1), (82, 1), (88, 1), (90, 1)},
        'resource': {(4, 1), (16, 1), (27, 1), (29, 1), (30, 1), (55, 1), (66, 1), (67, 1), (69, 1), (75, 1), (87, 1)},
        'recall': {(5, 1), (6, 1), (28, 1), (31, 1), (33, 1), (51, 1), (55, 1), (63, 1), (69, 1), (84, 1)},
        'papaya': {(5, 1), (13, 1), (14, 1), (19, 1), (37, 1), (38, 1), (65, 1), (89, 1), (90, 1), (95, 1)},
        'discourse': {(5, 1), (22, 1), (24, 1), (27, 1), (35, 1), (45, 1), (50, 1), (75, 1), (94, 1), (97, 1)},
        'crewmen': {(6, 1), (28, 1), (33, 1), (37, 1), (42, 1), (55, 1), (82, 1), (93, 1), (95, 1), (99, 1)},
        'parameter': {(7, 1), (22, 1), (33, 1), (41, 1), (46, 1), (48, 1), (56, 1), (60, 1), (71, 1), (83, 1)},
        'exit': {(7, 1), (21, 1), (25, 1), (35, 1), (53, 1), (65, 1), (67, 1), (68, 1), (74, 1), (88, 1), (96, 1)},
        'cartilage': {(7, 1), (11, 1), (14, 1), (21, 1), (31, 1), (33, 1), (42, 1), (53, 1), (55, 1), (61, 1), (70, 1),
                      (73, 1), (98, 1)},
        'windscreen': {(7, 1), (8, 1), (26, 1), (33, 1), (37, 1), (66, 1), (71, 1), (74, 1), (82, 1), (88, 1), (94, 1),
                       (96, 1)},
        'skean': {(8, 1), (10, 1), (18, 1), (29, 1), (42, 1), (43, 1), (53, 1), (66, 1), (70, 1), (87, 1), (96, 1)},
        'overcoat': {(9, 1), (18, 1), (29, 1), (33, 1), (35, 1), (64, 1), (76, 1), (84, 1), (87, 1), (92, 1)},
        'salute': {(9, 1), (11, 1), (28, 1), (37, 1), (42, 1), (48, 1), (75, 1), (82, 1), (84, 1), (89, 1)},
        'talking': {(10, 1), (12, 1), (22, 1), (29, 1), (37, 1), (46, 1), (62, 1), (78, 1), (83, 1), (87, 1), (88, 1),
                    (89, 1), (93, 1), (94, 1), (99, 1)},
        'reminder': {(11, 1), (30, 1), (34, 1), (42, 1), (43, 1), (54, 1), (57, 1), (69, 1), (81, 1), (89, 1), (90, 1)},
        'advocate': {(11, 1), (13, 1), (22, 1), (37, 1), (41, 1), (42, 1), (47, 1), (60, 1), (69, 1), (93, 1)},
        'weight': {(12, 1), (21, 1), (25, 1), (48, 1), (49, 1), (50, 1), (64, 1), (69, 1), (70, 1), (73, 1), (92, 1)},
        'disgusted': {(12, 1), (29, 1), (37, 1), (50, 1), (63, 1), (83, 1), (86, 1), (88, 1), (94, 1), (95, 1)},
        'relieved': {(12, 1), (13, 1), (19, 1), (22, 1), (35, 1), (71, 1), (72, 1), (75, 1), (83, 1), (87, 1), (94, 1)},
        'bridge': {(13, 1), (25, 1), (35, 1), (43, 1), (69, 1), (74, 1), (77, 1), (81, 1), (89, 1), (98, 1)},
        'bone': {(14, 1), (18, 1), (26, 1), (29, 1), (41, 1), (43, 1), (48, 1), (51, 1), (72, 1), (93, 1), (95, 1)},
        'pathogenesis': {(14, 1), (22, 1), (24, 1), (29, 1), (47, 1), (69, 1), (75, 1), (79, 1), (88, 1), (98, 1)},
        'eyelash': {(15, 1), (28, 1), (49, 1), (53, 1), (55, 1), (72, 1), (74, 1), (83, 1), (88, 1), (90, 1)},
        'maker': {(15, 1), (27, 1), (30, 1), (49, 1), (63, 1), (68, 1), (84, 1), (87, 1), (92, 1), (97, 1)},
        'eardrum': {(21, 1), (31, 1), (43, 1), (68, 1), (71, 1), (74, 1), (75, 1), (77, 1), (93, 1), (98, 1)},
        'feature': {(21, 1), (22, 1), (25, 1), (29, 1), (34, 1), (53, 1), (72, 1), (75, 1), (82, 1), (84, 1), (88, 1)},
        'asphalt': {(33, 1), (42, 1), (48, 1), (67, 1), (68, 1), (71, 1), (74, 1), (81, 1), (89, 1), (94, 1), (96, 1),
                    (98, 1)}}
    return do_func4_test(ID,K,expected)

# ----------------------------------- FUNC. 4----------------------------------- #
def do_func5_test(ID,expected):
    path_in  = f"func5/in_{ID}.png"
    path_out = f"func5/out_{ID}.png"
    path_exp = f"func5/expected_{ID}.png"

    if os.path.exists(path_out):
        os.remove(path_out)

    res = program.func5(path_in, path_out)
    testlib.check_dict(res, expected)
    testlib.check_img_file(path_out,path_exp)
    return 7/4

def test_func5_1():
    ID       = 20
    expected = {(226, 117, 208): {(3, 13)}, (189, 193, 254): {(5, 7)}, (251, 254, 183): {(17, 9)}}
    return do_func5_test(ID,expected)

def test_func5_2():
    ID       = 50
    expected = {(143, 201, 253): {(4, 26), (30, 11)}, (100, 194, 162): {(4, 32)}, (120, 220, 198): {(11, 47)},
                (203, 229, 209): {(16, 47)}, (212, 232, 204): {(19, 22)}, (140, 197, 156): {(35, 19)},
                (252, 157, 132): {(40, 28)}}
    return do_func5_test(ID,expected)

def test_func5_3():
    ID       = 100
    expected = {(135, 223, 156): {(10, 26), (92, 62)}, (216, 155, 193): {(38, 11), (27, 69)},
                (157, 181, 227): {(39, 58)}, (236, 139, 179): {(82, 74), (46, 27)},
                (168, 109, 119): {(65, 54), (93, 86)}, (218, 237, 208): {(73, 57)}, (171, 126, 185): {(75, 90)},
                (203, 247, 118): {(77, 41)}, (180, 106, 104): {(96, 65), (96, 60)}, (171, 176, 111): {(97, 30)}}
    return do_func5_test(ID,expected)

def test_func5_4():
    ID       = 150
    expected = {(194, 212, 131): {(3, 47), (30, 33)}, (154, 126, 153): {(4, 20)}, (216, 242, 117): {(19, 4)},
                (115, 145, 170): {(31, 4)}, (198, 167, 179): {(34, 33)}, (182, 174, 161): {(35, 5)},
                (128, 236, 247): {(46, 18)}, (177, 118, 117): {(47, 3)}}
    return do_func5_test(ID,expected)

# ----------------------------------- EX. 2----------------------------------- #
import nary_tree
def do_ex1_test(root, lista_pesi, expected):
    if not DEBUG:
        isrecursive2.DETECT = True
        try:
            radice = nary_tree.NaryTree.fromList(root)
            program.ex1(radice, lista_pesi)
        except isrecursive2.RecursionDetectedError:
            pass
        else:
            raise Exception(
                "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive2.DETECT = False

    radice    = nary_tree.NaryTree.fromList(root)
    expected  = nary_tree.NaryTree.fromList(expected)
    res = program.ex1(radice, lista_pesi)
    if res is None:
        my_print(
            f'''{'*' * 50}\n[ERROR]La funzione torna None!\nExpected={expected}''')
        return 0
    if res != expected:
        my_print(
            f'''{'*' * 50}
            [ERROR]Il valore tornato non è corretto!
            Expected={expected!r}
            Returned={res!r}
            ''')
        return 0
    return 2

def test_ex1_1(run=True):
    '''
       __________1_________
       |     |            |
     __2__   3___   _____40_____
     |   |      |   |   |  |    |
     4   5      6   7   8  9   10
    e lista_pesi = [2,7,3,1,2,5,9]
    '''
    root       = [1, [2, [4], [5]], [3, [6]], [40, [7], [8], [9], [10]]]
    lista_pesi = [2,7,3,1,2,5,9]
    expected   = [1, [4, [16], [70]], [21, [24]], [120, [28], [112], [54], [20]]]
    return do_ex1_test(root, lista_pesi, expected)

def test_ex1_2(run=True):
    '''
-57
|    -78
|   |    -7
|    6
|   |    64
|   |   |    79
|   |   |    -75
|   |    80
|   |   |    2
|   |   |    -19
|   |   |   |    29
|   |   |   |    -37
|   |   |   |    -40
|   |    29
    e lista_pesi = [2,7,3,1,2,5,9]
    '''
    root = [-57, [-78, [-7]], [6, [64, [79], [-75]], [80, [2], [-19, [29], [-37], [-40]]], [29]]]
    expected = [-57, [-156, [-28]], [24, [256, [474], [-900]], [640, [12], [-228, [232], [-592], [-480]]], [174]]]
    lista_pesi = [2, 4, 3, 5, 1, 6]
    return do_ex1_test(root, lista_pesi, expected)

def test_ex1_3(run=True):
    root = [86, [-60, [59], [18, [-99, [33], [-71, [14], [92, [-34], [-40]]]], [15, [22]]],
                 [23, [-50], [92, [3], [96, [86, [59], [-53, [-96], [-77]], [-58, [69], [-86]]]]], [14]]]]
    expected = [86, [-480, [944], [252, [-2376, [1056], [-1988, [560], [3220, [-1632], [-1680]]]], [315, [704]]],
                     [276, [-1200],
                      [1932, [96], [2688, [3440, [2832], [-2226, [-5376], [-3773]], [-2088, [3864], [-4214]]]]],
                      [252]]]]
    lista_pesi =  [8, 7, 6, 5, 4, 3, 2, 1]
    return do_ex1_test(root, lista_pesi, expected)
# ----------------------------------- EX.2 ----------------------------------- #

def do_ex2_test(directory, expected):
    if not DEBUG:
        isrecursive2.DETECT = True
        try:
            program.ex2(directory)
        except isrecursive2.RecursionDetectedError:
            pass
        else:
            raise Exception(
                "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive2.DETECT = False

    res = program.ex2(directory)
    testlib.check_dict(res, expected)
    return 2

def test_ex2_1(run=True):
    directory  = 'ex2/A'
    expected   = {'ex2/A': {'txt': 3}, 'ex2/A/C': {'bak': 1, 'txt': 4, 'png': 1}, 'ex2/A/B': {'txt': 2}}
    return do_ex2_test(directory, expected)


def test_ex2_2(run=True):
    directory = 'ex2/B'
    expected = {'ex2/B': {'txt': 6}, 'ex2/B/hfc44ba': {'txt': 2, 'tqq': 1, 'pqr': 1, 'fde': 1},
                'ex2/B/hfc44ba/B7n33lv': {'A3a': 1, 'P5f': 1}, 'ex2/B/hfc44ba/B7n33lv/gl88e642': {'txt': 1, 'ter': 1},
                'ex2/B/hfc44ba/ummc6eb93': {'no2': 1, '2fd': 1, 'txt': 1, 'a52': 1, 'awk': 1},
                'ex2/B/DBvt2h4': {'txt': 2}, 'ex2/B/DBvt2h4/55i4q73': {'txt': 2},
                'ex2/B/DBvt2h4/5nfhb6adjd': {'txt': 2}, 'ex2/B/DBvt2h4/8q2i3cb': {'txt': 5}}
    return do_ex2_test(directory, expected)


def test_ex2_3(run=True):
    directory = 'ex2/C'
    expected = {'ex2/C': {'txt': 5}, 'ex2/C/4q5ni': {'txt': 2, '25c': 1}, 'ex2/C/439': {'rqt': 1, 'qer': 1},
                'ex2/C/439/53d23yd': {'txt': 1, 'eab': 1}, 'ex2/C/A': {'txt': 5}, 'ex2/C/A/a9fa5r54ol': {'txt': 2},
                'ex2/C/A/a9fa5r54ol/9dlnpni': {'txt': 3}, 'ex2/C/A/a9fa5r54ol/9dlnpni/1bqeb8': {'txt': 1},
                'ex2/C/A/a9fa5r54ol/9dlnpni/p2q8': {'txt': 1}, 'ex2/C/A/v9gdti5xl': {'yns': 1},
                'ex2/C/A/r5g': {'txt': 1, '2i7': 1, 'ne3': 1, 'fd4': 1},
                'ex2/C/A/r5g/d501': {'6e7': 1, 'txt': 1, 's90': 1},
                'ex2/C/A/r5g/d501/tew8': {'vlq': 1, 'txt': 2, 'er3': 1, '56j': 1}, 'ex2/C/C': {'txt': 1},
                'ex2/C/C/9n5': {'png': 1}, 'ex2/C/C/9n5/22zi524j': {'txt': 2, 'Mok': 1, 'hhi': 1, 'e2m': 1},
                'ex2/C/C/9n5/22zi524j/1iha5': {'3fd': 1, 'txt': 1}, 'ex2/C/C/9n5/22zi524j/u2g': {'txt': 3, 'ke5': 1},
                'ex2/C/52e': {'pqr': 2}, 'ex2/C/52e/7ij': {'qrt': 1, 'spq': 1, 'pqr': 1, 'sqp': 1},
                'ex2/C/B': {'txt': 4}, 'ex2/C/B/p3zt345614': {'3dd': 1},
                'ex2/C/B/p3zt345614/17nt': {'txt': 1, 'png': 1}, 'ex2/C/B/p3zt345614/ei9ej73p': {'txt': 1},
                'ex2/C/B/p3zt345614/7j30i': {'txt': 2}}
    return do_ex2_test(directory, expected)

# ----------------------------------- EX. 4 ----------------------------------- #

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2,                                   # 2   / 2
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,     # 2   / 4
    test_func3_1, test_func3_2, test_func3_3,                     # 2   / 3
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,       # 6   / 4
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,       # 8   / 4

    test_ex1_1,   test_ex1_2,   test_ex1_3,                       # 6   / 3
    test_ex2_1,   test_ex2_2,   test_ex2_3,                       # 6   / 3
    test_personal_data_entry,
]


if __name__ == '__main__':
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    import program
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################

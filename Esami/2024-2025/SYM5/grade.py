# -*- coding: utf-8 -*-
from isort import check_file

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
#DEBUG = False
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
def do_func1_test(testo,K,expected):
    res = program.func1(testo,K)
    if res != expected:
        my_print(
            f'''{'*' * 50}\n[ERROR]Il valore ritornato non è corretto!\nReturned={res}, expected={expected}''')
        return 0
    return 1

def test_func1_1(run=True):
    K = 2
    testo = '''sopra la panca la capra campa, sotto la panca la capra crepa'''
    expected = {'capra', 'panca'}
    return do_func1_test(testo,K,expected)

def test_func1_2(run=True):
    K = 2
    testo = '''essere o non essere, questo è il dilemma: 
               se sia più nobile nella mente soffrire colpi di fionda e dardi d’atroce fortuna 
               o prender armi contro un mare d’affanni e, opponendosi, por loro fine? 
               morire, dormire; nient’altro; e con un sonno dire che poniamo fine al dolore 
               del cuore e ai mille tumulti naturali di cui è erede la carne: 
               è una conclusione da desiderarsi devotamente'''
    expected = {'fine', 'un', 'di', 'o', 'essere', 'd'}
    return do_func1_test(testo,K,expected)

# ----------------------------------- FUNC. 2----------------------------------- #
def do_func2_test(parole,expected):
    res = program.func2(parole)
    if res != expected:
        my_print(
            f'''{'*' * 50}\n[ERROR]Il valore ritornato non è corretto!\nReturned={res}, expected={expected}''')
        return 0
    return 1/2

def test_func2_1(run=True):
    parole = ['sei', 'sicuro', 'che', 'sopra', 'la', 'panca', 'le', 'capre', 'campino?',
              'certamente,', 'mentre', 'sotto', 'la', 'panca', 'le', 'capre', 'crepano!']
    expected = {'s': ['sei', 'sotto', 'sopra', 'sicuro'],
                'c': ['che', 'capre', 'capre', 'crepano!', 'campino?', 'certamente,'],
                'l': ['le', 'le', 'la', 'la'],
                'p': ['panca', 'panca'],
                'm': ['mentre']}
    return do_func2_test(parole,expected)

def test_func2_2(run=True):
    parole=['inexpensive', 'modification', 'definition', 'crucifixion', 'recession', 'pancreas', 'seal', 'controller',
            'oven', 'glockenspiel', 'curio', 'ottoman', 'fighter', 'unbecoming', 'mountain', 'square', 'forgery', 'app',
            'distributor', 'feed']
    expected={'i': ['inexpensive'], 'm': ['mountain', 'modification'], 'd': ['definition', 'distributor'],
              'c': ['curio', 'controller', 'crucifixion'], 'r': ['recession'], 'p': ['pancreas'], 's': ['seal', 'square'],
              'o': ['oven', 'ottoman'], 'g': ['glockenspiel'], 'f': ['feed', 'forgery', 'fighter'], 'u': ['unbecoming'],
              'a': ['app']}
    return do_func2_test(parole,expected)


def test_func2_3(run=True):
    parole = ['contract', 'nerve', 'bidder', 'simvastatin', 'lackadaisical', 'endurable', 'think', 'overview',
              'grapefruit', 'soy', 'mankind', 'prosecutor', 'instruct', 'teeny', 'gale', 'spume', 'cue', 'buyer',
              'pocketbook', 'maid', 'tenement', 'gnat', 'queen', 'chivalry', 'construction', 'gaffe', 'littleneck',
              'rally', 'detour', 'cruise', 'node', 'porcupine', 'cashew', 'daisy', 'prevalence', 'suet', 'earrings',
              'vibrissae', 'length', 'baseball', 'shiny', 'preservation', 'salon', 'emerald', 'freight', 'tinderbox',
              'nutty', 'youth', 'flare', 'leeway']
    expected = {'c': ['cue', 'cruise', 'cashew', 'contract', 'chivalry', 'construction'],
                'n': ['node', 'nutty', 'nerve'], 'b': ['buyer', 'bidder', 'baseball'],
                's': ['soy', 'suet', 'spume', 'shiny', 'salon', 'simvastatin'],
                'l': ['length', 'leeway', 'littleneck', 'lackadaisical'], 'e': ['emerald', 'earrings', 'endurable'],
                't': ['think', 'teeny', 'tenement', 'tinderbox'], 'o': ['overview'],
                'g': ['gnat', 'gale', 'gaffe', 'grapefruit'], 'm': ['maid', 'mankind'],
                'p': ['porcupine', 'prosecutor', 'prevalence', 'pocketbook', 'preservation'], 'i': ['instruct'],
                'q': ['queen'], 'r': ['rally'], 'd': ['daisy', 'detour'], 'v': ['vibrissae'], 'f': ['flare', 'freight'],
                'y': ['youth']}
    return do_func2_test(parole, expected)

def test_func2_4(run=True):
    parole = ['sneakers', 'seafood', 'monster', 'prison', 'improve', 'windshield', 'guideline', 'gauntlet', 'hardboard',
              'note', 'feedback', 'industrialization', 'hearthside', 'carabao', 'disk', 'cupboard', 'invasion', 'noisy',
              'endpoint', 'advice', 'potato', 'suggestion', 'clothe', 'sweat', 'encouraging', 'alibi', 'snowplow',
              'angiosperm', 'dictator', 'right', 'port', 'hatbox', 'sunglasses', 'prefer', 'sitar', 'cabin', 'stormy',
              'earrings', 'episode', 'fibrosis', 'place', 'desk', 'celebration', 'permissible', 'yielding', 'cleric',
              'reflect', 'netbook', 'royal', 'decade', 'argue', 'tweezers', 'nourishment', 'invoice', 'blackboard',
              'sell', 'fairy', 'ethereal', 'symbolize', 'tolerance', 'deficit', 'eyestrain', 'absorbed', 'adaptable',
              'thunderstorm', 'drawer', 'phone', 'disruption', 'moonlight', 'era', 'outset', 'doughnut', 'total',
              'fishbone', 'fearless', 'undertaker', 'bidder', 'essence', 'lackadaisical', 'pomegranate', 'match',
              'condemned', 'tenor', 'objective', 'bomb', 'shop', 'greed', 'curler', 'bride', 'champion', 'expedition',
              'belt', 'turnstile', 'workout', 'sensitive', 'ATM', 'shape', 'apologize', 'prostrate', 'shoemaker',
              'union', 'hippodrome', 'hybridization', 'fava', 'outstanding', 'jar', 'billboard', 'appetite',
              'productive', 'likeable', 'depressive', 'abrupt', 'banjo', 'backyard', 'mercury', 'stockings', 'traffic',
              'ostrich', 'silence', 'vitro', 'nutmeg', 'connection', 'particle', 'legislation', 'spiderling', 'exhibit',
              'flung', 'fraudster', 'contact', 'brownie', 'zither', 'momentous', 'department', 'veneer', 'injure',
              'channel', 'satire', 'epee', 'lever', 'logic', 'dune', 'roundabout', 'tan', 'frighten', 'dust storm',
              'glossy', 'armour', 'stencil', 'noxious', 'arena', 'airline', 'timber', 'crane', 'plywood', 'septicaemia',
              'period', 'chit-chat', 'macro', 'silica', 'demand', 'axis', 'berserk', 'drain', 'polyp', 'procurement',
              'spray', 'cricket', 'tuber', 'counsellor', 'bizarre', 'wide', 'charm', 'plum', 'woozy', 'faded',
              'dialogue', 'sanctuary', 'parka', 'dapper', 'lychee', 'constitution', 'abashed', 'full', 'content',
              'sesame', 'sock', 'remark', 'lane', 'skin', 'birth', 'brick', 'marble', 'jury', 'utilize', 'curious',
              'bleach', 'resource', 'deadpan', 'detection', 'invent']
    expected = {'s': ['sock', 'skin', 'shop', 'sell', 'sweat', 'spray', 'sitar', 'shape', 'stormy', 'silica', 'sesame',
                      'satire', 'stencil', 'silence', 'seafood', 'snowplow', 'sneakers', 'symbolize', 'stockings',
                      'shoemaker', 'sensitive', 'sanctuary', 'sunglasses', 'suggestion', 'spiderling', 'septicaemia'],
                'm': ['match', 'macro', 'marble', 'monster', 'mercury', 'moonlight', 'momentous'],
                'p': ['port', 'plum', 'polyp', 'place', 'phone', 'parka', 'prison', 'prefer', 'potato', 'period',
                      'plywood', 'particle', 'prostrate', 'productive', 'procurement', 'pomegranate', 'permissible'],
                'i': ['invent', 'injure', 'invoice', 'improve', 'invasion', 'industrialization'],
                'w': ['wide', 'woozy', 'workout', 'windshield'], 'g': ['greed', 'glossy', 'gauntlet', 'guideline'],
                'h': ['hatbox', 'hardboard', 'hippodrome', 'hearthside', 'hybridization'],
                'n': ['note', 'noisy', 'nutmeg', 'noxious', 'netbook', 'nourishment'],
                'f': ['full', 'fava', 'flung', 'fairy', 'faded', 'frighten', 'fishbone', 'fibrosis', 'feedback',
                      'fearless', 'fraudster'],
                'c': ['crane', 'charm', 'cabin', 'curler', 'clothe', 'cleric', 'curious', 'cricket', 'content',
                      'contact', 'channel', 'carabao', 'cupboard', 'champion', 'condemned', 'chit-chat', 'counsellor',
                      'connection', 'celebration', 'constitution'],
                'd': ['dune', 'disk', 'desk', 'drain', 'drawer', 'demand', 'decade', 'dapper', 'deficit', 'deadpan',
                      'doughnut', 'dictator', 'dialogue', 'detection', 'dust storm', 'disruption', 'depressive',
                      'department'],
                'e': ['era', 'epee', 'exhibit', 'essence', 'episode', 'ethereal', 'endpoint', 'earrings', 'eyestrain',
                      'expedition', 'encouraging'],
                'a': ['axis', 'argue', 'arena', 'alibi', 'armour', 'advice', 'abrupt', 'airline', 'abashed', 'appetite',
                      'absorbed', 'apologize', 'adaptable', 'angiosperm'],
                'r': ['royal', 'right', 'remark', 'reflect', 'resource', 'roundabout'], 'y': ['yielding'],
                't': ['tan', 'tuber', 'total', 'tenor', 'timber', 'traffic', 'tweezers', 'turnstile', 'tolerance',
                      'thunderstorm'],
                'b': ['bomb', 'belt', 'bride', 'brick', 'birth', 'banjo', 'bleach', 'bidder', 'brownie', 'bizarre',
                      'berserk', 'backyard', 'billboard', 'blackboard'],
                'o': ['outset', 'ostrich', 'objective', 'outstanding'], 'u': ['union', 'utilize', 'undertaker'],
                'l': ['lane', 'logic', 'lever', 'lychee', 'likeable', 'legislation', 'lackadaisical'], 'A': ['ATM'],
                'j': ['jar', 'jury'], 'v': ['vitro', 'veneer'], 'z': ['zither']}
    return do_func2_test(parole,expected)

# ----------------------------------- FUNC. 3----------------------------------- #
def do_func3_test(D1,D2,expected):
    res = program.func3(D1,D2)
    testlib.check_dict(res, expected)
    return 2/3

def test_func3_1(run=True):
    D1 = {'a': [1, 2, 3], 'b': [3, 4, 5]}
    D2 = {1: ['a', 'bb', 'ccc'], 3: ['qq', 'z'], 5: ['b', 'fff']}
    expected = {'a': ['a', 'z', 'bb', 'qq', 'ccc'], 'b': ['b', 'z', 'qq', 'fff']}
    return do_func3_test(D1,D2,expected)

def test_func3_2(run=True):
    D1 = {'misfit': [6631, 6075, 8235, 3766, 1132], 'belligerency': [8262, 1328, 6158, 7500, 400],
          'super': [508, 5504, 628, 3264, 3198], 'tabernacle': [140, 4646, 1321, 4592, 6195],
          'canopy': [8892, 6859, 1414, 4361, 8262]}
    D2 = {240: ['temptress', 'shoehorn', 'smelly', 'utility', 'fat'],
          4592: ['sandwich', 'predict', 'miniature', 'trophy', 'divider'],
          6380: ['snowboarding', 'fisting', 'longing', 'measure', 'trader'],
          6519: ['print', 'falling-out', 'misfit', 'sequel', 'craw'],
          5409: ['tabernacle', 'congo', 'lucky', 'asphalt', 'uppity']}
    expected = {'tabernacle': ['trophy', 'divider', 'predict', 'sandwich', 'miniature']}
    return do_func3_test(D1, D2, expected)

def test_func3_3():
    D1       = {'borrowing': [4105, 2694, 5089],
                'trailer': [1150, 9627, 8676],
                'enacted': [1657, 7118, 4952]}
    D2       = {4105: ['arrogant', 'gigantic', 'heterosexual', 'scallion', 'census', 'bathhouse', 'president', 'comestible'],
                4991: ['moat', 'tanker', 'lawn', 'normal', 'spectacular', 'tech', 'cliff', 'detective'],
                5734: ['snotty', 'lawn', 'disarm', 'register', 'corporation', 'jackfruit', 'zebrafish', 'bunch'],
                3405: ['beating', 'caribou', 'instinctive', 'big', 'lawn', 'arrogant', 'zebrafish', 'signal'],
                3752: ['siding', 'nit', 'scallion', 'tech', 'spectacular', 'classy', 'faith', 'disarm'],
                4952: ['arrogant', 'sordid', 'fixture', 'motivate', 'define', 'beating', 'arrogant', 'depression'],
                5326: ['stimulate', 'event', 'trust', 'register', 'coal', 'earrings', 'chipmunk', 'come'],
                1438: ['pajamas', 'define', 'tourist', 'lawn', 'parrot', 'normal', 'siding', 'grandpa']}
    expected = {'borrowing': ['census', 'arrogant', 'gigantic', 'scallion', 'bathhouse', 'president', 'comestible', 'heterosexual'],
                'enacted': ['define', 'sordid', 'beating', 'fixture', 'arrogant', 'arrogant', 'motivate', 'depression']}
    return do_func3_test(D1,D2,expected)

# ----------------------------------- FUNC. 4----------------------------------- #
def do_func4_test(ID,k,expected):
    path_in  = f"func4/in_{ID}.txt"
    path_out = f"func4/out_{ID}.txt"
    path_exp = f"func4/expected_{ID}.txt"

    res = program.func4(path_in,path_out,k)
    if res!=expected:
        print(res)
    testlib.check_dict(res, expected)
    testlib.check_text_file(path_out,path_exp)
    return 6/4

def test_func4_1(run=True):
    ID = 1
    K  = 2
    expected = {'a': [0, 2], 'b': [0, 2, 3], 'aa': [1, 3]}
    return do_func4_test(ID,K,expected)

def test_func4_2():
    ID = 2
    K = 3
    expected = {'suitcase': [0, 7, 10], 'hydrocarbon': [0, 4, 18], 'photodiode': [0, 5, 7, 20, 23],
                'famous': [0, 9, 18, 24], 'grief': [0, 4, 18], 'scissors': [0, 19, 21, 26],
                'calculator': [0, 3, 9, 15, 28], 'airbus': [0, 19, 21, 23, 27], 'risk': [0, 22, 28],
                'mow': [1, 19, 21, 29], 'cross': [1, 9, 21], 'locust': [1, 7, 9], 'fisting': [1, 5, 18, 22, 28],
                'engineer': [2, 4, 8, 15, 19], 'aunt': [2, 4, 8, 18, 25], 'effort': [2, 7, 10, 12],
                'paragraph': [2, 6, 8, 29], 'heifer': [2, 15, 22], 'pagan': [2, 6, 11], 'warfare': [2, 18, 26],
                'nonsense': [2, 3, 26, 29], 'chops': [2, 4, 9, 15], 'aspect': [2, 7, 28], 'carport': [2, 8, 9, 11, 14],
                'bronze': [2, 3, 22], 'ill': [2, 18, 19], 'epoch': [3, 5, 29], 'strength': [3, 20, 23],
                'hip': [3, 11, 19, 22], 'wild': [3, 5, 8], 'fix': [3, 13, 21, 29], 'average': [4, 5, 9],
                'grin': [4, 6, 8, 20, 23], 'reputation': [4, 5, 9, 18], 'inconvenience': [4, 22, 23],
                'attention': [4, 8, 24], 'cue': [5, 15, 18, 24], 'sweltering': [5, 12, 21], 'sea': [5, 21, 29],
                'quince': [5, 6, 22], 'brother': [5, 19, 22], 'training': [5, 9, 11], 'ceaseless': [5, 19, 20],
                'tactile': [5, 23, 26], 'poison': [5, 18, 21], 'testy': [6, 7, 18, 19, 21], 'netbook': [6, 7, 22, 24],
                'extend': [6, 10, 15], 'precision': [7, 9, 28], 'laparoscope': [7, 22, 26],
                'decongestant': [7, 9, 14, 20, 26], 'optimisation': [8, 19, 28], 'spectrograph': [8, 9, 24],
                'ashram': [8, 12, 21], 'gator': [8, 11, 21], 'termination': [9, 18, 22, 25],
                'sepal': [9, 11, 18, 21, 22], 'spud': [10, 11, 19, 20], 'condor': [14, 21, 29], 'sorrow': [15, 18, 19],
                'incarnation': [18, 20, 22], 'charset': [19, 20, 22, 25]}
    return do_func4_test(ID, K, expected)


def test_func4_3():
    ID = 3
    K = 5
    expected = {'synergy': [0, 2, 7, 22, 23, 25, 34, 35, 38], 'depend': [0, 19, 25, 45, 48, 49],
                'garter': [0, 6, 7, 34, 40], 'gamma-ray': [0, 13, 22, 32, 35], 'bug': [0, 8, 19, 21, 34, 39],
                'godly': [0, 1, 3, 30, 38], 'anybody': [0, 33, 37, 43, 47], 'tell': [0, 20, 33, 39, 43],
                'array': [0, 5, 13, 32, 40, 43], 'damaging': [1, 9, 34, 39, 43], 'sepal': [1, 21, 23, 36, 44],
                'fixture': [2, 21, 40, 41, 46], 'teriyaki': [2, 5, 24, 30, 34, 41, 48], 'rider': [2, 34, 39, 44, 48],
                'chromolithograph': [2, 9, 33, 45, 48], 'brain': [2, 19, 22, 23, 24],
                'affidavit': [2, 5, 19, 40, 42, 49], 'mat': [2, 5, 16, 28, 49],
                'modification': [2, 15, 17, 22, 29, 32, 40, 45], 'knit': [2, 15, 16, 22, 40],
                'blackberry': [2, 7, 30, 32, 39], 'scary': [2, 8, 15, 28, 39], 'walrus': [2, 15, 24, 38, 45, 49],
                'lamp': [3, 13, 22, 29, 32, 35, 37], 'wake': [5, 22, 23, 41, 48], 'blowhole': [5, 16, 22, 32, 37, 45],
                'strife': [5, 15, 17, 19, 34, 37], 'binoculars': [5, 8, 9, 25, 33, 34],
                'cathedral': [5, 19, 26, 32, 48], 'valance': [5, 28, 31, 37, 38, 41], 'fright': [5, 15, 34, 35, 44, 48],
                'echidna': [7, 22, 33, 39, 45, 46], 'dissect': [8, 17, 28, 32, 41], 'snore': [9, 24, 34, 38, 42],
                'fearless': [9, 31, 39, 44, 45], 'pool': [9, 28, 30, 32, 35, 37, 40],
                'briefing': [11, 15, 32, 34, 38, 42], 'receipt': [11, 15, 24, 35, 48], 'sill': [12, 22, 24, 38, 43],
                'engagement': [12, 15, 17, 34, 35, 40], 'derby': [13, 20, 38, 41, 47], 'captain': [15, 28, 32, 39, 47],
                'gran': [15, 19, 23, 46, 48], 'poker': [15, 22, 34, 37, 42, 49], 'headline': [15, 17, 28, 32, 43],
                'texture': [15, 20, 29, 33, 41], 'champagne': [15, 23, 30, 34, 37], 'angry': [17, 24, 26, 44, 49],
                'wire': [18, 22, 23, 33, 34], 'stepping-stone': [19, 30, 33, 42, 47],
                'enchanting': [20, 22, 27, 37, 47, 48], 'inside': [20, 25, 31, 34, 44], 'cherry': [22, 36, 37, 38, 49],
                'wafer': [33, 39, 43, 45, 48]}
    return do_func4_test(ID, K, expected)


def test_func4_4():
    ID       = 4
    K        = 10
    expected = {'snowstorm': [1, 11, 19, 21, 31, 49, 50, 71, 74, 75, 76],
                'summit': [1, 11, 21, 37, 43, 49, 52, 55, 68, 74, 94],
                'charm': [2, 6, 22, 25, 29, 34, 47, 66, 73, 78, 92],
                'litter': [2, 7, 10, 16, 29, 45, 53, 65, 68, 83, 94],
                'wardrobe': [2, 10, 12, 37, 48, 50, 51, 66, 77, 95], 'reading': [2, 10, 18, 23, 24, 26, 27, 56, 78, 97],
                'injury': [2, 7, 8, 10, 38, 52, 74, 83, 89, 95], 'mallard': [2, 7, 9, 22, 27, 33, 35, 43, 68, 83],
                'slash': [2, 11, 19, 27, 45, 47, 50, 65, 87, 90], 'glut': [2, 4, 22, 27, 31, 43, 48, 53, 66, 84],
                'plug': [3, 4, 7, 12, 24, 39, 46, 53, 82, 84, 95], 'dwell': [3, 8, 11, 30, 38, 65, 70, 77, 93, 95],
                'bongo': [3, 5, 16, 18, 19, 20, 33, 51, 84, 89], 'respect': [3, 21, 35, 66, 69, 71, 82, 85, 87, 88, 94],
                'devastation': [4, 13, 29, 33, 49, 50, 88, 93, 95, 99],
                'house': [4, 12, 19, 33, 37, 67, 74, 79, 82, 88, 90],
                'resource': [4, 16, 27, 29, 30, 55, 66, 67, 69, 75, 87],
                'recall': [5, 6, 28, 31, 33, 51, 55, 63, 69, 84], 'papaya': [5, 13, 14, 19, 37, 38, 65, 89, 90, 95],
                'discourse': [5, 22, 24, 27, 35, 45, 50, 75, 94, 97],
                'crewmen': [6, 28, 33, 37, 42, 55, 82, 93, 95, 99],
                'parameter': [7, 22, 33, 41, 46, 48, 56, 60, 71, 83],
                'exit': [7, 21, 25, 35, 53, 65, 67, 68, 74, 88, 96],
                'cartilage': [7, 11, 14, 21, 31, 33, 42, 53, 55, 61, 70, 73, 98],
                'windscreen': [7, 8, 26, 33, 37, 66, 71, 74, 82, 88, 94, 96],
                'skean': [8, 10, 18, 29, 42, 43, 53, 66, 70, 87, 96],
                'overcoat': [9, 18, 29, 33, 35, 64, 76, 84, 87, 92], 'salute': [9, 11, 28, 37, 42, 48, 75, 82, 84, 89],
                'talking': [10, 12, 22, 29, 37, 46, 62, 78, 83, 87, 88, 89, 93, 94, 99],
                'reminder': [11, 30, 34, 42, 43, 54, 57, 69, 81, 89, 90],
                'advocate': [11, 13, 22, 37, 41, 42, 47, 60, 69, 93],
                'weight': [12, 21, 25, 48, 49, 50, 64, 69, 70, 73, 92],
                'disgusted': [12, 29, 37, 50, 63, 83, 86, 88, 94, 95],
                'relieved': [12, 13, 19, 22, 35, 71, 72, 75, 83, 87, 94],
                'bridge': [13, 25, 35, 43, 69, 74, 77, 81, 89, 98],
                'bone': [14, 18, 26, 29, 41, 43, 48, 51, 72, 93, 95],
                'pathogenesis': [14, 22, 24, 29, 47, 69, 75, 79, 88, 98],
                'eyelash': [15, 28, 49, 53, 55, 72, 74, 83, 88, 90], 'maker': [15, 27, 30, 49, 63, 68, 84, 87, 92, 97],
                'eardrum': [21, 31, 43, 68, 71, 74, 75, 77, 93, 98],
                'feature': [21, 22, 25, 29, 34, 53, 72, 75, 82, 84, 88],
                'asphalt': [33, 42, 48, 67, 68, 71, 74, 81, 89, 94, 96, 98]}
    return do_func4_test(ID,K,expected)

# ----------------------------------- FUNC. 4----------------------------------- #
def do_func5_test(ID,expected):
    path_in  = f"func5/in_{ID}.png"
    path_out = f"func5/out_{ID}.png"
    #path_exp = f"func5/expected_{ID}.png"

    res = program.func5(path_in)
    testlib.check_dict(res, expected)
    #testlib.check_img_file(path_out,path_exp)
    return 2

def test_func5_1():
    ID       = 1
    expected = {(184, 188, 208): {(11, 1), (8, 9)}}
    return do_func5_test(ID,expected)

def test_func5_2():
    ID       = 2
    expected = {(158, 219, 147): {(24, 3), (1, 8), (1, 22)}, (242, 134, 157): {(25, 22), (7, 23)}}
    return do_func5_test(ID,expected)

def test_func5_3():
    ID       = 3
    expected = {(161, 142, 192): {(6, 13), (20, 25)}, (236, 200, 200): {(25, 16), (21, 19)},
                (215, 147, 247): {(25, 19), (18, 18)}, (254, 128, 235): {(22, 41), (7, 23)}}
    return do_func5_test(ID,expected)

def test_func5_4():
    ID       = 4
    expected = {(245, 200, 106): {(88, 13), (40, 13)}, (167, 234, 185): {(30, 94), (39, 53), (56, 13), (52, 27)},
                (104, 196, 237): {(49, 46), (6, 30)}, (139, 187, 228): {(26, 30), (19, 74)},
                (190, 130, 131): {(54, 82), (24, 33), (44, 89), (17, 45), (87, 62)},
                (174, 176, 211): {(89, 37), (95, 88), (5, 46)}, (139, 199, 119): {(35, 60), (80, 74)},
                (254, 203, 135): {(72, 90), (73, 77), (81, 86)}}
    return do_func5_test(ID,expected)

# ----------------------------------- EX. 2----------------------------------- #
def do_ex1_test(root, lista_pesi, expected):
    if not DEBUG:
        isrecursive2.DETECT = True
        try:
            radice = tree.BinaryTree.fromList(root)
            program.ex1(radice, lista_pesi)
        except isrecursive2.RecursionDetectedError:
            pass
        else:
            raise Exception(
                "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive2.DETECT = False

    radice = tree.BinaryTree.fromList(root)
    res = program.ex1(radice, lista_pesi)
    if res is None:
        my_print(
            f'''{'*' * 50}\n[ERROR]La funzione torna None!\nExpected={expected}''')
        return 0
    res = res.toList()
    rad = tree.BinaryTree.fromList(root)
    testlib.check(res,    expected, expl="Valore tornato non corretto")
    testlib.check(radice, rad,      expl="La funzione ha modificato l'albero originale")
    return 2

def test_ex1_1(run=True):
    '''
    ______5______
   |             |
   8__        ___2___
      |      |       |
      3      9       1
    '''
    root       = [5, [8, None, [3, None, None]], [2, [9, None, None], [1, None, None]]]
    lista_pesi = [5, 8, 2, 3, 9, 1]
    expected   = [25, [64, None, [6, None, None]], [16, [18, None, None], [2, None, None]]]
    return do_ex1_test(root, lista_pesi, expected)


def test_ex1_2(run=True):
    '''
        ______2______
       |             |
    __ 7__        ___5___
   |      |      |       |
  _4_     3_    _0_     _5_
 |   |      |  |   |   |   |
 2   -1     1  8   3   2   9
    '''
    root = [2, [7, [4, [2, None, None],
                       [-1, None, None]],
                   [3, None,
                       [1, None, None]]],
               [5, [0, [8, None, None],
                       [3, None, None]],
                   [5, [2, None, None],
                       [9, None, None]]]]
    lista_pesi = [2, 7, 4, 2, -1,]
    expected = [4, [49, [16, [4, None, None], [-2, None, None]], [12, None, [2, None, None]]], [35, [0, [16, None, None], [6, None, None]], [20, [4, None, None], [18, None, None]]]]
    return do_ex1_test(root, lista_pesi, expected)

def test_ex1_3():
    root     = [4, [5, [8, [-2, [29, [22, None, [4, [13, [9, [15, [16, None, [22, None, None]], None], [1, [-9, [26, None, None], [29, [20, None, None], [17, None, None]]], [30, [11, [8, None, None], None], [26, None, None]]]], [-10, [16, [8, [11, None, [18, None, None]], [-4, [21, [8, None, None], None], None]], None], [-4, [18, [4, None, None], None], [8, [-8, [17, None, None], None], None]]]], [-6, [7, [12, [24, None, None], [14, None, None]], [12, [14, [29, None, None], [9, None, None]], None]], [0, [28, [25, None, None], [1, [11, None, None], None]], [0, [18, [18, None, None], [0, None, None]], [-1, None, None]]]]]], [27, [24, [-1, None, None], [26, [16, [12, None, None], [12, None, [11, None, None]]], [18, None, [21, None, None]]]], [0, [14, None, [-1, None, None]], [6, [30, None, None], [11, None, None]]]]], [3, [19, [-3, [22, [-7, [-5, None, None], [-6, None, None]], [0, [9, [8, None, None], [-3, None, None]], [10, [-3, None, None], [14, None, [21, None, None]]]]], [28, None, [23, [18, [-9, None, None], [28, [8, None, None], None]], [-4, None, None]]]], [-1, [30, [-10, None, None], None], [27, [-9, [5, None, None], [16, None, None]], [-2, [28, None, None], [21, None, None]]]]], [28, [4, [6, [30, [22, None, None], [12, [5, None, None], None]], [4, [4, [29, None, None], None], [5, None, None]]], None], [26, [27, [20, [25, None, None], [30, None, None]], [-8, None, [20, None, None]]], [16, [11, [3, [4, None, None], None], [22, [-7, None, None], None]], [0, None, [4, None, None]]]]]]], [-4, [7, [20, [22, [-8, [24, None, None], [-1, None, None]], [28, [2, None, [18, [30, None, None], None]], [25, [-3, None, None], None]]], None], [26, [12, [10, [14, None, None], [-3, None, None]], None], [-4, [-5, [18, None, None], [-9, None, None]], [19, [-2, None, None], [21, [14, None, None], None]]]]], [4, [6, [-3, [14, None, [4, [1, [0, None, None], [6, None, None]], None]], [14, [12, None, [2, [20, None, [12, None, None]], [0, [30, None, None], [-5, None, None]]]], [27, [-8, [-5, None, None], None], [2, [-1, [-1, None, None], None], [7, None, None]]]]], None], [3, [4, [30, [30, [16, [17, None, None], [-7, None, None]], None], [30, [27, [8, [-7, None, [7, None, None]], [23, None, None]], [23, [0, None, [10, None, None]], [1, [30, None, None], None]]], [2, None, None]]], [16, [12, [30, [-1, [18, None, None], None], [23, [-8, [11, None, None], None], [4, None, None]]], [-5, None, [-9, [19, None, None], None]]], [8, [20, [19, [6, None, None], None], [29, [26, None, None], [15, [26, None, None], None]]], [24, [-8, None, None], [13, None, None]]]]], [9, [13, [6, [11, [8, None, None], [2, None, [20, None, None]]], [14, [23, None, None], None]], [28, [10, None, [3, None, None]], [6, [6, None, None], [7, None, None]]]], None]]]]], [26, [1, [16, [10, [-4, [13, [24, [3, [10, None, None], [17, None, [19, None, None]]], [26, None, None]], [9, [2, None, [1, None, None]], [20, [11, None, None], [-9, [-1, None, None], [19, None, None]]]]], None], [-2, [11, None, [9, [7, [19, None, None], None], [11, None, None]]], [-5, [-10, [28, [28, None, None], [13, None, None]], [-6, [25, None, None], [0, None, [-3, None, None]]]], [28, [8, [-10, [25, None, None], [25, None, None]], [14, [2, [10, None, None], [20, None, None]], None]], [21, [23, [5, [-2, None, [9, None, None]], [5, None, None]], [-2, None, [12, [28, None, None], None]]], None]]]]], None], [19, [8, [29, [24, [26, [-2, None, None], [2, None, None]], [-1, None, None]], [22, None, [30, None, None]]], None], [0, [0, [-2, [29, [10, [-3, [15, None, None], [26, None, [29, None, None]]], None], [28, [22, None, None], [30, None, None]]], [-10, [8, [16, None, None], [27, None, None]], [7, [28, None, None], None]]], [-1, [9, [19, [-1, [16, None, None], [30, [14, None, None], None]], [1, None, None]], [-7, [3, None, None], [-7, None, None]]], [24, [-1, [26, None, None], [19, None, None]], [11, [27, [-1, None, None], None], None]]]], None]]], None]], [19, [30, [4, [18, [14, [17, [29, [4, [27, [28, None, [17, None, None]], [2, [15, None, [-7, None, None]], None]], [14, [2, [18, [-5, None, [26, None, None]], [17, None, None]], [25, None, None]], [22, [28, None, None], [21, None, [-7, [21, None, None], None]]]]], [10, [-9, [6, [27, [2, None, None], None], [15, [11, None, None], None]], None], [12, [-2, [19, None, None], [14, None, None]], [2, None, [14, None, [24, None, None]]]]]], [1, [6, [-5, [6, [16, [16, [24, None, None], [12, None, None]], [27, [1, None, [8, None, None]], [-4, None, None]]], [-3, None, None]], [27, [1, None, None], [22, None, [-6, None, None]]]], [1, [-7, [10, [14, [26, None, None], [13, None, None]], [-6, None, None]], [19, [25, None, [-4, None, None]], None]], [3, None, [24, [29, None, None], [-4, None, None]]]]], None]], [6, [26, [7, [-2, [9, None, None], [3, [12, [-1, None, None], None], [9, None, None]]], [21, [-5, None, [27, None, None]], None]], [8, [-9, [18, [-10, None, None], None], [22, [28, None, None], [-9, [13, None, None], None]]], [-4, [17, None, None], [2, [-4, None, None], [19, None, None]]]]], [8, [-1, [17, [-7, [3, None, None], [20, None, None]], [-8, None, [2, None, None]]], [0, None, [0, None, [21, None, None]]]], [12, None, [1, None, [7, None, None]]]]]], [2, [12, [-7, [21, None, [27, None, None]], [29, [25, [18, None, None], [0, None, None]], [18, None, [30, None, None]]]], [-1, [1, [5, None, None], [0, None, None]], [12, [20, None, [15, None, None]], None]]], [9, [0, [13, [26, [16, None, None], [-8, [5, None, None], None]], [-8, [-6, None, [-8, None, None]], [-5, [26, None, None], None]]], [1, [22, [24, None, None], None], [22, None, [-2, None, None]]]], None]]], [26, [26, [13, [12, [-10, [28, [4, None, None], [-9, None, None]], [23, [7, None, None], None]], None], [7, None, [24, None, [-1, [9, None, None], None]]]], [-9, [9, [20, [-6, [17, [29, [22, [14, None, None], [-9, [10, [-8, None, None], None], [5, None, None]]], [-2, [25, None, None], [24, None, None]]], [27, [-6, None, None], [16, None, None]]], [-8, [13, [-8, None, None], [-4, None, None]], [16, None, [11, [15, None, None], None]]]], [24, [25, [18, None, [-2, None, None]], [1, None, None]], [12, [-5, [22, None, None], None], [25, [1, None, None], None]]]], [27, [8, [17, None, [-10, None, None]], None], [17, [-9, None, [-1, None, None]], [21, None, [3, None, None]]]]], [23, [-4, [18, None, [-8, None, None]], [8, [6, [-8, None, [25, None, None]], None], [27, [-5, None, None], [8, None, None]]]], [4, [-8, None, [9, [14, [8, None, None], [12, None, [0, None, None]]], [0, [-3, None, None], [-7, None, None]]]], [13, [29, [28, [3, None, None], [-5, None, None]], [-6, [-7, None, None], None]], None]]]]], [10, [8, [-4, [28, None, None], [30, None, [27, [25, [21, None, None], None], [5, None, None]]]], [10, [0, [-2, [4, [7, None, [18, None, None]], [15, None, None]], [5, None, None]], [1, [-7, None, None], None]], [11, [-5, [16, [-10, None, None], [0, None, None]], [29, None, None]], None]]], [-10, None, [7, [13, [17, [1, [6, None, None], None], [-6, None, None]], [21, None, [-9, None, None]]], [0, None, [17, [28, None, None], [13, [11, None, None], None]]]]]]]], None], [-5, None, [16, [9, [30, [17, [26, [29, [10, [4, None, None], [11, None, None]], [14, [-3, [22, [13, None, None], [-3, None, None]], [3, [7, None, [9, None, None]], [15, None, None]]], [20, [19, None, None], [-9, None, [16, None, None]]]]], [-4, [25, [14, [11, [10, None, None], None], [-9, [26, None, None], [13, None, None]]], [-10, None, None]], [25, [23, [24, [13, [1, None, None], None], [27, None, None]], [-5, None, [12, [2, None, None], [-10, None, None]]]], [-5, [13, None, None], None]]]], [10, [3, [26, [28, [18, None, None], [2, None, None]], [14, [15, [-10, None, None], [28, None, [-2, None, None]]], [11, [12, [-8, [-7, None, None], None], [-5, [17, None, None], None]], None]]], [30, [9, [24, [15, None, None], [2, None, [9, None, None]]], [-7, [7, [21, None, None], [27, [-6, None, None], None]], [0, [-7, [20, None, None], [16, None, [23, None, None]]], [16, None, [25, None, None]]]]], None]], [28, [8, [9, [24, None, None], [17, [20, [-5, None, None], [27, None, None]], [13, None, None]]], [12, [28, [24, None, [-1, None, None]], [14, [-3, None, None], [0, None, None]]], [-4, None, None]]], [-2, [14, [-1, [20, None, [6, None, None]], [29, None, [-6, None, None]]], [6, None, [1, None, None]]], [21, [5, [9, None, None], None], [3, [17, [23, None, None], [22, [11, [2, None, None], None], [23, [12, None, None], None]]], None]]]]]], [22, None, [14, [14, [5, [-7, None, None], [-1, None, None]], [-10, [-10, [-8, None, [11, None, None]], [-3, None, None]], [-8, None, None]]], [11, [14, [12, None, [7, None, None]], [3, None, [9, None, None]]], [6, [14, [25, [5, None, None], [12, None, None]], [12, [3, [11, None, None], None], [-4, None, None]]], [20, [17, None, None], [16, [25, None, None], [14, None, None]]]]]]]], [5, [-8, [11, [-4, [19, [-9, [26, None, [8, [16, None, None], [11, None, None]]], [18, [1, [21, None, None], None], [-10, None, None]]], [29, [5, [14, None, None], None], [14, None, None]]], [22, [29, None, [26, None, None]], None]], [22, [12, [27, [10, [26, [18, None, None], None], [-1, [8, None, None], None]], [23, [-1, [7, None, None], None], [17, [20, None, None], None]]], [-8, [-2, None, None], [25, None, None]]], [28, [-8, [2, [-9, [17, None, None], [12, None, None]], [-1, None, None]], [-6, [-7, [11, None, None], None], [-6, [-10, None, None], [25, None, None]]]], [18, [20, [6, [3, None, None], None], None], [29, [18, None, None], [-2, None, None]]]]]], [-8, None, None]], [20, [22, [-2, [6, [11, [-3, None, [-1, [-2, [5, None, None], [28, [15, None, None], None]], [-5, [27, None, None], [-10, None, None]]]], [-2, [28, None, None], [25, [23, None, None], None]]], [2, [23, [1, None, [-3, None, None]], [-9, None, None]], [12, [-2, None, None], [28, [10, None, None], [-10, None, None]]]]], [-2, [12, [-6, [8, [13, [28, None, None], [24, None, None]], [13, None, None]], [17, None, [12, None, None]]], [15, [23, [22, [6, None, None], [10, [-9, None, None], [29, None, [19, None, None]]]], [9, None, None]], [6, [26, None, [16, [24, None, None], None]], None]]], [2, [9, [3, None, None], None], [29, [25, None, None], [-9, None, None]]]]], [3, [13, [13, [0, [30, [5, [10, None, None], [11, None, None]], [23, [11, None, [-10, None, None]], [-9, None, None]]], [4, [24, [24, None, [28, None, None]], [-4, None, None]], [7, [-2, None, None], None]]], [-8, [25, [1, [15, None, None], None], [1, None, [27, None, None]]], [23, [8, [-2, [29, None, None], [4, None, None]], [27, [18, None, None], [1, None, None]]], [25, [13, None, None], None]]]], [-7, [4, [6, [-4, None, [-4, None, None]], [10, [22, None, None], [3, None, None]]], [4, [-1, None, None], [-10, None, None]]], [5, [-1, [-2, [15, None, None], [15, [17, None, None], [22, None, [11, None, None]]]], None], [-2, [-6, [20, None, None], None], [25, [25, None, None], [21, None, None]]]]]], [4, [9, [6, [16, None, None], None], [19, [17, None, [14, None, None]], [6, [9, None, [20, None, [28, None, None]]], [19, [4, [8, None, [25, None, None]], None], [30, None, None]]]]], [-8, [-10, [9, [12, None, [28, None, None]], [11, None, None]], [30, [-8, None, [13, None, None]], [13, [18, [-3, None, None], [8, None, None]], [20, None, None]]]], [30, [8, [-7, [21, None, [11, [26, None, None], None]], [10, [-9, None, None], [30, None, None]]], [-8, None, None]], [17, [1, [1, [21, None, None], None], [16, None, None]], [4, [27, [-3, None, None], [26, None, None]], [-4, None, None]]]]]]]], [25, None, [2, [16, [25, [-4, None, [30, None, None]], [-6, None, [-10, None, [-2, None, None]]]], [25, [21, [28, None, None], [-2, [16, None, [2, None, None]], None]], [19, None, [10, None, None]]]], [13, [7, [7, None, None], [-8, None, None]], [1, [26, [-10, [26, None, None], [10, None, None]], [-7, [-8, [4, None, None], None], [18, None, None]]], [2, [18, None, None], [12, None, None]]]]]]]]], [0, [28, [13, None, [11, [-6, None, [7, [8, [-2, None, None], None], [15, None, None]]], [25, [-4, [-2, None, None], None], [-2, None, None]]]], [11, [11, [-6, [15, [28, [12, None, None], [-2, None, None]], None], None], None], [20, [13, None, [29, [-7, [-6, [23, None, None], [-2, None, None]], [21, None, None]], [29, [7, None, None], None]]], [11, [14, [-6, None, [0, None, None]], [28, None, None]], None]]]], None]]]]]
    pesi     = [37, 89, 26, 53, 81, 87, 25, 35, 15, 74, 96, 10, 96, 73, 49, 69, 55, 23, 58, 78, 72]
    expected = [148, [445, [208, [-106, [2349, [1914, None, [100, [455, [135, [1110, [1536, None, [220, None, None]], None], [74, [-864, [260, None, None], [290, [1920, None, None], [1632, None, None]]], [2880, [110, [768, None, None], None], [260, None, None]]]], [-150, [1184, [768, [110, None, [1728, None, None]], [-40, [2016, [584, None, None], None], None]], None], [-296, [1728, [40, None, None], None], [768, [-80, [1632, None, None], None], None]]]], [-210, [105, [888, [2304, None, None], [1344, None, None]], [888, [1344, [290, None, None], [90, None, None]], None]], [0, [2072, [2400, None, None], [96, [110, None, None], None]], [0, [1728, [180, None, None], [0, None, None]], [-96, None, None]]]]]], [2349, [600, [-35, None, None], [910, [240, [888, None, None], [888, None, [1056, None, None]]], [270, None, [1554, None, None]]]], [0, [490, None, [-15, None, None]], [210, [450, None, None], [165, None, None]]]]], [243, [1653, [-75, [770, [-105, [-370, None, None], [-444, None, None]], [0, [666, [768, None, None], [-288, None, None]], [740, [-288, None, None], [1344, None, [210, None, None]]]]], [980, None, [345, [1332, [-864, None, None], [2688, [80, None, None], None]], [-296, None, None]]]], [-25, [1050, [-150, None, None], None], [945, [-135, [370, None, None], [1184, None, None]], [-30, [2072, None, None], [1554, None, None]]]]], [2436, [100, [210, [450, [1628, None, None], [888, [480, None, None], None]], [60, [296, [2784, None, None], None], [370, None, None]]], None], [650, [945, [300, [1850, None, None], [2220, None, None]], [-120, None, [1480, None, None]]], [560, [165, [222, [384, None, None], None], [1628, [-672, None, None], None]], [0, None, [296, None, None]]]]]]], [-212, [567, [1740, [550, [-280, [360, None, None], [-15, None, None]], [980, [30, None, [1332, [2880, None, None], None]], [375, [-222, None, None], None]]], None], [2262, [300, [350, [210, None, None], [-45, None, None]], None], [-100, [-175, [270, None, None], [-135, None, None]], [665, [-30, None, None], [315, [1036, None, None], None]]]]], [324, [522, [-75, [490, None, [60, [74, [0, None, None], [576, None, None]], None]], [490, [180, None, [148, [1920, None, [120, None, None]], [0, [300, None, None], [-50, None, None]]]], [405, [-592, [-480, None, None], None], [148, [-96, [-10, None, None], None], [672, None, None]]]]], None], [261, [100, [1050, [450, [1184, [1632, None, None], [-672, None, None]], None], [450, [1998, [768, [-70, None, [672, None, None]], [230, None, None]], [2208, [0, None, [960, None, None]], [10, [2880, None, None], None]]], [148, None, None]]], [560, [180, [2220, [-96, [180, None, None], None], [2208, [-80, [1056, None, None], None], [40, None, None]]], [-370, None, [-864, [190, None, None], None]]], [120, [1480, [1824, [60, None, None], None], [2784, [260, None, None], [150, [2496, None, None], None]]], [1776, [-768, None, None], [1248, None, None]]]]], [225, [455, [90, [814, [768, None, None], [192, None, [200, None, None]]], [1036, [2208, None, None], None]], [420, [740, None, [288, None, None]], [444, [576, None, None], [672, None, None]]]], None]]]]], [676, [53, [1296, [870, [-100, [455, [360, [222, [960, None, None], [1632, None, [190, None, None]]], [1924, None, None]], [135, [148, None, [96, None, None]], [1480, [1056, None, None], [-864, [-10, None, None], [190, None, None]]]]], None], [-50, [385, None, [135, [518, [1824, None, None], None], [814, None, None]]], [-175, [-150, [2072, [2688, None, None], [1248, None, None]], [-444, [2400, None, None], [0, None, [-30, None, None]]]], [420, [592, [-960, [250, None, None], [250, None, None]], [1344, [20, [960, None, None], [1920, None, None]], None]], [1554, [2208, [50, [-192, None, [657, None, None]], [480, None, None]], [-20, None, [1152, [2044, None, None], None]]], None]]]]], None], [1539, [696, [725, [840, [390, [-148, None, None], [148, None, None]], [-15, None, None]], [770, None, [450, None, None]]], None], [0, [0, [-70, [435, [740, [-288, [150, None, None], [260, None, [2784, None, None]]], None], [2072, [2112, None, None], [2880, None, None]]], [-150, [592, [1536, None, None], [2592, None, None]], [518, [2688, None, None], None]]], [-35, [135, [1406, [-96, [160, None, None], [300, [1344, None, None], None]], [96, None, None]], [-518, [288, None, None], [-672, None, None]]], [360, [-74, [2496, None, None], [1824, None, None]], [814, [2592, [-10, None, None], None], None]]]], None]]], None]], [1691, [780, [212, [1458, [1218, [425, [1015, [60, [1998, [2688, None, [170, None, None]], [192, [150, None, [-672, None, None]], None]], [1036, [192, [180, [-480, None, [1898, None, None]], [1632, None, None]], [250, None, None]], [2112, [280, None, None], [210, None, [-672, [1533, None, None], None]]]]], [150, [-666, [576, [270, [192, None, None], None], [150, [1056, None, None], None]], None], [888, [-192, [190, None, None], [140, None, None]], [192, None, [140, None, [2304, None, None]]]]]], [35, [90, [-370, [576, [160, [1536, [1752, None, None], [876, None, None]], [2592, [73, None, [392, None, None]], [-292, None, None]]], [-30, None, None]], [2592, [10, None, None], [220, None, [-576, None, None]]]], [74, [-672, [100, [1344, [1898, None, None], [949, None, None]], [-576, None, None]], [190, [2400, None, [-292, None, None]], None]], [288, None, [240, [2784, None, None], [-384, None, None]]]]], None]], [150, [910, [105, [-148, [864, None, None], [288, [120, [-96, None, None], None], [90, None, None]]], [1554, [-480, None, [270, None, None]], None]], [120, [-666, [1728, [-100, None, None], None], [2112, [280, None, None], [-90, [1248, None, None], None]]], [-296, [1632, None, None], [192, [-40, None, None], [190, None, None]]]]], [280, [-15, [1258, [-672, [30, None, None], [200, None, None]], [-768, None, [20, None, None]]], [0, None, [0, None, [210, None, None]]]], [180, None, [74, None, [672, None, None]]]]]], [174, [300, [-245, [315, None, [1998, None, None]], [435, [1850, [1728, None, None], [0, None, None]], [1332, None, [2880, None, None]]]], [-35, [15, [370, None, None], [0, None, None]], [180, [1480, None, [1440, None, None]], None]]], [225, [0, [195, [1924, [1536, None, None], [-768, [50, None, None], None]], [-592, [-576, None, [-80, None, None]], [-480, [260, None, None], None]]], [15, [1628, [2304, None, None], None], [1628, None, [-192, None, None]]]], None]]], [2106, [2262, [325, [420, [-150, [2072, [384, None, None], [-864, None, None]], [1702, [672, None, None], None]], None], [245, None, [360, None, [-74, [864, None, None], None]]]], [-225, [315, [300, [-444, [1632, [290, [2112, [1022, None, None], [-657, [490, [-552, None, None], None], [245, None, None]]], [-192, [1825, None, None], [1752, None, None]]], [270, [-576, None, None], [1536, None, None]]], [-768, [130, [-768, None, None], [-384, None, None]], [160, None, [1056, [1095, None, None], None]]]], [1776, [2400, [180, None, [-192, None, None]], [10, None, None]], [1152, [-50, [2112, None, None], None], [250, [96, None, None], None]]]], [405, [592, [1632, None, [-100, None, None]], None], [1258, [-864, None, [-10, None, None]], [2016, None, [30, None, None]]]]], [805, [-60, [1332, None, [-768, None, None]], [592, [576, [-80, None, [2400, None, None]], None], [2592, [-50, None, None], [80, None, None]]]], [60, [-592, None, [864, [140, [768, None, None], [1152, None, [0, None, None]]], [0, [-288, None, None], [-672, None, None]]]], [962, [2784, [280, [288, None, None], [-480, None, None]], [-60, [-672, None, None], None]], None]]]]], [870, [200, [-140, [420, None, None], [450, None, [1998, [2400, [210, None, None], None], [480, None, None]]]], [350, [0, [-148, [384, [70, None, [1728, None, None]], [150, None, None]], [480, None, None]], [74, [-672, None, None], None]], [165, [-370, [1536, [-100, None, None], [0, None, None]], [2784, None, None]], None]]], [-250, None, [245, [195, [1258, [96, [60, None, None], None], [-576, None, None]], [1554, None, [-864, None, None]]], [0, None, [1258, [2688, None, None], [1248, [110, None, None], None]]]]]]]], None], [-130, None, [848, [729, [2610, [425, [910, [435, [740, [384, None, None], [1056, None, None]], [1036, [-288, [220, [1248, None, None], [-288, None, None]], [30, [672, None, [657, None, None]], [1440, None, None]]], [1920, [190, None, None], [-90, None, [1536, None, None]]]]], [-60, [1850, [1344, [110, [960, None, None], None], [-90, [2496, None, None], [1248, None, None]]], [-960, None, None]], [1850, [2208, [240, [1248, [73, None, None], None], [2592, None, None]], [-50, None, [1152, [146, None, None], [-730, None, None]]]], [-480, [130, None, None], None]]]], [350, [45, [1924, [2688, [180, None, None], [20, None, None]], [1344, [150, [-960, None, None], [2688, None, [-146, None, None]]], [110, [1152, [-584, [-343, None, None], None], [-365, [833, None, None], None]], None]]], [2220, [864, [240, [1440, None, None], [192, None, [657, None, None]]], [-70, [672, [1533, None, None], [1971, [-294, None, None], None]], [0, [-511, [980, None, None], [784, None, [1587, None, None]]], [1168, None, [1225, None, None]]]]], None]], [420, [592, [864, [240, None, None], [170, [1920, [-365, None, None], [1971, None, None]], [1248, None, None]]], [1152, [280, [2304, None, [-73, None, None]], [1344, [-219, None, None], [0, None, None]]], [-40, None, None]]], [-148, [1344, [-10, [1920, None, [438, None, None]], [2784, None, [-438, None, None]]], [60, None, [96, None, None]]], [2016, [50, [864, None, None], None], [30, [1632, [1679, None, None], [1606, [539, [138, None, None], None], [1127, [828, None, None], None]]], None]]]]]], [550, None, [490, [210, [370, [-672, None, None], [-96, None, None]], [-740, [-960, [-80, None, [1056, None, None]], [-30, None, None]], [-768, None, None]]], [165, [1036, [1152, None, [70, None, None]], [288, None, [90, None, None]]], [444, [1344, [250, [480, None, None], [1152, None, None]], [120, [288, [803, None, None], None], [-384, None, None]]], [1920, [170, None, None], [160, [2400, None, None], [1344, None, None]]]]]]]], [435, [-200, [385, [-60, [1406, [-864, [260, None, [768, [1168, None, None], [803, None, None]]], [180, [96, [1533, None, None], None], [-960, None, None]]], [2784, [50, [1344, None, None], None], [140, None, None]]], [1628, [2784, None, [260, None, None]], None]], [330, [888, [2592, [100, [2496, [1314, None, None], None], [-96, [584, None, None], None]], [230, [-96, [511, None, None], None], [1632, [1460, None, None], None]]], [-768, [-20, None, None], [250, None, None]]], [2072, [-768, [20, [-864, [1241, None, None], [876, None, None]], [-96, None, None]], [-60, [-672, [803, None, None], None], [-576, [-730, None, None], [1825, None, None]]]], [1728, [200, [576, [219, None, None], None], None], [290, [1728, None, None], [-192, None, None]]]]]], [-280, None, None]], [500, [770, [-30, [444, [1056, [-30, None, [-96, [-146, [245, None, None], [1372, [1035, None, None], None]], [-365, [1323, None, None], [-490, None, None]]]], [-20, [2688, None, None], [2400, [1679, None, None], None]]], [192, [230, [96, None, [-219, None, None]], [-864, None, None]], [120, [-192, None, None], [2688, [730, None, None], [-730, None, None]]]]], [-148, [1152, [-60, [768, [949, [1372, None, None], [1176, None, None]], [949, None, None]], [1632, None, [876, None, None]]], [150, [2208, [1606, [294, None, None], [490, [-621, None, None], [2001, None, [1045, None, None]]]], [657, None, None]], [576, [1898, None, [784, [1656, None, None], None]], None]]], [192, [90, [288, None, None], None], [290, [2400, None, None], [-864, None, None]]]]], [45, [962, [1248, [0, [2880, [365, [490, None, None], [539, None, None]], [1679, [539, None, [-690, None, None]], [-441, None, None]]], [384, [1752, [1176, None, [1932, None, None]], [-196, None, None]], [511, [-98, None, None], None]]], [-80, [2400, [73, [735, None, None], None], [73, None, [1323, None, None]]], [2208, [584, [-98, [2001, None, None], [276, None, None]], [1323, [1242, None, None], [69, None, None]]], [1825, [637, None, None], None]]]], [-672, [40, [576, [-292, None, [-196, None, None]], [730, [1078, None, None], [147, None, None]]], [384, [-73, None, None], [-730, None, None]]], [50, [-96, [-146, [735, None, None], [735, [1173, None, None], [1518, None, [605, None, None]]]], None], [-192, [-438, [980, None, None], None], [1825, [1225, None, None], [1029, None, None]]]]]], [296, [864, [60, [1536, None, None], None], [190, [1632, None, [1022, None, None]], [576, [657, None, [980, None, [1932, None, None]]], [1387, [196, [552, None, [1375, None, None]], None], [1470, None, None]]]]], [-768, [-100, [864, [876, None, [1372, None, None]], [803, None, None]], [2880, [-584, None, [637, None, None]], [949, [882, [-207, None, None], [552, None, None]], [980, None, None]]]], [300, [768, [-511, [1029, None, [759, [1430, None, None], None]], [490, [-621, None, None], [2070, None, None]]], [-584, None, None]], [1632, [73, [49, [1449, None, None], None], [784, None, None]], [292, [1323, [-207, None, None], [1794, None, None]], [-196, None, None]]]]]]]], [875, None, [30, [1184, [2400, [-40, None, [2880, None, None]], [-60, None, [-960, None, [-146, None, None]]]], [2400, [210, [2688, None, None], [-192, [1168, None, [98, None, None]], None]], [190, None, [960, None, None]]]], [962, [672, [70, None, None], [-80, None, None]], [96, [260, [-960, [1898, None, None], [730, None, None]], [-672, [-584, [196, None, None], None], [1314, None, None]]], [20, [1728, None, None], [1152, None, None]]]]]]]]], [0, [2436, [325, None, [385, [-90, None, [518, [768, [-20, None, None], None], [1440, None, None]]], [375, [-296, [-192, None, None], None], [-148, None, None]]]], [275, [385, [-90, [1110, [2688, [120, None, None], [-20, None, None]], None], None], None], [700, [195, None, [2146, [-672, [-60, [2208, None, None], [-192, None, None]], [210, None, None]], [2784, [70, None, None], None]]], [165, [1036, [-576, None, [0, None, None]], [2688, None, None]], None]]]], None]]]]]
    return do_ex1_test(root, pesi, expected)


# ----------------------------------- EX.3 ----------------------------------- #

def do_ex2_test(directory, extensions, expected):
    if not DEBUG:
        isrecursive2.DETECT = True
        try:
            program.ex2(directory, extensions)
        except isrecursive2.RecursionDetectedError:
            pass
        else:
            raise Exception(
                "The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive2.DETECT = False

    res = program.ex2(directory, extensions)
    testlib.check_dict(res, expected)
    return 2

def test_ex2_1(run=True):
    directory  = 'ex2/A'
    extensions = ["txt", "pdf", "png", "gif"]
    expected   = {'txt': {'ex2/A/C', 'ex2/A', 'ex2/A/B'}, 'pdf': {'ex2/A/C', 'ex2/A'}, 'png': {'ex2/A/C'}, 'gif': {'ex2/A/C'}}
    return do_ex2_test(directory, extensions, expected)

def test_ex2_2(run=True):
    directory  = 'ex2'
    extensions = ["png", "gif", "tqq"]
    expected   = {'png': {'ex2/C/C', 'ex2/A/C', 'ex2/C/B/p3zt345614/17nt', 'ex2/C/C/9n5'}, 
                  'gif': {'ex2/A/C', 'ex2/C/C/9n5/22zi524j', 'ex2/C/C/9n5', 'ex2/C/C'}, 'tqq': {'ex2/B/hfc44ba'}}
    return do_ex2_test(directory, extensions, expected)

def test_ex2_3(run=True):
    directory  = 'ex2/C'
    extensions = ["pdf", "png", "txt", "ne3"]
    expected   = {'pdf': {'ex2/C/C', 'ex2/C/C/9n5', 'ex2/C/B/p3zt345614/17nt'}, 
                  'png': {'ex2/C/C', 'ex2/C/C/9n5', 'ex2/C/B/p3zt345614/17nt'}, 
                  'txt': {'ex2/C/A/a9fa5r54ol/9dlnpni', 'ex2/C/A', 'ex2/C', 'ex2/C/A/a9fa5r54ol', 'ex2/C/B', 'ex2/C/A/r5g/d501/tew8', 
                          'ex2/C/C/9n5/22zi524j', 'ex2/C/A/r5g', 'ex2/C/A/a9fa5r54ol/9dlnpni/1bqeb8', 'ex2/C/C/9n5/22zi524j/1iha5', 
                          'ex2/C/B/p3zt345614/17nt', 'ex2/C/A/r5g/d501', 'ex2/C/B/p3zt345614/ei9ej73p', 'ex2/C/C/9n5/22zi524j/u2g', 
                          'ex2/C/439/53d23yd', 'ex2/C/A/a9fa5r54ol/9dlnpni/p2q8', 'ex2/C/4q5ni', 'ex2/C/B/p3zt345614/7j30i'}, 
                  'ne3': {'ex2/C/A/r5g'}}
    return do_ex2_test(directory, extensions, expected)

# ----------------------------------- EX. 4 ----------------------------------- #

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2,                                 # 2   / 2
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,     # 2   / 4
    test_func3_1, test_func3_2, test_func3_3,                   # 2   / 3
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,     # 6   / 4
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,     # 8   / 4

    test_ex1_1,    test_ex1_2,   test_ex1_3,                    # 6   / 3
    test_ex2_1,    test_ex2_2,   test_ex2_3,                    # 6   / 3
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

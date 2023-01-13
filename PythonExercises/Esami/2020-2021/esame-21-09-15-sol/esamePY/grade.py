import testlib
import isrecursive
import os

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    exit(0)
import program as program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(vec, idx, expected):
    res = program.ex1(vec, idx)
    testlib.check(res, expected)
    return 2

def test_ex1_1():
   vector = [ [1,2,3],    # 0
              [50,20,30], # 1
              [0,12,13],   # 2
              [3,1,0]     # 3
            ]
   idx  = [  [0,1,3],
             [0,0,0],
             [3,2,1],
          ]
   expected = [[[1, 2, 3], [50, 20, 30], [3, 1, 0]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[3, 1, 0], [0, 12, 13], [50, 20, 30]]]
   return do_test_ex1(vector, idx,  expected)

def test_ex1_2():
   vector = [ 
              [1,2,3],    # 0
              [50,20,30], # 1
              [0,12,13],   # 2
              [3,1,0],     # 3
              [11,12,13],    # 4
              [150,120,130], # 5
              [10,112,113],   # 6
              [13,11,10],     # 7
            ]
   idx  = [  
             [0,1,3],
             [0,0,0],
             [3,2,1],
             [4,1,5],
             [6,4,0],
             [3,7,7],
          ]
   expected = [
           [[1, 2, 3], [50, 20, 30], [3, 1, 0]], 
           [[1, 2, 3], [1, 2, 3], [1, 2, 3]], 
           [[3, 1, 0], [0, 12, 13], [50, 20, 30]],
           [[11,12,13], [50,20,30], [150,120,130],],
           [[10,112,113], [11,12,13], [1,2,3],],
           [[3,1,0], [13,11,10], [13,11,10],],
               ]
   return do_test_ex1(vector, idx,  expected)

def test_ex1_3():
   vector = [ 
              [0,12,13],      # 0
              [1,2,3],        # 1
              [10,112,113],   # 2
              [11,12,13],     # 3
              [13,11,10],     # 4
              [150,120,130],  # 5
              [3,1,0],        # 6
              [50,20,30],     # 7
            ]
   idx  = [  
             [0,1,3],
             [0,0,0],
             [3,2,1],
             [4,1,5],
             [6,4,0],
             [3,7,7],
          ]
   expected = [
           [[0, 12, 13], [1, 2, 3], [11, 12, 13]], 
           [[0, 12, 13], [0, 12, 13], [0, 12, 13]], 
           [[11, 12, 13], [10, 112, 113], [1, 2, 3]], 
           [[13, 11, 10], [1, 2, 3], [150, 120, 130]], 
           [[3, 1, 0], [13, 11, 10], [0, 12, 13]], 
           [[11, 12, 13], [50, 20, 30], [50, 20, 30]]
              ]
   return do_test_ex1(vector, idx,  expected)
# ----------------------------------- EX.2 ----------------------------------- #
def do_test_ex2(rects, W, H, file_png, expected):
    expected_png = 'rectangles/' + file_png
    res = program.ex2(rects, W, H, file_png)
    testlib.check(res, expected)
    testlib.check_img_file(file_png, expected_png)
    return 2

def test_ex2_1():
    file_png = 'example.png'
    W,H = 500,400
    expected = 42336 # 55168
    rects = [   (316, 260, (171, 155, 135)),
                (304, 328, (77, 176, 176)),
                (172, 180, (193, 76, 56))]
    return do_test_ex2(rects, W, H, file_png, expected)

def test_ex2_2():
    file_png = '10rect.png'
    rects = [(390, 304, (133, 99, 173)),
             (208, 172, (230, 178, 212)),
             (248, 368, (230, 62, 125)),
             (316, 346, (166, 211, 170)),
             (320, 250, (221, 80, 103)),
             (394, 354, (175, 99, 215)),
             (172, 204, (246, 212, 89)),
             (338, 184, (105, 93, 210)),
             (190, 152, (83, 208, 207)),
             (152, 240, (230, 103, 227))]
    W,H = 1000, 2000
    expected = 1388297 # 125349
    return do_test_ex2(rects, W, H, file_png, expected)

def test_ex2_3():
    file_png = '20rect.png'
    W,H = 1500, 1400
    expected = 1473503 # 426028
    rects = [(398, 158, (87, 62, 164)), (308, 398, (55, 99, 109)), (238, 132, (81, 216, 150)), (322, 180, (208, 122, 225)), (338, 118, (207, 52, 185)), (192, 130, (176, 51, 81)), (340, 234, (215, 245, 183)), (210, 126, (230, 97, 84)), (308, 272, (201, 151, 205)), (358, 246, (138, 136, 137)), (264, 230, (233, 149, 208)), (298, 344, (245, 95, 59)), (208, 388, (164, 145, 124)), (142, 170, (52, 64, 208)), (308, 352, (104, 76, 106)), (368, 286, (225, 202, 95)), (306, 376, (204, 187, 50)), (378, 198, (195, 209, 135)), (262, 254, (87, 63, 158)), (128, 354, (135, 132, 222))]
    return do_test_ex2(rects, W, H, file_png, expected)

def test_ex2_4():
    file_png = '30rect.png'
    W,H = 1500, 2400
    expected = 2729930 # 610230
    rects = [
        (350, 110, (129, 202, 239)), (120, 184, (143, 201, 194)), (396, 394, (66, 81, 53)), (298, 328, (218, 219, 169)),
        (208, 372, (62, 81, 177)), (304, 290, (67, 178, 240)), (194, 190, (174, 202, 154)),
        (134, 312, (242, 51, 177)), (162, 354, (199, 209, 163)), (182, 222, (208, 119, 97)),
        (156, 108, (184, 152, 134)), (184, 396, (211, 105, 225)), (292, 394, (53, 106, 77)),
        (386, 154, (143, 63, 50)), (250, 276, (191, 107, 219)), (360, 234, (86, 113, 164)),
        (112, 262, (138, 168, 227)), (304, 186, (141, 228, 68)), (116, 398, (93, 118, 104)),
        (202, 396, (234, 87, 139)), (230, 350, (100, 178, 248)), (380, 104, (133, 64, 77)),
        (242, 254, (210, 128, 246)), (170, 370, (86, 160, 149)), (242, 264, (179, 211, 82)),
        (226, 396, (72, 62, 226)), (344, 392, (131, 239, 123)), (106, 298, (196, 102, 159)),
        (168, 370, (71, 151, 252)), (330, 282, (191, 137, 215))]
    return do_test_ex2(rects, W, H, file_png, expected)



# ----------------------------------- EX.3 ----------------------------------- #

def do_test_ex3(path, searched, extensions, expected):
    try:
        isrecursive.decorate_module(program)
        program.ex3(path, searched, extensions)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    found = program.ex3(path, searched, extensions)
    for k,v in expected.items():
        if k not in found:
            print('missing key', f"'{k}': '{v}',")
    for k,v in found.items():
        if k not in expected:
            print('key that should not be present', f"'{k}': '{v}',")
            continue
        if v != expected[k]:
            print('wrong value', k, v, expected[k])
    testlib.check(found, expected)
    return 3

def test_ex3_1():
    path = 'dirs/d1'
    searched = [ 
         'abrogators', 'alkalizes', 'contemporaneous', 'contrarily', 'cussedly',
         'debilitate', 'debs', 'fletch', 'fuzzi', 'fuzzily', 'incantations', 'involution',
         'letterbox', 'permutes', 'porri', 'porridge', 'primp', 'rebuses', 'refrigerates',
         'requesting', 'ritziest', 'sidewalks', 'slinger', 'slobbered', 'tarantellas',
         'validates', 'walks', 'worlds',
         ]
    extensions = ['txt','rtf']
    expected = { 
        'dirs/d1/keeps.txt': 'fuzzily',
        'dirs/d1/reexplained/tuberculosis.rtf': 'abrogators',
        'dirs/d1/reexplained/creepiest/alee.txt': 'alkalizes',
        'dirs/d1/reexplained/missioner/meetinghouses.txt': 'ritziest',
        'dirs/d1/reexplained/handcuffed/archduke.rtf': 'debs',
        'dirs/d1/reexplained/handcuffed/acyclovir.txt': 'primp',
        'dirs/d1/reexplained/stoma/axiological.rtf': 'rebuses',
        'dirs/d1/complainant/reputably/spiker.txt': 'contrarily',
        'dirs/d1/complainant/growth/multiversity.rtf': 'porridge',
        'dirs/d1/complainant/growth/gettable.txt': 'slobbered'}
    return do_test_ex3(path, searched, extensions, expected)

def test_ex3_2():
    path = 'dirs/d2'
    searched = [ 
        'bank', 'commences', 'defuse', 'degrade', 'degradedly', 'electromechanics',
        'embanking', 'followed', 'foregoer', 'freshens', 'giggled', 'go',
        'grumbler', 'iconoclasm', 'iguanas', 'lebensraum', 'minion', 'monkeys',
        'resupplied', 'sever', 'sierra', 'sophistical', 'stillness', 'toadding',
        'tomcat', 'transposable', 'vitriolic', 'wader', 'warmed', 'wine', 'winegrower',
        ]
    extensions = ['html', 'doc']
    expected = {
        'dirs/d2/squiggled.html': 'commences',
        'dirs/d2/porousness/incredulity.doc': 'sever',
        'dirs/d2/porousness/boosts.html': 'tomcat',
        'dirs/d2/porousness/remanding.html': 'iconoclasm',
        'dirs/d2/porousness/untellable/gratitude.doc': 'followed',
        'dirs/d2/porousness/curiouser/brandies.html': 'embanking',
        'dirs/d2/porousness/curiouser/killable.doc': 'grumbler',
        'dirs/d2/porousness/curiouser/hauberk/notifiers.html': 'sierra',
        'dirs/d2/porousness/barbering/dichotomy.doc': 'stillness',
        'dirs/d2/porousness/proves/winkers.html': 'iguanas',
        }
    return do_test_ex3(path, searched, extensions, expected)

def test_ex3_3():
    path = 'dirs/d3'
    searched = [ 
        'almoners', 'ambidextrous', 'aminobenzoic', 'applauding', 'appropriator',
        'archiving', 'articulator', 'attire', 'banes', 'batching',
        'beneficently', 'betterment', 'birdlike', 'boasting',
        'burden', 'cal', 'candidly', 'canopying', 'canvasing',
        'chartreuse', 'chasm', 'chickened', 'chimp', 'chrysanthemums',
        'circumference', 'clenched', 'clunk', 'coaler', 'condescends',
        'tender', 'coot', 'cosmologically', 'couch', 'counteroffensives',
        'coups', 'couriers', 'cowsheds', 'crank', 'crisis',
        'crosspatches', 'cumbers', 'deallocate', 'decustomised',
        'defectives', 'dehumidifiers', 'deified', 'delete', 'demented',
        'deputize', 'derrieres', 'dilled', 'dimensionless', 'dinosaurs',
        'disallow', 'discerned', 'discourteousness', 'disproving', 'dissevers',
        'disvalues', 'divulges', 'doctored', 'druthers', 'duelers',
        'dulls', 'dumpsters', 'effectives', 'eleven',
        'entitles', 'equivocal', 'evolutionists', 'examen',
        'experimental', 'exploiter', 'feinting', 'fervently',
        'fiendishness', 'figuring', 'finalize', 'finises', 'fisted',
        'flukiest', 'four', 'frappe', 'freakishly', 'gaggle',
        'gasifiers', 'glimmered', 'gloved', 'goosed', 'harassments',
        'helpfully', 'homering', 'humph', 'hurdled', 'hurrying',
        'husks', 'hussar', 'hydroplaned', 'hydroxyls', 'incorporated',
        'inhales', 'insouciance', 'intonations', 'iratest',
        'keepsakes', 'kielbasas', 'lag', 'lent', 'litigated',
        'liverymen', 'loyally', 'mainlands', 'marrieds',
        'melioration', 'messengers', 'miasmas', 'midways', 'militarily',
        'minestrone', 'miscoded', 'muddle', 'myriad', 'new',
        'nickelodeons', 'nieces', 'nonfattening', 'operating', 'osiers',
        'outbounds', 'overwintering', 'pebbliest', 'pelleting', 'penny',
        'perisher', 'pestilently', 'planetoid', 'pocks', 'poisonings',
        'predestine', 'prickles', 'privatest', 'procreation', 'pseudos',
        'pulsates', 'punctuation', 'radiotelegraphs', 'reachably', 'reapportions',
        'rearranged', 'recovery', 'recriminative', 'refinement', 'refuted',
        'reinsurance', 'represses', 'reproves', 'resist', 'resultant',
        'richly', 'roars', 'salons', 'saltiest', 'sandbank',
        'sardined', 'scaling', 'scrambled', 'screes', 'seahorses',
        'seediness', 'semipermanently', 'shalt', 'shear', 'sieges',
        'simply', 'sketched', 'skydiving', 'smell', 'solver',
        'soused', 'sprang', 'stagers', 'staircases', 'stanch',
        'startles', 'strongbox', 'struts', 'sugarcane', 'superbness',
        'superegos', 'supposable', 'sweatshop', 'tartans', 'teacloth',
        'tensive', 'though', 'threadbare', 'thuggee', 'thumps',
        'tissuing', 'topiary', 'torquing', 'totalitarianism', 'tousling',
        'transistor', 'tua', 'unburdening', 'underflowing', 'uninviting',
        'unnormalized', 'unrequested', 'unrevealed', 'virtuously',
        'waveguides', 'whig', 'wifeliest', 'wilts', 'yammering',
        'elevens', 'crankiness'
        ]
    extensions = ['pdf', 'txt','png']
    expected = {
        'dirs/d3/crestfallen/dawdle/implementation.pdf': 'crisis',
        'dirs/d3/crestfallen/fettled.png': 'examen',
        'dirs/d3/crestfallen/likeness/barbarians/chew.txt': 'penny',
        'dirs/d3/crestfallen/likeness/barbarians/smirk.pdf': 'ambidextrous',
        'dirs/d3/crestfallen/likeness/barbarians/whisker.txt': 'elevens',
        'dirs/d3/crestfallen/likeness/husbanded/chagrins.png': 'deallocate',
        'dirs/d3/crestfallen/likeness/husbanded/emergency/bailed.pdf': 'tousling',
        'dirs/d3/crestfallen/likeness/husbanded/emergency/bookbinders.pdf': 'disallow',
        'dirs/d3/crestfallen/likeness/husbanded/exercisable.pdf': 'sketched',
        'dirs/d3/crestfallen/likeness/husbanded/tarmacs.pdf': 'underflowing',
        'dirs/d3/crestfallen/likeness/newsprint/bromide.txt': 'fisted',
        'dirs/d3/crestfallen/likeness/newsprint/honk/remigrates.png': 'sweatshop',
        'dirs/d3/crestfallen/likeness/newsprint/insurrectionists.pdf': 'thuggee',
        'dirs/d3/crestfallen/likeness/newsprint/snickers.png': 'chasm',
        'dirs/d3/crestfallen/naughty.pdf': 'reachably',
        'dirs/d3/crestfallen/polygamists.png': 'four',
        'dirs/d3/crestfallen/satisfies/glamor/orderer/clangorous.txt': 'finises',
        'dirs/d3/crestfallen/satisfies/glamor/rockiest.png': 'fisted',
        'dirs/d3/crestfallen/satisfies/glamor/slough.png': 'gloved',
        'dirs/d3/crestfallen/satisfies/loathsome/chattiness/burbler.pdf': 'semipermanently',
        'dirs/d3/crestfallen/satisfies/loathsome/chattiness/transmogrify.txt': 'gasifiers',
        'dirs/d3/crestfallen/satisfies/loathsome/dispersion.txt': 'defectives',
        'dirs/d3/crestfallen/satisfies/loathsome/flanges/filtering.txt': 'supposable',
        'dirs/d3/crestfallen/satisfies/loathsome/trivium.png': 'duelers',
        'dirs/d3/crestfallen/satisfies/loathsome/unfairly.png': 'outbounds',
        'dirs/d3/crestfallen/satisfies/log.pdf': 'whig',
        'dirs/d3/crestfallen/satisfies/reversals/caterpillar.pdf': 'stanch',
        'dirs/d3/crestfallen/satisfies/reversals/metatheses/tarpapered.pdf': 'harassments',
        'dirs/d3/crestfallen/satisfies/reversals/rejecter/humphs.txt': 'seahorses',
        'dirs/d3/crestfallen/satisfies/reversals/rejecter/regalement.txt': 'batching',
        'dirs/d3/crestfallen/satisfies/speediness/differential/fattens.txt': 'crosspatches',
        'dirs/d3/crestfallen/satisfies/speediness/endorsements/zillions.txt': 'crankiness',
        'dirs/d3/crestfallen/satisfies/speediness/imperfectness/accursedly.txt': 'discourteousness',
        'dirs/d3/crestfallen/satisfies/speediness/imperfectness/regardlessly.png': 'stagers',
        'dirs/d3/crestfallen/satisfies/speediness/interlingual.txt': 'deputize',
        'dirs/d3/crestfallen/satisfies/speediness/lumberyards/desecrates.png': 'hurrying',
        'dirs/d3/crestfallen/satisfies/speediness/worldliness/breadcrumbs.png': 'condescends',
        'dirs/d3/crestfallen/satisfies/turnbuckles.pdf': 'punctuation',
        'dirs/d3/morris/ditched/noncontiguous.pdf': 'lag',
        'dirs/d3/morris/leeward/callousness/flashcube/inbound.png': 'poisonings',
        'dirs/d3/morris/leeward/callousness/flashcube/stockades.png': 'hydroxyls',
        'dirs/d3/morris/leeward/chillers.pdf': 'pulsates',
        'dirs/d3/morris/leeward/conferees/agonized/militia.png': 'entitles',
        'dirs/d3/morris/leeward/conferees/agonized/phrasings.pdf': 'litigated',
        'dirs/d3/morris/leeward/conferees/pectorals.png': 'hussar',
        'dirs/d3/morris/leeward/conferees/subservients/flayer.pdf': 'struts',
        'dirs/d3/morris/leeward/inhering.pdf': 'privatest',
        'dirs/d3/morris/leeward/ligature/dedicates/positivists.pdf': 'counteroffensives',
        'dirs/d3/morris/leeward/ligature/firmly.txt': 'reproves',
        'dirs/d3/morris/leeward/ligature/hairless/discrepancy.pdf': 'circumference',
        'dirs/d3/morris/leeward/ligature/perigee.pdf': 'circumference',
        'dirs/d3/morris/leeward/ligature/unfinished/crummier.txt': 'clunk',
        'dirs/d3/morris/leeward/swab.pdf': 'pebbliest',
        'dirs/d3/morris/rewarder.pdf': 'batching',
        'dirs/d3/priesthoods.txt': 'circumference',
        'dirs/d3/twins.pdf': 'militarily',
        }
    return do_test_ex3(path, searched, extensions, expected)

# ----------------------------------- EX.4 ----------------------------------- #
def do_test_ex4(alphabet, k, expected):
    try:
        isrecursive.decorate_module(program)
        program.ex4(alphabet, k)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    word_list = program.ex4(alphabet, k)
    diff1 = word_list - expected
    if diff1:
        print( "unneeded words:", list(diff1)[:10])
    diff2 = expected - word_list
    if diff2:
        print( "missing words:", list(diff2)[:10])
    testlib.check(word_list, expected)
    return 2

def test_ex4_1():
    # in
    alphabet = 'abc'
    k = 4
    # out
    expected =  {'acca', 'bbbb', 'abba', 'baab', 'aaaa', 'cbbc', 'cccc', 'caac', 'bccb'}
    return do_test_ex4(alphabet, k, expected)

def test_ex4_2():
    # in
    alphabet = 'abc'
    k = 5
    # out
    expected =  {'cbcbc', 'accca', 'abbba', 'ccbcc', 'acaca', 'baaab', 'cbabc', 'acbca', 'babab', 'bcacb', 'bcbcb', 'aaaaa', 'bbcbb', 'ccccc', 'bacab', 'ccacc', 'bcccb', 'bbbbb', 'bbabb', 'ababa', 'aacaa', 'caaac', 'cacac', 'abcba', 'cabac', 'aabaa', 'cbbbc'}
    return do_test_ex4(alphabet, k, expected)

def test_ex4_3():
    # in
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = 3
    # out
    expected =  {'aaa', 'sks', 'ufu', 'bsb', 'jhj', 'sas', 'bqb', 'ere', 'lcl', 'yxy', 'ywy', 'vkv', 'pwp', 'gtg', 'ihi', 'oho', 'zzz', 'iti', 'tyt', 'yyy', 'xcx', 'xwx', 'jaj', 'wnw', 'cxc', 'xdx', 'jnj', 'mxm', 'tqt', 'pip', 'pqp', 'pup', 'rhr', 'nhn', 'aba', 'aua', 'tvt', 'sts', 'pfp', 'vfv', 'tpt', 'unu', 'ncn', 'obo', 'kqk', 'mem', 'dad', 'rtr', 'ttt', 'jjj', 'oao', 'vuv', 'cnc', 'ece', 'eqe', 'hjh', 'lal', 'iki', 'rpr', 'wbw', 'jdj', 'bcb', 'cfc', 'pgp', 'tjt', 'cvc', 'yty', 'fhf', 'jzj', 'bdb', 'fwf', 'jxj', 'srs', 'nwn', 'qlq', 'lel', 'wew', 'lvl', 'vev', 'ded', 'lsl', 'hvh', 'zvz', 'mhm', 'dgd', 'lrl', 'bbb', 'wvw', 'aia', 'kxk', 'iai', 'asa', 'eze', 'mjm', 'tnt', 'nun', 'ebe', 'qbq', 'rwr', 'uju', 'vvv', 'zaz', 'zuz', 'yoy', 'ioi', 'wcw', 'ozo', 'blb', 'txt', 'xrx', 'lyl', 'lil', 'mcm', 'izi', 'sws', 'yry', 'eme', 'wiw', 'gbg', 'cjc', 'vjv', 'ege', 'ddd', 'dfd', 'eje', 'xlx', 'ici', 'owo', 'zhz', 'mwm', 'yhy', 'ubu', 'bvb', 'cbc', 'lbl', 'dtd', 'uwu', 'ztz', 'dxd', 'yny', 'imi', 'qrq', 'hph', 'dld', 'ede', 'qkq', 'vwv', 'wpw', 'plp', 'chc', 'geg', 'nrn', 'mvm', 'fcf', 'mbm', 'bub', 'hlh', 'msm', 'qjq', 'cuc', 'mim', 'uvu', 'vdv', 'wlw', 'bhb', 'eae', 'yay', 'gug', 'sqs', 'ror', 'lkl', 'non', 'gfg', 'utu', 'awa', 'hsh', 'iri', 'npn', 'eue', 'qoq', 'xax', 'kyk', 'jpj', 'fnf', 'dud', 'gvg', 'ovo', 'kek', 'kvk', 'nyn', 'aza', 'fsf', 'ipi', 'zlz', 'wuw', 'kdk', 'nnn', 'lpl', 'pap', 'rlr', 'yuy', 'aqa', 'clc', 'jtj', 'rcr', 'ini', 'qmq', 'krk', 'wxw', 'bib', 'iei', 'tht', 'tlt', 'ldl', 'isi', 'kmk', 'ydy', 'byb', 'cwc', 'whw', 'cec', 'fif', 'ixi', 'hqh', 'tat', 'jfj', 'hnh', 'qnq', 'pop', 'jqj', 'vmv', 'pvp', 'eee', 'ucu', 'olo', 'hdh', 'rrr', 'aga', 'zcz', 'aoa', 'qqq', 'gsg', 'dhd', 'ryr', 'grg', 'xpx', 'ziz', 'cic', 'ala', 'glg', 'ofo', 'ghg', 'xkx', 'pbp', 'ysy', 'cac', 'zez', 'mlm', 'jwj', 'ksk', 'yly', 'oio', 'uqu', 'mdm', 'uru', 'rer', 'ljl', 'fyf', 'hih', 'fgf', 'qyq', 'ggg', 'uiu', 'vav', 'njn', 'qgq', 'ugu', 'mom', 'xex', 'hyh', 'hbh', 'kfk', 'flf', 'afa', 'mqm', 'xgx', 'zgz', 'qfq', 'bnb', 'tbt', 'gqg', 'fof', 'oco', 'ama', 'twt', 'znz', 'rjr', 'gog', 'lhl', 'szs', 'qzq', 'oeo', 'kjk', 'cgc', 'sbs', 'mrm', 'ono', 'rxr', 'ndn', 'pnp', 'gxg', 'fpf', 'nan', 'odo', 'jmj', 'pep', 'sis', 'xhx', 'uou', 'pxp', 'ewe', 'bwb', 'rir', 'pkp', 'igi', 'ibi', 'uhu', 'ifi', 'bxb', 'zxz', 'rqr', 'kpk', 'gng', 'wjw', 'ada', 'hxh', 'wkw', 'xqx', 'fkf', 'ctc', 'oyo', 'faf', 'qtq', 'xxx', 'zjz', 'svs', 'pyp', 'ses', 'sos', 'php', 'pcp', 'kwk', 'xtx', 'lll', 'vzv', 'vyv', 'yjy', 'aha', 'ueu', 'qdq', 'fbf', 'www', 'lwl', 'upu', 'knk', 'oqo', 'udu', 'zsz', 'qcq', 'mnm', 'dsd', 'tet', 'xfx', 'aja', 'gkg', 'xvx', 'iyi', 'opo', 'idi', 'pjp', 'rmr', 'prp', 'sfs', 'cyc', 'aka', 'bfb', 'quq', 'xux', 'nln', 'waw', 'mpm', 'fmf', 'omo', 'ckc', 'ycy', 'xzx', 'sds', 'rar', 'jij', 'yiy', 'khk', 'jyj', 'gyg', 'sjs', 'yfy', 'yvy', 'ava', 'jej', 'vxv', 'vqv', 'ojo', 'oto', 'rvr', 'fzf', 'iwi', 'sxs', 'eoe', 'gjg', 'tot', 'ata', 'kok', 'cdc', 'tgt', 'wzw', 'bkb', 'oso', 'did', 'tst', 'ngn', 'wyw', 'eke', 'qiq', 'ygy', 'gmg', 'vrv', 'ymy', 'mum', 'uzu', 'pmp', 'ppp', 'axa', 'kbk', 'eie', 'rur', 'hkh', 'lgl', 'yky', 'wgw', 'jsj', 'rdr', 'rsr', 'nxn', 'gag', 'sns', 'wqw', 'apa', 'huh', 'xjx', 'oko', 'vov', 'sys', 'ptp', 'cpc', 'rzr', 'drd', 'heh', 'mtm', 'sms', 'wsw', 'ooo', 'eye', 'hzh', 'ana', 'psp', 'rnr', 'tdt', 'qaq', 'wrw', 'cmc', 'zmz', 'qxq', 'lql', 'vgv', 'hhh', 'czc', 'rkr', 'jgj', 'wfw', 'iqi', 'tit', 'ccc', 'zyz', 'qwq', 'yzy', 'vhv', 'dbd', 'yey', 'dwd', 'oro', 'hah', 'sps', 'umu', 'ypy', 'mkm', 'joj', 'zqz', 'kzk', 'lol', 'xsx', 'sss', 'xox', 'zkz', 'nfn', 'hch', 'ktk', 'ouo', 'hfh', 'ili', 'dkd', 'vcv', 'dvd', 'hmh', 'ogo', 'rfr', 'uuu', 'qsq', 'tut', 'ntn', 'gdg', 'jbj', 'jvj', 'sgs', 'xnx', 'jkj', 'iui', 'dzd', 'nkn', 'nbn', 'uyu', 'cqc', 'juj', 'jlj', 'fff', 'ulu', 'lml', 'sls', 'dcd', 'ehe', 'fef', 'gcg', 'dqd', 'gzg', 'kuk', 'zdz', 'wow', 'pzp', 'lul', 'aea', 'fuf', 'bjb', 'csc', 'lxl', 'gig', 'nqn', 'scs', 'nsn', 'dnd', 'tzt', 'vtv', 'hgh', 'ara', 'eve', 'lzl', 'bzb', 'coc', 'zwz', 'tct', 'dmd', 'tmt', 'ele', 'wdw', 'mfm', 'tkt', 'xix', 'viv', 'jcj', 'jrj', 'beb', 'vpv', 'mam', 'kkk', 'fdf', 'vsv', 'gpg', 'yqy', 'btb', 'dod', 'frf', 'hwh', 'zoz', 'gwg', 'kck', 'qpq', 'ftf', 'vnv', 'mzm', 'tft', 'dyd', 'oxo', 'yby', 'qeq', 'sus', 'zbz', 'uau', 'wmw', 'qvq', 'epe', 'fqf', 'efe', 'ese', 'ete', 'kak', 'zpz', 'hoh', 'lfl', 'djd', 'vbv', 'xmx', 'mmm', 'aca', 'iji', 'wtw', 'bgb', 'rgr', 'brb', 'uxu', 'fxf', 'nin', 'qhq', 'nzn', 'uku', 'hth', 'mym', 'fvf', 'kgk', 'exe', 'bpb', 'nen', 'aya', 'fjf', 'hrh', 'bmb', 'ltl', 'crc', 'bab', 'ene', 'nvn', 'kik', 'mgm', 'trt', 'xbx', 'zrz', 'rbr', 'lnl', 'dpd', 'pdp', 'xyx', 'iii', 'nmn', 'ivi', 'bob', 'shs', 'usu', 'zfz', 'vlv', 'klk'}

    return do_test_ex4(alphabet, k, expected)

def test_ex4_4():
    # in
    alphabet = '12345'
    k = 7
    # out
    expected =  {'4412144', '4314134', '3522253', '3244423', '4545454', '5253525', '2433342', '2125212', '4455544', '5522255', '2411142', '3312133', '3554553', '1222221', '3524253', '5231325', '5225225', '5332335', '4311134', '1131311', '1255521', '2534352', '4355534', '1541451', '1443441', '5452545', '4535354', '5124215', '1511151', '5111115', '4513154', '2221222', '4415144', '5523255', '1425241', '3155513', '2412142', '5551555', '1234321', '2541452', '5511155', '1415141', '2511152', '4124214', '3113113', '5234325', '2315132', '3551553', '2142412', '2133312', '3355533', '5534355', '4515154', '3344433', '3345433', '1555551', '3452543', '3213123', '2453542', '2543452', '3315133', '4411144', '2214122', '3521253', '2545452', '4112114', '3221223', '1533351', '3151513', '4242424', '4541454', '4533354', '2542452', '1152511', '1242421', '3322233', '4425244', '3352533', '2522252', '1113111', '5245425', '2353532', '3234323', '1544451', '4551554', '2134312', '4521254', '2155512', '3133313', '3145413', '3533353', '1315131', '1345431', '4424244', '5345435', '2123212', '3555553', '1111111', '5341435', '2351532', '1523251', '1114111', '5445445', '3514153', '2535352', '2352532', '2445442', '2443442', '2243422', '5143415', '3241423', '5235325', '5134315', '1422241', '5211125', '3214123', '1311131', '3143413', '1355531', '3542453', '4512154', '5543455', '4342434', '4452544', '3235323', '2432342', '4132314', '2452542', '3154513', '4353534', '2423242', '2552552', '5251525', '3334333', '4324234', '2311132', '2131312', '5254525', '1521251', '2533352', '1335331', '2512152', '2135312', '4542454', '4443444', '4453544', '4215124', '1512151', '2253522', '1423241', '3525253', '4345434', '3222223', '1514151', '3252523', '4255524', '2212122', '2114112', '3532353', '3512153', '5133315', '3421243', '5532355', '3515153', '5141415', '4232324', '5553555', '4313134', '2515152', '3111113', '2222222', '1551551', '4135314', '5244425', '3255523', '1324231', '3135313', '2215122', '2312132', '3212123', '4544454', '2111112', '1411141', '2233322', '1553551', '1321231', '2531352', '5455545', '2442442', '5513155', '2124212', '4534354', '3313133', '4155514', '5451545', '3233323', '3413143', '3343433', '5442445', '5453545', '4554554', '1351531', '5431345', '2251522', '3142413', '1153511', '5145415', '4531354', '1112111', '3543453', '4325234', '1524251', '5121215', '1235321', '5541455', '1134311', '2255522', '4514154', '2211122', '5334335', '4243424', '2524252', '5154515', '1232321', '4351534', '2231322', '5414145', '2553552', '5255525', '5242425', '1334331', '1313131', '2234322', '3534353', '4234324', '1525251', '1413141', '1211121', '2451542', '4524254', '4115114', '5132315', '2252522', '1453541', '2441442', '5443445', '2143412', '4315134', '4114114', '2141412', '4432344', '3333333', '2152512', '4552554', '1332331', '3342433', '3141413', '4133314', '3444443', '3425243', '3424243', '5123215', '1534351', '1115111', '5545455', '1452541', '5433345', '3125213', '5554555', '4334334', '3324233', '2113112', '5342435', '5415145', '4143414', '1225221', '3325233', '4145414', '1224221', '2554552', '2223222', '5412145', '4123214', '4224224', '2314132', '3112113', '4151514', '4341434', '4134314', '2321232', '4433344', '5514155', '4214124', '2415142', '2333332', '5343435', '3511153', '3332333', '3414143', '4344434', '3353533', '5555555', '5144415', '4423244', '1233321', '3225223', '5422245', '2413142', '1454541', '1123211', '3544453', '1132311', '1322231', '5434345', '3445443', '5142415', '4213124', '4212124', '5224225', '4414144', '5515155', '4245424', '4122214', '1341431', '2454542', '5151515', '3242423', '2151512', '2434342', '4321234', '3152513', '5131315', '3122213', '1543451', '3251523', '5125215', '2421242', '3541453', '5113115', '5213125', '4553554', '1531351', '1143411', '4121214', '5421245', '1435341', '5411145', '4125214', '4223224', '5552555', '3153513', '3254523', '1142411', '1154511', '2254522', '2154512', '5321235', '2241422', '5441445', '4153514', '4354534', '1432341', '3535353', '3351533', '3245423', '1312131', '4222224', '2332332', '3114113', '3314133', '5114115', '4543454', '3123213', '2551552', '5322235', '3455543', '4241424', '2334332', '2112112', '1125211', '2232322', '4251524', '1124211', '3323233', '3422243', '1213121', '4231324', '1314131', '2414142', '5314135', '4211124', '2424242', '3431343', '5112115', '2244422', '5325235', '3341433', '1141411', '4335334', '1532351', '1554551', '4454544', '2431342', '4253524', '5315135', '2354532', '4511154', '1442441', '5212125', '3415143', '1352531', '4244424', '3132313', '1133311', '1144411', '2245422', '1353531', '4142414', '1214121', '2514152', '4421244', '4131314', '4532354', '2425242', '5135315', '5152515', '5223225', '3253523', '5313135', '1412141', '3321233', '3531353', '5525255', '5221225', '2331332', '4333334', '4225224', '3552553', '2555552', '5432345', '2121212', '5232325', '2132312', '4233324', '3412143', '5324235', '2444442', '2224222', '5454545', '1545451', '2344432', '1244421', '5423245', '4441444', '4152514', '4442444', '2521252', '3335333', '5155515', '2335332', '5311135', '5521255', '1252521', '3224223', '4444444', '4235324', '4113114', '5335335', '1342431', '2343432', '5353535', '4141414', '2313132', '3513153', '5355535', '1542451', '3115113', '5524255', '4312134', '5243425', '1354531', '2115112', '1343431', '1344431', '3134313', '4332334', '3331333', '5214125', '3454543', '3553553', '4343434', '5535355', '4352534', '5323235', '2325232', '5331335', '5425245', '2145412', '4144414', '3434343', '1433341', '1421241', '2341432', '5312135', '3144413', '3215123', '4331334', '1122211', '2144412', '3523253', '1241421', '4154514', '5153515', '2213122', '2544452', '1221221', '2122212', '4254524', '1434341', '5544455', '3131313', '4555554', '1455541', '1253521', '1535351', '3411143', '1151511', '1414141', '1145411', '5444445', '4323234', '2513152', '5424245', '5531355', '5352535', '2525252', '5122215', '3545453', '2225222', '1223221', '2322232', '5435345', '3443443', '3451543', '2532352', '1121211', '3223223', '3124213', '4445444', '1325231', '4435344', '2435342', '1331331', '4322234', '5354535', '5344435', '1522251', '5252525', '2523252', '2345432', '1515151', '1254521', '1441441', '3211123', '2422242', '1231321', '4252524', '1155511', '1215121', '5115115', '2342432', '3232323', '5512155', '1445441', '1451541', '2355532', '1513151', '5215125', '4422244', '1243421', '5413145', '2235322', '3442443', '4431344', '5233325', '4413144', '4525254', '3453543', '1251521', '4111114', '3433343', '1323231', '1424241', '5333335', '3311133', '3423243', '1212121', '3231323', '3354533', '4221224', '5533355', '2455542', '2242422', '2153512', '3432343', '3121213', '1431341', '5542455', '4451544', '1245421', '4434344', '3441443', '2324232', '3243423', '1333331', '1552551', '5241425', '1135311', '3435343', '4522254', '1444441', '5222225', '5351535', '4523254', '2323232'}
    
    return do_test_ex4(alphabet, k, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1, test_ex1_2, test_ex1_3,                                # vertex mesh indexing
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4,                    # draw rectangles ona the second diagonal
    test_ex3_1, test_ex3_2, test_ex3_3,                                # search for files containing words
    test_ex4_1, test_ex4_2, test_ex4_3, test_ex4_4,                    # gen mat
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################

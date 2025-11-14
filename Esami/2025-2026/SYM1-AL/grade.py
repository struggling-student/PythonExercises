# -*- coding: utf-8 -*-
import testlib
from testlib import my_print, COL
import sys

import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = True    # with    stack trace of errors
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

def do_func1_tests(a_dict, word, a_dict_exp, expected):
    res = program.func1(a_dict, word)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di chiavi rimosse atteso è {expected} e non {res}. / Removed strings should be {expected}, but {res} were returned.\n {'*'*50}''')
        return 0
    testlib.checkDict(a_dict, a_dict_exp)
    return 1

def test_func1_1():
    '''
    a_dict = {'a':['a','barbagianni','c'], 'b':['a','bifolco'], 'c':['a','c']}
    word = 'b'
    '''
    a_dict = {'a':['a','barbagianni','c'], 'b':['a','bifolco'], 'c':['a','c']}
    word = 'b'
    a_dict_exp = {'c': ['a', 'c']}
    expected = 2
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_2():
    '''
    a_dict = {'a':['a','bordo','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'd'
    '''
    a_dict = {'a':['a','bordo','c'], 'b':['a','b'], 'c':['a','c']}
    word = 'd'
    a_dict_exp = {'b':['a','b'], 'c':['a','c']}
    expected = 1
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_3():
    '''
    a_dict = {'a':['ciccia','b','c'], 'b':['moneta','b'], 'c':['sapone','c']}
    word = 'a'
    '''
    a_dict = {'a':['ciccia','b','c'], 'b':['moneta','b'], 'c':['sapone','c']}
    word = 'a'
    a_dict_exp = {}
    expected = 3
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_4():
    '''
    a_dict = {'capslock'........}
    word = 'hindered'
    '''
    a_dict = {'capslock': ['electrocuted', 'mistake', 'hobbledehoys', 'superadded'],
              'unhindered': ['arts'],
              'backlist': ['unordered', 'hobbledehoys', 'hobbledehoys', 'allegorizes', 'mistake', 'hobbledehoys', 'unhindered'],
              'arts': ['unhindered', 'superadded'],
              'games': ['unhindered', 'games', 'parasol'],
              'parasol': ['futons', 'allegorizes', 'prevaricate'],
              'philters': ['unordered', 'mistake', 'allegorizes', 'futons'],
              'hobbledehoys': ['electrocuted', 'unhindered', 'backlist', 'mdv', 'objectiveness', 'games', 'capslock'],
              'mdv': ['disgusting', 'prated', 'hobbledehoys', 'philters', 'allegorizes', 'disgusting'],
              'prated': ['capslock', 'hobbledehoys', 'unreleased'],
              'futons': ['unhindered', 'objectiveness', 'parasol', 'disgusting', 'electrocuted'],
              'electrocuted': ['hobbledehoys', 'objectiveness', 'philters', 'backlist', 'philters', 'parasol'],
              'prevaricate': ['superadded', 'hobbledehoys', 'allegorizes', 'mistake', 'mdv', 'capslock'],
              'mistake': ['backlist', 'electrocuted'],
              'objectiveness': ['mistake', 'superadded', 'hobbledehoys', 'allegorizes'],
              'allegorizes': ['allegorizes', 'superadded', 'mistake'],
              'disgusting': ['unhindered', 'futons'],
              'unordered': ['backlist', 'mistake', 'parasol', 'mistake', 'backlist'],
              'unreleased': ['prated', 'unordered', 'mdv'],
              'superadded': ['mdv', 'hobbledehoys', 'disgusting']}
    word = 'hindered'
    a_dict_exp = {'capslock': ['electrocuted', 'mistake', 'hobbledehoys', 'superadded'],
              'unhindered': ['arts'],
              'parasol': ['futons', 'allegorizes', 'prevaricate'],
              'philters': ['unordered', 'mistake', 'allegorizes', 'futons'],
              'mdv': ['disgusting', 'prated', 'hobbledehoys', 'philters', 'allegorizes', 'disgusting'],
              'prated': ['capslock', 'hobbledehoys', 'unreleased'],
              'electrocuted': ['hobbledehoys', 'objectiveness', 'philters', 'backlist', 'philters', 'parasol'],
              'prevaricate': ['superadded', 'hobbledehoys', 'allegorizes', 'mistake', 'mdv', 'capslock'],
              'mistake': ['backlist', 'electrocuted'],
              'objectiveness': ['mistake', 'superadded', 'hobbledehoys', 'allegorizes'],
              'allegorizes': ['allegorizes', 'superadded', 'mistake'],
              'unordered': ['backlist', 'mistake', 'parasol', 'mistake', 'backlist'],
              'unreleased': ['prated', 'unordered', 'mdv'],
              'superadded': ['mdv', 'hobbledehoys', 'disgusting']}
    expected = 6
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

###########################################################################################################################

def do_func2_tests(dictionary, expected):
    res = program.func2(dictionary)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista ritornata è sbagliata! / The returned list is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func2_1():
    dictionary = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}
    expected = [('c', 'h'), ('b', 'w'), ('b', 'a')]
    return do_func2_tests(dictionary, expected)

def test_func2_2():
    dictionary = {1: ["c", "h", "f", "g", "e"], 0: ["a", "z", "b", "w"], 2: ["a", "b", "a"]}
    expected = [('g', 'e'), ('z', 'a'), ('a', 'b')]
    return do_func2_tests(dictionary, expected)

def test_func2_3():
    dictionary = {0: ["ball", "bike", "blue"], 1: ["bike", "ball", "blue"], 2: ["blue", "bike", "ball"]}
    expected = [('blue', 'ball'), ('bike', 'bike'), ('ball', 'blue')]
    return do_func2_tests(dictionary, expected)

def test_func2_4():
    dictionary = {0: ["ball", "bike", "blue"], 1: ["cat", "cube", "coat"], 2: ["dog", "day", "data"]}
    expected = [('blue', 'ball'), ('coat', 'coat'), ('data', 'dog')]
    return do_func2_tests(dictionary, expected)

###########################################################################################################################

def do_func3_tests(a_list,expected):
    res = program.func3(a_list)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}\nexpected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func3_1():
    a_list = ["monkey", "cat", "panda", "boy", "alligator"]
    expected = [959, 659, 516, 330, 312]
    return do_func3_tests(a_list, expected)

def test_func3_2():
    a_list = strList = ["Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Ape", "Armadillo", "Donkey", "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bison", "Boar", "Buffalo", "Butterfly", "Camel", "Capybara", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cattle", "Chamois", "Cheetah", "Chicken", "Chimpanzee", "Chinchilla", "Chough", "Clam", "Cobra", "Cockroach", "Cod", "Cormorant", "Coyote", "Crab", "Crane", "Crocodile", "Crow", "Curlew", "Deer", "Dinosaur", "Dog", "Dogfish", "Dolphin", "Dotterel", "Dove", "Dragonfly", "Duck", "Dugong", "Dunlin", "Eagle", "Echidna", "Eel", "Eland", "Elephant", "Elk", "Emu", "Falcon", "Ferret", "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gaur", "Gazelle", "Gerbil", "Giraffe", "Gnat", "Gnu", "Goat", "Goldfinch", "Goldfish", "Goose", "Gorilla", "Goshawk", "Grasshopper", "Grouse", "Guanaco", "Gull", "Hamster", "Hare", "Hawk", "Hedgehog", "Heron", "Herring", "Hippopotamus", "Hornet", "Horse", "Human", "Hummingbird", "Hyena", "Ibex", "Ibis", "Jackal", "Jaguar", "Jay", "Jellyfish", "Kangaroo", "Kingfisher", "Koala", "Kookabura", "Kouprey", "Kudu", "Lapwing", "Lark", "Lemur", "Leopard", "Lion", "Llama", "Lobster", "Locust", "Loris", "Louse", "Lyrebird", "Magpie", "Mallard", "Manatee", "Mandrill", "Mantis", "Marten", "Meerkat", "Mink", "Mole", "Mongoose", "Monkey", "Moose", "Mosquito", "Mouse", "Mule", "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi", "Opossum", "Oryx", "Ostrich", "Otter", "Owl", "Oyster", "Panther", "Parrot", "Partridge", "Peafowl", "Pelican", "Penguin", "Pheasant", "Pig", "Pigeon", "Pony", "Porcupine", "Porpoise", "Quail", "Quelea", "Quetzal", "Rabbit", "Raccoon", "Rail", "Ram", "Rat", "Raven", "Red deer", "Red panda", "Reindeer", "Rhinoceros", "Rook", "Salamander", "Salmon", "Sand Dollar", "Sandpiper", "Sardine", "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Shrew", "Skunk", "Snail", "Snake", "Sparrow", "Spider", "Spoonbill", "Squid", "Squirrel", "Starling", "Stingray", "Stinkbug", "Stork", "Swallow", "Swan", "Tapir", "Tarsier", "Termite", "Tiger", "Toad", "Trout", "Turkey", "Turtle", "Viper", "Vulture", "Wallaby", "Walrus", "Wasp", "Weasel", "Whale", "Wildcat", "Wolf", "Wolverine", "Wombat", "Woodcock", "Woodpecker", "Worm", "Wren", "Yak", "Zebra"]
    expected = [1289, 1139, 1166, 1142, 1130, 1028, 1028, 1007, 1034, 1052, 1016, 1043, 939, 927, 917, 901, 961, 956, 909, 949, 916, 934, 910, 938, 927, 930, 949, 831, 934, 946, 955, 812, 820, 824, 803, 837, 835, 817, 813, 816, 795, 818, 829, 819, 839, 865, 820, 849, 731, 814, 845, 826, 855, 836, 849, 839, 825, 703, 709, 708, 690, 693, 708, 718, 684, 708, 692, 714, 724, 702, 724, 719, 751, 722, 711, 731, 701, 699, 713, 717, 749, 758, 732, 722, 718, 700, 726, 742, 709, 710, 750, 745, 730, 730, 759, 716, 712, 578, 593, 581, 597, 605, 606, 627, 626, 618, 612, 618, 595, 616, 597, 629, 624, 582, 602, 634, 595, 620, 615, 627, 646, 632, 610, 605, 596, 618, 615, 644, 640, 638, 609, 618, 507, 482, 487, 489, 478, 484, 488, 509, 508, 513, 505, 501, 488, 517, 487, 521, 520, 515, 521, 500, 526, 508, 508, 505, 501, 521, 524, 503, 498, 518, 531, 512, 507, 542, 518, 497, 500, 378, 388, 381, 376, 411, 384, 398, 391, 394, 398, 399, 394, 395, 404, 384, 395, 392, 391, 409, 394, 402, 399, 397, 403, 414, 434, 422, 392, 411, 389, 409, 392, 411, 408, 421, 412, 291, 278, 279, 268, 280, 278, 282, 278, 284, 295, 299, 301, 298, 292, 306, 288, 288, 295, 293]
    return do_func3_tests(a_list, expected)

def test_func3_3():
    a_list = "lorem ipsum dolor sit amet Roma".split()
    expected = [544, 558, 543, 399, 423, 336]
    return do_func3_tests(a_list, expected)

def test_func3_4():
    a_list = map(str, list(range(1, 50)))
    expected = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    return do_func3_tests(a_list, expected)

###########################################################################################################################

def do_func4_tests(string_list1, string_list2, expected):
    res = program.func4(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 1.5

def test_func4_1():
    '''
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark']
    expected = ['elichopter','park', 'shop']
    '''
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark']
    expected = ['elichopter','park', 'shop']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_2():
    '''
    string_list1=['fig', 'hoy', 'ids', 'save', 'roe', 'detersive', 'list']
    string_list2=['devastatingly', 'strategists', 'formalist']
    expected = ['formalist']
    '''
    string_list1=['fig', 'hoy', 'ids', 'save', 'roe', 'detersive', 'list']
    string_list2=['devastatingly', 'strategists', 'formalist']
    expected = ['formalist']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_3():
    '''
    string_list1=['succouring', 'compartmental', 'sour', 'varityped', 'go', 'fulmination', 'wilfulness', 'dangerous', 'subtracting', 'fragmented', 'preciseness', 'rem', 'hypnotically']
    string_list2=['hartebeests', 'absorbencies', 'straitening', 'precise', 'saragossa', 'enumerates', 'regna', 'margarines', 'invigilates', 'maladapted', 'prosperous', 'capitalize']
    expected = ['preciseness', 'saragossa']
    '''
    string_list1=['succouring', 'compartmental', 'sour', 'varityped', 'go', 'fulmination', 'wilfulness', 'dangerous', 'subtracting', 'fragmented', 'preciseness', 'rem', 'hypnotically']
    string_list2=['hartebeests', 'absorbencies', 'straitening', 'precise', 'saragossa', 'enumerates', 'regna', 'margarines', 'invigilates', 'maladapted', 'prosperous', 'capitalize']
    expected = ['preciseness', 'saragossa']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_4():
    '''
    string_list1=['succouring', 'compartmental', 'sour', 'varityped', 'go', 'fulmination', 'wilfulness', 'dangerous', 'subtracting', 'fragmented', 'preciseness', 'rem', 'hypnotically']
    string_list2=['hartebeests', 'absorbencies', 'straitening', 'precise', 'saragossa', 'enumerates', 'regna', 'margarines', 'invigilates', 'maladapted', 'prosperous', 'capitalize']
    expected = ['hierarchy']
    '''
    string_list1=['surface', 'chaplain', 'participant', 'association', 'criteria', 'conversation', 'kindness', 'embellishment', 'brandy', 'yourself', 'manipulate', 'stuff', 'thoughtless', 'patient', 'unusual', 'spending', 'large', 'opposite', 'reelging', 'eternity', 'verification', 'hierarchy', 'hospice', 'softening', 'suggestion', 'bitten', 'page', 'tech', 'carry', 'horse', 'meander', 'filing', 'small', 'breakpoint', 'espadrille', 'entrepreneur', 'minority', 'billing', 'mound', 'place', 'linguistics']
    string_list2=['give', 'tangy', 'ruin', 'perch', 'metro', 'wed', 'tool', 'silk', 'buy', 'jot', 'alive', 'jelly', 'chase', 'spat', 'cacao', 'wit', 'toot', 'fairy', 'clerk', 'epee', 'crack', 'poll', 'monk', 'era', 'shoe', 'dawn', 'panda', 'robe', 'hotel', 'medal', 'drink', 'glee', 'colon', 'star', 'arrowhcets','wound', 'area', 'id', 'ark', 'ego', 'myth', 'noir', 'berry', 'spud', 'iron', 'maize', 'shade', 'blood', 'mist', 'wee', 'rhyme', 'flax', 'agegap', 'probe', 'tired', 'win', 'pool', 'leg', 'SUV', 'tide', 'knit']
    expected = ['hierarchy']
    return do_func4_tests(string_list1, string_list2, expected)

###########################################################################################################################

def do_func5(points, expected):
    res = program.func5(points)
    if res != expected:
        my_print(f'''{'*' * 50}\n[ERROR] La tupla ritornata è sbagliata! / The returned tuple is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*' * 50}''')
        return 0
    return 2

def test_func5_1():
    points = [(2, 2), (-1, 1), (3, 0), (-3, -2), (2, -1)]
    expected = (0.667, 0.0)
    return do_func5(points, expected)

def test_func5_2():
    points = [(-10, 2), (2, 0), (2, 5), (-2, 2), (0, -7), (-2, -2)]
    expected = (-2.667, 0.0)
    return do_func5(points, expected)

def test_func5_3():
    points = [(x, -2*x) for x in range(1, 10)]
    expected = (8.0, -16.0)
    return do_func5(points, expected)

def test_func5_4():
    points = [(x*x, -x) for x in range(1, 10)]
    expected = (64.667, -8.0)
    return do_func5(points, expected)

###########################################################################################################################

def do_func6_tests(text, expected):
    res = program.func6(text)

    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        if type(res) == dict:
            for k in expected:
                if expected[k] != res[k]:
                    my_print(f'''[ERROR] Ad esempio, il carattere {k} si trova in {expected[k]} parole invece che in {res[k]}.''')
                    my_print(f'''[ERROR] For example, char {k} appears in {expected[k]} words instead than in {res[k]}.''')
                    break
        return 0
    return 1

def test_func6_1():
    '''
    testo = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
    expected   = {'P': 6, 'L': 8, 'C': 6, 'S': 10}
    '''
    text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
    expected = {'P': 6, 'L': 8, 'C': 6, 'S': 10}
    return do_func6_tests(text, expected)

def test_func6_2():
    '''
    text = 'Nel Mezzo del caMmin Di nostra vita mi ritrovai in una selva oscura che la diritta via era smarrita'
    expected   = {'L': 15, 'U': 17, 'I': 10, 'D': 16, 'E': 13, 'C': 16, 'R': 13, 'V': 15, 'N': 14, 'O': 15, 'M': 15, 'S': 15}
    '''
    text = 'Nel Mezzo del caMmin Di nostra vita mi Ritrovai in una selva oscura che la diritta via era smarrita'
    expected = {'L': 15, 'U': 17, 'I': 10, 'D': 16, 'E': 13, 'C': 16, 'R': 13, 'V': 15, 'N': 14, 'O': 15, 'M': 15, 'S': 15}
    return do_func6_tests(text, expected)

def test_func6_3():
    '''
    text = 'To be or not to be that is the question Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles And by opposing end them'
    expected = {'W': 37, 'M': 36, 'N': 27, 'F': 35, 'O': 23, 'A': 29, 'S': 27, 'I': 31, 'B': 34, 'E': 23, 'Q': 38, 'T': 21}
    '''
    text = 'To be or not to be that is the question Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles And by opposing end them'
    expected = {'W': 37, 'M': 36, 'N': 27, 'F': 35, 'O': 23, 'A': 29, 'S': 27, 'I': 31, 'B': 34, 'E': 23, 'Q': 38, 'T': 21}
    return do_func6_tests(text, expected)

def test_func6_4():
    text = 'FAR Out in THe unchArTEd baCKwaTers Of the uNFashIonaBlE End Of tHE westeRn SpirAl ARm of tHe GalaXY liEs A SMaLl UnrEgarded yelLow sUn OrbItiNg this at A DISTaNce OF rOUGHlY nINEtY TWO miLLioN Miles IS an utTerLy iNSiGnifIcAnt lITtle Blue greeN pLaneT whOse APE deSCenDeD lIfE forMS Are SO aMAZinglY prImitivE thaT tHeY sTill thiNk DigITal WAtcheS aRE A preTTy nEat IDEA This plaNet HAs or RAthEr HaD A probleM WHiCh wAs tHis mOSt Of thE peOple on It Were unHappy for PRETty mUcH OF the tIMe MAnY sOluTIonS Were suggEsTEd FOr THiS prOBLem buT most of These weRe lArGeLy COncERNEd WIth the MoVements oF smAlL GrEeN pieceS of pAPeR WhICh iS odD becaUse on tHe WhOLe It WASN t the SmaLL GReeN piEcEs oF paper tHAt Were uNHaPPY And SO the PrObLEm remaINeD LotS of ThE pEOpLe weRe meaN aNd mOst oF them weRe mIsErAble even tHe ONES WITh DIgital WaTches MAny weRE iNcReasiNgly of thE oPiNIoN that they D aLL madE A bIg MistAKe iN coMIng dOwn from the treEs in The firST PLace AND sOMe saiD THAt EVeN tHE trEEs HAd BEen A bad move and thAT no onE shoUld ever hAve LEft tHe ocEAns And THEn oNe ThUrSDAY NeArLY twO ThouSAND yearS afTeR ONE mAn HaD BEen NaIled to a tREE for sAying hOw greAt It woulD bE To be nIce to peOpLe FoR a CHangE oNe girL SiTtINg on hEr owN in A sMAlL CAfE in RICkmansWorth sUdDeNly rEaliZed WHAT it Was that haD BeEN GoING wroNG ALL This TiME aNd sHe FinaLly knEw hOw tHe WoRLd cOulD be MAdE A gOOD aNd hapPy pLAcE THiS TimE it waS Right IT WOUld WoRK and nO oNE Would hAvE to GEt naiLed to ANyThIng SaDly hOweVER BEfORe sHe Could gEt tO a pHone to TELL anyonE about iT A terriblY sTuPID CatAstrOPHe OcCUrrED aND the idEa wAs lOsT FOREvEr ThiS iS noT hEr sTOrY'
    expected = {'N': 232, 'M': 283, 'S': 246, 'H': 241, 'Y': 291, 'L': 262, 'U': 292, 'O': 222, 'K': 313, 'G': 291, 'P': 293, 'B': 298, 'E': 175, 'T': 203, 'A': 206, 'C': 292, 'I': 245, 'R': 250, 'D': 270, 'W': 280, 'F': 289}
    return do_func6_tests(text, expected)

###########################################################################################################################

tests = [
    # TO DISABLE SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4, # OK 4
    test_func2_1, test_func2_2, test_func2_3, test_func2_4, # OK 4
    test_func3_1, test_func3_2, test_func3_3, test_func3_4, # OK 4
    test_func4_1, test_func4_2, test_func4_3, test_func4_4, # OK 6
    test_func5_1, test_func5_2, test_func5_3, test_func5_4, # OK 8
    test_func6_1, test_func6_2, test_func6_3, test_func6_4, # OK 4
    test_personal_data_entry,
]

if __name__ == '__main__':
    test_personal_data_entry()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################

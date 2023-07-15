# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program



def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['BOLD']+COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['BOLD']+COL['RED']
        if col:
            return func(f'{col}', *args, f'{COL["RST"]}{COL["ENDC"]}',
                        **kwargs, )
        else:
            return func(*args, **kwargs, )
    return wrapped_func

my_print = my_decorator(print)

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
DEBUG = True
#DEBUG = False
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
    return 1e-9

###############################################################################


def do_func1_tests(dictionary, expected):
    res = program.func1(dictionary)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista ritornata è sbagliata! / The returned list is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func1_1():
    dictionary = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}
    expected = ["c", "b", "b"]
    return do_func1_tests(dictionary, expected)

def test_func1_2():
    dictionary = {1: ["c", "h", "f", "g", "e"], 0: ["a", "z", "b", "w"], 2: ["a", "b", "a"]}
    expected = ['g', 'z', 'a']
    return do_func1_tests(dictionary, expected)

def test_func1_3():
    dictionary = {0: ["ball", "bike", "blue"], 1: ["bike", "ball", "blue"], 2: ["blue", "bike", "ball"]}
    expected = ['blue', 'bike', 'ball']
    return do_func1_tests(dictionary, expected)

def test_func1_4():
    dictionary = {0: ["ball", "bike", "blue"], 1: ["cat", "cube", "coat"], 2: ["dog", "day", "data"]}
    expected = ['blue', 'coat', 'data']
    return do_func1_tests(dictionary, expected)

def do_func2_tests(list_all, list_rm, expected):
    program.func2(list_all, list_rm)

    if list_all != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista è stata modificata in modo sbagliato! / The list was not changed as expected!\nChanged list={list_all}, expected list={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func2_1():
    list_all = [2, 4, 3, 4, 4, 3, 4, 5, 2, 6]
    list_rm = [5, 3, 2, 7]
    expected = [2, 3, 5]
    return do_func2_tests(list_all, list_rm, expected)

def test_func2_2():
    list_all = list(range(100))
    list_rm = [-1]
    expected = []
    return do_func2_tests(list_all, list_rm, expected)

def test_func2_3():
    list_all = list(range(100))
    list_rm = list(range(-100, 99))
    expected = list(range(99))
    return do_func2_tests(list_all, list_rm, expected)

def test_func2_4():
    list_all = list(range(100))
    list_rm = list(range(-100, 100, 2))
    expected = list(range(0, 100, 2))
    return do_func2_tests(list_all, list_rm, expected)


def do_func3_tests(a_list,expected):
    res = program.func3(a_list)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func3_1():
    a_list = ["monkey", "cat", "panda", "alligator"]
    expected = [959, 312, 659, 516]
    return do_func3_tests(a_list, expected)

def test_func3_2():
    a_list = strList = [
        "Aardvark",
        "Albatross",
        "Alligator",
        "Alpaca",
        "Ant",
        "Anteater",
        "Antelope",
        "Ape",
        "Armadillo",
        "Donkey",
        "Baboon",
        "Badger",
        "Barracuda",
        "Bat",
        "Bear",
        "Beaver",
        "Bee",
        "Bison",
        "Boar",
        "Buffalo",
        "Butterfly",
        "Camel",
        "Capybara",
        "Caribou",
        "Cassowary",
        "Cat",
        "Caterpillar",
        "Cattle",
        "Chamois",
        "Cheetah",
        "Chicken",
        "Chimpanzee",
        "Chinchilla",
        "Chough",
        "Clam",
        "Cobra",
        "Cockroach",
        "Cod",
        "Cormorant",
        "Coyote",
        "Crab",
        "Crane",
        "Crocodile",
        "Crow",
        "Curlew",
        "Deer",
        "Dinosaur",
        "Dog",
        "Dogfish",
        "Dolphin",
        "Dotterel",
        "Dove",
        "Dragonfly",
        "Duck",
        "Dugong",
        "Dunlin",
        "Eagle",
        "Echidna",
        "Eel",
        "Eland",
        "Elephant",
        "Elk",
        "Emu",
        "Falcon",
        "Ferret",
        "Finch",
        "Fish",
        "Flamingo",
        "Fly",
        "Fox",
        "Frog",
        "Gaur",
        "Gazelle",
        "Gerbil",
        "Giraffe",
        "Gnat",
        "Gnu",
        "Goat",
        "Goldfinch",
        "Goldfish",
        "Goose",
        "Gorilla",
        "Goshawk",
        "Grasshopper",
        "Grouse",
        "Guanaco",
        "Gull",
        "Hamster",
        "Hare",
        "Hawk",
        "Hedgehog",
        "Heron",
        "Herring",
        "Hippopotamus",
        "Hornet",
        "Horse",
        "Human",
        "Hummingbird",
        "Hyena",
        "Ibex",
        "Ibis",
        "Jackal",
        "Jaguar",
        "Jay",
        "Jellyfish",
        "Kangaroo",
        "Kingfisher",
        "Koala",
        "Kookabura",
        "Kouprey",
        "Kudu",
        "Lapwing",
        "Lark",
        "Lemur",
        "Leopard",
        "Lion",
        "Llama",
        "Lobster",
        "Locust",
        "Loris",
        "Louse",
        "Lyrebird",
        "Magpie",
        "Mallard",
        "Manatee",
        "Mandrill",
        "Mantis",
        "Marten",
        "Meerkat",
        "Mink",
        "Mole",
        "Mongoose",
        "Monkey",
        "Moose",
        "Mosquito",
        "Mouse",
        "Mule",
        "Narwhal",
        "Newt",
        "Nightingale",
        "Octopus",
        "Okapi",
        "Opossum",
        "Oryx",
        "Ostrich",
        "Otter",
        "Owl",
        "Oyster",
        "Panther",
        "Parrot",
        "Partridge",
        "Peafowl",
        "Pelican",
        "Penguin",
        "Pheasant",
        "Pig",
        "Pigeon",
        "Pony",
        "Porcupine",
        "Porpoise",
        "Quail",
        "Quelea",
        "Quetzal",
        "Rabbit",
        "Raccoon",
        "Rail",
        "Ram",
        "Rat",
        "Raven",
        "Red deer",
        "Red panda",
        "Reindeer",
        "Rhinoceros",
        "Rook",
        "Salamander",
        "Salmon",
        "Sand Dollar",
        "Sandpiper",
        "Sardine",
        "Scorpion",
        "Seahorse",
        "Seal",
        "Shark",
        "Sheep",
        "Shrew",
        "Skunk",
        "Snail",
        "Snake",
        "Sparrow",
        "Spider",
        "Spoonbill",
        "Squid",
        "Squirrel",
        "Starling",
        "Stingray",
        "Stinkbug",
        "Stork",
        "Swallow",
        "Swan",
        "Tapir",
        "Tarsier",
        "Termite",
        "Tiger",
        "Toad",
        "Trout",
        "Turkey",
        "Turtle",
        "Viper",
        "Vulture",
        "Wallaby",
        "Walrus",
        "Wasp",
        "Weasel",
        "Whale",
        "Wildcat",
        "Wolf",
        "Wolverine",
        "Wombat",
        "Woodcock",
        "Woodpecker",
        "Worm",
        "Wren",
        "Yak",
        "Zebra"
    ]
    expected = [812, 939, 927, 578, 291, 820, 824, 278, 917, 593, 581, 901, 279, 378, 597, 268, 507, 388, 703, 961, 482, 803, 709, 956, 280, 1139, 605, 708, 690, 693, 1028, 1007, 606, 381, 487, 909, 278, 949, 627, 376, 489, 916, 411, 626, 384, 837, 282, 708, 718, 618, 835, 398, 934, 391, 612, 618, 478, 684, 278, 484, 817, 284, 295, 595, 616, 488, 394, 813, 299, 301, 398, 399, 708, 597, 692, 394, 298, 395, 910, 816, 509, 714, 724, 1166, 629, 702, 404, 724, 384, 395, 795, 508, 719, 1289, 624, 513, 505, 1142, 501, 392, 391, 582, 602, 292, 938, 818, 1034, 488, 927, 751, 409, 722, 394, 517, 711, 402, 487, 731, 634, 521, 520, 829, 595, 701, 699, 819, 620, 615, 713, 399, 397, 839, 627, 515, 865, 521, 403, 717, 414, 1130, 749, 500, 758, 434, 732, 526, 306, 646, 722, 632, 930, 718, 700, 726, 820, 288, 610, 422, 949, 849, 508, 605, 742, 596, 709, 392, 288, 295, 508, 731, 831, 814, 1052, 411, 1016, 618, 1028, 934, 710, 845, 826, 389, 505, 501, 521, 524, 503, 498, 750, 615, 946, 518, 855, 836, 849, 839, 531, 745, 409, 512, 730, 730, 507, 392, 542, 644, 640, 518, 759, 716, 638, 411, 609, 497, 712, 408, 955, 618, 825, 1043, 421, 412, 293, 500]
    return do_func3_tests(a_list, expected)

def test_func3_3():
    a_list = list("lorem ipsum dolor sit amet")
    expected = [32, 32, 32, 32, 97, 100, 101, 101, 105, 105, 108, 108, 109, 109, 109, 111, 111, 111, 112, 114, 114, 115, 115, 116, 116, 117]
    return do_func3_tests(a_list, expected)

def test_func3_4():
    a_list = map(str, list(range(1, 100)))
    expected = [49, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 50, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 51, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 52, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 53, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 54, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 55, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 56, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 57, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]
    return do_func3_tests(a_list, expected)


# ----------------------------------- EX.1 ----------------------------------- #


def do_func4_tests(a_list,expected):
    res = program.func4(a_list)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1


def test_func4_1():
    a_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
    expected = 21600
    return do_func4_tests(a_list, expected)

def test_func4_2():
    a_list = [[1, 2, 3, 4] for x in range(10)]
    expected = 10000240000
    return do_func4_tests(a_list, expected)

def test_func4_3():
    a_list = [[x for x in range(10)] for x in range(2)]
    expected = 2025
    return do_func4_tests(a_list, expected)

def test_func4_4():
    a_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
    expected = 21600
    return do_func4_tests(a_list, expected)

def test_func4_5():
    a_list = [[1 for x in range(5)] for x in range(2)]
    expected = 57
    return do_func4_tests(a_list, expected)

def do_test_func5(points, expected):
    res = program.func5(points)
    if res != expected:
        my_print(f'''{'*' * 50}\n[ERROR] La tupla ritornata è sbagliata! / The returned tuple is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*' * 50}''')
        return 0
    return 1.5


def test_func5_1():
    points = [(2, 2), (-1, 1), (3, 0), (3, 2), (2, -1)]
    expected = (1.0, 0.667)
    return do_test_func5(points, expected)


def test_func5_2():
    points = [(0, 2), (2, 0), (2, 2), (-2, 0), (0, -2), (-2, -2)]
    expected = (0.0, 0.667)
    return do_test_func5(points, expected)


def test_func5_3():
    points = [(x, x) for x in range(1, 10)]
    expected = (2.0, 2.0)
    return do_test_func5(points, expected)


def test_func5_4():
    points = [(x, -x) for x in range(1, 10)]
    expected = (2.0, -2.0)
    return do_test_func5(points, expected)

# ----------------------------------- EX. 1----------------------------------- #
def do_ex1_test(root, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            res = []
            program.ex1(root, res)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = []
    program.ex1(root, res)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è corretto! / The returned value is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    return 2


def test_ex1_1():
    '''
    ______5______
   |             |
   8__        ___2___
      |      |       |
      3      9       1
    '''
    root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    expected = [5, 10, 13]
    return do_ex1_test(root, expected)

def test_ex1_2():
    '''
        ______2______
       |             |
    __ 7__        ___5___
   |      |      |       |
  _4_     3_    _0_     _5_
 |   |      |  |   |   |   |
 2   -1     1  8   3   2   9
    '''
    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    expected =  [2, 12, 12, 24]
    return do_ex1_test(root, expected)


def test_ex1_3():
    '''
    A big tree
    '''
    root = tree.BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    expected = [-2, 25, 28, 58, 41, 213, 339, 644, 535, 551, 624, 425, 25, 12]
    return do_ex1_test(root, expected)


# ----------------------------------- EX.2 ----------------------------------- #
def do_ex2_test(directory, words, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(directory, words)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(directory, words)
    if res is None: return 0
    if res == expected:
        return 3
    if set(res) == set(expected):
        return 2
    my_print(
        f'''{'*' * 50}\n[ERROR]La lista ritornata non è corretta! / The returned list is incorrect!!\nReturned={res}, expected={expected}''')
    return 0

def test_ex2_1():
    directory = 'ex2'
    words = ["cat", "dog"]
    expected = [('dog', 10), ('cat', 5)]
    return do_ex2_test(directory, words, expected)


def test_ex2_2():
    directory = 'ex2/A'
    words = ["gnu", "cat", "fish"]
    expected = [('cat', 3), ('fish', 3),  ('gnu', 1)]
    return do_ex2_test(directory, words, expected)


def test_ex2_3():
    directory = 'ex2'
    words = ["bird", "dog", "gnu", "tuna"][::-1]
    expected = [('dog', 10), ('bird', 8), ('tuna', 2), ('gnu', 1)]
    return do_ex2_test(directory, words, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4, test_func4_5,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,   test_ex1_2, test_ex1_3,
    test_ex2_1, test_ex2_2, test_ex2_3,
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
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['BOLD']+COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
################################################################################

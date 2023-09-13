# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import nary_tree
from testlib import my_print, COL


############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print(  'WARNING: Save program.empty.py as program.py\n'
            'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

def test_personal_data_entry():
    non_filled = {
        'nome': ['nome', 'cognome', 'matricola' ],
        'name': ['name', 'surname', 'student_id']
    }
    for tag, vars in non_filled.items():
        if tag in program.__dict__:
            for v in vars:
                if getattr(program, v, v.upper()) == v.upper():
                    print(
                        f"{COL['RED']}ERROR: Please assign the '{v}' variable with YOUR {v.upper()} in program.py{COL['RST']}")
                    return -32 # se una var manca
            return 0 # se per una lingua tutto OK
    return -32       # se nessuna lingua OK

# ----------------------------------- FUNC. 1 ----------------------------------- #

def do_func1_tests(diz1, diz2, expected):
    res = program.func1(diz1, diz2)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dict is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 0.5


def test_func1_1():
    '''
    diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
    expected = {1: ['bc', 'cd', 'f'], 3: ['qrt', 'bn', 'st', 'c']}
    '''
    diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
    expected = {1: ['bc', 'cd', 'f'], 3: ['qrt', 'bn', 'st', 'c']}
    return do_func1_tests(diz1, diz2, expected)

def test_func1_2():
    '''
    diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 1: ['a', 'cd', 'f'], 2: ['b', 'cr', 'e'], 8: ['a', 'bn', 'c'] }
    expected = {1: ['bc', 'cd', 'f'], 2: []}
    '''
    diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 1: ['a', 'cd', 'f'], 2: ['b', 'cr', 'e'], 8: ['a', 'bn', 'c'] }
    expected = {1: ['bc', 'cd', 'f'], 2: []}
    return do_func1_tests(diz1, diz2, expected)

def test_func1_3():
    '''
    diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 4: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 6: ['a', 'bn', 'c'] }
    expected = {}
    '''
    diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 4: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 6: ['a', 'bn', 'c'] }
    expected = {}
    return do_func1_tests(diz1, diz2, expected)

def test_func1_4():
    '''
    diz1 = { 1: ['a', 'bc', 'a', 'sei', 'nove', 'q' ], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 1: ['a', 'cd', 'f', 'be', 'tre', 'otto'], -1: ['b', 'cr', 'e'], 6: ['a', 'bn', 'c'] }
    expected = {1: ['nove', 'otto', 'sei', 'tre', 'bc', 'be', 'cd', 'f', 'q']}
    '''
    diz1 = { 1: ['a', 'bc', 'a', 'sei', 'nove', 'q' ], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
    diz2 = { 1: ['a', 'cd', 'f', 'be', 'tre', 'otto'], -1: ['b', 'cr', 'e'], 6: ['a', 'bn', 'c'] }
    expected = {1: ['nove', 'otto', 'sei', 'tre', 'bc', 'be', 'cd', 'f', 'q']}
    return do_func1_tests(diz1, diz2, expected)

# ----------------------------------- FUNC. 2 ----------------------------------- #

def do_func2_tests(text, expected):
    res = program.func2(text)

    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        if type(res) == dict:
            for k in expected:
                if expected[k] != res[k]:
                    my_print(f'''[ERROR] Ad esempio, il carattere {k} si trova in {expected[k]} parole invece che in {res[k]}.''')
                    my_print(f'''[ERROR] For example, char {k} appears in {expected[k]} words instead than in {res[k]}.''')
                    break
        return 0
    return 0.5


def test_func2_1():
    '''
    testo = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
    expected   = { 's':2, 'l':4, 'p':6, 'c':6}
    '''
    text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
    expected = {'s': 2, 'l': 4, 'p': 6, 'c': 6}
    return do_func2_tests(text, expected)

def test_func2_2():
    '''
    text = 'Nel Mezzo del caMmin Di nostra vita mi ritrovai in una selva oscura che la diritta via era smarrita'
    expected   = {'n': 5, 'm': 4, 'd': 3, 'c': 3, 'v': 4, 'r': 6, 'i': 9, 'u': 2, 's': 4, 'o': 4, 'l': 4, 'e': 6}
    '''
    text = 'Nel Mezzo del caMmin Di nostra vita mi Ritrovai in una selva oscura che la diritta via era smarrita'
    expected = {'n': 5, 'm': 4, 'd': 3, 'c': 3, 'v': 4, 'r': 6, 'i': 9, 'u': 2, 's': 4, 'o': 4, 'l': 4, 'e': 6}
    return do_func2_tests(text, expected)

def test_func2_3():
    '''
    text = 'To be or not to be that is the question Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles And by opposing end them'
    expected = {'t': 18, 'b': 5, 'o': 16, 'n': 12, 'i': 8, 'q': 1, 'w': 2, 'm': 3, 's': 12, 'a': 10, 'f': 4, 'e': 16}
    '''
    text = 'To be or not to be that is the question Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles And by opposing end them'
    expected = {'t': 18, 'b': 5, 'o': 16, 'n': 12, 'i': 8, 'q': 1, 'w': 2, 'm': 3, 's': 12, 'a': 10, 'f': 4, 'e': 16}
    return do_func2_tests(text, expected)

def test_func2_4():
    text = 'FAR Out in THe unchArTEd baCKwaTers Of the uNFashIonaBlE End Of tHE westeRn SpirAl ARm of tHe GalaXY liEs A SMaLl UnrEgarded yelLow sUn OrbItiNg this at A DISTaNce OF rOUGHlY nINEtY TWO miLLioN Miles IS an utTerLy iNSiGnifIcAnt lITtle Blue greeN pLaneT whOse APE deSCenDeD lIfE forMS Are SO aMAZinglY prImitivE thaT tHeY sTill thiNk DigITal WAtcheS aRE A preTTy nEat IDEA This plaNet HAs or RAthEr HaD A probleM WHiCh wAs tHis mOSt Of thE peOple on It Were unHappy for PRETty mUcH OF the tIMe MAnY sOluTIonS Were suggEsTEd FOr THiS prOBLem buT most of These weRe lArGeLy COncERNEd WIth the MoVements oF smAlL GrEeN pieceS of pAPeR WhICh iS odD becaUse on tHe WhOLe It WASN t the SmaLL GReeN piEcEs oF paper tHAt Were uNHaPPY And SO the PrObLEm remaINeD LotS of ThE pEOpLe weRe meaN aNd mOst oF them weRe mIsErAble even tHe ONES WITh DIgital WaTches MAny weRE iNcReasiNgly of thE oPiNIoN that they D aLL madE A bIg MistAKe iN coMIng dOwn from the treEs in The firST PLace AND sOMe saiD THAt EVeN tHE trEEs HAd BEen A bad move and thAT no onE shoUld ever hAve LEft tHe ocEAns And THEn oNe ThUrSDAY NeArLY twO ThouSAND yearS afTeR ONE mAn HaD BEen NaIled to a tREE for sAying hOw greAt It woulD bE To be nIce to peOpLe FoR a CHangE oNe girL SiTtINg on hEr owN in A sMAlL CAfE in RICkmansWorth sUdDeNly rEaliZed WHAT it Was that haD BeEN GoING wroNG ALL This TiME aNd sHe FinaLly knEw hOw tHe WoRLd cOulD be MAdE A gOOD aNd hapPy pLAcE THiS TimE it waS Right IT WOUld WoRK and nO oNE Would hAvE to GEt naiLed to ANyThIng SaDly hOweVER BEfORe sHe Could gEt tO a pHone to TELL anyonE about iT A terriblY sTuPID CatAstrOPHe OcCUrrED aND the idEa wAs lOsT FOREvEr ThiS iS noT hEr sTOrY'
    expected = {'f': 30, 'o': 97, 'i': 74, 't': 116, 'u': 27, 'b': 21, 'e': 144, 'w': 39, 's': 73, 'a': 113, 'g': 28, 'l': 57, 'y': 28, 'd': 49, 'r': 69, 'n': 87, 'm': 36, 'p': 26, 'h': 78, 'c': 27, 'k': 6}
    return do_func2_tests(text, expected)


# ----------------------------------- FUNC. 3 ----------------------------------- #

def do_func3_tests(ID, expected):
    input_filename    = f'func3/in_{ID}.txt'
    output_filename   = f'func3/your_output_{ID}.txt'
    expected_filename = f'func3/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func3(input_filename, output_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 1


def test_func3_1():
    '''
    textfile_in  = 'func3/in_1.txt'
    textfile_out = 'func3/your_output_1.txt'
    expected     = 'func3/expected_1.txt'
    '''
    ID = 1
    expected = 5
    return do_func3_tests(ID, expected)

def test_func3_2():
    '''
    textfile_in  = 'func3/in_2.txt'
    textfile_out = 'func3/your_output_2.txt'
    expected     = 'func3/expected_2.txt'
    '''
    ID = 2
    expected = 11
    return do_func3_tests(ID, expected)

def test_func3_3():
    '''
    textfile_in  = 'func3/in_3.txt'
    textfile_out = 'func3/your_output_3.txt'
    expected     = 'func3/expected_3.txt'
    '''
    ID = 3
    expected = 37
    return do_func3_tests(ID, expected)

def test_func3_4():
    '''
    textfile_in  = 'func3/in_4.txt'
    textfile_out = 'func3/your_output_4.txt'
    expected     = 'func3/expected_4.txt'
    '''
    ID = 4
    expected = 51
    return do_func3_tests(ID, expected)


# ----------------------------------- FUNC. 4 ----------------------------------- #


def do_func4_tests(ID, expected):
    input_filename  = f'func4/in_{ID}.txt'
    res = program.func4(input_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il risultato è sbagliato! / The result is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1


def test_func4_1():
    '''
    input_filename = 'func4/in_1.txt'
    expected =  [[12, 8, 4],
                 [11, 7, 3],
                 [10, 6, 2],
                 [ 9, 5, 1]]
    '''
    ID = 1
    expected = [[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    input_filename = 'func4/in_2.txt'
    expected = [[-694, 273, 473, 589, -278, -609],
                [795, 699, 271, -660, -954, -893],
                [626, -884, -391, 881, 247, 496]]
    '''
    ID = 2
    expected = [[-694, 273, 473, 589, -278, -609],
                [795, 699, 271, -660, -954, -893],
                [626, -884, -391, 881, 247, 496]]
    return do_func4_tests(ID, expected)


def test_func4_3():
    '''
    input_filename = 'func4/in_3.txt'
    '''
    ID = 3
    expected = [[-104, -197, -250, 526, -450, -332, -332],
                [398, -84, 962, 386, 531, 389, 226],
                [30, -690, 912, 780, -420, -573, 116],
                [407, 804, -472, -708, 163, -416, -555],
                [-808, 949, 181, -869, 172, -206, 31],
                [570, -168, -830, -715, 114, 401, 618],
                [719, 452, -490, -416, 125, -230, -309],
                [-911, 587, -161, -373, -90, -274, 892],
                [678, 229, 274, 856, 957, -243, -939],
                [537, 317, -894, 904, 760, -451, -897],
                [862, -298, 76, -683, 476, 194, -791],
                [-290, -661, -526, 494, -67, 920, -211],
                [191, -872, 768, -382, 529, 102, -288],
                [-526, 132, -457, 468, -79, -798, -289],
                [-170, -694, -811, -671, 578, 235, 757],
                [486, -945, 684, 862, 661, 175, 431],
                [194, 706, -770, 442, 717, -909, -102],
                [-247, -501, 824, -177, 709, -735, -311],
                [-370, 38, 236, -988, 369, 866, -822],
                [-40, -636, -403, 768, -428, -22, 246]]
    return do_func4_tests(ID, expected)

def test_func4_4():
    '''
    input_filename = 'func4/in_4.txt'
    '''
    ID = 4
    expected = [[14, 685, -812, -522, 126, -840, 261, -384, 475, -639, -487, -782, 779],
                [13, 615, 353, 637, -254, 817, -378, -791, 51, -116, -543, -675, 488],
                [295, -987, -193, 287, 608, 648, -480, 578, 587, -810, -287, -183, 237],
                [686, 259, 917, -457, -903, -598, 227, -505, 861, -879, 700, 596, -471],
                [716, -434, 47, 587, 215, 404, 634, -803, -812, 693, 114, 783, 61],
                [332, -60, -262, 657, 804, -591, 332, 71, 285, -939, 87, 696, -442],
                [756, -921, -242, 500, 873, 32, -545, -734, -198, 235, -206, 175, 528],
                [988, 842, -746, -553, 353, -682, 774, 301, -54, -328, 462, 166, -779],
                [-525, 205, 152, 293, -585, 11, 825, -632, -321, 549, 748, -815, 448],
                [603, 698, 520, 941, 730, 433, 13, 919, -907, -710, -491, 507, 431],
                [233, 437, 621, 341, 681, 55, 916, 996, -405, -441, 274, 954, 468],
                [-204, 22, 88, -119, -354, 107, -119, -441, -299, -129, 90, -251, 77],
                [-936, -856, -795, 72, 654, 883, 239, -884, -751, 511, 83, -297, 911],
                [850, -157, 855, 28, 564, -121, -882, -5, -968, 835, 251, -2, -830],
                [55, -32, -63, 67, 978, 726, 818, 47, -1, 13, -744, -466, -89],
                [676, -489, 370, -941, -127, 867, -150, -961, -26, -806, 233, 326, -581],
                [562, 183, -88, -9, -418, -112, 841, -9, -893, -448, 262, -49, -702],
                [-875, -587, -696, 451, -557, 664, 72, 409, 470, 812, 598, 360, -126],
                [417, 369, -156, 476, -189, -865, 315, 25, -25, 595, -765, -211, 812],
                [-381, 976, 569, 987, -651, 346, -967, 763, -860, 322, -529, -386, 819],
                [252, -510, 453, 504, -258, 157, 777, 195, 94, -162, -563, -870, -810],
                [286, -301, 312, -555, 311, -935, 882, -106, 867, 940, -24, 840, -394],
                [-209, 304, -786, -282, -588, -953, 190, -116, 257, -320, -504, -805, 197]]
    return do_func4_tests(ID, expected)

# ----------------------------------- FUNC. 5 ----------------------------------- #


def do_test_func5(ID, W, H, expected):
    txt_in  = f'func5/in_{ID}.txt'
    img_out = f'func5/your_image_{ID}.png'
    img_exp = f'func5/expected_{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func5(txt_in, W, H, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di rettangoli e ellissi è sbagliato! / The number of rectangles and ellipses are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''
    txt_file = func5/in_1.txt
    output_imagefile = func5/your_image_1.png
    width = 50
    heigth = 100
    expected_imagefile = func5/expected_1.png
    expected = (2, 1)
    '''
    ID = 1
    width = 50
    heigth = 100
    expected = (2, 1)
    return do_test_func5(ID, width, heigth, expected)

def test_func5_2():
    '''
    txt_file = func5/in_2.txt
    output_imagefile = func5/your_image_2.png
    width = 200
    heigth = 200
    expected_imagefile = func5/expected_2.png
    expected = (4, 7)
    '''
    ID = 2
    width = 200
    heigth = 200
    expected = (4, 7)
    return do_test_func5(ID, width, heigth, expected)


def test_func5_3():
    '''
    txt_file = func5/in_3.txt
    output_imagefile = func5/your_image_3.png
    width = 300
    heigth = 400
    expected_imagefile = func5/expected_3.png
    expected = (8, 13)
    '''
    ID = 3
    width = 300
    heigth = 400
    expected = (8, 13)
    return do_test_func5(ID, width, heigth, expected)


def test_func5_4():
    '''
    txt_file = func5/in_4.txt
    output_imagefile = func5/your_image_4.png
    width = 500
    heigth = 200
    expected_imagefile = func5/expected_4.png
    expected = (32, 23)
    '''
    ID = 4
    width = 500
    heigth = 200
    expected = (32, 23)
    return do_test_func5(ID, width, heigth, expected)

# ----------------------------------- EX. 1 ----------------------------------- #

def do_test_ex1(rootlist, values, expected, sum_expected):
    if not DEBUG:
        root = nary_tree.NaryTree.fromList(rootlist.copy())
        try:
            isrecursive.decorate_module(program)
            program.ex1(root, values)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    root     = nary_tree.NaryTree.fromList(rootlist.copy())
    expected = nary_tree.NaryTree.fromList(expected.copy())
    res = program.ex1(root, values)
    testlib.check(res, sum_expected, None, f'''{'*'*50}\n[ERROR]Le due somme tornate non sono corrette! / Incorrect sums!\nReturned={res}, expected={sum_expected}''')
    testlib.check(root, expected, None, f'''{'*'*50}\n[ERROR]L'albero ritornato non è corretto! / Incorrect tree!\nReturned={root}, expected={expected}''')
    return 2

def test_ex1_1():
    '''
    values: [-42, -80, 68, 2, 81, 75, 54, 48, -4, 5]
    root:                        -7                         | -42
                    /      |      |      |    \             |
                  -10      -3     -8    -10    -5           | -80
                /   \      |       |     |                  |
               6    -2     9       7     -9                 | +68

    expected:                    -49                         |
                    /      |       |      |     \            |
                  -90     -83     -88    -90    -85          |
                /   \      |       |      |                  |
               74    66   77       75     59                 |
    total = -134
    '''
    root = [-7, [-10, [6],
                      [-2]],
                [-3,  [9]],
                [-8,  [7]],
                [-10, [-9]],
                [-5]]
    values = [-42, -80, 68, 2, 81, 75, 54, 48, -4, 5]
    expected = [-49, [-90, [74],
                           [66]],
                     [-83, [77]],
                     [-88, [75]],
                     [-90, [59]],
                     [-85]]
    total = -134
    return do_test_ex1(root, values, expected, total)

def test_ex1_2():
    root =  [-53, [-5, [-87, [-21]], [-81], [67, [68, [-66, [-2]], [2, [-69], [52, [97]]],
            [-12, [-16, [23], [-64, [60], [-43], [-71]], [89]], [97, [59, [93], [78]]]]],
            [36, [75, [-81], [37, [31], [-47]], [-70, [27], [12]]], [-96, [22, [85], [67, [-12],
            [17], [-8]], [95]], [-14]], [-24, [-87], [19], [99, [-25]]]], [-44, [0], [24, [-78]]]]]]
    values = [-67, 89, -59, -68, 3, 44, 28, -45, 41, -99]
    expected = [-120, [84, [-146, [-89]], [-140], [8, [0, [-63, [42]], [5, [-25], [96, [125]]],
            [-9, [28, [51], [-36, [15], [-88], [-116]], [117]], [141, [87, [48], [33]]]]],
            [-32, [78, [-37], [81, [59], [-19]], [-26, [55], [40]]], [-93, [66, [113], [95,
            [-57], [-28], [-53]], [123]], [30]], [-21, [-43], [63], [143, [3]]]], [-112, [3], [27, [-34]]]]]]
    total = 472
    return do_test_ex1(root, values, expected, total)

def test_ex1_3():
    root = [-4, [-3, [-7, [-7, [1, [9], [2]], [-2], [2, [-10], [-5]], [3, [10]], [-6, [-3],
            [0], [-8], [6], [0]]], [7, [-8, [-6], [3, [-8], [4], [3], [-8], [1]]], [-5, [10, [6], [-3],
            [4], [2]], [8], [4], [-6]]]], [6, [-3, [9], [0], [7, [-4]], [-6]], [-3, [2, [9], [4], [5],
            [-1], [1, [3], [-9, [-8], [10], [0], [2], [-5]], [9]]], [6, [-2]]], [3],
            [3, [-5], [8], [-7], [5], [10]]], [-4], [-4, [-3, [-9, [10, [-5]]]],
            [-9, [-6, [-8, [3], [-9]], [-3], [-9], [-6]], [-5, [8], [-2], [-1], [-4]], [10], [0]],
            [-1, [8, [4, [-6], [2]], [2, [-2], [2], [-8], [7]], [-8], [-6, [5], [1, [-3], [-4], [0]],
            [-8, [10], [1]]]]]]]]
    values = [37, -80, -58, -6, -95, 48, 18, 16, 83, -41]
    expected =  [33, [-83, [-65, [-13, [-94, [57], [50]], [-97], [-93, [38], [43]], [-92, [58]],
                [-101, [45], [48], [40], [54], [48]]], [1, [-103, [42], [51, [10], [22], [21], [10], [19]]],
                [-100, [58, [24], [15], [22], [20]], [56], [52], [42]]]], [-52, [-9, [-86], [-95], [-88, [44]],
                [-101]], [-9, [-93, [57], [52], [53], [47], [49, [21], [9, [8], [26], [16], [18], [11]], [27]]],
                [-89, [46]]], [-3], [-3, [-100], [-87], [-102], [-90], [-85]]], [-62], [-62, [-9, [-104, [58,
                [13]]]], [-15, [-101, [40, [21], [9]], [45], [39], [42]], [-100, [56], [46], [47], [44]],
                [-85], [-95]], [-7, [-87, [52, [12], [20]], [50, [16], [20], [10], [25]], [40],
                [42, [23], [19, [13], [12], [16]], [10, [26], [17]]]]]]]]
    total = -314
    return do_test_ex1(root, values, expected, total)



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
        return 2
    if set(res) == set(expected):
        return 1
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
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1, test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################

# -*- coding: utf-8 -*-
import testlib, os
from testlib import my_print, COL, test_personal_data_entry

# Import the student's code
import program

###############################################################################
#### Mettete DEBUG=True per fare debug delle funzioni più facilmente attivando
#### la stack trace degli errori (più verbosa)
DEBUG = True
# DEBUG = False
###############################################################################

################################################################################
################################################################################
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
################################################################################

################################################################################
# %% ---------------------- TEST SECTION -------------------
################################################################################
# ----------------------------------- Func.1 ----------------------------------- #

def do_func1_tests(ID, expected):
    f1 = f'func1/input_{ID}_a.txt'
    f2 = f'func1/input_{ID}_b.txt'
    res = program.func1(f1, f2)
    if res != expected:
        my_print(f"[ERROR] Wrong return value! Returned={res}, expected={expected}")
        return 0
    return 2

def test_func1_1():
    '''
    file_input_a = 'func1/input_0_a.txt'
    file_input_b = 'func1/input_0_b.txt'
    '''
    expected = {'a': 'b-c'}
    return do_func1_tests('0', expected)

def test_func1_2():
    '''
    file_input_a = 'func1/input_1_a.txt'
    file_input_b = 'func1/input_1_b.txt'
    '''
    expected = {'uscio': 'lascio-mesci', 'ascia': 'lascia-mesci'}
    return do_func1_tests('1', expected)

def test_func1_3():
    '''
    file_input_a = 'func1/input_2_a.txt'
    file_input_b = 'func1/input_2_b.txt'
    '''
    expected = {'rallargata': 'ringinocchiava-sfineremmo',
 'dorava': 'chiavino-riturbati',
 'innovavamo': 'guattivate-riturbati',
 'immillavano': 'rimormoreremo-sprolungo'}
    return do_func1_tests('2', expected)



# %% ----------------------------------- FUNC 2 ------------------------- #

def do_func2_tests(ID, expected):
    input_file   = f'func2/input_{ID}.txt'
    output_file  = f'func2/output_{ID}.txt'
    expected_file= f'func2/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_file):
        os.remove(output_file)

    res = program.func2(input_file, output_file)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è corretto! / Returned value is incorrect!\n'''
              f'''[ERROR] Expected {expected} returne {res}\n {'*'*50}''')
        return 0
    testlib.check_text_file(output_file, expected_file)
    return 2


def test_func2_1():
    '''
    input_file = func2/input_1.txt
    output_file = func2/output_1.txt
    expected = 12
    '''
    ID = 1
    expected = 12
    return do_func2_tests(ID, expected)

def test_func2_2():
    '''
    input_file = func2/input_2.txt
    output_file = func2/output_2.txt
    expected = 10
    '''
    ID = 2
    expected = 10
    return do_func2_tests(ID, expected)


def test_func2_3():
    '''
    input_file = func2/input_3.txt
    output_file = func2/output_3.txt
    expected = 32
    '''
    ID = 3
    expected = 32
    return do_func2_tests(ID, expected)

# %%----------------------------------- Func 3 ----------------------------------- #

def do_func3_tests(ID, length, chars, expected):
    input_filename  = f'func3/in_0{ID}.txt'
    output_filename = f'func3/out_0{ID}.txt'
    expected_filename = f'func3/exp_0{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func3(input_filename, output_filename, length, chars)
    testlib.checkList(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2


def test_func3_1(run=True):
    '''
    input_filename = 'func3/in_01.txt'
    ouput_filename = 'func3/out_01.txt'
    expected_filename = 'func3/exp_01.txt'
    length = 5
    chars = 'asd'
    expected = ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
    '''
    ID = 1
    length = 5
    chars = 'asd'
    expected = ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
    return do_func3_tests(ID, length, chars, expected)

def test_func3_2(run=True):
    '''
    input_filename = 'func3/in_02.txt'
    ouput_filename = 'func3/out_02.txt'
    expected_filename = 'func3/exp_02.txt'
    length = 8
    chars = 'qwerty'
    expected = ['chronologies', 'annuitants', 'bridgeport', 'precluding', 'sauerkraut', 'cutworms', 'speculum', 'subfloor']
    '''
    ID = 2
    length = 8
    chars = 'qwerty'
    expected = ['chronologies', 'annuitants', 'bridgeport', 'precluding', 'sauerkraut', 'cutworms', 'speculum', 'subfloor']
    return do_func3_tests(ID, length, chars, expected)

def test_func3_3(run=True):
    '''
    input_filename = 'func3/in_03.txt'
    ouput_filename = 'func3/out_03.txt'
    expected_filename = 'func3/exp_03.txt'
    length = 2
    chars = 'aiu'
    expected = ['psychologically', 'mephistopheles', 'modifications', 'apotheosizes', 'midwesterner', 'forewarning', 'magnetising', 'mellifluous', 'sulfonamide', 'altercates', 'deficiency', 'fascinator', 'cufflinks', 'euthenics', 'inserting', 'prompting', 'rewriting', 'brasilia', 'cinching', 'gnarling', 'harpists', 'chacers', 'triadic', 'viaduct', 'geisha', 'aires', 'scite']
    '''
    ID = 3
    length = 2
    chars = 'aiu'
    expected = ['psychologically', 'mephistopheles', 'modifications', 'apotheosizes', 'midwesterner', 'forewarning', 'magnetising', 'mellifluous', 'sulfonamide', 'altercates', 'deficiency', 'fascinator', 'cufflinks', 'euthenics', 'inserting', 'prompting', 'rewriting', 'brasilia', 'cinching', 'gnarling', 'harpists', 'chacers', 'triadic', 'viaduct', 'geisha', 'aires', 'scite']
    return do_func3_tests(ID, length, chars, expected)

# ----------------------------------- FUNC. 4 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename    = f'func4/in_{ID}.txt'
    output_filename   = f'func4/your_output_{ID}.txt'
    expected_filename = f'func4/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func4(input_filename, output_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 1.5

def test_func4_1():
    '''
    textfile_in  = 'func4/in_1.txt'
    textfile_out = 'func4/your_output_1.txt'
    expected     = 'func4/expected_1.txt'
    result       = 5
   '''
    ID = 1
    expected = 5
    return do_func4_tests(ID, expected)

def test_func4_2():
    '''
    textfile_in  = 'func4/in_2.txt'
    textfile_out = 'func4/your_output_2.txt'
    expected     = 'func4/expected_2.txt'
    result       = 11
    '''
    ID = 2
    expected = 11
    return do_func4_tests(ID, expected)

def test_func4_3():
    '''
    textfile_in  = 'func4/in_3.txt'
    textfile_out = 'func4/your_output_3.txt'
    expected     = 'func4/expected_3.txt'
    result       = 37
    '''
    ID = 3
    expected = 37
    return do_func4_tests(ID, expected)

def test_func4_4():
    '''
    textfile_in  = 'func4/in_4.txt'
    textfile_out = 'func4/your_output_4.txt'
    expected     = 'func4/expected_4.txt'
    result       = 51
    '''
    ID = 4
    expected = 51
    return do_func4_tests(ID, expected)


# ----------------------------------- FUNC. 5 ----------------------------------- #

def do_func5_tests(ID, expected):
    input_filename  = f'func5/in_{ID}.txt'
    res = program.func5(input_filename)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il risultato è sbagliato! / The result is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1.5


def test_func5_1():
    '''
    input_filename = 'func5/in_1.txt'
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
    return do_func5_tests(ID, expected)

def test_func5_2():
    '''
    input_filename = 'func5/in_2.txt'
    expected = [[-694, 273, 473, 589, -278, -609],
                [795, 699, 271, -660, -954, -893],
                [626, -884, -391, 881, 247, 496]]
    '''
    ID = 2
    expected = [[-694, 273, 473, 589, -278, -609],
                [795, 699, 271, -660, -954, -893],
                [626, -884, -391, 881, 247, 496]]
    return do_func5_tests(ID, expected)


def test_func5_3():
    '''
    input_filename = 'func5/in_3.txt'
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
    return do_func5_tests(ID, expected)

def test_func5_4():
    '''
    input_filename = 'func5/in_4.txt'
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
    return do_func5_tests(ID, expected)

################################################################################
# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1,   test_func1_2,   test_func1_3,   # dizionari
    test_func2_1, test_func2_2, test_func2_3,
    test_func3_1, test_func3_2, test_func3_3,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_personal_data_entry,
]

# %% --------------------- MAIN ---------------------
if __name__ == '__main__':
    test_personal_data_entry()
    # Check that input files have not been changed
    testlib.check_expected()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)

################################################################################
# %% --------------------- END OF FILE ---------------------

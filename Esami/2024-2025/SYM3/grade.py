# -*- coding: utf-8 -*-
import testlib, os
from testlib import my_print, COL, check_expected

import program
import images

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = False   # without stack trace of errors
DEBUG = True    # with    stack trace of errors

#############################################################################
# %% ---------------------- TEST SECTION -------------------
#############################################################################

def test_personal_data_entry():
    assert program.nome      != 'NOME',      f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME',   f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9

###########################################################################################################################


# %% ----------------------------------- FUNC1 ------------------------- #


def do_test_func1(ID, expected):
    img_in = f'func1/img{ID}_in.png'
    img_out = f'func1/img{ID}_out.png'
    img_exp = f'func1/img{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func1(img_in)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    return 2


def test_func1_1():
    '''
    imagefile = func4/img1_in.png
    '''
    ID = 1
    expected = 256*256
    return do_test_func1(ID, expected)


def test_func1_2():
    '''
    imagefile = func4/img2_in.png
    '''
    ID = 2
    expected = 4
    return do_test_func1(ID, expected)

def test_func1_3():
    '''
    imagefile = func4/img3_in.png
    '''
    ID = 3
    expected = 18838
    return do_test_func1(ID, expected)


def test_func1_4():
    '''
    imagefile = func4/img4_in.png
    '''
    ID = 4
    expected = 192871
    return do_test_func1(ID, expected)


# %% ----------------------------------- FUNC2 ------------------------- #

def do_test_func2(ID,val,expected):
    img_in = f'func2/img{ID}_in.png'
    img_out = f'func2/img{ID}_out.png'
    img_exp = f'func2/img{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func2(img_in, img_out,val)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_img_file(img_out, img_exp)
    testlib.check_val(res, expected)
    return 2


def test_func2_1():
    '''
    imagefile = func2/img1_in.png
    output_imagefile = func2/img1_out.png
    '''
    ID = 1
    return do_test_func2(ID,100,0)


def test_func2_2():
    '''
    imagefile = func2/img2_in.png
    output_imagefile = func2/img2_out.png
    '''
    ID = 2
    return do_test_func2(ID,100,256*256)


def test_func2_3():
    '''
    imagefile = func2/img3_in.png
    output_imagefile = func2/img3_out.png
    '''
    ID = 3
    return do_test_func2(ID,512,256*256)


def test_func2_4():
    '''
    imagefile = func2/img4_in.png
    output_imagefile = func2/img4_out.png
    '''
    ID = 4
    return do_test_func2(ID,315,262144)

# %% ----------------------------------- FUNC3 ------------------------- #


def do_test_func3(ID, expected):
    img_in  = f'func3/image0{ID}.png'

    res = program.func3(img_in)
    if res != expected:
        testlib.checkList(res, expected)
    return 2


def test_func3_1():
    '''
    imm_in = func3/image01.png
    expected = [121,861]
    '''
    ID = 1
    expected = [(6, 8, 11), (18, 11, 42), (33, 12, 18), (34, 19, 31)]
    return do_test_func3(ID, expected)


def test_func3_2():
    '''
    imm_in = func3/image02.png
    expected = [100, 400, 900, 1600, 2500]
    '''
    ID = 2
    expected = [(6, 8, 8), (49, 0, 49)]
    return do_test_func3(ID, expected)


def test_func3_3():
    '''
    imm_in = func3/image03.png
    expected = [2500]
    '''
    ID = 3
    expected = [(0, 0, 49), (1, 0, 49), (2, 0, 49), (3, 0, 49), (4, 0, 49), (5, 0, 49), (6, 0, 49), (49, 0, 49)]
    return do_test_func3(ID, expected)


def test_func3_4():
    '''
    imm_in = func3/image04.png
    expected = []
    '''
    ID = 4
    expected = [(0, 0, 49), (1, 0, 49), (2, 0, 49), (3, 0, 49), (4, 0, 49), (5, 0, 49), (6, 0, 49), (7, 25, 25), (8, 25, 25), (9, 25, 25), (10, 25, 25), (11, 25, 25), (12, 25, 25), (13, 25, 25), (14, 25, 25), (15, 25, 25), (16, 25, 25), (17, 25, 25), (18, 25, 25), (19, 25, 25), (20, 25, 25), (21, 25, 25), (22, 25, 25), (23, 25, 25), (24, 25, 25), (25, 25, 25), (26, 25, 25), (27, 25, 25), (28, 25, 25), (29, 25, 25), (30, 25, 25), (31, 25, 25), (32, 25, 25), (33, 25, 25), (34, 25, 25), (35, 25, 25), (36, 25, 25), (37, 25, 25), (38, 25, 25), (39, 25, 25), (40, 25, 25), (41, 25, 25), (42, 25, 25), (43, 25, 25), (44, 25, 25), (45, 25, 25), (46, 25, 25), (47, 25, 25), (48, 25, 25), (49, 0, 49)]
    return do_test_func3(ID, expected)


# %% ----------------------------------- FUNC4 ------------------------- #

def do_test_func4(ID, expected):
    img_in = f'func4/img{ID}_in.png'
    img_out = f'func4/img{ID}_out.png'
    img_exp = f'func4/img{ID}_exp.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func4(img_in, img_out)
    if res == None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected)
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func4_1():
    '''
    imagefile = func4/img1_in.png
    output_imagefile = func4/img1_out.png
    '''
    ID = 1
    expected = 13
    return do_test_func4(ID, expected)


def test_func4_2():
    '''
    imagefile = func4/img2_in.png
    output_imagefile = func4/img2_out.png
    '''
    ID = 2
    expected = 2
    return do_test_func4(ID, expected)


def test_func4_3():
    '''
    imagefile = func4/img3_in.png
    output_imagefile = func4/img3_out.png
    '''
    ID = 3
    expected = 0
    return do_test_func4(ID, expected)


def test_func4_4():
    '''
    imagefile = func4/img4_in.png
    output_imagefile = func4/img4_out.png
    '''
    ID = 4
    expected = 15686
    return do_test_func4(ID, expected)


# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
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


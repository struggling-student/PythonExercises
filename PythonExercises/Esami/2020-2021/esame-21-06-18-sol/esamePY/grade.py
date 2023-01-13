import testlib
import isrecursive
import os

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    exit(0)
import program

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

def do_test_ex1(files, expected):
    res = program.ex1(*files)
    testlib.check(res, expected)
    return 2

def test_ex1_1():
    files = ['matrices/file_rows_00.txt','matrices/file_cols_00.txt','matrices/file_values_00.txt']
    expected =  [[4, None], [3, 5]]
    return do_test_ex1(files, expected)

def test_ex1_2():
    files = ['matrices/file_rows_01.txt','matrices/file_cols_01.txt','matrices/file_values_01.txt']
    expected =  [[5, 10, 3], [3, 10, 5], [60, 1, 999]]
    return do_test_ex1(files, expected)

def test_ex1_3():
    files = ['matrices/file_rows_02.txt','matrices/file_cols_02.txt','matrices/file_values_02.txt']
    expected =  [[24, -33, -45, 82, -163, 95],
                [-20, None, -59, -20, 179, -59],
                [-33, -45, -163, None, 82, 179]]
    return do_test_ex1(files, expected) + 1

# ----------------------------------- EX.2 ----------------------------------- #

def do_test_ex2(ID, expected):
    filein              = f'{ID}.png'
    res = program.ex2(filein)
    testlib.check(res, expected)
    return 2

def test_ex2_1():
    ID = 'ex2p1'
    expected = {20: 120, 3: 12}
    return do_test_ex2(ID, expected)

def test_ex2_2():
    ID = 'ex2p2'
    expected = {9: 602, 17: 462}
    return do_test_ex2(ID, expected)

def test_ex2_3():
    ID = 'ex2p3'
    expected = {25: 100, 21: 84, 17: 68, 13: 52, 9: 36, 5: 20}
    return do_test_ex2(ID, expected)

def test_ex2_4():
    ID = 'ex2p4'
    expected = {6: 632, 17: 782, 29: 228, 9: 546, 3: 180}
    return do_test_ex2(ID, expected)


# ----------------------------------- EX.3 ----------------------------------- #
def do_test_ex3(stringa, expected):
    try:
        isrecursive.decorate_module(program)
        program.ex3(stringa)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The function does not employ recursion / La funzione non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)
    
    res = program.ex3(stringa)
    testlib.check(res, expected)
    return 3

def test_ex3_1():
    stringa = 'aBbACc'
    expected = [ 'Cc', '' ] 
    return do_test_ex3(stringa, expected)

def test_ex3_2():
    stringa = 'EtTABbTeE'
    expected = ['EeE', 'B', 'E', 'T']
    return do_test_ex3(stringa, expected)

def test_ex3_3():
    stringa = 'aAbBcCadDbeEcfFgG'
    expected = ['aAa', 'cCc', 'D', 'G', 'a', 'c', 'e']
    return do_test_ex3(stringa, expected)

# ----------------------------------- EX.4 ----------------------------------- #
def do_test_ex4(dir1, ext, expected):
    try:
        isrecursive.decorate_module(program)
        program.ex4(dir1, ext)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The function does not employ recursion / La funzione non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)
    
    res = program.ex4(dir1, ext)
    testlib.check(res, expected)
    return 2

def test_ex4_1():
    dir1 = 'ex4/a0'
    ext = '.txt'
    expected =  {'ex4/a0': ['Roar.txt', 'Miaao.txt', 'Muuuu.txt'], 'ex4/a0/b1': ['Bau.txt', 'Ciao.txt', 'Miao.txt']}
    return do_test_ex4(dir1, ext, expected)

def test_ex4_2():
    dir1 = 'ex4/a1'
    ext = '.conf'
    expected =  {'ex4/a1/b1': ['CPU.conf'], 'ex4/a1/b2/c2': ['Hefn3j.conf', 'MNM£Ssf3.conf'], 'ex4/a1/b2': ['Lego.conf', 'Mario.conf'], 'ex4/a1/b2/c1': ['Mg5yw3o.conf']}
    return do_test_ex4(dir1, ext, expected)

def test_ex4_3():
    dir1 = 'ex4/a1'
    ext = '.txt'
    expected =  {'ex4/a1': ['ACD.txt', 'ARD.txt', 'ASD.txt', 'ACDC.txt'], 'ex4/a1/b1': ['IO.txt', 'Bus.txt', 'CPU.txt', 'RAM.txt'], 'ex4/a1/b1/c2': ['Lost.txt', 'Friends.txt', 'GamesofThrones.txt'], 'ex4/a1/b1/c1': ['Raf.txt', 'Ron.txt', 'Giorgia.txt', 'Ruggeri.txt'], 'ex4/a1/b2': ['Lego.txt', 'Mario.txt'], 'ex4/a1/b2/c1': ['Lgr4ego.txt']}
    return do_test_ex4(dir1, ext, expected)

def test_ex4_4():
    dir1 = 'ex4/a2'
    ext = '.doc'
    expected =  {'ex4/a2/b1/c1': ['FCA.doc', 'Fiat.doc', 'Ford.doc', 'Ferrari.doc'], 'ex4/a2/b2/c2': ['Toyota.doc']}
    return do_test_ex4(dir1, ext, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1, test_ex1_2, test_ex1_3,                  # triple matrix indexing
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4,      # white rectangles
    test_ex3_1, test_ex3_2, test_ex3_3, # test_ex3_4,    # string game tree / albero di gioco della stringa 
    test_ex4_1, test_ex4_2, test_ex4_3, test_ex4_4,      # capitalized files in dirtree / file iniziale maiuscola in albero directory
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################

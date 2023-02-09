import copy

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

def do_test_ex1(files, expected):
    res = program.ex1(*files)
    testlib.check(res, expected)
    return 2

def test_ex1_1():
    files = ['matrices/file_rows_00.txt','matrices/file_cols_00.txt','matrices/file_values_00.txt']
    expected =  [[-10, 5, None, None, None, None], [None, None, 3, None, None, 2], [None, None, None, 12, 11, None]]
    return do_test_ex1(files, expected)

def test_ex1_2():
    files = ['matrices/file_rows_01.txt','matrices/file_cols_01.txt','matrices/file_values_01.txt']
    expected =  [[None, 100, None, None, None, 0, None, None, 5, None, None, None, None, 177, None, None, None, None, 172, None], [1000, None, None, None, None, None, None, 183, None, 4, None, None, 178, None, None, None, None, None, None, 171], [None, None, None, 187, -1, None, None, None, None, None, None, 179, None, None, None, 175, 174, None, None, None], [None, None, 10, None, None, None, 1, None, None, None, 5, None, None, None, 176, None, None, 173, None, None]]
    return do_test_ex1(files, expected)

def test_ex1_3():
    files = ['matrices/file_rows_02.txt','matrices/file_cols_02.txt','matrices/file_values_02.txt']
    expected =  [[None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, 10], [None, None, None, None, None, None], [None, None, -1, None, None, None], [None, None, None, None, 11, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, 12, None, None], [15, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None], [None, 14, None, None, None, None]]
    return do_test_ex1(files, expected) + 1

# ----------------------------------- EX.2 ----------------------------------- #

def do_test_ex2(image_file, space_intruder_pic_file, expected):
    res = program.ex2(image_file, space_intruder_pic_file)
    # -- Check the type(s) of the result data
    testlib.check(type(res), tuple, None,
                  "The function should return a tuple / La funzione dovrebbe restituire una tupla")
    testlib.check(type(res[0]), int, None,
                  "The first element of the tuple should be an integer / Il primo elemento della tupla dovrebbe essere un intero")
    testlib.check(type(res[1]), int, None,
                  "The second element of the tuple should be an integer / Il secondo elemento della tupla dovrebbe essere un intero")
    testlib.check(res, expected)
    return

def test_ex2_1():
    image_file = "img/pastel.png"
    space_intruder_pic_file = "img/intruder-00.png"
    expected = (91, 52)
    do_test_ex2(image_file, space_intruder_pic_file, expected)
    return 1

def test_ex2_2():
    image_file = "img/napoleon.png"
    space_intruder_pic_file = "img/intruder-00.png"
    expected = (-1, -1)
    do_test_ex2(image_file, space_intruder_pic_file, expected)
    return 2

def test_ex2_3():
    image_file = "img/landscape.png"
    space_intruder_pic_file = "img/intruder-01.png"
    expected = (346, 89)
    do_test_ex2(image_file, space_intruder_pic_file, expected)
    return 1

def test_ex2_4():
    image_file = "img/landscape-.png"
    space_intruder_pic_file = "img/intruder-01.png"
    expected = (-1, -1)
    do_test_ex2(image_file, space_intruder_pic_file, expected)
    return 1

def test_ex2_5():
    image_file = "img/primavera.png"
    space_intruder_pic_file = "img/intruder-11.png"
    expected = (328, 69)
    do_test_ex2(image_file, space_intruder_pic_file, expected)
    return 2

# ----------------------------------- EX.3 ----------------------------------- #

import json
def do_test_ex3a(familyJson, name, expected, recursive=True):
    with open(familyJson) as F:
        family = json.load(F)
        family1 = copy.deepcopy(family)
        family2 = copy.deepcopy(family)
    if recursive:
        try:
            isrecursive.decorate_module(program)
            program.avi(name, family1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The function does not employ recursion / La funzione non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.avi(name, family1)
    testlib.check(family, family2, "You should not change the family dictionary")
    testlib.check(res, expected)
    return 2

def test_ex3a_1():
    familyJson = 'families/example.json'
    name = 'Ciro'
    expected = {'Ciro':0, 'Aurora': 1, 'Lucia': 2, 'Carlo': 2, 'Giovanni': 1}
    return do_test_ex3a(familyJson, name, expected)
def test_ex3a_2():
    familyJson = 'families/small.json'
    name = 'Lakisha'
    expected = {'Lakisha':0, 'Jaunita': 1, 'Marcos': 2, 'Emanuel': 2, 'Mickey': 1}
    return do_test_ex3a(familyJson, name, expected)
def test_ex3a_3():
    familyJson = 'families/big.json'
    name = 'Geoffrey'
    expected = {'Geoffrey': 0, 'Desmond': 1, 'Marlyn': 1, 'Maire': 2, 'Tiffany': 3, 'Jesenia': 4, 'Janella': 5, 'Cassidy': 6,
                'Elana': 6, 'Juana': 7, 'Polly': 4, 'Britni': 5, 'Cari': 3, 'Isabell': 2, 'Tessie': 3, 'Georgiana': 3}
    return do_test_ex3a(familyJson, name, expected, False)


import json
def do_test_ex3b(familyJson, name, expected, recursive=True):
    with open(familyJson) as F:
        family = json.load(F)
        family1 = copy.deepcopy(family)
        family2 = copy.deepcopy(family)
    if recursive:
        try:
            isrecursive.decorate_module(program)
            program.ex3(family1, name)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The function does not employ recursion / La funzione non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex3(family, name)
    testlib.check(family, family2, "You should not change the family dictionary")
    testlib.check(res, expected)
    return 1

def test_ex3b_1():
    familyJson = 'families/example.json'
    name = 'Ciro'
    expected = {'Giovanni', 'Aurora'}
    return do_test_ex3b(familyJson, name, expected)
def test_ex3b_2():
    familyJson = 'families/small.json'
    name = 'Lakisha'
    expected = {'Emanuel', 'Zenia'}
    return do_test_ex3b(familyJson, name, expected)
def test_ex3b_3():
    familyJson = 'families/big.json'
    name = 'Juana'
    expected = {'Robbyn', 'Buena', 'Scottie', 'Kristie', 'Nicolas'}
    return do_test_ex3b(familyJson, name, expected, False)
def test_ex3b_4():
    familyJson = 'families/huge.json'
    name = 'Holley'
    expected = {'Rocky', 'Barabara', 'Londa', 'Denae', 'Kiana', 'Jerrod', 'Rodrigo', 'Cari'}
    return do_test_ex3b(familyJson, name, expected)

# ----------------------------------- EX.4 ----------------------------------- #

def do_test_ex4(testbed_dir, expected_tools, expected_results):
    try:
        isrecursive.decorate_module(program)
        program.ex4(testbed_dir)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
    finally:
        isrecursive.undecorate_module(program)

    (tools, results) = program.ex4(testbed_dir)
    testlib.check(tools, expected_tools)
    testlib.check(results, expected_results)
    return

def test_ex4_1():
    testbed_dir = "testbed/00"
    expected_tools = {'powertool', 'fastsolver'}
    expected_results = {'alaska/demo-v3/demo-v-00.txt': {'powertool': 'unsat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v-00.txt': {'powertool': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v-01.txt': {'powertool': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v-02.txt': {'powertool': 'sat'}}
    do_test_ex4(testbed_dir, expected_tools, expected_results)
    return 2

def test_ex4_2():
    testbed_dir = "testbed/01"
    expected_tools = {'powertool', 'fastsolver'}
    expected_results = {'alaska/demo-v3/demo-v3-00.txt': {'powertool': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v3/demo-v3-01.txt': {'powertool': 'unsat', 'fastsolver': 'unsat'}, 'alaska/demo-v3/demo-v3-02.txt': {'powertool': 'timeout', 'fastsolver': 'timeout'}, 'alaska/demo-v2/demo-v2-01.txt': {'powertool': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v2-02.txt': {'powertool': 'sat'}, 'alaska/demo-v2/demo-v2-00.txt': {'powertool': 'sat', 'fastsolver': 'sat'}}
    do_test_ex4(testbed_dir, expected_tools, expected_results)
    return 2

def test_ex4_3():
    testbed_dir = "testbed/02"
    expected_tools = {'megareason', 'fastsolver'}
    expected_results = {'alaska/demo-v3/demo-v3-00.txt': {'megareason': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v3/demo-v3-01.txt': {'megareason': 'unsat', 'fastsolver': 'unsat'}, 'alaska/demo-v3/demo-v3-02.txt': {'megareason': 'timeout', 'fastsolver': 'timeout'}, 'alaska/demo-v2/demo-v2-01.txt': {'megareason': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v2-02.txt': {'megareason': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v2-00.txt': {'megareason': 'sat', 'fastsolver': 'sat'}, 'acacia/lift/lift_r/lift_00.txt': {'megareason': 'sat', 'fastsolver': 'sat'}, 'acacia/lift/lift_l/lift_01.txt': {'megareason': 'timeout', 'fastsolver': 'unsat'}, 'acacia/lift/lift_l/lift_02.txt': {'megareason': 'timeout', 'fastsolver': 'timeout'}, 'acacia/lift/lift_l/lift_00.txt': {'megareason': 'timeout', 'fastsolver': 'sat'}, 'acacia/lift/lift_l/lift_03.txt': {'megareason': 'timeout', 'fastsolver': 'sat'}, 'acacia/lift/lift_r/lift_01.txt': {'fastsolver': 'sat'}, 'acacia/lift/lift_r/lift_02.txt': {'fastsolver': 'unsat'}}
    do_test_ex4(testbed_dir, expected_tools, expected_results)
    return 2

def test_ex4_4():
    testbed_dir = "testbed/03"
    expected_tools = {'megareason', 'powertool', 'fastsolver'}
    expected_results = {'alaska/demo-v3/demo-v3-00.txt': {'powertool': 'sat', 'megareason': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v3/demo-v3-01.txt': {'powertool': 'unsat', 'megareason': 'unsat', 'fastsolver': 'unsat'}, 'alaska/demo-v3/demo-v3-02.txt': {'powertool': 'timeout', 'megareason': 'timeout', 'fastsolver': 'timeout'}, 'alaska/demo-v2/demo-v2-01.txt': {'powertool': 'sat', 'megareason': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v2-02.txt': {'powertool': 'sat', 'megareason': 'sat', 'fastsolver': 'sat'}, 'alaska/demo-v2/demo-v2-00.txt': {'powertool': 'sat', 'megareason': 'sat', 'fastsolver': 'sat'}, 'acacia/lift/lift_r/lift_01.txt': {'powertool': 'unsat', 'fastsolver': 'sat'}, 'acacia/lift/lift_r/lift_02.txt': {'powertool': 'unsat', 'fastsolver': 'unsat'}, 'acacia/lift/lift_r/lift_00.txt': {'powertool': 'unsat', 'megareason': 'sat', 'fastsolver': 'sat'}, 'acacia/lift/lift_l/lift_01.txt': {'powertool': 'unsat', 'megareason': 'timeout', 'fastsolver': 'unsat'}, 'acacia/lift/lift_l/lift_02.txt': {'powertool': 'timeout', 'megareason': 'timeout', 'fastsolver': 'timeout'}, 'acacia/lift/lift_l/lift_00.txt': {'powertool': 'sat', 'megareason': 'timeout', 'fastsolver': 'sat'}, 'acacia/lift/lift_l/lift_03.txt': {'powertool': 'sat', 'megareason': 'timeout', 'fastsolver': 'sat'}}
    do_test_ex4(testbed_dir, expected_tools, expected_results)
    return 2
################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1, test_ex1_2, test_ex1_3,                          # triple matrix indexing v2
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5,  # space intruder
    test_ex3a_1, test_ex3a_2, test_ex3a_3,                       # ancestor a
    test_ex3b_1, test_ex3b_2, test_ex3b_3, test_ex3b_4,          # ancestor b
    test_ex4_1, test_ex4_2, test_ex4_3, test_ex4_4,              # filesystem AI tools
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################

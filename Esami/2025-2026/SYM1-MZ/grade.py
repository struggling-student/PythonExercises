# -*- coding: utf-8 -*-
import testlib
from testlib import my_print, COL

import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
# %% ---------------------- DEBUG VARIABLE -------------------
# DEBUG = True    # with    stack trace of errors
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
# ----------------------------------------- FUNC 1 TESTS -----------------------------------------
###########################################################################################################################

def do_func1_tests(a_dict, word, a_dict_exp, expected):
    a_dict_copy = {k: v[:] for k, v in a_dict.items()}
    res = program.func1(a_dict, word)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero TOTALE di elementi rimossi atteso è {expected} e non {res}. / Total elements removed should be {expected}, but {res} were returned.\n {'*'*50}''')
        return 0
    testlib.checkDict(a_dict, a_dict_exp)
    return 1

def test_func1_1():
    a_dict = {'a':['alpha','beta','gamma'], 'b':['axle','zeta']}
    word = 'aura'
    a_dict_exp = {'a':['beta','gamma'], 'b':['axle','zeta']}
    expected = 1
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_2():
    a_dict = {'a':['alfa','acca','beta','gamma','axa'], 'b':['a','b','z','za']}
    word = 'a'
    a_dict_exp = {'a':['beta','gamma'], 'b':['b','z','za']}
    expected = 4
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_3():
    a_dict = {'x':['top','tip','tap','tup'], 'y':['tot','tit','tat']}
    word = 'trap'
    a_dict_exp = {'x': [], 'y': ['tot', 'tit', 'tat']}
    expected = 4
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

def test_func1_4():

    a_dict = {'data':['start','finish','stut','fat','fun','last'], 'keys':['k1k','k2k','k3']}
    word = 'kek'
    a_dict_exp = {'data':['start','finish','stut','fat','fun','last'], 'keys':['k3']}
    expected = 2
    return do_func1_tests(a_dict, word, a_dict_exp, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 2 TESTS -----------------------------------------
###########################################################################################################################

def do_func2_tests(dictionary, expected):
    res = program.func2(dictionary)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista ritornata è sbagliata! / The returned list is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func2_1():
    dictionary = {4: ["a", "b", "c", "de", "fgh"], 2: ["a", "z", "b", "w"], 0: ["a", "b"]}
    expected = ['fgh', 'de', 'z', 'w', 'c', 'b', 'b', 'a', 'a']
    return do_func2_tests(dictionary, expected)

def test_func2_2():
    dictionary = {3: ["hi", "bye", "hello"], 5: ["five", "six", "seven", "eight"], 1: ["x", "y", "z"]}
    expected = ['five', 'six', 'hi']
    return do_func2_tests(dictionary, expected)

def test_func2_3():
    dictionary = {10: ["a", "aa", "aaa", "aaaaa", "aaaaa"], 6: ["six", "seven", "eight"], 4: ["one", "two", "three", "four"]}
    expected = ['seven', 'eight', 'aaaaa', 'aaaaa', 'two', 'six', 'one', 'aaa', 'aa', 'a']
    return do_func2_tests(dictionary, expected)

def test_func2_4():
    dictionary = {}
    expected = []
    return do_func2_tests(dictionary, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 3 TESTS -----------------------------------------
###########################################################################################################################

def do_func3_tests(a_list,expected):
    res = program.func3(a_list)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}\nexpected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func3_1():
    a_list = ["monkey", "cat", "panda", "alligator"]
    expected = [4, 2, 2, 1]
    return do_func3_tests(a_list, expected)

def test_func3_2():
    a_list = ["RYTHM", "schEdule", "PrOcEss", "rOuTine", "pythagORAS"]
    expected = [4, 3, 3, 2, 0]
    return do_func3_tests(a_list, expected)

def test_func3_3():
    a_list = ["a", "e", "i", "o", "u", "b", "c", "d"]
    expected = [1, 1, 1, 1, 1, 0, 0, 0]
    return do_func3_tests(a_list, expected)

def test_func3_4():
    a_list = ["AaaB", "EeI", "iou"]
    expected = [3, 3, 3]
    return do_func3_tests(a_list, expected)


###########################################################################################################################
# ----------------------------------------- FUNC 4 TESTS -----------------------------------------
###########################################################################################################################

def do_func4_tests(string_list1, string_list2, expected):
    res = program.func4(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 1.5

def test_func4_1():
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark', 'shop', 'cat']
    expected = ['park', 'elephant', 'elichopter']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_2():
    string_list1=['aba', 'aab', 'baa', 'bab', 'abb']
    string_list2=['bab', 'aaa']
    expected = ['aab', 'aba', 'abb', 'baa']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_3():
    string_list1=['zzzzz', 'xxyy', 'abc', 'defg', 'q']
    string_list2=['abc', 'zzzzz', 'q']
    expected = ['xxyy', 'defg']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_4():
    string_list1=['apple', 'banana', 'cherry']
    string_list2=['date', 'elderberry', 'fig']
    expected = ['banana', 'apple', 'cherry']
    return do_func4_tests(string_list1, string_list2, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 5 TESTS -----------------------------------------
###########################################################################################################################
def do_func5(points, expected):
    res = program.func5(points)
    if res != expected:
        my_print(f'''{'*' * 50}\n[ERROR] La tupla ritornata è sbagliata! / The returned tuple is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*' * 50}''')
        return 0
    return 2

def test_func5_1():
    points = [(1, 5), (3, 2), (4, 5), (5, 1), (2, 4)]
    expected = (2, 5)
    return do_func5(points, expected)

def test_func5_2():
    points = [(1, 10), (5, 8), (7, 10), (3, 10), (9, 2)]
    expected = (3, 10)
    return do_func5(points, expected)

def test_func5_3():
    points = [(1, 1), (3, 3), (2, 2), ]
    expected = (2, 2)
    return do_func5(points, expected)

def test_func5_4():
    points = [(3-x, 15-x) for x in range(5)] + [(x*x, 5+x) for x in range(5)]
    expected = (2, 14)
    return do_func5(points, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 6 TESTS -----------------------------------------
###########################################################################################################################

def do_func6_tests(text, expected):
    res = program.func6(text)

    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func6_1():
    text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
    expected = {'s': 2, 't': 3, 'l': 4, 'p': 6, 'n': 3, 'c': 6, 'r': 4}
    return do_func6_tests(text, expected)

def test_func6_2():
    text = 'Nel Mezzo del caMmin Di nostra vita mi ritrovai in una selva oscura che la diritta via era smarrita'
    expected = {'n': 5, 'l': 4, 'm': 5, 'z': 2, 'd': 3, 'c': 3, 's': 4, 't': 6, 'r': 8, 'v': 4, 'h': 1}
    return do_func6_tests(text, expected)

def test_func6_3():
    text = 'This is the question, to be or not to be'
    expected = {'t': 6, 'h': 2, 's': 3, 'q': 1, 'n': 2, 'b': 2, 'r': 1}
    return do_func6_tests(text, expected)

def test_func6_4():
    text = 'b c d f g h j k l m n p q r s t v w x y z'
    expected = {'b': 1, 'c': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
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
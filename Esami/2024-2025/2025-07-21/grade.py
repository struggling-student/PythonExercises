# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
from testlib import my_print, COL, check_expected
from tree import *

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
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
DEBUG = False
# DEBUG = True


#############################################################################

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

# Mock Node class for BinaryTree for EX.1 testing
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # For check_val to compare trees by string representation
    def __str__(self):
        return self._to_str(self)

    def _to_str(self, node):
        if node is None:
            return "None"
        return f"({node.value}, {self._to_str(node.left)}, {self._to_str(node.right)})"

    # Helper to create tree from list format for tests (similar to tree.py's fromList)
    @staticmethod
    def fromList(lst):
        if not lst:
            return None

        nodes = [None] * len(lst)
        # Create all nodes first
        for i, val in enumerate(lst):
            if val is not None:
                nodes[i] = Node(val)

        # Link children
        for i, val in enumerate(lst):
            if nodes[i] is not None:
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2
                if left_idx < len(lst) and nodes[left_idx] is not None:
                    nodes[i].left = nodes[left_idx]
                if right_idx < len(lst) and nodes[right_idx] is not None:
                    nodes[i].right = nodes[right_idx]

        return nodes[0] if nodes else None


import images

def test_personal_data_entry(run=True):
    if 'name' in program.__dict__:
        assert program.name != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'STUDENT_ID', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR STUDENT_ID in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Student info: {program.name} {program.surname} {program.student_id}{COL["RST"]}')
    else:  # Fallback for old variable names if they exist
        assert program.nome != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9


def add_docstring(f, local):
    S = ''
    if 'run' in local: del local['run']
    for key, val in local.items():
        S += f'\n{key} = {val}'
    f.__doc__ = S


###############################################################################
# FUNC.1 Tests
def do_func1_tests(embeddings1, embeddings2, expected):
    res = program.func1(embeddings1, embeddings2)
    testlib.check_val(res, expected)
    return 1.0  # 4 tests * 1.0 point = 4 points


def test_func1_1(run=True):
    embeddings1 = [('king', [0.1, 0.2]), ('queen', [0.3, 0.4])]
    embeddings2 = [('man', [0.05, 0.15]), ('woman', [0.25, 0.35])]
    # Cosine sim (queen, woman) = 0.9997, (king, man) = 0.9887
    expected = ('queen', 'woman', 0.9997)
    return do_func1_tests(embeddings1, embeddings2, expected) if run else None


def test_func1_2(run=True):
    embeddings1 = [('apple', [1.0, 0.0]), ('banana', [0.0, 1.0])]
    embeddings2 = [('red', [1.0, 0.0]), ('green', [0.0, 1.0])]
    # All sims are 1.0 or 0.0. ('apple', 'red') is 1.0, ('banana', 'green') is 1.0
    # Tie-breaking: 'apple' < 'banana', 'red' < 'green'
    expected = ('apple', 'red', 1.0)
    return do_func1_tests(embeddings1, embeddings2, expected) if run else None


def test_func1_3(run=True):
    embeddings1 = [('cat', [0.5, 0.5])]
    embeddings2 = [('dog', [0.5, -0.5]), ('mouse', [0.5, 0.5])]
    # (cat, mouse) sim = 1.0, (cat, dog) sim = 0.0
    expected = ('cat', 'mouse', 1.0)
    return do_func1_tests(embeddings1, embeddings2, expected) if run else None


def test_func1_4(run=True):
    embeddings1 = [('x', [1, 1, 1]), ('y', [0, 0, 0])]  # y has 0 magnitude
    embeddings2 = [('z', [1, 1, 1])]
    # x-z sim = 1.0. y-z sim = 0.0
    expected = ('x', 'z', 1.0)
    return do_func1_tests(embeddings1, embeddings2, expected) if run else None


# FUNC.2 Tests
def do_func2_tests(text_corpus, sentiment_lexicon, top_k_sentences, expected):
    res = program.func2(text_corpus, sentiment_lexicon, top_k_sentences)
    testlib.check_dict(res, expected)
    return 1.0  # 4 tests * 1.0 point = 4 points


def test_func2_1(run=True):
    text_corpus = ["This is a great movie!", "It was terrible.", "What a lovely day."]
    sentiment_lexicon = {'great': 0.8, 'terrible': -0.9, 'lovely': 0.7}
    expected = {
        'overall_sentiment': 0.20,
        'top_positive_sentences': [(0.80, 'This is a great movie!')],
        'total_sentences_analyzed': 3
    }
    return do_func2_tests(text_corpus, sentiment_lexicon, 1, expected) if run else None


def test_func2_2(run=True):
    text_corpus = ["Coding is fun.", "Bugs are annoying.", "Learning is good.", "This is easy.", "Hard problems."]
    sentiment_lexicon = {'fun': 0.5, 'annoying': -0.7, 'good': 0.6, 'easy': 0.4, 'hard': -0.3}
    expected = {
        'overall_sentiment': 0.10,  # (0.5 + -0.7 + 0.6 + 0.4 + -0.3) / 5 = 0.5 / 5 = 0.1
        'top_positive_sentences': [(0.60, 'Learning is good.'), (0.50, 'Coding is fun.')],
        'total_sentences_analyzed': 5
    }
    return do_func2_tests(text_corpus, sentiment_lexicon, 2, expected) if run else None


def test_func2_3(run=True):
    text_corpus = ["Neutral sentence.", "Another neutral one."]
    sentiment_lexicon = {'positive': 0.1, 'negative': -0.1}  # No words from corpus in lexicon
    expected = {
        'overall_sentiment': 0.00,
        'top_positive_sentences': [],
        'total_sentences_analyzed': 2
    }
    return do_func2_tests(text_corpus, sentiment_lexicon, 1, expected) if run else None


def test_func2_4(run=True):
    text_corpus = ["the quick brown fox, is sad.", "lorem ipsum dolor sit amet?", "the goat under the bench is alive!"]
    sentiment_lexicon = {'quick': 0.1, "dolor": -0.9, "alive": 0.5, "sad": -0.9}
    expected = {
        'overall_sentiment': -0.40,
        'top_positive_sentences': [(0.5, 'the goat under the bench is alive!')],
        'total_sentences_analyzed': 3
    }
    return do_func2_tests(text_corpus, sentiment_lexicon, 1, expected) if run else None


# FUNC.3 Tests
def do_func3_tests(sentence_list, forbidden_words, expected_removed_count, expected_remaining_list):
    # Make a copy of the list as it's modified in-place
    original_list_copy = list(sentence_list)
    res_removed_count = program.func3(original_list_copy, forbidden_words)
    testlib.check_val(res_removed_count, expected_removed_count)
    testlib.check_list(original_list_copy, expected_remaining_list)
    return 1.0  # 4 tests * 1.0 point = 4 points


def test_func3_1(run=True):
    sentence_list = ["This is a test sentence.", "Bad words here.", "Another one for good measure."]
    forbidden_words = {"bad", "terrible", "forbidden"}
    expected_removed_count = 1
    expected_remaining_list = ["This is a test sentence.", "Another one for good measure."]
    return do_func3_tests(sentence_list, forbidden_words, expected_removed_count,
                          expected_remaining_list) if run else None


def test_func3_2(run=True):
    sentence_list = ["Hello world.", "Python is great.", "Java is also good."]
    forbidden_words = {"java", "world"}
    expected_removed_count = 2
    expected_remaining_list = ["Python is great."]
    return do_func3_tests(sentence_list, forbidden_words, expected_removed_count,
                          expected_remaining_list) if run else None


def test_func3_3(run=True):
    sentence_list = ["No forbidden words here.", "All clear."]
    forbidden_words = {"secret", "hidden"}
    expected_removed_count = 0
    expected_remaining_list = ["No forbidden words here.", "All clear."]
    return do_func3_tests(sentence_list, forbidden_words, expected_removed_count,
                          expected_remaining_list) if run else None


def test_func3_4(run=True):
    sentence_list = ["Remove this.", "And this too.", "Also this one."]
    forbidden_words = {"this", "one"}
    expected_removed_count = 3
    expected_remaining_list = []
    return do_func3_tests(sentence_list, forbidden_words, expected_removed_count,
                          expected_remaining_list) if run else None


# FUNC.4 Tests
def do_func4_tests(text, n, expected):
    res = program.func4(text, n)
    testlib.check_list(res, expected)
    return 1.0  # 4 tests * 1.0 point = 4 points


def test_func4_1(run=True):
    text = "The quick brown fox jumps over the lazy dog. The fox is quick."
    expected = [('the', 3), ('fox', 2), ('quick', 2)]
    return do_func4_tests(text, 3, expected) if run else None


def test_func4_2(run=True):
    text = "apple banana apple orange banana apple"
    expected = [('apple', 3), ('banana', 2), ('orange', 1)]
    return do_func4_tests(text, 3, expected) if run else None


def test_func4_3(run=True):
    text = "a b a b a c c c d"
    expected = [('a', 3), ('c', 3), ('b', 2)]  # Tie-breaking by word: 'a' then 'c'
    return do_func4_tests(text, 3, expected) if run else None


def test_func4_4(run=True):
    text = "singleword"
    expected = [('singleword', 1)]
    return do_func4_tests(text, 1, expected) if run else None


# FUNC.5 Tests
def do_func5_tests(word_list, expected):
    res = program.func5(word_list)
    # Convert sets in expected to sorted lists for consistent comparison if needed, or just compare sets
    # For comparing dicts with sets as values, direct comparison works if sets are equal.
    testlib.check_dict(res, expected)
    return 1.0  # 4 tests * 1.0 point = 4 points


def test_func5_1(run=True):
    word_list = ["listen", "silent", "Enlist", "apple", "Banana", "apPLe"]
    expected = {
        'eilnst': {'listen', 'silent', 'Enlist'},
        'aelpp': {'apple', 'apPLe'},
        'aaabnn': {'Banana'}
    }
    return do_func5_tests(word_list, expected) if run else None


def test_func5_2(run=True):
    word_list = ["cat", "act", "tac", "dog", "god", "doG"]
    expected = {
        'act': {'cat', 'act', 'tac'},
        'dgo': {'dog', 'god', 'doG'}
    }
    return do_func5_tests(word_list, expected) if run else None


def test_func5_3(run=True):
    word_list = ["a", "b", "c"]
    expected = {'a': {'a'}, 'b': {'b'}, 'c': {'c'}}
    return do_func5_tests(word_list, expected) if run else None


def test_func5_4(run=True):
    word_list = ["Race", "care", "acer", "rAce"]
    expected = {'acer': {'Race', 'care', 'acer', 'rAce'}}
    return do_func5_tests(word_list, expected) if run else None


# EX.1 Tests (Recursive Path to Deepest Node)
def do_test_ex1(root, target_value, expected_result_list):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            # Create a dummy result list for the recursion check
            dummy_result = []
            program.ex1(root, dummy_result, target_value)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Il programma non adotta un approccio ricorsivo / The function does not use recursion")
        finally:
            isrecursive.undecorate_module(program)

    actual_result = [] # This is the list that program.ex1 will populate
    program.ex1(root, actual_result, target_value)
    testlib.check_list(actual_result, expected_result_list)
    return 1.0 # 6 tests * 1.0 point = 6 points

def test_ex1_1(run=True):
    # Tree: 1 (root)
    root = BinaryTree(1, None, BinaryTree(2, None, BinaryTree(3)))
    result = []
    expected = [1]
    return do_test_ex1(root, 1, expected) if run else None

def test_ex1_2(run=True):
    # Tree:
    #    1
    #   / \
    #  2   3
    root = BinaryTree(1, BinaryTree(2), BinaryTree(3))
    result = []
    expected = [1, 2] # Leftmost at depth 1
    return do_test_ex1(root, 2, expected) if run else None

def test_ex1_3(run=True):
    # Tree:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 4   9
    #  / \
    # 8   9
    root = BinaryTree(1,
                    BinaryTree(2,
                         BinaryTree(4,
                              BinaryTree(8),
                              BinaryTree(9)),
                         BinaryTree(5)),
                    BinaryTree(3,
                         BinaryTree(4),
                         BinaryTree(9)))
    result = []
    expected = [1, 2, 4, 9] # Deepest 9 at depth 3
    return do_test_ex1(root, 9, expected) if run else None

def test_ex1_4(run=True):
    # Tree: Same as above
    root = BinaryTree(1,
                    BinaryTree(2,
                         BinaryTree(4,
                              BinaryTree(8),
                              BinaryTree(9)),
                         BinaryTree(5)),
                    BinaryTree(3,
                         BinaryTree(4),
                         BinaryTree(9)))
    result = []
    expected = [1, 2, 4] # Leftmost 4 at depth 2
    return do_test_ex1(root, 4, expected) if run else None

def test_ex1_5(run=True):
    # Tree with multiple deepest, leftmost ties
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   4  <- target 4 at same depth
    #  / \     / \
    # 7   8   9   10
    root = BinaryTree(1,
                    BinaryTree(2,
                         BinaryTree(4,
                              BinaryTree(7),
                              BinaryTree(8)),
                         BinaryTree(5)),
                    BinaryTree(3,
                         BinaryTree(6,
                              BinaryTree(9),
                              BinaryTree(10)),
                         BinaryTree(4))) # Second '4' on the right
    result = []
    # Both 4s are at depth 2. The left one is [1, 2, 4]. The right one is [1, 3, 4].
    # Lexicographically, [1, 2, 4] comes before [1, 3, 4].
    expected = [1, 2, 4]
    return do_test_ex1(root, 4, expected) if run else None

def test_ex1_6(run=True):
    # Target not found
    root = BinaryTree(1, BinaryTree(2), BinaryTree(3))
    result = []
    expected = []
    return do_test_ex1(root, 10, expected) if run else None


# EX.2 Tests (Recursive Flood Fill)
def do_ex2_test(input_image_name, output_image_name, expected_image_name, x, y, replacement_color):
    input_path = f"ex2_test_data/input_images/{input_image_name}"
    output_path = f"ex2_test_data/output_images/{output_image_name}"
    expected_path = f"ex2_test_data/expected_images/{expected_image_name}"

    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            # Call with a valid path to trigger recursion check
            program.ex2(input_path, output_path, x, y, replacement_color)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    # Load the expected image data from the pre-generated file
    expected_image_data = images.load(expected_path)
    if expected_image_data is None:
        raise FileNotFoundError(
            f"Expected image not found at {expected_path}. Please run generate_ex2_test_images.py first.")

    # Call the student's function
    program.ex2(input_path, output_path, x, y, replacement_color)

    # Retrieve the image saved by the student's program
    actual_image_data = images.load(output_path)
    if actual_image_data is None:
        raise FileNotFoundError(f"Output image not found at {output_path}. Program might not be saving correctly.")

    testlib.check_img_file(output_path, expected_path)
    return 1.2  # 5 tests * 1.2 points = 6 points


def test_ex2_1(run=True):
    return do_ex2_test(
        input_image_name="blue_square_on_black.png",
        output_image_name="output_blue_square_fill.png",
        expected_image_name="expected_blue_square_fill.png",
        x=8, y=8, replacement_color=(255, 0, 0)  # Red
    ) if run else None


def test_ex2_2(run=True):
    return do_ex2_test(
        input_image_name="solid_red.png",
        output_image_name="output_solid_red_fill.png",
        expected_image_name="expected_solid_red_fill.png",
        x=0, y=0, replacement_color=(0, 255, 0)  # Green
    ) if run else None


def test_ex2_3(run=True):
    return do_ex2_test(
        input_image_name="checkerboard_32px.png",
        output_image_name="output_checkerboard_fill.png",
        expected_image_name="expected_checkerboard_fill.png",
        x=0, y=0, replacement_color=(0, 0, 255)  # Blue
    ) if run else None


def test_ex2_4(run=True):
    return do_ex2_test(
        input_image_name="green_circle_on_white.png",
        output_image_name="output_green_circle_fill.png",
        expected_image_name="expected_green_circle_fill.png",
        x=0, y=0, replacement_color=(255, 0, 255)  # Magenta
    ) if run else None


def test_ex2_5(run=True):
    return do_ex2_test(
        input_image_name="complex_shape_fill.png",
        output_image_name="output_complex_shape_fill.png",
        expected_image_name="expected_complex_shape_fill.png",
        x=7, y=8, replacement_color=(255, 0, 0)  # Yellow
    ) if run else None

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1, test_ex1_2, test_ex1_3, test_ex1_4, test_ex1_5, test_ex1_6,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4, test_ex2_5,
    test_personal_data_entry,
]

if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(
            f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(
            f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(
            f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
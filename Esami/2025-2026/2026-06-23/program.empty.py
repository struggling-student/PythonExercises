#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER"""

name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

################################################################################
################################################################################
################################################################################

import tree
import images
import os

# %% ---------------------------------- FUNC1 ---------------------------------- #
"""Func 1: 2 points

Write a function func1(students) that receives a list of dictionaries.
Each dictionary has the following keys:
  - 'name' (str): student's name
  - 'scores' (list[int]): list of grades
  - 'bonus' (int): bonus points

The function must compute for each student:
    total = sum(scores) + bonus

The function must return a list of tuples (name, total) sorted:
  1. by total descending,
  2. by name alphabetically, if total is equal.

Examples:
    func1([
        {'name': 'Alice', 'scores': [18, 24], 'bonus': 3},
        {'name': 'Bob',   'scores': [30, 28], 'bonus': 0}
    ]) -> [('Bob', 58), ('Alice', 45)]

    func1([
        {'name': 'Zara', 'scores': [20], 'bonus': 5},
        {'name': 'Anna', 'scores': [20], 'bonus': 5}
    ]) -> [('Anna', 25), ('Zara', 25)]
"""

def func1(students):
    pass

# print(func1([
#     {'name': 'Alice', 'scores': [18, 24], 'bonus': 3},
#     {'name': 'Bob',   'scores': [30, 28], 'bonus': 0}
# ]))
# print(func1([
#     {'name': 'Zara', 'scores': [20], 'bonus': 5},
#     {'name': 'Anna', 'scores': [20], 'bonus': 5}
# ]))

# %% ---------------------------------- FUNC2 ---------------------------------- #
"""Func 2: 2 points

Write a function func2(list1, list2) that receives two lists of strings.
The function must return a list sorted alphabetically and containing,
without repetitions, all the strings that appear in ONLY ONE of the two lists
(symmetric difference).

Examples:
    func2(['a', 'b', 'c'], ['b', 'c', 'd']) -> ['a', 'd']
    func2(['x', 'y'], ['x', 'y']) -> []
    func2([], ['a', 'b']) -> ['a', 'b']
"""

def func2(list1, list2):
    pass


# print(func2(['a', 'b', 'c'], ['b', 'c', 'd']))
# print(func2(['x', 'y'], ['x', 'y']))
# print(func2([], ['a', 'b']))
# %% ---------------------------------- FUNC3 ---------------------------------- #
"""Func 3: 2 points

Write a function func3(pairs) that receives a list of pairs
(word, definition), where word and definition are strings.

The function must build and return a dictionary with:
  - key: the first letter (lowercase) of each word
  - value: the alphabetically sorted list of the words whose definition
    contains AT LEAST 5 words (separated by spaces)

Examples:
    func3([
        ("colubro","serpente molto molto velenoso che striscia"),
        ("cane",   "animale domestico a quattro zampe"),
        ("gatto",  "felino domestico"),
        ("casa",   "edificio per abitare")
    ]) -> {'c': ['cane', 'colubro']}
    # "gatto" excluded (definition has only 2 words < 5)
    # "casa"  excluded (definition has only 3 words < 5)
    # "cane" has a definition with 5 words -> included under 'c'
    # "colubro" has a definition with 6 words -> included under 'c' after 'cane'
"""

def func3(pairs):
    pass

# func3([
#     ("colubro","serpente molto molto velenoso che striscia"),
#     ("cane",   "animale domestico a quattro zampe"),
#     ("gatto",  "felino domestico"),
#     ("casa",   "edificio per abitare")
# ])
# %% ---------------------------------- FUNC4 ---------------------------------- #
"""Func 4: 4 points

Write a function func4(input_path, output_path) that receives two strings
representing file paths.

The input_path file contains one word per line (no spaces).

For each word, the function counts the number of vowels (a, e, i, o, u),
IGNORING case differences.

Then it must write to output_path, one line per word, in the format:
    word:number_of_vowels

The lines must be sorted by:
  1. number_of_vowels descending
  2. if equal, word alphabetically

The function returns the TOTAL number of words that contain
AT LEAST ONE vowel.

Examples:
    If input_path contains:
        Ciao
        Mondo
        Xyzzy
        Python
        Gatto
    The output file will contain:
        Ciao:3
        Gatto:2
        Mondo:2
        Python:1
        Xyzzy:0
    (Note: 'Python' has 1 vowel, 'Ciao' has 3, 'Mondo' and 'Gatto' have 2)
    and the function returns 4 (Xyzzy has no vowels).
"""

def func4(input_path, output_path):
    pass


# %% ---------------------------------- FUNC5 ---------------------------------- #
"""Func 5: 8 points

Write a function func5(input_path, output_path) that loads a PNG image
from input_path, finds all non-black pixels and for each non-black color found,
it computes the minimum rectangle that contains all pixels of that color
(bounding box: row_min, row_max, col_min, col_max).

The function must draw the border of each bounding box in that color on
the image and save the resulting image to output_path.
WARNING: rectangles must be drawn in order of increasing colors
(i.e. by increasing R, if tied by increasing G, if tied by increasing B)

Return the number of colors found.

If there are no non-black pixels, return 0 and save a copy of the original
image.

Use images.load() and images.save() to load and save images.

Example:
    10x10 image with three pixels at (3,6), (5,2) and (2,8)
    -> result 1
       rectangle with corners at (2,2) and (5,8)

"""

def func5(input_path, output_path):
    pass


# %% ----------------------------------- EX1 ----------------------------------- #
"""Ex 1: 7 points

Write a RECURSIVE function ex1(root) that receives a binary tree
(of class tree.BinaryTree) and returns a tuple (depth, value),
where:
  - depth is the maximum depth (number of edges from the root) of the
    deepest leaf (if the root is a leaf, depth = 0)
  - value is the value of the deepest leaf; if there are multiple leaves
    at the same maximum depth, it returns the maximum value among them.
If the tree is None (empty), it returns (None, None).

Examples:
    Tree:       1
            |---|---|
            2       3
        ex1(tree) -> (1, 3)  (depth 1, leaves with values 2 and 3 -> max = 3)

    Tree:           1
                |---|---|
                2       3
            |---|---|
            4       5
        leaves: 4 (depth 2), 5 (depth 2), 3 (depth 1)
        ex1(tree) -> (2, 5)  (max depth = 2, max value = 5)

    Tree (single root 42):
            42
        ex1(tree) -> (0, 42)

    Empty tree: ex1(None) -> (None, None)
"""

def ex1(root):
    pass


# %% ----------------------------------- EX2 ----------------------------------- #
"""Ex 2: 7 points

Write a RECURSIVE function ex2(nested, depth=0) that receives a nested list
of integers (i.e. a list that may contain integers or other nested lists).
The function returns a new list containing all integers that are at an EVEN depth.

Depth is counted as follows:
  - the outermost list is at depth 0
  - each time you enter a nested list, the depth increases by 1.

Therefore integers directly in the main list are at depth 0
(EVEN -> included), integers inside its nested lists are at depth 1
(ODD -> excluded), those in a nested-nested-list are at depth 2
(EVEN -> included), and so on.

The depth=0 parameter is for recursion, it must not be changed in
external calls.

The collected values in the final list must be in the same order
as they are visited in a preorder traversal.

Examples:
    ex2([1, [2, 3], 4]) -> [1, 4]
        (1 and 4 are at depth 0, 2 and 3 are at depth 1)

    ex2([1, [2, [3, 4], 5], 6]) -> [1, 3, 4, 6]
        (1,6: depth 0 included; 2,5: depth 1 excluded; 3,4: depth 2 included)

    ex2([]) -> []
    ex2([[1]]) -> []
        (1 is at depth 1 -> excluded)
"""

def ex2(nested, depth=0):
    pass


######################################################################################

if __name__ == '__main__':
    print('Run grade.py for automatic testing.')

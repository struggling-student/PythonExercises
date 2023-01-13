#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number
"""
name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To check the error stack trace, you can uncomment the dedicated line in
# testlib.py (see the comment in the body of function runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #

""" Ex 1: 6 points

Part 1)
A dictionary D is given as input. D has integer keys and its values are
lists of integers with repetitions.

D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}

Write the function ex1(D, list_rm) that builds and returns the "inverse"
dictionary W that:
 - contains a key for each integer present in the value lists
 - the values associated to each W key are lists of the D keys
   that had that value in D, repeated as many times as the value was
   repeated in D

The inverse dictionary W must have each list associated to each key
sorted so that even numbers appear first and then odd numbers; then
even numbers must be ordered in decresing order while odd numbers in
increasing order.

The above example should return:

    W = {6: [2], 4: [2, 1, 1, 1], 2: [1], 3: [2, 1], 5: [2]}

Part 2) Extend the ex1(D, list_rm) function to destructively delete
from D all the integers of the D lists that are contained in list_rm
(a list of integers).
If, after the removal, a list is empty, the corresponding key must be deleted.

Example: if  D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
         and list_rm = [4, 3, 2, 5]
         D must be destructively changed to {2: [6]}
         as all values except 6 have been deleted
         and 1 remained with an empty list.
"""
def ex1(D, list_rm):
    # INDERT YOUR CODE HERE
    pass


# ----------------------------------- EX.2 ----------------------------------- #

''' Ex 2: 8 points
    Implement the function  ex2(grid, path) that takes as arguments:
    - grid: a 2 dimentional matrix represented as lists of lists
    - path: a string
    The function returns a list.

    The path string represents a series of moves in the grid.
    We start from the 0,0 top/left corner.
    The possible moves are: 'L' (left), 'R' (right), 'U' (up), 'D' (down), 'S' (stay).
    If a move brings you out of the grid, you reenter from the opposite side.
    If a move is an unknown character the walk stops.
    The function returns the list of values encountered by moving in the grid
    by following the path movements.

    Example:
        Supposing the grid is:
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
        If path = 'RRDS',   the returned list will be [2,3,7,7],
        If path = 'RRUSRR', the returned list will be [2,3,1,1,2,9],
        If path = 'DDXUU',  the returned list will be [5, 9].
'''
def ex2(grid, path):
    pass
    ### INSERT HERE YOUR CODE

# ----------------------------------- EX.3 ----------------------------------- #

''' Ex 3: 9 points
    implement the ex3(root, depth) function, recursive or using recursive functions,
    with arguments:
    - root:  the root of a binary tree
    - depth: an integer
    The tree is made of instances of the BinaryTree class defined in tree.py.
    The function should return the product of the sum of all left son nodes
    times the sum of all right son nodes that are at the given depth in the
    tree (assuming the root is at depth 0).

    Example:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    If the tree is the left one and depth=2, the function returns
    9*(1+3)=36.
    If the tree is the right one and depth=3, the function returns
    (2+8+2)*(-1+1+3+9)=144.
    '''
from tree import BinaryTree

def ex3(root, depth):
    pass
    ### INSERT HERE YOUR CODE


# ----------------------------------- EX.4 ----------------------------------- #

''' Ex 4: 9 points
    Implement the ex4(dirin, dirout, depth) function, recursive or using recursive
    functions or methods, that receive the arguments:
    - dirin:  the path of an input directory
    - dirout: the path of an output directory
    - depth:  an integer
    The function must build inside the dirout directory a file for each text
    file (.txt) found in dirin or in one of its subdirectories at the indicated depth
    (assuming dirin is at depth 0).
    The directory structure containing the txt files must be recreated
    under dirout.

    Each txt file created under dirout must contan the same content of the
    dirin file, with the case swapped ( lowercase <-> uppercase ).
    All non-alpha chars must be left as they are.
    The function returns the total number of chars written in the files
    created under dirout.

    NOTICE: you could find useful the functions: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTICE: it is forbiddent to use the os.walk function

'''

import os

def ex4(dirin, dirout, depth):
    pass
    ### INSERT HERE YOUR CODE

# --------------------------------------------------------------------------- #

if __name__ == '__main__':
    pass
    ### INSERT HERE YOUR TESTS


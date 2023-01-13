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
''' Ex 1: 7 points
    Implement a function that takes three file names as input and
    returns a pair of integers.
    The parameters file1 and file2 are strings containing the names of
    two text files. These files contain, on each line, a series of
    strings separated by spaces, tabs, commas, or semicolons.
    The function must write inside a new file indicated by
    the input parameter file3 a line for each line in file1 whose
    corresponding line in file2 has at least one string in common.
    In particular:
        - given the strings of the i-th row of file1, if the i-th row
          in file2 contains at least one of those strings, then in file3
          there will be a line with all strings in common.
        - The common strings are written in the lines of file3 separated
          by spaces. They are ordered by increasing number of
          characters and, in case of equal number, in alphabetical order.
        - The rows in file3 have the same order as the source rows.
    The function returns a tuple in which the first and the second element
    are, respectively, the number of strings and the number of rows
    written in file3.
'''


def ex1(file1, file2, file3):
    ### INSERT YOUR CODE HERE
    pass

# ----------------------------------- EX.2 ----------------------------------- #


''' Ex. 2: 7 points
    Write a function ex2(gridFilePath) that, given a NxN grid stored
    in a json file as a list of lists, returns a positive integer. In
    the given grid, each cell can have one of three values:
     - the value 0 representing an empty cell;
     - the value 1 representing a fresh orange;
     - the value 2 representing a rotten orange.
    Every minute, any fresh orange that is horizontally or vertically
    adjacent to a rotten orange becomes rotten.

    The function must return the minimum number of minutes that must
    elapse until no cell has a fresh orange. If that is impossible, it
    must return -1.

    For example, given the grid:
    [[2,1,1],
     [1,1,0],
     [0,1,1]]
    the function will return 4.

    While, given the grid:
    [[2,1,1],
     [0,1,1],
     [1,0,1]]
    the function will return -1.

    Note: You can use json.load() to get the grid.
'''


import json

def ex2(gridFilePath):
    ### INSERT YOUR CODE HERE
    pass


# ----------------------------------- EX.3 ----------------------------------- #

''' Ex 3: 9 points
    Implement a recursive function that takes as input a pair of
    strings "a" and "b", and an integer "k" and returns a list.  In
    the returned list are contained all the possible strings that can be
    obtained from the concatenation of a substring of length k of the
    first string with a substring of length k of the second
    string. The returned list is sorted with respect to the position
    of the substring of "a" in "a" and, in case of tie, with respect
    to the substring of "b" in "b".


    example: ex3('casa', 'riccio', 3) returns the list:
     ['casric', 'casicc', 'cascci', 'cascio', 'asaric', 'asaicc',
     'asacci', 'asacio']

    NOTICE: please do not place your recursive function inside another
    function, else the test system will not detect it and all test
    will fail.
'''


def ex3(a, b, k):
    ### INSERT YOUR CODE HERE
    pass


# ----------------------------------- EX.4 ----------------------------------- #

'''Ex. 4: 9 points

    Write a function ex4(folderPath), recursive or using recursive
    function/methods, that, given the path of a folder being the root of a
    folder tree containing text files only, creates and returns a
    dictionary in which:

     - there is one pair (key, value) for each text file that was
       found in the folderPath folder or, recursively, in any of
       its subfolders;
     - each key is the path of a text file, relative to the root folderPath
       folder received by the first call to ex4;
     - the corresponding value is an integer, obtained as the sum of
       the unicode equivalent of all the characters in the text file (the
       newline characters are NOT included in the sum).

    For example, given the following folder tree:

    ex4
      |-f1
         |-f1-1

    and the following files:

    ex4/t1.txt          -   file content: hello world
    ex4/f1/f1-1/t2.txt  -   file content: let's count to 3, 1-2-3

    ex4("ex4") will return the dictionary
    {'ex4/t1.txt': 1116, 'ex4/f1/f1-1/t2.txt': 1722}
    as the sum of the unicode equivalent of "hello world" is 1116,
    while the one of "let's count to 3, 1-2-3" is 1722.

    NOTICE: it's forbidden to use the os.walk function.
    NOTICE: please do not place your recursive function inside another
    function, else the test system will not detect it and all test
    will fail.
'''

import os

def ex4(folderPath):
    ### INSERT YOUR CODE HERE
    pass

# ----------------------------------- END ----------------------------------- #


if __name__ == '__main__':
    # Insert your own tests here
    pass

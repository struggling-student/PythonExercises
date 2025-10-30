#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER

To pass the exam you must:
    - solve at least 3 exercises of type func AND;
    - solve at least 1 exercise of type ex (recursive problem) AND;
    - obtain a score greater than or equal to 18

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "NAME"
surname = "SURNAME"
student_id = "MATRICULATION NUMBER"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 points
Define the function func1(D1, D2),
which receives as arguments two dictionaries D1 and D2: D1 has strings as keys
and integers as values, while D2 has integers as keys and strings as values.
The function must find all the values of D1 that are keys of D2 and return
a list obtained concatenating the corresponding keys of D1 with the corresponding
value of D2. The list must be sorted in decreasing order of length and, in case
of a tie, in ascending alphabetical order.

Example:
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
D2 = {4:'bb', 1:'ff', 2:'ggg'}

Result: ['bbggg', 'aaff', 'ccff', 'ebb']
'''

def func1(D1,  D2):
    ## Write your code here
    pass
## Tests
# D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
# D2 = {4:'bb', 1:'ff', 2:'ggg'}
# print(func1(D1, D2))  # ['bbggg', 'aaff', 'ccff', 'ebb']

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Define a function func2(l) that takes a list of int l as input and modifies
the list so that the element in position i is the sum of all the elements
from position 0 to i. The function returns the value of the last element
of the modified list.

Example: if l = [3, -3, 6, -1, 10], the call func2(l) returns the value 15
    and modifies l in [3, 0, 6, 5, 15].
'''
def func2(l):
    ## Write your code here
    pass

## Tests
# l = [3, -3, 6, -1, 10]
# print(func2(l) )
# print(l)
# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Define a function func3(words, l) that that takes as input:
    - a set of strings 
    - an int
and returns a new set with all the strings of length at least l in the set
words that are a substring of another string in words.

Example: if words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
the call func3(words, 3) should return the set
{'cat', 'bert'}
'''

def func3(words, l):
    ## Write your code here
    pass

## Tests
# print(func3({'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}, 3))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 points
Define a function func4(file_in, file_out, length, chars) that takes as input:
    -two strings representing the paths of two text files
    -an integer length,
    -a string chars.
The function must return the list of all the words found in the file pointed
by file_in with a length at least length and containing at least one of the
characters in the string chars.
The list must be sorted by decreasing length and, in case of a tie, in
alphabetical order.
Moreover, the function must write the words of the list in output in the
file pointed by file_out separated by a whitespace.

Example: func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd')
     should return the list ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
     and write the string 'hippopotamus elephant cobra horse panda snake' in func4/out_01.txt.
"""

def func4(file_in, file_out, length, chars):
    ## Write your code here
    pass

## Tests
# print(func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd'))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Define a function func5(input_png, output_png, m, M) which takes as inputs
    - the path to an image stored in a .png file named input_png,
    - the path to an output png file output_png
    - two ints m and M.
The input image contains several colored horizontal lines on a black background. 
The function has to find the lines with a length included in the range [m, M]
and create a new image with only those found lines.

The function returns the difference between the number of lines found in
the input and those in the output image.
"""
import images

def func5(input_png, output_png, m, M):
    ## Write your code here
    pass

## Tests
# print(func5('func5/func5_test1.png', 'func5/func5_out1.png', 1, 20))
# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(chars, l), recursive or using recursive functions
or methods, that takes as input a set of characters (strings of length one)
and an int l and outputs the set of all the possible palindrome strings of
length l made of characters taken from chars.
Ex:
    ex1({'a', 'b', 'c'}, 3) must return the set {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}

"""
def ex1(chars, l):
    ## Write your code here
    pass

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

Define a function ex2(root), recursive or using recursive functions
or methods, that takes as input root an instance of a BinaryTree as defined
in the tree module, representing the root of a binary tree with int values.
The function must return a pair (v, l) with the value and the level of the
node of the tree with the max product v*l. In case of more nodes with
the same product, the function returns the one with the minimum level.
Assume that the root is at level 1.

For example, if input is the root of following tree:

               6
              / \
             5   16
            /   / \
           4   10  6
              /   / \
             7   8  1
             
there are two nodes with maximum product v*l=32, namely 8*4 and 16*2, thus
the function should return the pair (16, 2).
"""
import tree

def ex2(root):
    ## Write your code here
    pass

# Tests
T = tree.BinaryTree.fromList([6, [5, [4, None, None], None ], [16, [10, [7, None, None], None],
                                                                [6, [8, None, None], [1, None, None]]]])
# print(ex2(T))

###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

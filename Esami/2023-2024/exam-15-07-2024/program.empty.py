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

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 marks
Let us define the function func1(L) which, receiving as an argument a list of strings L,
returns a list of tuples. Each tuple contains two elements: the first one is the length 
of the original string, the second one is the number of vowels (aeiou) in the
original string, ignoring the case. 
The list of tuples must be sorted in descending order with respect to the number
of vowels and, in case of equal length, in alphabetical order (of the original strings).

For example:
L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
risultato = [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]
'''
def func1(L):
    ## your code goes here
    pass

# L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
# print(func1(L)) # risultato = [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 marks
Let us define the function func2(D) which, receiving as an argument a dictionary D,
containing integer values as keys and lists of strings as as values, returns a set of tuples. 
Each tuple contains three elements: the first one is the key, the second one
is the first word of the list of strings in alphabetical order, the third one is
the last word of the list of strings in alphabetical order.

For example:
D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
result = {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}
'''
def func2(D):
    ## your code goes here
    pass
    
# D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
# print(func2(D)) # {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 marks
Let us define the function func3(L1, L2) which, receiving as arguments
two lists of strings L1 and L2, returns a dictionary that contains the strings
found only in L1 as keys and the strings found only in L2 as values.
Each key is a L1 string having the same length of the L2 strings contained in the
corresponding set.

For example:
L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip']
result = {'elefante': {'paperino'}, 'oca': {'cip'}, 'casa': {'topo'}}
'''

def func3(L1, L2):
    ## your code goes here
    pass

# L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
# L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip']
# print(func3(L1, L2)) # {'elefante': {'paperino'}, 'oca': {'cip'}, 'casa': {'topo'}}

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 marks
Let us define the function func4(file_input, file_output) which,
receiving as an argument the path to a text file file_input,
containing words separated by spaces and other nonalpha characters,
creates a text file file_output which contains the same words as
file_input, WITHOUT REPETITIONS, and with the following rules:
1. words beginning with the same letter, regardless of whether
uppercase or lowercase, must be on the same line in descending alphabetical order;
2. rows must be sorted in ascending alphabetical order with respect
to the first word in each row.

The function returns the number of words read from the file and
the total number of characters read from the input file.

For example:
If the input file contains the 20 words:
    casa cane,gatto topo
    paperino!ragno topo
    cane cip:cip
    casa cane£gatto topo
    paperino'ragno topo
    cane cip^cip
the resulting file is:
    cip casa cane
    gatto
    paperino
    ragno
    topo
and the function returns (20, 156)
"""

def func4(input_filename, output_filename):
    ## your code goes here
    pass

# print(func4('func4/in_0.txt', 'func4/out_0.txt')) # (20, 156)

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 marks
Let us define the function func5(input_png, output_png, S) which,
receiving as an argument the path to a .png file input_png,
and an integer S, creates an output png file output_png containing
the input image, split into SxS squares, in which each 
square is rotated clockwise by 90°, respect to the input image.
Note: If there are squares that overhang to the right or below,
they should not be rotated.

The function returns the number of rotated squares.

For Example:
given the input image func5/3cime.png and S=50,
the output image is the same as in func5/3cime_expected.png
and the function returns 15.
"""
import images

def func5(input_png, output_png, S):
    ## your codeg goes here
    pass

# print(func5('func5/3cime.png', 'func5/3cime-rotated-50.png', 50)) # 15
# print(func5('func5/3cime.png', 'func5/3cime-rotated-13.png', 13)) # 294

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks

Define the function ex1(string, l), recursive or using recursive functions
or methods, that takes as input a string and an integer l and returns
the set with all the possible anagrams of length l without any double
character that can be built with the characters in string.
If l is bigger than the length of the string, the returned set is empty.

For example:
    ex1('aabca', 4) should return the set
    {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}

"""
import os

def ex1(string, l):
    ## your code goes here
    pass

# print(ex1('aabca', 4)) # {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}
# print(ex1('aabca', 5)) # {'abaca', 'acaba'}

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 6 marks

Define a function ex2(root), recursive or using recursive functions
or methods, that takes as input a tree with int values, instance of
the tree.BinaryTree class.
The function has to modify the tree in place so that every node with
two childs has the left child smaller than the right one. The exchange
has to swap the whole trees, not only the values.
The function has to return the height of the tree. 

For example, if the input tree is:

               6
              / \
             5   3
            /   / \
           4   10  6
              /   / \
             7   8  1
             
the function modifies it in this way:

                6
              /   \
             3     5
            / \   /
           6  10  4
          / \  /  
         1  8 7   
                 
The function returns the value 4
"""
import tree

def ex2(root):
    ## your code goes here
    pass

# T = tree.BinaryTree.fromList([6, [5, None, [4, None, None] ], [3, [10, [7, None, None], None],
#                                                               [6, [8, None, None], [1, None, None]]]])
# print(T)
# print(ex2(T))
# print(T)
    
# %% 
###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

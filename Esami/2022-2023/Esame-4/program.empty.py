#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 ex problem
    - get a score greater or equal to 18

The final score is the sum of the solved problems.
Important: set DEBUG = True in grade.py to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False!
"""
name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 points

Implement the function func1(a_dict, word) that takes as input a
dictionary 'a_dict' and a word 'word'. Each key in the dictionary is
a string that has a list of strings as its value. The function must
remove from the dictionary all those keys associated with a list
that contains the string 'word'.  The function returns the number of
keys removed from the dictionary 'a_dict'.

Example: if a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
  the invocation of func1(a_dict, 'b') must return 2 and
  a_dict must result modified to {'c':['a', 'c']}.
  In fact: the key 'a' is removed because the list ['a','b','c']
  contains 'b'; the key 'b' is also removed because the list
  ['a','b'] contains 'b'.

'''

def func1(a_dict, word):
    # YOUR CODE HERE
    pass

# a = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
# print(func1(a, 'b'))
# print(a)


# %%  ---- FUNC2 ----
''' func2: 2 points
Implement the function func2(a_string) that takes as input a
string 'a_string' and returns another string. The new string has
all the letters of the input string repeated once and in
reverse alphabetical order.

Example: if a_string='welcome' the invocation of func2(a_string) shall
         return the string 'womlec'

'''

def func2(a_string):
    # YOUR CODE HERE
    pass

# print(func2('welcome'))


# %%  ---- FUNC3 ----
'''  func3: 2 points
Implement the function func3(string_list1, string_list2) that takes
as input two lists of strings with the same number of elements and
returns a new list consisting of the strings obtained by
concatenating:
 - the first string of the first list with the last string of the
   second list,
 - the second string of the first list with the second-to-last string
   of the second list,
 - and so on.
The resulting list should be sorted by number of characters
ascending, in case of a tie, in alphabetical order.

Example: if string_list1=['so', 'sin', 'vas', 'rin', 'vul'] and
            string_list2=['cane', 'casai', 'to', 'cero', 'sia']
         the invocation of func3(string_list1, string_list2) shall return
         the list ['sosia','vasto','sincero','vulcane','rincasai']

'''


def func3(string_list1, string_list2):
    # YOUR CODE HERE
    pass

# string_list1=['so', 'sin', 'vas', 'rin', 'vul']
# string_list2=['cane', 'casai', 'to', 'cero', 'sia']
# print(func3(string_list1, string_list2))


# %%  ---- FUNC4 ----
''' func4: 6 points

Implement the function func4(input_file, output_file) that takes in
input two strings, 'input_file' and 'output_file' representing
the paths to two files.  Within the file pointed by 'input_file'
there are on a single line a series of words (composed of
alphabetic characters) separated by commas, spaces, semicolons and by
periods.
The function must locate all the words in the file
indicated by 'input_file' and write them within a new file
indicated by 'output_file'.  The words must be written
within the file on a single line terminated by the character of
new line, separated by a space and in the following order:
    - increasing number of characters,
    - in case of a tie, in alphabetical order, regardless of
      upper and lower case
    - in case of identical words, in lexicographic order.
The function must return the number of words written in the file in
output.

Example: if the content of the file 'input_file' is as follows
Dog,cat,dog;cat.bird car

the invocation of func4('input_file', 'output_file') must write in the
'output_file' file the following line
car Cat cat dog dog bird

and return the value 6.
'''

def func4(input_file, output_file):
    # WRITE HERE YOUR CODE
    pass

# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
# print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %%  ---- FUNC5 ----
''' func5: 8 points

Implement the function func5(input_pngfile) that takes as input
a string containing the path to a file with an image in
PNG format.
The image pointed by 'input_pngfile' contains a series of
white pixels on a black background. The function must locate all
rectangles defined by four white pixels that can be
considered the edges of those rectangles (see the
example image in func5/image01.png).

It can be assumed that:
    - each row has at most two white pixels and
    - each column has at most two white pixels.

The function must return a list containing the area of all rectangles
identified in the image, sorted by increasing size.

Example: in the image of the file func5/image01.png there are the edges of the
         rectangle (5,5), (45,5), (5,25), (45,25) with area 861
         and of the rectangle (10,10), (20,10), (10,20), (20,20) with area 121
         and there is a pixel in (31, 15), so the invocation of
         func5('func5/image01.png') must return the list [121, 861].
         The edges given above are in the format:
         top-left, top-right, bottom-left, bottom-right.
         The coordinates are (x,y).
'''

import images

def func5(input_pngfile):
    # WRITE HERE YOUR CODE
    pass

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ----------------------------------- #
'''
Ex1: 6 points
Implement the recursive function ex1(directory), or that
uses a recursive function, which takes as input a string
'directory' representing the path to a directory.
The function must recursively explore the directory tree starting
from 'directory' and return a dictionary.
The keys of the dictionary are the paths to the subdirectories of
'directory', in string form.
The value of a directory key is a set of strings with the names
of those '.txt' files in 'directory' for which the first character
of the file contents is equal to the last character.
If a directory contains no .txt files with that characteristic,
then that directory does NOT appear in the dictionary.

Example: if the function is called on 'ex1/A', it returns:

{'ex1/A/B': {'b.txt'}, 'ex1/A/C': {'c.txt'}}

since ex1/A/B/b.txt and ex1/A/C/c.txt are the only files in which
the first character of the contents is equal to the last ('k' for the first,
'a' for the second file, respectively).

NOTE: It is forbidden to use the os.walk function. You can use:
  os.listdir, os.path.isfile, os.path.exists, etc.  To concatenate the
  path, use the concatenation operation with the character '/'

NOTE: We strongly recommend dividing the exercise into subproblems
  dividing into functions for each subproblem.
'''

import os

def ex1(root):
    # WRITE HERE YOUR CODE
    pass

# print(ex1('ex1/A'))
# print(ex1('ex1/B'))
# print(ex1('ex1'))


# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 6 points
Implement the function ex2(root), recursive or that makes use of a
recursive function, that receives as input the root of
a binary tree, as defined in the `BinaryTree` class of the module
tree.py.  The input tree has strings as values.
The function must return the string resulting from the concatenation of
all the values associated with the nodes in the tree with the following rule:
  - concatenation occurs with the order LNR if the node is located
    in an even level
  - with the order RNL if the node is in an odd level
where L is the left subtree, N is the node, and R is the right subtree.
The root is assumed to be at level 0.

Example:
        ______A______                        ______A______
       |             |                      |             |
       B__        ___C___                __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F             _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                                      H   I      J  K   L   M   N

  If the tree is the one on the left, the function must return
  the string 'DBAFCE'.

  If the tree is the right tree, the function must return the
  string 'EJBHDIAMGNCKFL'

'''

def ex2(root):
    # WRITE HERE YOUR CODE
    pass


# from tree import BinaryTree
# root = BinaryTree.fromList(['A', ['B',None,['D',None,None]], ['C', ['E',None,None], ['F',None,None]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',None,None],['I',None,None]],['E',None,['J',None,None]]], ['C', ['F',['K',None,None],['L',None,None]], ['G',['M',None,None],['N',None,None]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',['L',None,None],None],None],['E',None,['I',None,None]]],['C', ['F',['J',None,None],None],['G',None,['K',None,['M',None,None]]]]])
# print(ex2(root))
###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

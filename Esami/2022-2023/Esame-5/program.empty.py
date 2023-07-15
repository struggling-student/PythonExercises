#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER

To pass the exam you are required to:
    - solve at least 3 func problems,
    - solve at least 1 rec problem, and
    - obtain a score of 18 or greater

The final score is the sum of the scores associated with each problem.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "NAME"
surname = "SURNAME"
student_id = "MATRICULATION NUMBER"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 marks

Define the function func1(list_a, list_b, list_c) that takes as input
three lists containing strings. The function returns all the
strings that appear in all the three lists, without repetition.
The resulting list must be sorted alphabetically.

For example:
    list_a = ['goofy', 'pluto', 'minnie', 'minnie','goofy']
    list_b = ['archimedes', 'goofy', 'pete', 'minnie', 'goofy']
    list_c = ['goofy', 'pluto', 'gladstone', 'goofy', 'archimedes','minnie']
both 'minnie' and 'goofy' are in all the three lists so the function returns
['goofy', 'minnie'], in alphabetical order.
'''

def func1(list_a, list_b, list_c):
    # your code goes here
    pass

# list_a = ['goofy', 'pluto', 'minnie', 'minnie','goofy']
# list_b = ['archimedes', 'goofy', 'pete', 'minnie', 'goofy']
# list_c = ['goofy', 'pluto', 'gladstone', 'goofy', 'archimedes','minnie']
# print(func1(list_a, list_b, list_c))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 marks

Define a function func2(d1, d2) that takes as input two dictionaries
d1 and d2 and returns a new dictionary d3. d1 and d2 keys are strings,
while values are lists of integers. d3 must contain only the keys that
are both in d1 and d2. Given a key that is in d1 and d2, the new value
associated with that key is the concatenation of the lists taken from
d1 and d2.

For example:
    d1 = {'goofy': [5, 2],
          'pluto': [1, 2, 3],
          'gladstone': [50, 50]}

    d2 = {'gladstone': [5, 23, 2],
          'donald': [3, 2, 1],
          'pluto': [10, -1]}

    expected = {'gladstone': [50, 50, 5, 23, 2], 'pluto': [1, 2, 3, 10, -1]}
'''

def func2(d1, d2):
    # your code goes here
    pass


# d1 = {'goofy': [5, 2, ],
#       'pluto': [1, 2, 3],
#       'gladstone': [50, 50]}
#
# d2 = {'gladstone': [5, 23, 2],
#       'donald': [3, 2, 1],
#       'pluto': [10, -1]}

# print(func2(d1,d2))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 marks

Define a function func3(string_list1, string_list2) that takes as
input two lists of strings with the same number of items.  Each pair
of strings taken from the same position in string_list1 and
string_list2 always have the same length.

For example: if  string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
                 string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

'sIN' has the same length as 'cas', 'VUL' has the same length as
'sia', and so on.

The function must return a new list computed from string_list2 by
applying the following rules:
- the case of the characters of the strings in string_list1
  determine the case of the characters of the strings in
  string_list2
- in particular, if a character of a string in string_list1 is
  lowercase, then the corresponding character in the new string must
  be taken from the corresponding character of the corresponding
  string in string_list2 by taking it in lowercase

- conversely, if a character of a string in string_list1 is UPPERCASE,
  then the new character must be taken from the corresponding
  character of the corresponding string in string_list2 by taking it
  in UPPERCASE
- if a character is neither lowercase nor UPPERCASE it is left
  unchanged

The lists may contain empty strings.  The new list should be sorted in
descending order according to the length of the strings; in case of a
tie, in alphabetical order.

         
For example: given the input above, the invocation of
func3(string_list1, string_list2) should return the list
    ['cE', 'SIA', 'TOO', 'cAs', 'ceo']
That is, 'ce' --> 'cE' as 'sO' starts with a lowercase 's', while the
second character 'O' is UPPERCASE.

NOTE: use the string functions isupper(), lower() etc.
'''


def func3(string_list1, string_list2):
    # your code goes here
    pass

# string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
# string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

# print(func3(string_list1, string_list2))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 marks
Define a function func4(input_file, output_file) that takes as
input two strings, 'input_file' and 'output_file' representing
the paths to two files.  The file 'input_file' contains a matrix,
in such a way that each line of the file is a row of the matrix.
For example, func4/func4_test1.txt contains:

1,    2, 3
 4, 5,      6
7,   8,    9

The function must read the file 'input_file' and write a matrix by
adding the square brackets to each row and by removing all the spaces
except the first one, so that the content of 'output_file' will have
the following content:

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

The function must return the number of items in the matrix, 9 in the
example above.  Check 'func4/func4_test1.txt' to see the input and
'func4/func4_exp1.txt' to see the expected output.  """


def func4(input_file, output_file):
    # your code goes here
    pass


# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
# print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 marks

Define a function func5(input_pngfile) that takes as input a string
containing the path to file with a PNG image.  The image in
'input_pngfile' contains black and white pixels only.  The function
must identify and return in a list all the horizontal segments made of
sequences of white pixels. Each row of the image can have 1 segment
max.  Moreover, the length of a segment can go from 1 pixel to the
image width.

The function must return a list in which each horizontal segment is
encoded as a tuple (y, xstart, xend), where:
- y is the row number,
- xstart is the horizontal position of the first pixel of the segment
- xend is the horizontal position of the last pixel of the segment.
The list must be sorted in ascending order based on the y-coordinate.

For example given the following image:

 0 1 2 3 4 5
0. . . . . .
1. . . . . .
2. . x . . .
3. . . . . .
4. . . . . .
5x x x x x x

where . is black and x is white, the function must return:
[(2,2,2), (5,0,5)].

To see some test cases, check the images in func5/image01.png, etc.
"""

import images


def func5(input_pngfile):
    # your code goes here
    pass

#print(func5('func5_test1.png'))
#print(func5('func5_test2.png'))
#print(func5('func5_test3.png'))
#print(func5('func5_test4.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks

Define a recursive function (or a function calling a recursive
function) ex1(directory) which takes as input a string 'directory'
representing the path of a directory. The function must recursively
explore the directory tree whose root is 'directory' and return a list
of tuples of two elements.
Each tuple contains:
    - in the first position the path to a text file whose
      filename ends in .txt;
    - in second position the length L of the longest line of the
      text file, excluding the newline character.
The list is sorted in ascending order according to L and, if the
length L is the same, in alphabetical order, based on the file path.

For example, if the function is called on 'ex1/A', it returns:

[('ex1/A/QBwXM/KVobU.txt', 19)]

In fact, the longest line in 'ex1/A/QBwXM/KVobU.txt' has 19 characters
(excluding the '\n' and including any other space).

NOTE: it is forbidden to use the os.walk function. You can use:
  os.listdir, os.path.isfile, os.path.exists, etc. To concatenate the
  path, use the string concatenation operator and the separator character '/'.

NOTE: We strongly recommend splitting the exercise into subproblems,
   and implementing several functions for each subproblem.
"""

import os

def ex1(directory):
    # your code goes here
    pass

# print(ex1('ex1/A'))
# print(ex1('ex1/B'))
# print(ex1('ex1/C'))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 marks

Define the function ex2(root), receiving as input the root of
a binary tree, as defined in the `BinaryTree` class of the module
tree.py. The nodes of the input tree have strings as values. The
function must return the string resulting from the concatenation of
all the values in the nodes of the tree based the following rules:
- the values are joined based on level number, starting from those at
  level 0, then those at level 1, etc.
- the separator '-' is added between each group of values of different
  levels.

For example:

        ______A______                        ______A______
       |             |                      |             |
       B__        ___C___                __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F             _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                                      H   I      J  K   L   M   N

If the tree is the one on the left, the function should return A-BC-DEF
If the tree is the one on the right, the function should return A-BC-DEFG-HIJKLMN

"""


def ex2(root):
    # your code goes here
    pass



# from tree import BinaryTree
# root = BinaryTree.fromList(['A', ['B',[],['D',[],[]]], ['C', ['E',[],[]], ['F',[],[]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',[],[]],['I',[],[]]],['E',[],['J',[],[]]]], ['C', ['F',['K',[],[]],['L',[],[]]], ['G',['M',[],[]],['N',[],[]]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',['L',[],[]],[]],[]],['E',[],['I',[],[]]]],['C', ['F',['J',[],[]],[]],['G',[],['K',[],['M',[],[]]]]]])
# print(ex2(root))
###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

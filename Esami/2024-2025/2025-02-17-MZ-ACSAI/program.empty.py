#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save the file as program.py
 2) Assign the variables below with your
    NAME, SURNAME, STUDENT ID

To pass the exam it is necessary:
    - to obtain a score greater than or equal to 18 (15 for DSA students)

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to increase the debug level
and know where an exercise generates an error.
Remember that to test and evaluate recursion it is necessary to set DEBUG = False

To quickly comment/uncomment the code use Control + 1!
"""
name        = "NAME"
surname     = "SURNAME"
student_id  = "STUDENT_ID"
#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 marks

Implement the function func1(text: str) -> dict[str, list[int]] that takes as an argument:
- text: a string of text
and returns a dictionary in which the keys are the alphabetic letters appearing in the string
and, for each letter, the corresponding value is the average number of occurrences of that letter
in the string. The average number is calculated as the number of occurrences of the letter in the
string divided by the length of the string.
The average number of occurrences is rounded to the second decimal place using the round() function.

Example:
    text = 'sopra la panca la capra campa, sotto la panca la capra crepa'
    expected = {'s': 0.03, 'o': 0.05, 'p': 0.12, 'r': 0.07, 'a': 0.27, 'l': 0.07,
                'n': 0.03, 'c': 0.1, 'm': 0.02, 't': 0.03, 'e': 0.02}
'''

def func1(text):
    # Your code here
    pass


# testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
# expected = {'s': 0.03, 'o': 0.05, 'p': 0.12, 'r': 0.07, 'a': 0.27, 'l': 0.07,
#             'n': 0.03, 'c': 0.1, 'm': 0.02, 't': 0.03, 'e': 0.02}
# print(func1(testo))

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 marks

Implement the function func2(lists) that takes as input a list of lists. 
Each inner list contains integers, that can possibly repeat multiple times.
The function returns a list that contains all the integers 
that appear in exactly one of the inner lists, repeated as many times as they appear
in that specific list.
The integers in the output list are sorted from largest to smallest.

For example, if lists = [[4, 4, 10, 4, 1, 10], [4, 2, 1], [1, 4]]

then the function returns [10, 10, 2], as both 10 and 2 appear in only one list;
10 appears two times in the list where it appears, so it is repeated two times;
2 appears one time in the list where it appears, so it does not repeat;
instead, 1 and 4 are not included as they appear in more than one list.

We assume that the variable lists is never empty.
'''


def func2(lists: list[list[str]]) -> list[str]:
    # Your code here
    pass

# print(func2([[4, 4, 10, 4, 1, 10], [4, 2, 1], [1, 4]]))

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 4 marks
Implement the function func3(textfile_in, textfile_out) that takes as arguments:
- textfile_in: the path of a text file to be read
- textfile_out: the path of a text file to be written

The function must read from textfile_in and write into textfile_out.

textfile_in contains a series of text lines, each of which contains a sequence 
of integers separated by commas and, possibly, by a variable number of spaces and \t.

The function must write into the textfile_out one line for each line in textfile_in;
each line in textfile_out must contain the sum of the even numbers minus the sum of the odd numbers 
found in the corresponding line of textfile_in.

Important note: the last line of the textfile_out is never empty (so, it cannot contain just a \n;
be sure that you are not storing a \n in the last line of textfile_out, otherwise all the
tests will fail!)!

The function must return the pair (sum_even, sum_odd) where sum_even and sum_odd are, 
respectively, the sum of all even and odd numbers in the textfile_in file.

Example: if the textfile_in file contains the lines:
    1,    2,    17, 22
    6, -38, 71, 50,  3
    12, -8, 190,  0,  1

The textfile_out file must contain the 3 lines:
6
-56
193

and the function must return the pair (sum_even, sum_odd) = (236, 93)
'''

def func3(textfile_in, textfile_out):
    # Your code here
    pass


# print(func3('func3/in_1.txt', 'func3/your_output_1.txt'))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 2 marks

Implement the function func4(S1: set[str], S2: set[str]) -> dict[str, list[str]]
that takes as arguments two sets of strings S1 and S2 and returns a dictionary
where the keys are the strings from S1 that are substrings of at least one string in S2,
and the values are the lists of strings from S2 that contain that particular string from S1.
The lists associated with each key must be sorted by descending length,
and in case length is the same, in ascending alphabetical order.

Example:
S1 = {'a', 'b', 'c', 'e'}
S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
Result = {'a': ['abc', 'aa', 'ab'], 'b': ['abc', 'ab', 'bb', 'bc'], 'c': ['abc', 'bc', 'cc', 'cd']}
Note: 'e' does not appear in the resulting dictionary as it does not appear in any string of S2.
"""

def func4(S1: set[str], S2: set[str]) -> dict[str, list[str]]:
    # Your code here
    pass


# S1 = {'a', 'b', 'c', 'e'}
# S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
# print(func4(S1, S2))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 marks

Define the function func5(png_input: str) -> tuple[int,int] that takes as input
a string png_input which is the path of a png image. 
The image has a white background and, on top of the background, there is a number of 
filled rectangles of uniform color (which is always different from white)
that do not touch or overlap each other. See, for example, the image in func5/in_01.png.
The function must find the rectangles in the image png_input and return 
a dictionary of items (key, value), where:
- key is a tuple (R, G, B) representing the color of (at least) one of the rectangles in png_input;
- value is the number of rectangles of color key found in png_input.

For example, for the image func5/in_01.png, the function must return:
{(28, 33, 221): 1, (187, 0, 0): 1, (187, 177, 0): 1, (191, 190, 186): 1, (0, 255, 7): 1}

To load the PNG files, you can use load(png_path) from the images library.
"""

import images


def func5(png_input):
    # Your code here
    pass


# print(func5("func5/in_01.png"))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks

Implement the function ex1(root: BinaryTree) -> int that takes as input
the root of a binary tree, as defined in the 'BinaryTree' class of the 'tree.py' module,
and returns an integer corresponding to the maximum value that can be obtained
by multiplying the value of a node by its level, assuming that the level of the root is 1.

Example:

        ______20_____       level 1          ______13______
       |             |                      |              |
      15__        ___1___   level 2      ___7___        ___10___
          |      |       |              |       |      |        |
          -2    11       4  level 3    _-5_    -1_    _9_      _3_
                                      |    |      |  |   |    |   |
                            level 4 -10    4      6  5  -2    -6  2

 If the tree is the one on the left, the function must return the value 33 = 11 * 3

 If the tree is the one on the right, the function must return the value 27 = 9 * 3
********************************************************************
Note: if you write an additional function, DO NOT define the additional recursive function 
as an internal function but place it at the same level as ex1, 
otherwise you will not pass the recursive test!
"""
from tree import BinaryTree

def ex1(root: BinaryTree) -> int:
    # Your code here
    pass

# root = BinaryTree.fromList([20, [15,None,[-2,None,None]],
# [1, [11,None,None], [4,None,None]]])
# print(ex1(root))
# 
# root = BinaryTree.fromList([13,
# [7,[-5,[-10,None,None],[4,None,None]],[-1,None,[6,None,None]]],
# [10, [9,[5,None,None],[-2,None,None]],
#  [3,[-6,None,None],[2,None,None]]]])
# print(ex1(root))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 8 marks

Implement the function ex2(I: set[int], m: int, M: int) -> list[int]
recursively or using recursive functions or methods, that takes as input
a set of any number of integers and a pair of integers m and M, with m < M.
The function returns the list of integers between m and M inclusive
obtained by considering all possible values obtained by multiplying
one or more elements of the set I, without repetitions.
The returned list is sorted in ascending order.

Example: ex2({2, 3, 7}, 5, 15) returns [6, 7, 14],
because all the possible subsets of set {2, 3, 7} are:
{2} -> product 2 (less than 5)
{3} -> product 3 (less than 5)
{7} -> product 7 (OK)
{2, 3} -> product 6 (OK)
{2, 7} -> product 14 (OK)
{3, 7} -> product 21 (greater than 15)
{2, 3, 7} -> product 42 (greater than 15)

NOTE: it is forbidden to import external libraries apart from those already imported.

********************************************************************
NB: if you write an additional function, DO NOT define the additional
recursive function as an internal function but place it at the same
level as ex2, otherwise you will not pass the recursive test!
********************************************************************
"""
def ex2(I : set[int], m : int, M : int) -> list[int]:
    # Your code here
    pass

# print(ex2({1, 2, 3, 7}, 1, 15))
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Write your tests here
    print('*' * 50)
    print('You need to run grade.py if you want to debug with the built-in grader.')
    print('Otherwise, you can insert code here to test your functions, but you need to write the test cases yourself.')
    print('*' * 50)
    # from tree import BinaryTree
    # root = BinaryTree.fromList(['A', ['B',[],['D',[],[]]], ['C', ['E',[],[]], ['F',[],[]]]])
    # print(ex1(root))
    # root = BinaryTree.fromList(['A', ['B',['D',['H',[],[]],['I',[],[]]],['E',[],['J',[],[]]]], ['C', ['F',['K',[],[]],['L',[],[]]], ['G',['M',[],[]],['N',[],[]]]]])
    # print(ex1(root))
    # 
    # ex2({1, 2, 3, 7}, 1, 15)



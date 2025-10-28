#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Steps to do FIRST:
 1) save this file as program.py
 2) assign the variables below with your
    FIRST NAME, LAST NAME, STUDENT ID (Sapienza matriculation number)

To pass the exam it is necessary to:
    - !!!fill in your personal information in the variables below!!!
    - AND solve at least 1 ex-type exercise (recursive problem)
    - AND solve at least 3 func-type exercises
    - AND obtain a score greater than or equal to 18

The final score is the sum of the scores of the solved problems.
"""

name       = 'NAME'
surname    = 'SURNAME'
student_id = 'STUDENT_ID'    # your Sapienza registration number

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

#%% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 2 marks

Define the function func1(int_list, keys) that takes as input an
'int_list' list and a set 'keys' containing integers. The function
returns a dictionary in which the keys are the integers from 'keys'
and the values are lists with the integers from 'int_list' divisible
by the corresponding key.  The lists are sorted in descending order.


Example: if int_list=[4, 6, 10, 13] and keys={2, 3, 5}
  the invocation of func1(int_list, keys) must return the dictionary
  {2:[10, 6, 4], 3:[6], 5:[10]}
'''

def func1(int_list, keys):
    # INSERT HERE YOUR CODE
    pass

# int_list=[4, 6, 10, 13]
# keys={2, 3, 5}

# print(func1(int_list, keys))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 marks
Define a function func2(L0, L1) that receives 2 lists L0 and L1.
The first list L0 contains strings S0, S1, ... Sn-1,
the second list L1 contains positive integers I0, I1, ... In-1.
The function returns a string obtaining by concatenating each string
Sj repeated Ij times.
For example, if L0 = ['ab', 'o o'] and L1 = [2, 3] the function returns:
'ababo oo oo o'.
'''
def func2(L0, L1):
    # INSERT HERE YOUR CODE
    pass


# L0 = ['ab', 'o o']
# L1 = [2, 3]
# print(func2(L0, L1))


# ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 2 marks
Define a function func3(string_list1, string_list2) that takes as
input two lists of strings and returns a new list of strings.  The new
list consists of all those strings in one of the two input lists that
contain as a substring at least one string or an inverted string from
the other list.  The resulting list must be sorted in descending order
by number of characters, in case of equality, in alphabetical order.

Example: if string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] and
            string_list2=['ark', 'contact', 'hop', 'mark']
         the invocation of func3(string_list1, string_list2) shall return
         the list ['elichopter','contact','park', 'shop']

         In fact:
             'elichopter' contains 'hop',
             'contact' contains the inverted string of 'cat'
             'park' contains 'ark'
             'shop' contains 'hop'
'''

def func3(string_list1, string_list2):
    # INSERT HERE YOUR CODE
    pass

# string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
# string_list2=['ark', 'contact', 'hop', 'mark']
# print(func3(string_list1, string_list2))


#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 marks
Define a function func4(D) that receives as input a dictionary, in which
each key is a string.
The function returns a list of lists, in which each sublist corresponds
to an item in the dictionary, the first item of the list is the key and
the second item of the list is the corresponding value.
The list is sorted by the length of the second item of the sublists,
in reversed order (from the longest to the shortest).
If the second items of two or more sublists have the same length, they
are sorted by the first items (alphabetically).
For example, if D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
the function returns: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
"""

def func4(D):
    # INSERT HERE YOUR CODE
    pass

# D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
# print(func4(D))


#%% ---------------------------- FUNC 5 ---------------------------- #


'''
Func 5: 8 marks

Write a function func5(input_pngfile) that takes as input a string
that contains the path to a file with an image in PNG format.
The image given by 'input_pngfile' contains horizontal segments of
uniform color on a black background. A line can contain multiple
segments of different colors, even attached to each other.

The function must locate all the segments present in the image and
return a list of triples representing the colors of the identified
segments, ordered from longest to shortest.
In case of segments of equal length, the colors should be sorted in
ascending order considering the order of the third component, then of
the second, and finally of the first one.
In case of segments of equal color, one should consider the longest
one.

Example: in the image of the file func5/image01.png there are four segments
         one of length 50 with color (0, 128, 200)
         one of length 30 with color (200, 128, 200)
         one of length 30 with color (200, 200, 128)
         one of length 29 with color (0, 128, 200),
         so func5('func5/image01.png') must return the list
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
'''

import images


def func5(input_pngfile):
    # INSERT HERE YOUR CODE
    pass

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 8 marks

Define the function ex1(), recursive or using recursive functions
or methods, that, given a list of N lists of M characters each, builds and returns
the list of all the possible strings of N characters obtained by concatenating
a character from the first list, another one from the second, then thirs, and so on.
For example, if the input list is: [['c', 'q', 'a'], ['w', 'e', 'y']],
the function returns: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy']
The returned list must be sorted in alphabetical order.
"""

def ex1(L):
    # INSERT HERE YOUR CODE
    pass


# L = [['c', 'q', 'a'], ['w', 'e', 'y'], ['w','v']]
# print(ex1(L))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

Define a function ex2(root), recursive or using recursive functions or
methods, that takes a binary tree as input and modifies it (in-place)
by recursively adding to each node the values of its child nodes (if
any).  The sum must be done bottom-up, that is, leaves will be added
to their parent nodes, and so on, until the root is reached.  The
function returns a tuple of two integers, representing the number of
odd and even values in the original tree.

Example: if the input tree is

               1
              / \
             2   3
            /   / \
           4   5   6
              /
             7
The modified tree will be:
               28
              /  \
             6    21
            /    / \
           4    12  6
               /
              7
and the function will return (4, 3).
"""

import tree
def ex2(root):
    # INSERT HERE YOUR CODE
    pass


# T = tree.BinaryTree.fromList([1, [2, [4, None, None], None], [3, [5, [7, None, None], None], [6, None, None]]])
# print(ex2(T))
# print(T)

######################################################################################

if __name__ == '__main__':
    print('*' * 50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*' * 50)

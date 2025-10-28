#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to perform FIRST OF ALL:
 1) Save the file as program.py
 2) Assign the variables below with your
    NAME, SURNAME, STUDENT_ID

To pass the exam, it is necessary to meet all the following requirements:
    - obtain a score greater than or equal to 18 (15 for DSA)

The final grade is the sum of the scores of the solved problems.

Attention! DEBUG=True in grade.py to improve debugging.
However, to properly test recursion, DEBUG=False is necessary.

"""
name       = "NAME"
surname    = "SURNAME"
student_id = "STUDENT_ID"


#########################################

################################################################################
# ---------------------------- DEBUGGING SUGGESTIONS --------------------- #
# To run only some of the tests, you can comment out the entries
# corresponding to the tests you do not want to run within the `test` list
# at the END of `grade.py`.
#
# To debug recursive functions, you can disable the recursion test by
# setting `DEBUG=True` inside the `grade.py` file.
#
# Setting DEBUG=True also activates the terminal printout of the STACK
# TRACE of errors, which allows you to know the line number in `program.py`
# that generated an error.
################################################################################
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 points
Define the function func1(string_list1, string_list2) that takes as arguments 
two lists of strings and returns a new list of strings containing the strings 
present only in one of the two input lists (i.e., that do not appear in both lists).
The output list must be sorted in ascending order of length and, 
in case of a tie, in reverse alphabetical order.
'''
def func1(string_list1, string_list2):
    # Complete the code here
    pass

# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 2 points
Define the function func2(path_to_file) that takes as argument a string 
representing the path to a text file. 
The function should return a dictionary that maps each character in the text 
to the count of its occurrences.

Example:
  The content of func2_test_1.txt is:
cat rat fat
art
  The expected output from the invocation of func2('func2/func2_test_1.txt') is:
  {'c':1, 'a':4, 't':4, 'r':2, 'f':1, ' ':2, '\n':1}

Note:
  Open the file with encoding 'utf-8'.
'''
def func2(path_to_file):
    # Complete the code here
    pass

# %% -------------------------------- FUNC.3 -------------------------------- #
''' func3: 2 points
Define the function func3(a_list) that takes as argument a list of numbers 
and modifies it (i.e., causing side effects) by removing all elements equal 
to the maximum and minimum values.
The function should return the difference between the initial length and the 
final length of the list.

Example:
    if a_list = [3, 12, -3, 4, 6, 12]
    after calling func3(a_list), the list should be
    a_list = [3, 4, 6]
    and the function should return 3.

IMPORTANT: the list `a_list` must be changed at the end
of the function execution.
'''

def func3(a_list):
    # Complete the code here
    pass

# %% -------------------------------- FUNC.4 -------------------------------- #
""" func4: 6 points
Define the function func4(input_filepath, output_filename) that takes as arguments
two file paths:
  - The file `input_filepath` contains a sequence of words, i.e., strings 
    separated by spaces, tabs, or newlines.
  - The file `output_filename` indicates where to save a new text file, 
    whose contents are specified below.
The output file must contain all the words present in `input_filepath`, 
repeated only once and organized into lines as follows.

The lines in the output file are in descending alphabetical order.
Within each line, the words
  - have the same initial letter, regardless of case;
  - are separated by a space;
  - are ordered by their length and, in case of a tie, in alphabetical order, 
    regardless of case. If none of the criteria provided so far distinguish 
    the words, those that coincide must be arranged in alphabetic order 
    (i.e., case differences are considered only as a last resort).

The function must return the number of lines written in the file `output_filename`.

Example:
  The file 'func4/func4_test1.txt' contains the following two lines:
cat bat    rat
Condor baT
  The invocation of func4('func4/func4_test1.txt', 'func4/func4_out1.txt')
  should write the following three lines in the file 'func4/func4_out1.txt' 
  and return the value 3:
rat
cat Condor
baT bat
"""

def func4(input_filename, output_filename):
    # Complete the code here
    pass

# %% -------------------------------- FUNC.5 -------------------------------- #
""" func5: 8 points
Define the function func5(imagefile, output_imagefile, color) that takes 
as arguments two strings representing paths to PNG image files and a color 
provided as an RGB tuple.
The image in the `imagefile` contains only horizontal white segments on a black 
background. Each row has at most one white segment.
The function should create a new image containing the same segments as the input 
image and change the color of the shortest segments using the input color.

The resulting image should be saved in PNG format in the file with path 
`output_imagefile`.

The function returns the number of colored segments in the output image.
"""
import images
def func5(imagefile, output_imagefile, color):
    # Complete the code here
    pass

# %% --------------------------------- EX.1 --------------------------------- #
"""
Ex1: 6 points

Implement the function ex1 (recursively or using recursive functions) as follows. 
The function ex1 takes the following arguments:
  - `directory`, a string representing the path to a directory
  - `ext`, a string representing a file extension.
The function should recursively search within the `directory` and all its 
subdirectories for files with the `ext` extension. These files should be 
interpreted as text files. The function ex1 should calculate the sum of the sizes
of all the files found in the subdirectories and return a dictionary structured 
as follows:
  - the keys are all the subdirectories containing at least one file 
    with the `ext` extension
  - the values are the sum of the sizes of ALL the files contained in that 
    subdirectory (including those with different extensions).
The subdirectories should be reported with the path relative to the current directory. For example, given the directory structure:
A/
  B/
    file1.png    #4 bytes
    file2.txt    #18 bytes
  file3.txt      #8 bytes

The invocation `ex1("A", ".png")` should return `{"A/B":22}`

The size of a file can be calculated by counting the number of characters read 
from the file.

It is recommended to use the functions os.listdir, os.path.isfile, 
and os.path.isdir and NOT the os.join function in Windows. 
Use string concatenation with the '/' character.

It is FORBIDDEN to use the os.walk function.
"""

import os
def ex1(directory, ext):
    # Complete the code here
    pass



# %% --------------------------------- EX.2 --------------------------------- #
"""
Ex2: 6 points

Define the function ex2(root) that takes as argument the root of a binary tree, 
as defined in the `BinaryTree` class of the `tree.py` module.
The function should return the sum of all values associated with nodes 
at odd levels in the tree with root `root`, subtracting all values associated 
with nodes at even levels. The root is assumed to be at level 0.

Example:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    If the tree is the one on the left, the function should return the value -8.
    If the tree is the one on the right, the function should return the value 22.
"""


def ex2(root):
    # Complete the code here
    pass

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)

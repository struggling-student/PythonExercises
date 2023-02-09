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

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 ex (recursive) problem and
    - get a score greater or equal to 18

The final score is the sum of the solved problems.

## OVERALL POINTS
# | type            | score     |
# | func1           |         2 |
# | func2           |         2 |
# | func3           |         2 |
# | func4           |         6 |
# | func5           |         6 |
# | ex1 (recursive) |         6 |
# | ex2 (recursive) |         8 |
# | --------------- |        -- |
# | total           |        32 |
"""

name       = "NAME"
surname    = "LASTNAME"
student_id = "STUDENTID"


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


# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 points
Implement the function func1(string_list, word) that takes as input a
list of strings 'string_list' and a string 'word' and destructively deletes
from string_list all the strings that contain 'word'.
Remember: the input string_list has to be modified!

The function returns the number of strings removed.
'''

def func1(string_list, word):
    # write here you code
    pass


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Implement a function func2(pathname) that takes as input
a string representing the path to a text file. The file
contains on each line a "number,student_id" pair separated by
a comma. The numbers are always greater than or equal to zero.  The
function must return a dictionary. The dictionary has the
'student_id' as key in the form of a string and the
'number' as the value but as an integer type.  In addition, a student_id can be
associated with more than one number: in case this happens, the dictionary
needs to only keep the maximum number.
Example:
Content of func2_test_1.txt
 27,123456
 78,121212
 90,111111
 79,121212
 26,123456
 91,111111
The function func2('func2_test_1') returns {'123456': 27, '121212': 79, '111111': 91}
'''

def func2(pathname):
    # write here you code
    pass


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 points
Implement the function func3(listA, pathname) that takes as its
input a list of strings 'listA' and a string pointing to a
file at the path 'pathname'. The function must write to the path
'pathname' a text file in which every line has a string from listA.
The strings are written in increasing order by the number of characters.
In case of a tie, strings are sorted in reverse alphabetical order.
The function returns the total number of characters of all the strings
in listA.

The expected outputs are available in func3_1_exp.txt, func3_2_exp.txt, func3_3_exp.txt
'''


def func3(listaA, pathname):
    # write here you code
    pass


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Implement the function func4(S) which takes as input a string 'S'.
Given 'S', it is necessary to remove all non-alphabetic
characters, extract all the words in the string while converting them
to lower case.

Example. From:

S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta
al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era
scordato di chiamare Paperino'

we go to:

['pippo', 'e', 'topolino', 'sono', 'andati', 'al', 'mare', 'hanno',
'mangiato', 'una', 'bella', 'pasta', 'al', 'pesce', 'pescato', 'in',
'mare', 'il', 'giorno', 'prima', 'ma', 'purtroppo', 'topolino', 'si',
'era', 'scordato', 'di', 'chiamare', 'paperino']

Then, the function calculates the frequency of the words found and has
to produce the related histogram.

The histogram is a string representing the frequency of each word,
constructed according to the following rules:
- the words appear in alphabetical order
- every word appears followed by one or more spaces, many asterisks
  ('*') as its frequency, and one newline character ('\n')
- the number of spaces added is so that all the asterisks are
  left-aligned in all the lines.

The inital part of the string hence will be:
'al        **\nandati    *\nbella     *\n .....'
so that the printed string will be
al        **
andati    *
bella     *


For more examples please see functions test_func4_1, test_func4_2, test_func4_3
in grade.py
"""


def func4(S):
    # write here you code
    pass


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 6 points
Implement a function func5(img, output_file_name) that takes as input
'img', an image modeled as a list of lists and effects a RIGHT rotation
of the image by 90 degrees. The new rotated image must be saved in
'output_file_name' via the images module.
The function returns a tuple where the first element is the height and
the second is the width of the rotated image.
"""

import images


def func5(img, output_file_name):
    # write here you code
    pass


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points
Implement a recursive function ex1(root), or another function that uses
recursion, that takes a string pointing to a directory as input and
recursively explores the directory tree and returns a
dictionary.
The key in the dictionary is the absolute path starting
from the 'root' dir in the form of a string.  The value corresponds to a
string built as follows: considering a directory, we take
ALL the files in THAT directory ONLY with the extension ".txt" sorted
alphabetically.
The files .txt are text files where on each line there is a series of
integer numbers followed by a space.
An example is the file 'ex1_A/XYCwdkCokL.txt' which contains:

75 84 84 73 83
76 74 76

From top to bottom, left to right, read each number sequentially by
interpreting it as a Unicode value and thus converting it to a character.
The concatenation of all characters forms a string.

For example, the above sequence is converted to the string "KTTISLJL".

The value in the dictionary is the string obtained by concatenating the
strings generated for each text file for that directory according to the
alphabetical order of the files.txt.

If the directory does not contain any .txt files then that directory
does not appear in the dictionary.

If the function is called on 'ex1_A', it will return the following dictionary:

{'ex1_A/bkLbD': 'A\x9eŻĂĳŜǖ', 'ex1_A': 'KTTISLJL'}

NOTE: It is forbidden to use the os.walk function. You can use:
os.listdir, os.path.isfile, os.path.exists, etc.
NOTE: we strongly suggest dividing the exercise into subproblems
organizing the code into small functions for each subproblem.
"""

import os


def ex1(root):
    # write here you code
    pass


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 8 punti
Implement the recursive function ex2(nums, ops), or another function that uses
recursion, which takes as input a set of positive integers 'nums' and a list
of strings 'ops' indicating operations on the numbers.
The function must recursively generate all possible arithmetic expressions,
where each expression is a string. The expressions are derived by joining
two or more numbers taken from 'nums' with operations from the set 'ops'.
The function must return all the constructed expressions.

The following rules apply when constructing the expression:

1. Once a number is used in the expression, it can no longer be used
   For example, if nums={5,8,0} and ops=['+','*']
   '8+5+0' is a valid expression, while '8+5+8' is NOT valid.

2. Operations can be reused at will as many times as desired.
   For example, in the above example '8+5+0', the + was used twice.

The function returns a set with all the generated expressions.

Example: if nums={5,8,0} and ops=['+','*'], the function will generate:
{'8*5*0', '5+0+8', '5+0*8', '0+5+8', '0+8+5', '8+5*0', '0+5*8',
'0*8*5', '0*8+5', '8+5+0', '5*0*8', '8+0*5', '5*8+0', '5*0+8',
'5+8+0', '8*0+5', '0*5*8', '0+8*5', '8*5+0', '8*0*5', '5*8*0',
'5+8*0', '0*5+8', '8+0+5'}

NOTE: do NOT define the recursive function to be inner functon of ex2 otherwise
you fail the recursive test.
NOTE: we strongly suggest dividing the exercise into subproblems
organizing the code into small functions for each subproblem.
"""


def ex2(nums, ops):
    # write here you code
    pass



###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

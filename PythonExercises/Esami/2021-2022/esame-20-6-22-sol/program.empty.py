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

# ----------------------------------- EX.1 ----------------------------------- #

"""
Exercise 1: 6 points

Write a function ex1(Q, file_db, k) that takes as input a
tuple Q, file_db that points to a text file, while k is an
integer. Q is a tuple (x, y) indicating the coordinates of the point of the
query. Instead file_db contains 2D points on each row. Each row
contains the integer x and y coordinates separated by a space, such as:

  -5 -5
  10 5

The function must read the content of file_db. Given a point Q, it
finds the indices of the k points closest to Q in file_db. For the
distance between (x1, y1) and (x2, y2) use:
(x1-x2)² + (y1-y2)²

For example, if k=2 and Q=(-5, -5) and file_db contains:

  1 1
  -3 -5
  -5 -3
  20 10

the indices and distances of file_db with respect to Q are:

 | index |  x |  y | dist |
 |     0 |  1 |  1 |   72 |
 |     1 | -3 | -5 |    4 |
 |     2 | -5 | -3 |    4 |
 |     3 | 20 | 10 |  850 |

The two neighbors of Q are the list [2, 1] since they have the smallest k=2 distances.
In case of parity on distance, as in this case, we
return the indices from largest to smallest.

Return the list that contains the k neighboring indices as described above.
If Q=(-5, -5) and file_db is db_00.txt and k=2, return:

 [2, 1]

NOTE: We strongly suggest to break the complexity of the problem
by writing multiple, small functions
"""


def ex1(Q, file_db, k):
    # INSERT YOUR CODE HERE
    pass


# %% ----------------------------------- EX.2 ----------------------------------- #
""" 
Exercise 2: 6+3 points

Write a function that takes as input two filenames 'img_in' and 'img_out'. 
The function (6 points) must read a png image contained in the file 'img_in'
consisting of a black background and several colored pixels. It should build and save
in a new file 'img_out' an image of the same size as the one
contained in img_in. The image has at most three pixels per line.

The new image should contain horizontal segments calculated given the 
image contained in the 'img_in' file as follows:
    - for each line containing exactly three pixels, there is exactly one
      segment
    - for each line with less than three pixels, there is no segment nor
      pixels but remains black.
    - each segment is located at the same row of the three pixels in 'img_in'
                                (example: if on row y, there are the points
                                  x1<x2<x3, the segment will go from point x1 to
                                  point x3 and will have length x3-x1+1)
    - the color of each segment is given by the average of the three colors of x1, x2, x3
      for each component (example: if the R components of x1, x2 and x3 are
                                 11, 22, 66 respectively, the component R
                                 of the segment will be 33)

Operations on the component values should be rounded with the function
int.

(+3 points) Given the image in 'img_out', the function also returns the
MAXIMUM number of consecutive rows containing a segment
(1 if all lines are separated, 0 if no lines contain segments).

Example: ex2('img_1.png', 'img1_out.png') shall save in 'out21.png' an image
         equal to that of 'img1_exp.png' and return the value 18

NOTE: We strongly suggest to break the complexity of the problem
by writing multiple, small functions
"""

import images

def ex2(img_in, img_out):
    # INSERT HERE YOUR SOLUTION
    pass


# %% ----------------------------------- EX.3 ----------------------------------- #

"""
Exercise 3: 8 points 

Write a recursive function or one that makes use of recursive functions that
takes as input a string representing the name of a directory and
an integer k and returns a dictionary.

Within the dictionary, the keys are strings representing
the paths to some files with the extension '.txt', relative to the input directory, using '/' as a separator.
The value associated with a key is the integer given by the sum
of all the numeric strings contained in the file indicated by the key.

WARNING: Only the files that contain numeric strings whose sum is a multiple value
of the integer k should be contained in the dictionary.
It is assumed that the sum is always different from zero.

Ex: If a file contains "34 house c4a 22," the sum of the numeric strings
    contained in it is 34+22=56 (in fact c4a *is not* a numeric string).
    
It is not allowed to use the os.walk function.
To evaluate whether a string is numeric, you can use isnumeric method

NOTE: We strongly suggest to break the complexity of the problem
by writing multiple, small functions
"""

import os


def ex3(path, k):
    # INSERT HERE YOUR SOLUTION
    pass

"""
Exercise 4: 9 points (6+3)

The enqueuing operation "§" between two strings A and B is possible if string
A ends with the first character of string B. The result of the operation
A § B is similar to concatenation, only that the first character of B is
removed: dog § good = dogood.

Write a recursive function or one that makes use of recursive functions that
takes as input a 'start' string and a set of string 'words' and computes
recursively all the possible maximal strings that can be generated
by successive enqueuing from 'start' string, removing the enqueued words
so far.

 NOTE: By 'removing the enqueued words' we mean that each time
 a word in 'words' has been successfully concatenated to start,
 exploration of that branch of the game tree continues without
 reusing that word. See in the examples below, how the set of 
 valid word is updated, for each move in the game tree.

Maximal string means that a string cannot be further
concatenated with any other string remaining in words, after all the
enqueuing.

The function must return the set of all strings that it is possible to
generate (i.e., the leaves of the game tree), as a set (6 points),
    or (+3 points) as an ordered list in which:
    - the strings are sorted in ascending order with respect to their length
    - in case of equal length, in alphabetical order.

Example 1: 'aa' {'abb', 'acc', 'bdd', 'be'}

aa {abb, acc, bdd, be}
|
|- § abb -- aabb {acc, bdd, be}
|  |
|  |- § bdd -- aabbdd(*) {acc, be}
|  |
|  |- § be -- aabbe(*) {acc, bdd}
|
|- § acc -- aacc(*) {abb, bdd, be}

Strings with (*) are maximal with respect to the CURRENT set words.

In the example ex4('aa' ,{'abb', 'acc', 'bdd', 'be'}) the function returns the set
{'aacc', 'aabbdd', 'aabbe'} (6 points)
or the list
['aacc', 'aabbe', 'aabbdd'] (9 points)

Esempio 2: 'dog' {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'}

dog {good, gost, goat, mood, doom, gasp, pool, loop}
|
|- § gost -- dogost(*) {good, goat, mood, doom, gasp, pool, loop}
|
|- § goat -- dogoat(*) {good, gost, mood, doom, gasp, pool, loop}
|
|- § good -- dogood {gost, goat, mood, doom, gasp, pool, long, loud}
|  |
|  |- § doom -- dogoodoom {gost, goat, mood, gasp, pool, long, loud}
|     |
|     |- § mood -- dogoodoomood(*) {gost, goat, gasp, pool, long, loud}
|
|- § gasp -- dogasp {good, gost, goat, mood, doom, pool, long, loud}
   |
   |- § pool -- dogaspool {good, gost, goat, mood, doom, long, loud}
      |
      |- § loud  -- dogaspooloud {good, gost, goat, mood, doom, long}
      |  |
      |  |- § doom -- dogaspooloudoom {good, gost, goat, mood, long}
      |     |
      |     |- § mood -- dogaspooloudoomood(*) {good, gost, goat, long}
      |
      |- § long -- dogaspoolong {good, gost, goat, mood, doom, loud}
         |
         |- § good -- dogaspoolongood {mood, gost, goat, doom, loud}
         |  |
         |  |- § doom -- dogaspoolongoodoom {mood, gost, goat, loud}
         |     |
         |     |- § mood -- dogaspoolongoodoomood(*) {gost, goat, loud}
         |
         |- § gost -- dogaspoolongost(*) {good, goat, mood, doom, loud}
         |
         |- § goat -- dogaspoolongoat(*) {good, gost, mood, doom, loud}

The strings with (*) are maximal with respect to the set words CURRENT 
(they cannot be concatenated further).

In the example ex4('dog', {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'})
the function returns the set
{'dogaspoolongoodoomood', 'dogaspooloudoomood', 'dogoodoomood', 'dogaspoolongost',
 'dogaspoolongoat', 'dogost', 'dogoat'} (6 points)
or the list
['dogoat', 'dogost', 'dogoodoomood', 'dogaspoolongoat',
'dogaspoolongost', 'dogaspooloudoomood', 'dogaspoolongoodoomood']
 (9 points)
"""


def ex4(start, words):
    # INSERT HERE YOUR SOLUTION
    pass




###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

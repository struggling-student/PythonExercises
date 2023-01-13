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

# %% ----------------------------------- EX.1 ----------------------------------#
"""
Ex1: 6 points

Define the function ex1(triangles) that takes as input a list of
triples of positive numbers and eliminates from the list all triples
that cannot be the sides of a right triangle. Each number in the
triple can be either cathetus or hypotenuse, and there is no
predetermined order.  The function must return the number of triples
deleted from the triangles list. The triangles list must be modified
in-place.  To evaluate whether a triangle is right-angled one can use
the Pythagorean theorem: the sum of the squares constructed on the
catheti must equal the square constructed on the hypotenuse.  For
comparisons, use the round(x,3) rounding function.

Example: if triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         the function ex1(triangles) return the value 3 and modifies the list
         so that
         triangles = [(3, 4, 5), (12, 36.05551, 34)].

In fact, considering the expected result triangles = [(3, 4, 5), (12, 36.05551, 34)]
it holds the following:

| triplet            | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTE: Break down the problem in small sub problems. Write small functions
for each sub problem. Compose everything together.

"""


def ex1(triangles):
    # WRITE HERE YOUR CODE
    pass


# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex2: 8 points
We have to create an image from a black image with some colored
dots. We also have a dictionary that associates some colors with a
tuple with exactly two positive integers, representing height and
width, respectively.

Define the function ex2 that takes as input two strings ('img_in' and
'img_out', representing the names of two files) and a dictionary
'colors'.  The file given by img_in contains a PNG image with a black
background and with some colored dots. The function must construct a
rectangle in the new image img_out for each colored dot in img_in
having a color in the colors dictionary.  The colored dot is the upper
left corner of the rectangle. The dimensions of the rectangle are
associated with the color of the dot in the colors dictionary, if such
a color exists.  The image with the rectangles must be saved in PNG
format in a file named img_out.  The function must return the number
of rectangles drawn.

If the color of a point is not present in the dictionary, that point
will not have to become a rectangle in the new image, but it must also
be present in the new image as well--unless it is covered by another
rectangle.

The rectangles should be drawn in the order of the points in the
image, considering each point as a tuple (row, column): for example,
first the rectangle for the point (0,0), followed by the rectangle for
(0,100), followed by (30,0).
WARNING: you must draw a rectangle FOR EACH point of a color in
colors, EVEN IF a point is covered by a rectangle of another point.

You may assume that the dimensions in colors require you to draw
rectangles with all points within the edges of the image (i.e.
rectangles never exceed the margins of the image).

img_in = 'ex2/image01.png'
colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}
the image to be constructed is the one in the file ex2/expected01.png

NOTE: Break down the problem in small sub problems. Write small
functions for each sub problem. Compose everything together.
"""

import images


def ex2(img_in, img_out, colors):
    # WRITE HERE YOUR CODE
    pass

    
# %% ----------------------------------- EX.3 ----------------------------------- #
"""
Ex3: 9 points

Define the recursive function ex3 that takes as input a string
'directory' and a string 'namefile'. The function must search recursively
within the directory given by directory and in all subdirectories for
all files with name equal to namefile.  Such files are to be
interpreted as text files. Each text file contains only positive
numeric strings. Files with the same namefile always have the same
number of numeric strings.  The function must return a list of
integers obtained by summing the numeric strings of the files found,
position by position.

Example: if two files with the SAME namefile are found and those
files contain the sequences "11 23 90" and "11 77 0," the function ex3
returns the list [22, 100, 90].

We suggest using the functions os.listdir, os.path.isfile and
os.path.isdir and NOT to use the os.join function in Windows (use
concatenation between strings with the '/' character).

It is forbidden to use the os.walk function.

NOTE: Break down the problem in small sub problems. Write small
functions for each sub problem. Compose everything together.
"""

import os


def ex3(directory, namefile):
    # WRITE HERE YOUR CODE
    pass


# %% ----------------------------------- EX.4 ----------------------------------- #
"""
Ex4: 6+3 points
Define a recursive function (or one that uses recursive functions)
ex4(strings, n) that takes a set 'strings' and an integer 'n' and
recursively generates all possible strings that can be constructed by
concatenating n strings of the set strings. The function must return
all strings constructed. The function can return either a set with all
strings constructed (6 points), or a sorted list (9 points).  The list
is ordered considering the descending order of the length of the
strings and, in case of parity, considering the alphabetical order.

Example: if strings={'a','b','c','de'}, the function ex4(strings, 2)
returns the set {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 points)
or the list ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 points)
"""


def ex4(strings, n):
    # WRITE HERE YOUR CODE
    pass

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

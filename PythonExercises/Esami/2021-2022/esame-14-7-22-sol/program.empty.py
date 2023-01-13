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

"""Ex 1: 6 points

Write a function ex1(file_db, k) that takes as input the name
of a text file file_db, while k is an integer. The file contains a
sequence of strings separated by spaces and/or carriage returns, for example:

  hola this
  
              is
    a                        sequence

The function must read the content of the file and calculate the sum
between the lengths of all pairs of strings, always in the following order:
first, the pair formed by the first string and the second one, then
the one formed by the first string and the third one, then the first one and the
fourth one, and so on; then the second string and the third one, the second
one and the fourth one, and so on; then the third string and the fourth one,
the third one and the fifthone , and so on.

In the example above, the pairs to be considered and will be the following ones:

 index | lunghezza1 | lunghezza2 | somma |
   0   |     5      |     4      |   8   | (hola + this)
   1   |     5      |     2      |   6   | (hola + is)
   2   |     5      |     1      |   5   | (hola + a)
   3   |     5      |     8      |   12  | (hola + sequence)
   4   |     4      |     2      |   6   | (this + is)
   5   |     4      |     1      |   5   | (this + a)
   6   |     4      |     8      |   12  | (this + sequence)
   7   |     2      |     1      |   3   | (is + a)
   8   |     2      |     8      |   10  | (is + sequence)
   9   |     1      |     8      |   9   | (a + sequence)

The function, considering the pairs in descending order of sum,
must return the indices of the k pairs that have the highest sum.
In case the sum of lengths for two pairs is identical,
the two pairs retain the order they had when they were initially
considered (see the column "index" in the example above).

For example, if k=2 and file_db contains:

  hola this
  
              is
    a                        sequence

the pairs to be considered are those in the table above
and the function will return the list:
[3, 6]

"""

def ex1(file_db, k):
    # INSERT YOUR CODE HERE
    pass

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 8 points

Assume youare provided as input two integers H and W that define the height and
width of an image. We would like to create an image of size
HxW and save it at the path 'img_out'.
We are also provided as input a list 'pts' of 2D points; each point
is a pair of floating-point coordinates x, y and a list 'colors' of RGB colors,
for example:

               x      y        x     y      x     y
    pts    = [[17.0, 48.0], [34.0, 94.0], [6.0, 95.0]]
                r   g   b     r   g   b     r    g    b
    colors = [[117, 85, 80], [79, 83, 68], [67, 143, 134]]


The first point [17.0, 48.0] is associated with the first color [117, 85, 80],
and so on.

For image pixel P = (x, y) in the image we need to find
the index I of the nearest point in 'pts', based on
the distance between the points d = |x1-x2| + |y1-y2|.
In case of parity, the order in 'pts' and 'colors' is maintained.

The image pixel P = (x, y) will be colored using the
color of the nearest point in 'pts'.  For example, given the points 'pts'
shown above and considering the image pixel P = (2, 1),
then the closest point turns out to be the one with index I=0 since the
distances are:

P = (2, 1)
| index I  |  0 |   1 |  2 |
| x        | 17 |  34 |  6 |
| y        | 48 |  94 | 95 |
| dist     | 62 | 125 | 98 |

so, the pixel (2, 1) will be colored with [117, 85, 80].

The pixels in the coordinates specified in 'pts' should be drawn
in black (0, 0, 0), rounding off their coordinates to int.
You can assume that the points in 'pts' are all inside
the image (6 points).

The first test in the grader generates the image in 'ex2/ex2_1_expected.png',
while your result is in 'ex2_your_result_img_1.png'

Finally, you have to remove all points from 'pts' destructively.
(+2 points).

NOTE: We strongly suggest that you break down your code into simpler functions.

"""

import images

def ex2(H, W, pts, colors, img_out):
    # YOUR CODE GOES HERE
    pass



# %% ----------------------------------- EX.3 ----------------------------------- #

"""
Given some image files, we want to combine them through
a series of operations. The sequence of operations is represented
as a binary tree having strings as nodes values.
In particular:
- the leaves of the tree contain strings pointing to the paths of the
  images on disk;
- the internal nodes are strings that indicate the operations to be performed on the
  their child nodes (subtrees).

Internal nodes can contain binary or unary operations, depending on
the number of their children.
The possible operations are:
- 'catLR': the left and right image are concatenated horizontally (LEFT image first).
- 'catRL': the left and right image are concatenated horizontally (RIGHT image first).
Note: you can assume that the images to be merged always have the same height.
- 'flip_v': a single image is flipped with respect to its vertical axis.
So, for example, ᴐ becomes c.

In case of a node containing a binary operation, the operation in the node
applies to the result of the operations in the left and right subtrees.
In case of a unary node, the operation applies to the only subtree present.

Design an ex3 function that is recursive, or makes use of recursive functions, and:
- takes as input a root object of class BinTree that
  points to the root node of a binary tree that models operations
  on images, as described above;
- loads the images referenced to by the leaves;
- performs the operations indicated in the internal nodes on the subtrees,
  until it obtains the image corresponding to the operation in the root;
- saves the resulting image in the root into the file in the parameter
  'saved_image'
- returns a tuple containing the height and width of the resuling image.

Note: Given a node, the left and right children are accessed with the
left and right attributes (see the file tree.py).
The value attribute of each node always contains a string.

For example:
1)           catRL
            /   \
           o     i
constructs the image i|o, see the file expected_img_01.png

2)             catLR
              /     \
            catRL    o
           /    \
        catRL  flip_v
        /   \       \
       a     i       ᴐ


constructs the image c|i|a|o, see the file expected_img_03.png

"""

import tree
import images

def ex3(root, saved_image):
    # INSERT HERE YOUR SOLUTION
    pass


"""
Ex 4: 9 points
    Given as input a list of syllables, you want to construct
    the list of all the strings that can be generated by combining
    two or more of such syllables.
    Write a function ex4(syllables), which is recursive or makes
    use of recursive functions, that computes all the strings
    that you can generate using the syllables in the list.
    The function returns a set with all the resulting strings (6 points).
    The function can optionally return a list (without repetitions)
    sorted in descending order by the number of characters in each string,
    and, in case of an equal number of characters, in alphabetical order
    (+3 points).
    
    Ex: syllables = ['bos', 'co', 'sa']
    the function returns (6 points):
    {'bossa', 'cobossa', 'sacobos', 'cosabos', 'bosco', 'boscosa',
     'sabos', 'saco', 'bossaco', 'cobos', 'sabosco', 'thing'} (6 points)
    or (9 points):
    ['wooded', 'bossaco', 'cobossa', 'cosabos', 'sabosco', 'sacobos',
     'forest', 'bossa', 'cobos', 'sabos', 'thing', 'saco'] (8 points)
"""

def ex4(string, numbers):
    pass
    # INSERT YOUR SOLUTION HERE



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

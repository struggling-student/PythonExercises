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


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 points
Define the function func1(int_list, bottom, up) that takes as
input a list of integers and two integers and modifies the list by
removing all integers that are not in the range [bottom, up],
extremes included. Warning: the list must be modified at the end of
the function.
The function returns the number of elements removed from the list.
Example:
    func1([4, 5, 10, 3, -1, 2], 0, 5) should return the value 2
    and modify the input list to [4, 5, 3, 2].
'''
def func1(int_list, bottom, up):
    ## Write your code here
    pass

# l1 = [4, 5, 10, 3, -1, 2]
# print(func1(l1, 0, 5))
# print(l1)


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Define a function func2(dict1, dict2) that takes as input
two dictionaries that have values of type string and returns a new
dictionary. The new dictionary contains only the keys common
to the two input dictionaries.
Each key in the new dictionary is associated with the minor of the
values of the input dictionaries associated with that key.
All value strings in the new dictionary are turned to lowercase.
Example:
    func2({'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}, {'a':'Bad', 'c':'greaT'})
    must return the dictionary {'a':'bad', 'c':'excellent'}
'''
def func2(dict1, dict2):
    ## Write your code here
    pass

# print(func2({'a':'GoOd', 'b':'bAd', 'c':'EXCELLENT'}, {'a':'Bad', 'c':'greaT'}))

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Define a function func3(str1, str2) that takes as input two strings
and constructs a new string str3 obtained by selecting only the
characters for which str1 and str2 are equal, with no distinction
between lowercase and uppercase, but by selecting the character of
the shorter string.
The function returns the string constructed as above.
Example:
    func3('abracadabra', 'ABerrant') should return the string 'ABa'
'''

def func3(str1, str2):
    ## Write your code here
    pass

# print(func3('abracadabra', 'ABerrant'))
# print(func3('delIberAtIVelY', 'ReproductIvE'))
#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Define a function func4(input_filename, output_filename, length)
that takes two strings representing two filenames and an integer
as input.
The input_filename file contains strings separated by spaces,
tabs, or carriage returns.
The function must create a new text file named output_filename
containing all the strings of length 'length' present in the file
input_filename organized by rows.
The rows are in alphabetical order.
The words in each row:
    - have the same initial letter, with no distinction between
      uppercase and lowercase
    - are separated by a space
    - are sorted in alphabetical order, with no distinction between
      uppercase and lowercase. In the case of equal words, they are
      in alphabetical order.

The function must return the number of strings of the length
required found in the input file.

Example
If the following three lines are present in the file 'func4_test1.txt'
cat bat rat
Condor baT
cat cAr CAR

the function func4('func4_test1.txt', 'func4_out1.txt', 3) must write
in the file 'func4_out1.txt' the following 3 lines:
baT bat
CAR cAr cat
rat

and return the value 7.

"""

def func4(input_filename, output_filename, length):
    ## Write your code here
    pass


# print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 3))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Write a function func5(input_filename, output_imagefile) that takes
two strings representing two filenames as input.
The input_filename file in each line contains a series of
integers separated by a comma. For each set of integers, the function
must draw the perimeter of a shape in an image with a black background,
respecting the order of the rows in the input file.
Each series may consist of 6 or 7 integers, depending on whether the shape
to be drawn is a square or a rectangle.
The structure of each set of values is as follows:
    (r, g, b, x, y, w, h), where
- r, g, b represent the three color channels with which to draw the shape
- x, y represent the coordinates of the upper left corner of the shape
- w, h represent the width and height of the shape, respectively.
In the case of a square, the value h is not present.
The size of the image is such that it perfectly contains all the
shapes so that:
    - the shape with the rightmost bottom corner will have its right
      side on the edge of the image,
    - the shape with the bottom right corner furthest down will have
      its bottom side on the edge of the image.

The image thus obtained should be saved in PNG format in the file in
the file specified by the output_imagefile path.

The function returns the number of shapes drawn in the output image.

See the files in the func5 directory for examples.

To save the image into a file, you can use the save method
of the images module.
"""
import images

def func5(input_filename, output_imagefile):
    ## Write your code here
    pass


# print(func5('func5/func5_test1.txt', 'func5/func5_test1.png'))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(n, faces), recursive or using recursive functions
or methods, having as input two integers n and faces.

The function must return a list with all the possible outcomes of rolling
'n' dices, each with 'faces' faces. Each outcome is represented as a tuple
with 'n' elements. The returned list must be sorted in increasing order.

Example:
    ex1(2, 3) must return the list
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
"""

def ex1(n, faces):
    ## Write your code here
    pass

# print(ex1(2,3))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

Define the function ex2(root), recursive or using recursive functions
or methods, that takes as input the root of a tree, which is the root
of a binary tree consisting of nodes of type BinaryTree, as defined
in the tree.py module.
The function must transform the input tree so that each node
with two children has the left child with a smaller value than the
right child by swapping the node values of the two children if needed.
The function returns the number of swaps made.

Example:

        root                   expected root
    ______5______              ______5______
   |             |            |             |
   8__        ___2___         2__        ___8___
      |      |       |           |      |       |
      3      9       1           3      1       9

      expected = 2

    If the tree is one on the left, the function should return the
    value 2 and transform the tree into the one to the right.

Other example:

              root                          expected root
          ______2______                      ______2______
         |             |                    |             |
      __ 7__        ___5___              __ 5__        ___7___
     |      |      |       |            |      |      |       |
    _4_     3_    _0_     _5_          _3_     4_    _0_     _5_
   |   |      |  |   |   |   |        |   |      |  |   |   |   |
   2   -1     1  8   3   2   9       -1   2      1  3   8   2   9

       expected = 4

    If the tree is one on the left, the function should return the
    value 4 and transform the tree into the one to the right.

"""
import tree

def ex2(root):
    ## Write your code here
    pass

# root = tree.BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
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

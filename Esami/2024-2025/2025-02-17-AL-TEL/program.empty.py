#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save the file as program.py
 2) Assign the variables below with your
    NAME, SURNAME, STUDENT ID NUMBER

To pass the exam it is necessary:
    - to obtain a score greater than or equal to 18 (15 for DSA students)

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to increase the debug level and know where an exercise generates an error.
Remember that to test and evaluate recursion it is necessary to set DEBUG = False

To quickly comment/uncomment the code use Control + 1 !
"""
name       = "NAME"
surname    = "SURNAME"
student_id = "STUDENT ID"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #

''' func1: 2 points
Define the function func1(S, D) that takes a set S of integers 
and a dictionary D and returns a new dictionary.
The input dictionary is composed of integer keys and string values.
The returned dictionary contains a key for each integer in S.
The value corresponding to a key x in S is the value associated with 
the largest key in D that is a multiple or a divisor of x.

NOTE: if none of the keys in D is a multiple or a divisor of x,
the key x does not appear in the returned dictionary.

Example: if
    S = {2, 3, 55, 4, 11, 7} and D = {11:'a', 88:'b', 66:'c', 2:'d', 100:'e', 5:'f'}
        then the function returns the dictionary
        {2:'e', 3:'c', 55:'a', 4:'e', 11:'b'}

'''

def func1(S: set[int], D: dict[int,str]) -> dict[int,str]:
    # Your code here
    pass
                    
# S = {2, 3, 55, 4, 11, 7}
# D = {11:'a', 88:'b', 66:'c', 2:'d', 100:'e', 5:'f'}
# print(func1(S, D))    


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Define the function func2(L) that takes a list of strings as input 
and returns a list of strings.
The strings in the returned list are obtained by concatenating 
all the strings that have the same length,
maintaining the order in the input list.
The returned list is sorted in descending order of length and, in case of a tie,
in alphabetical order.

Example: if L = ['xx', 'asd', 'qwe', 'bb', 'cc', 'fond']
    the function returns the list ['asdqwe', 'xxbbcc', 'fond']

'''

def func2(L: list[str]) -> str:
    # Your code here
    pass

# print(func2( ['xx', 'asd', 'qwe', 'bb', 'cc', 'fond']))



# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Define the function func3(strings, tuples) that takes a list 'strings' 
of lists of words and a list 'tuples' of pairs.
Each pair in tuples is composed of two integers (list, element) that indicate,
respectively, the index of the list from which to take a word
and the index of the word to select in that list.
The function must return the string obtained by selecting the words
from the lists in strings using the indices of the tuples.
The words must be concatenated, separated by a space,
in the order in which the pairs appear in the list tuples.

Example: if strings = [['works', 'is'], ['science', 'magic'], ['that']]
   tuples = [(1,0), (0,1), (1,1), (2,0), (0,0)]
   the function returns the string
   'science is magic that works'
'''


def func3(strings: list[list[str]], tuples: list[tuple[int, int]]) -> str:
    # Your code here
    pass

# strings = [['works', 'is'], ['science', 'magic'], ['that']] 
# tuples = [(1,0), (0,1), (1,1), (2,0), (0,0)]
# print(func3(strings, tuples))
# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Define the function func4(input_filename, output_filename) that
takes two file names as parameters. The function reads the text file
input_filename.
Each line of the input_filename file contains a series of strings separated
by spaces or tabs. Each string can be composed of alphabetic characters
or numeric characters.
The function must use a 'weight' function for each string that consists
of calculating the value obtained by summing the unicode value of the
alphabetic characters and the value of the numeric characters that make up the string.
To calculate the unicode value of a character, you can use the ord function.

For each line in input_filename, the function must write in the
output_filename file a new line with all the strings of the corresponding line,
separated by exactly one space and ordered with
the following criteria:
    - Increasing number of characters
    - in case of a tie, alphabetical order without distinction between uppercase and lowercase,
    - in case of a tie, the weight of the string,
    - in case of a tie, alphabetical order.

The function returns the string with the maximum weight found in the file
input_filename.

NOTE: ignore empty lines in the input file

"""

def func4(input_filename: str, output_filename: str) -> int:
    # Your code here
    pass


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 7 points
Define the function func5(input_imgs: list[str], output_path: str) ->
tuple that takes a list of strings where each string points to a PNG image.
Given these images in the list, it is necessary to create a new image to be
saved in the file output_path.
The output image is created as follows: the input images in the list must be
concatenated horizontally in the order from left to right. That is, if
input_imgs = [img1, img2, img3], the output is constructed by concatenating
img1 | img2 | img3.
The input images have different widths and heights. 
The output image must be created in such a way that it is the "minimum" image
in height and width that contains all the images resting on the upper edge of
the resulting image.
In case there are parts in the output that are not covered by any input image,
these parts should be colored black.

The function returns the tuple (H, W) where H is the height and W is the
width of the output image and saves the latter in output_path.

Example, given the following 3 images:

img 1         img2          img3
HxW           HxW           HxW
20x30        30x50          40x10

xxx          +++++           .
xxx          +++++           .
             +++++           .
                             .

x=grey       +=green         . = red

The output image will be:

xxx+++++.
xxx+++++.   where o = black
ooo+++++.
oooooooo.

and the output image is 40x90 pixels in size.
see func5/in_1_1.png func5/in_1_2.png func5/in_1_3.png and
func5/exp_1.png for the correct output image

To load and save PNG files, you can use the load and save functions 
from the images library.
"""

import images

def func5(input_imgs: list[str], output_path: str) -> tuple:
    # Your code here
    pass

# %% ----------------------------------- EX.1 ------------------------- #
""" Ex1: 6 points

Define the recursive function ex1(root1: BinaryTree, root2: BinaryTree)
(or using recursive functions or methods) that receives
as parameters the roots root1 and root2 of two binary trees formed
by nodes of the type BinaryTree defined in the module tree.py. The two trees
contain strings with a single character as value and are structurally
identical, except for the fact that the value of corresponding nodes does not
always match. The function must return a list of tuples that
contain triples.

Each triple is constructed as follows:
for each pair of corresponding nodes between root1 and root2 that do NOT have the
same value, save in the triple
- first the level in the tree (considering the root as level 0),
- then the value of the node taken from the left tree
- and then the value of the node taken from the right tree.

The triples in the list must be ordered:
- in ascending order of level;
- in case of a tie on the level, in reverse alphabetical order based on the second value;
- in case of a tie on the second value, in alphabetical order based on the third value.

Hint: the 'ord' function can be useful to obtain the unicode value of characters.

Example:
           root1                                 root2

        ______A______       level 0          ______A______
       |             |                      |             |
       B__        ___C___   level 1         X__        ___C___
          |      |       |                     |      |       |
          D      E       F  level 2            Y      F       G 


If the input trees are these two above, the function returns
the list [(1, 'B', 'X'), (2, 'F', 'G'), (2, 'E', 'F'), (2, 'D', 'Y')]

in fact at level 1 the node 'B' of root1 is different from the node 'X' of
root2 and so on. The other elements are all at the same level 2 (therefore tied)
and are ordered in reverse alphabetical order based on
the second value so F-->E-->D.

********************************************************************
NB: if you write an additional function, do NOT define the additional
recursive function as an internal function but place it at the usual
level of ex, as an external function, otherwise you will not pass the recursive test!
********************************************************************
"""

from tree import BinaryTree

def ex1(node1: BinaryTree, node2: BinaryTree) -> list:
    # Your code here
    pass

# %% ----------------------------------- EX.2 -------------------------------#
'''Ex2: 3 + 3 points
Implement the function ex2(dirin, words), recursive or using recursive functions or methods, 
having as argument:
    - dirin: the path of an existing directory as a string
    - words: a list of words

The function will examine all text files (i.e., files with .txt extension) 
present in dirin and all its subfolders (at any level) and count 
the occurrences of the words in the list 'words'.
The words in a file are separated by one or more of the following characters: 
space, tab, or newline character.

(3 points) The function returns a list of tuples (word, occ), in which:
    - the first value of each pair is one of the words in the input list;
    - the second value 'occ' of the pair is the total number of occurrences 
      of that word in the text files.

(+ 3 points) The list is sorted based on the number of occurrences of the words 
(in descending order). If two or more words have the same number of occurrences,
they are sorted alphabetically (in ascending order). 
If a word from the input list is never found in the text files, it must still 
be returned by the function with a count of 0.

NOTICE 1: It is recommended to use the functions os.listdir, os.path.isfile, 
and os.path.isdir and NOT the os.join function in Windows. 
Use string concatenation with the '/' character.

NOTICE 2: It is forbidden to use the os.walk function or import other libraries

For example, given the folder "ex2/" and if words = ["cat", "dog"]
the function returns: [("dog", 11), ("cat", 6)].
'''
import os

def ex2(dirin, words):
    # Your code here
    pass
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Write your tests here
    print('*' * 50)
    print('You need to run grade.py if you want to debug with the built-in grader.')
    print('Otherwise, you can insert code here to test your functions, but you need to write the test cases yourself.')
    print('*' * 50)



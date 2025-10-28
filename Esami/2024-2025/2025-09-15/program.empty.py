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
    - solve at least 3 exercises of type func AND
    - obtain a score greater than or equal to 18

The final grade is the sum of the marks of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "NAME"
surname = "SURNAME"
student_id = "MATRICULATION NUMBER"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 marks
func1: 2 marks
Define the function func1(D), which receives as a parameter a dictionary
D, where each key is a positive integer N and the corresponding value
is a list of alphabetic characters L.
The function returns a list with one string for each key of the dictionary.
The strings are obtained by concatenating all the characters in L, except
for the character at the index equal to the corresponding key. If the index
is outside the list, the string contains all the characters of L.
The list is sorted in descending alphabetical order.
For example if D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'], the function will
return L = ['qa', 'su']
'''
def func1(D):
    ## Write your code here
    pass

# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 2 marks
Define the function func2(L) which has as parameter a list L of N lists.
Each list P inside the list L may contain one or more lists that can be empty
or contain one or more elements.
The function returns a list of N integers, where the i-th element
indicates the number of empty lists inside the list at the i-th position of L.
For example, if L = [ [3, []], [2, [3]], [4, [], [3,4], []]]
the function will return [1, 0, 2]
'''
def func2(L):
    ## Write your code here
    pass

# %% ----------------------------------- FUNC3 ------------------------- #
'''func3: 2 marks
Define the function func3(S, m, M) which receives as input a string containing
words separated by commas and, optionally, also by spaces.
The function must extract the words from S, considering only those whose
length is between m and M inclusive, and insert them into a second list
sorted alphabetically without considering the difference between uppercase
and lowercase.
For example if S = "Brad,ALIce, keVin,  oscar, Dana,   UMA,ian, Zoe"
the function func3(S, 3, 4) will return ['Brad', 'Dana', 'ian', 'UMA', 'Zoe']
'''

def func3(S):
    ## Write your code here
    pass

#%% ----------------------------------- FUNC4 ------------------------- #
"""func4: 8 marks
Define the function func4(input_filepath, output_filepath) that reads the
file indicated by input_filepath.  The input file contains words separated
by newlines, spaces, tabs, commas, or semicolons.  

The considered words must be grouped according to the letter that occurs
most frequently, without distinguishing between uppercase and lowercase.
For each group you must write to the output file one line in the format:

<lowercase letter>: <list of the words separated by a space>

The initial letter of the line is lowercase, followed by ": " (a colon plus
a space); then comes the list of words that have that letter with the highest
frequency, regardless of whether the letter in the word is uppercase or
lowercase. The lines must appear in alphabetical order based on the letter.
The lists are in alphabetical order, ignoring case, or maintaining alphabetical
order in the case of identical words that differ only by capitalization.
If a word has multiple letters with maximum frequency, then that word appears
on the line of each of those letters.

Caution, at the end of each line in the output file there is NO space but there is
ALWAYS a newline!

The function must return the total number of words, including duplicates,
found in the input file.

Example:

contents of func4/test1_in.txt:
GE
wOa;II,see	ua;PAO,oA;wOA
pao iu;jJa,kE

Call
n = func4("func4/test1_in.txt", "func4/test1_out.txt")

expected contents of func4/test1_out.txt:
a: oA PAO pao ua wOA wOa
e: GE kE see
g: GE
i: II iu
j: jJa
k: kE
o: oA PAO pao wOA wOa
p: PAO pao
u: iu ua
w: wOA wOa

Return value: 12
"""

def func4(input_filepath, output_filepath):
    ## Write your code here
    pass

# %% ----------------------------------- FUNC5 ------------------------- #
"""func5: 6 marks
Define the function func5(file_in, file_out) that uses images.load to
load the image present in file_in. The image is a list of lists
and each inner element is a pixel represented by the tuple (r, g, b).
The background is completely black, i.e. (0, 0, 0).

In the image there are pixels of different colors.

The function must identify for each row the color that occurs most
frequently and replace with black all the other pixels not of that color.
In the event that different colors in a row appear the same number of times,
choose the color with the lowest value in the first component, in case of a tie,
the lowest value in the second component, in case of a tie,
the lowest value in the third component.

The function must then save the result in file_out using images.save and
return the number of pixels whose color was replaced with black.
"""
import images

def func5(file_in, file_out):
    ## Write your code here
    pass

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks

Consider the class BinaryTree contained in the file tree.py that defines
a binary tree node. Write a function ex1(T, n) that is recursive or that
uses one or more recursive functions.
The function receives as input the root of a BinaryTree and an integer n.
The nodes of the input tree store integers.
The function must identify all root-to-leaf paths that traverse nodes for
which the sum of the values stored in them is equal to n.
The function must return a list containing the list of the values of the
nodes traversed for each identified path. The returned list must be sorted
in ascending order.

For example, 


        ______20_____       level 1          ______13______
       |             |                      |              |
       4__        ___1___   level 2      ___7___        ___10___
          |      |       |              |       |      |        |
          -2     1       4  level 3    _-5_    -1_    _-9_       3
                                      |    |      |  |    |       
                            level 4   5    4      6  6   -2    

If T is the tree on the left, then the function ex1(T, 22) must return
the list [[20, 1, 1], [20, 4, -2]]; if T is the tree on the right, then
the function ex1(T, 20) must return the list [[13, 7, -5, 5], [13, 10, -9, 6]]
"""
import tree

def ex1(T, n):
    ## Write your code here
    pass

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 marks

Write the function ex2(L, k) that is recursive or that makes use of
recursive functions. L is a list of strings of variable length.
k is an integer greater than 0.

The function must build and return the set of all strings of length k
obtained by concatenating two or more strings from L.

Example:
L = ['a', 'bb', 'ccc', 'd']
k = 3

Expected output:
{'dbb', 'bba', 'bbd', 'abb'}
"""

def ex2(L, k):
    ## Write your code here
    pass


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

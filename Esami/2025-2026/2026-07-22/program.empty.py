#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to perform BEFORE:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID
 3) Do not move the file outside the exam disrectory.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and evaluated) only if DEBUG = False
"""

nome = "NAME"
cognome = "SURNAME"
matricola = "STUDENT_ID"


# %% ----------------------------------- FUNC1 ------------------------- #

'''func1: 2 points
Define the function func1(L1, L2) that receives two lists of numbers. The function
must compare the pairs of elements in the same position of the two lists
ignoring the sign and return a new list containing the
smaller numbers, with their sign. If the lists have a different number of elements, the
returned list has the same number of elements as the shorter list.

Examples:
    func1([-2,3,4,-5],[1,-2,6]) returns [1,-2,4]
    func1([-1,4,5,2,0,15], [4,6,0,-16,3,1,1,5,3]) returns [-1, 4, 0, 2, 0, 1]

'''
def func1(L1, L2):
    # Write your code here
    pass

# print(func1([-2,3,4,-5],[1,-2,6]))
#print(func1([-1,4,5,2,0,15], [4,6,0,-16,3,1,1,5,3]))
# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 2 points
Define the function func2(words) that receives a set of alphabetic character strings
and returns a dictionary. The returned dictionary has
integers as keys and for values the sets of words that contain a number
of consonants equal to the corresponding key.

    Example:
        words = {"yak", "Gollum", "Batman", "AI", "star"}
        func2(words) returns {4: {'Batman', 'Gollum'}, 2: {'yak'}, 3: {'star'}, 0: {'AI'}}

'''

def func2(words):
    # Write your code here
    pass

# words = {"yak", "Gollum", "Batman", "AI", "star"}
# print(func2(words))

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 4 points
Implement the function func3(sales_log_path, report_path) that 
reads the file indicated by the string sales_log_path and generates a new file
indicated by the string report_path. The sales_log_path file contains lines
in the format product:unit_price:quantity, indicating the sales
of a certain product indicating the product name, its unit price and
the quantities sold. Lines of the same product may repeat,
even with different costs.
The function must calculate and return the total revenue from the sale of all
products and their total number and create a report file that contains lines in the format
product:total_quantity_sold:total_product_profit, ordered by
alphabetical order of the product.

'''
def func3(sales_log_path, report_path):
    # Write your code here
    pass



# %% ----------------------------------- FUNC4 ------------------------- #
''' Func 4: 4 points
Define func4(words_file, outfile) that receives two strings as input.
The function must read the content of the file indicated by the string
words_file, which contains alphanumeric strings separated by spaces,
tabs or newlines. The function must then write in a new file
indicated by the string outfile all the strings read, grouped on
different lines by first character, separated by a space and ordered in the
following order:
    - by decreasing string length
    - in case of equal length, by decreasing number of numeric characters
    - in case of tie, in alphabetical order.
The lines are ordered in alphabetical order.
The function returns the total number of strings read.

Example: if the input file contains the strings 'a4er', '4ever', '40er', 'forty', '007'
  func4 returns the value 5 and the created file will have the following content:
007
4ever 40er
a4er
forty
'''
def func4(words_file, outfile):
    # Write your code here
    pass

# print(func3(75, 'outf'))

# %% ----------------------------------- FUNC5 ------------------------- #
""" Func 5: 8 points
Define the function func5(minr, inputfile_png, outputfile_png) that receives as input
an integer value minr, two strings representing the names of two png files.
The function must read the image stored in the inputfile_png file, which is
a black image with pixels of different colors.
The function must write in a new file outputfile_png the image obtained
by copying from the inputfile_png image only the non-black isolated pixels that have a color whose
first component (Red) is greater than or equal to the value minr. A pixel is said to be isolated
if it has only black pixels adjacent vertically and horizontally.
Border pixels are isolated if above/below/beside there are black pixels.

Finally, the function must return the number of pixels copied in the output
image.
Remember to use the images.load and images.save functions to load and
save images from/to a file.
"""
import images
black = (0,0,0)

def func5(minr, inputfile_png, outputfile_png):
    # Write your code here
    pass

# %% ----------------------------------- EX1 ------------------------- #
""" Ex1: 6 points

The weight of a tree node corresponds to the node's value multiplied
by its depth.
Write the function ex1(root) recursive or that uses recursive helpers
that takes an instance of a BinaryTree node "root", in which
each node has as attributes value (float), left (BinaryTree or None) and right (BinaryTree or None),
and returns a pair (min, max) corresponding to the minimum and maximum weight
of the tree nodes, rounded to the second decimal place.

Consider the depth of the root equal to 1.

For example

depth      root
   1         20
            /  \
   2       10   5
            /  \
   3    0.5  0.2

  ex1(root) returns the pair (0.6, 20)
ATTENTION: the recursive part should not implemented as a inner function, else tests will fail.

"""
from tree import BinaryTree

def ex1(root):
    # Write your code here
    pass

# root = BinaryTree.fromList([20, [10, [0.5, None, None], [0.2, None, None]], [5, None, None]])
# print(ex1(root))
# root = BinaryTree.fromList([4, [25, [-4, None, None], [-1, None, None]], [11, [11, [8, [10, None, None], [24, [-4, None, None], None]], None], [-5, None, None]]])
# print(ex1(root))
# root = BinaryTree.fromList([23, [30, None, None], [3, [20, None, None], [-1, None, None]]])
# print(ex1(root))
# root = BinaryTree.fromList([27, [22, [-6, [10, None, [16, None, None]], [17, None, None]], [1, [13, [-9, [-3, None, None], None], [-2, None, [24, None, None]]], [5, None, None]]], [23, [22, [21, None, None], None], [10, None, None]]])
# print(ex1(root))
# %% ----------------------------------- EX2 ------------------------- #
""" Ex2: 6 points

Define the function ex2(lista) recursive or that uses another function or
recursive method that receives as input a list that can have as elements:
    - integers
    - strings
    - another list with the same characteristics.
The function must return the string obtained by concatenating all characters
contained in it and in all its sublists, at any level and in the
same order in which they appear.

Example if the list is the following:
    lista = [42, 'a',
             [7, 'b', [100, 'c']],
             9,  'z', ['x', 24]
             ]
    the function returns the string 'abczx'.

ATTENTION: the recursive part should not implemented as a inner function, else tests will fail.

"""

def ex2(lista):
    # Write your code here
    pass
# lista = [42, 'a', [7, 'b', [100, 'c']], 9, 'z', ['x', 24]]
# print(ex2(lista))

# directory_structure = ["secret_vault",["data.txt", "sec_log"],[["backup", "sec_root"],"notes.txt"]]
# key = 'sec'
# print(ex2(directory_structure, key))
#
# directory_structure = ["secret_vault",["data.txt", "sec_log", ["insect.txt", "out_sector.jpg"]],["night.txt",["backup", "sec_root"],"notes.txt",[['insect', 'sectorial']],["one, two", "three", "four"]]]
# key = 'sec'
# print(ex2(directory_structure, key))
#
# directory_structure = ["secret_vault",["data.txt", "sec_log", ["insect.txt", "out_sector.jpg"]],["night.txt",["backup", [["sec_root"]]],"notes.txt', 'office.exe', ['run', 'offline'],[['insect', 'sectorial']],["one, two", "three", "four"]]]
# key = 'o'
# print(ex2(directory_structure, key))
###########################################################################
# %% --------------------- MAIN ------------------------
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You must run grade.py if you want to debug with the automatic evaluator.')
    print('Otherwise you can insert your code here to test the functions but you must write your tests')
    print('*'*50)
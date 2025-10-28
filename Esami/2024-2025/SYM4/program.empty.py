#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Dict
import os
import tree

################################################################################
################################################################################
################################################################################

"""
First, assign the following variables with your FIRST NAME, LAST NAME,
STUDENT ID NUMBER

Add your implementations of the functions described below.

The final grade is the sum of the scores of solved problems.
To pass the simulation, you need to obtain a score greater than or equal to 18 
(students with SLD must obtain at least 15, after communication from Sapienza's 
SLD Service).

To obtain the score, run the grade.py file in the folder.
Set DEBUG=True in grade.py to view error stack traces.

To quickly comment/uncomment code, you can use the 
key combination Control + 1
"""

nome = "NOME"
cognome = "COGNOME"
matricola = "MATRICOLA"

# %% ----------------------------------- FUNC1 ------------------------- #

""" func1: 6 points
Write a recursive function func1(list) that, given a list of elements, 
returns a dictionary where the keys are the elements of the list and the 
values represent the number of occurrences of each element.

NOTE: It is possible to call recursive functions, but they cannot be 
internal (recursive functions can only be defined at the top level of the 
module and cannot be defined within other functions or classes).
"""


def func1(l: List, counts: Dict = None) -> Dict:
    pass


# %% ----------------------------------- FUNC2 ------------------------- #
""" func2: 9 points

Write a recursive function func2(directory), or a function that uses a 
recursive function internally, that takes a string 'directory' representing 
the path to a directory.

The function must recursively explore the directory tree rooted at 'directory' 
and return a dictionary.
The keys of the dictionary are the paths of subdirectories of 'directory', 
in the form of a string.

The value associated with a directory's key is a set of strings with the 
names of '.txt' files in the directory whose content starts and ends with 
the same character.

If a directory does not contain any .txt files with such a characteristic, 
then that directory does not appear in the dictionary.

If the function is called on 'func2/A', it returns:

{'func2/A/B': {'b.txt'}, 'func2/A/C': {'c.txt'}}

NOTE: Using os.walk is prohibited. You can use:
  os.listdir, os.path.isfile, os.path.exists, etc. To concatenate paths, 
  use the concatenation operation with the '/' character

NOTE: It is strongly recommended to break down the exercise into sub-problems 
by dividing into functions for each sub-problem.

NOTE: It is possible to call recursive functions, but they cannot be 
internal (recursive functions can only be defined at the top level of the 
module and cannot be defined within other functions or classes).
"""


def func2(root):
    pass


#%% ----------------------------------- FUNC3 ------------------------- #
""" func3: 5 points 

The Greatest Common Divisor (GCD) of two positive integers is the largest 
integer that divides both numbers without leaving a remainder.

The procedure to calculate the GCD follows these steps:

- Take two numbers, a and b.
- Check if the second number (b) is equal to 0:
    - If yes, the GCD is the first number (a).
    - If no, calculate the remainder of a divided by b (a%b).
- Repeat the procedure with the new values:
    - Replace a with the value of b.
    - Replace b with the value of the calculated remainder (a%b).
    - Continue until b becomes 0. At that point, the GCD is the current 
      value of a.

Write a recursive function or a function using recursive functions that 
calculates the GCD of two numbers. Assume a and b are non-negative integers.

Example: Finding the GCD of 48 and 18:

1. 48 % 18 = 12 (the remainder of 48 divided by 18 is 12).
2. Now calculate the GCD of 18 and 12: 18 % 12 = 6.
3. Now calculate the GCD of 12 and 6: 12 % 6 = 0.
4. The remainder is 0, so the GCD is 6.

NOTE: It is possible to call recursive functions, but they cannot be 
internal (recursive functions can only be defined at the top level of the 
module and cannot be defined within other functions or classes).
"""


def func3(a: int, b: int) -> int:
    pass


# ---------------------------- FUNC 4 ---------------------------- #
""" func4: 10 points

Write a recursive function or a function using recursive functions that 
takes as input a tree root (consisting of nodes that are instances of the 
BinaryTree class from the tree module) and an integer k, and returns two integers.

The first value to return (4 points) is the sum of all nodes in the tree 
that are at an even level minus the sum of all nodes in the tree that are 
at an odd level.
The root is at level 0 and is considered even.

The second value to return (4 points) is the number of nodes that have a 
value greater than the input value k.

    Examples:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    If the tree is the one on the left and k=2, the function returns the pair
    8, 4.
    If the tree is the one on the right and k=3, the function returns the pair
    -22, 6.
"""


def func4(root, k):
    pass


if __name__ == '__main__':
    pass
# ---------------------------- EOF ---------------------------- #

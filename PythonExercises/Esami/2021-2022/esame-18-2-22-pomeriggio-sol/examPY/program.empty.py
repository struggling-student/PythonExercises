#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

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

# %% ----------------------------------- EX.1 ----------------------------------- #

"""Ex 1: 7 points
Write a function that takes as input a list of strings and
an integer K and returns a pair of floats calculated as follows.

Let's call average of a sequence of K strings the average of the sums
of the unicode values of the strings that compose it.  For example:
the strings 'casa', 'coso', 'cosa', 'chiuso' have the sums of the unicode
values 408, 436, 422, 651, respectively. If K=2, the averages of the
consecutive strings will be 422.0, 429.0, and 536.5.

The variance, on the other hand, is calculated as the mean of the squared difference of each string from the mean, i.e.:
- given sequence S long K, if m is its mean, its variance v is
calculated as:
   v = sum(( m - s)**2)/K
where the sum is for each string s in S.

The two floats to be returned are the mean and variance of the group
of K consecutive strings of the input list that have the maximum mean.
All the floats have to be rounded to the third decimal place.

Example:
 ex1(['casa', 'coso', 'cosa', 'chiuso'], 2) will return (536.5, 13110.25)
since the sums of the unicode values are
[408, 436, 422, 651] and the mean, variance pairs for K=2 are,
 respectively
422.0 196.0
429.0 49.0
536.5 13110.25.
"""


def ex1(strings, K):
    ## INSERT HERE YOUR CODE
    pass

# %%----------------------------------- EX.2 ----------------------------------- #

""" Ex 2: 7 points

You have an image with a black background where a variable number of
crosses are drawn. The crosses can have different or same colors.
Each cross is composed of two crossing lines, one horizontal and one
vertical that meet in one point. 
The lines have thickness of 1 pixel and can be of
different lengths.  Two arbitrary crosses cannot overlap and there is
always at least one background pixel between the two. Each line of
the cross is at least one pixel long.

Tip: Before start coding, have a look at the images in the 'crosses/' directory

Design and implement the function ex2 which takes as input a PNG file
with one of the above images and finds all crosses. Each cross must
be described as a tuple of 4 points plus the color tuple.

The 4 points are in the order "top", "bottom", "left", "right", where:
    - "top" is the topmost point,
    - "bottom" is the lowest point,
    - "left" is the leftmost point,
    - "right" is the rightmost point.

Each point is a tuple of y, x coordinates, where y is the row and x is the column.

For example, the following cross:
     0 1 2 3 4
   0 . . . . .
   1 . . x . .
   2 . x x x x
   3 . . x . .
   4 . . x . .
   5 . . . . .

                   top    bottom left   right    color
is desbribed as: ((1, 2), (4,2), (2,1), (2, 4), (r, g, b))

The function has to return all the found crosses in a dictionary where:
- keys are the colors of the crosses found
- values are the set of all the crosses with that color
"""
import images

def ex2(path_to_im):
    pass
    # INSERT HERE YOUR CODE


# ----------------------------------- EX.3 ----------------------------------- #

"""
Ex 3: 9 points (6+3)

We have a sequence of numbers represented as a string S. We are
interested in finding all the leaves of the game tree that starts from
S and applies the following move:

- any triple of consecutive digits representing a binary number (i.e.,
  it only has zeros and ones) is replaced by the corresponding decimal
  value in the sequence.

For example, given the triple "501", it is impossible to apply any
move because the digit "5" invalidates that all numbers must be
binary. On the contrary, you can use the move on "101" and replace the
triple with the single-digit "5" that comes from the conversion of the
binary triple, that is "101"-->"5" = 1*2**2 + 0*2**1 + 1*2**0 = 4 + 1.
NOTE: for conversion functions, you can look at help(int)

Design and implement the recursive function ex3(S) (or make use of
recursive functions), which takes as input S and returns the leaves of
the game tree to which it is no longer possible to apply the move. The
leaves contain the integers you obtain by converting the strings into
"int".

For example: if the string is '5111001', the game tree (indented) will
be as follows. Note: the parentheses indicate the transformation of
the move.

5111001     #   Starting string - 5111001
-57001      #   5(111)001   becomes 5(7)001
--571*      #       57(001) becomes 571,   *leaf, no other move possible
-51601*     #   51(110)01   becomes 51601, *leaf, no other move possible
-51141*     #   511(100)1   becomes 51141, *leaf, no other move possible
-51111      #   5111(001)   becomes 51111
--571*      #       5(111)1 becomes 571,   *leaf, no other move possible
--517*      #       51(111) becomes 517,   *leaf, no other move possible

6 points: The function must return a list with all the leaves without
  repetitions.
The example above yields [571, 51601, 51141, 517].

3 extra points: The list must be sorted so that integers with fewer
  digits appear first. Moreover, the integers are sorted in descending
  order of numerical value for the same number of digits.
When sorted, the example above yields [571, 517, 51601, 51141].
"""
def ex3(S):
    pass
    # INSERT HERE YOUR CODE

# ----------------------------------- EX.4 ----------------------------------- #


"""
Es 4: 9 punti

Design and implement the function ex4(node, k), recursive or using
recursive functions or methods, which receives as arguments a binary
tree and finds the node divisible by k at maximum depth (starting from
root=0). The function returns the depth of the found node. If no node
is divisible by k, the function returns -1.  

Each node is an object of the class tree.BinaryTree

Example: if k=5 and the tree is as follows
                    1                           # 0 depth
                /       \                       #
            25           7  ------------------- # 1
        /      \                                #
       3        65 ---------------------------- # 2
     /   \                                      #
    4     55  --------------------------------- # 3

the function ex4 must return 3, because 55 is the node with value
multiple of 5 that is at maximum depth, that is 3. The other potential
nodes are 25 and 65, but they are at a lower depth (1 and 2
respectively).

"""
import tree
def ex4(node, k):
    # INSERT HERE YOUR CODE
    pass




###################################################################################

if  __name__ == '__main__':
    pass
    # INSERT HERE YOUR TESTS

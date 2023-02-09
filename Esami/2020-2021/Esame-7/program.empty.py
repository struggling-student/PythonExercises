################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER"""

name       = "NAME"
surname    = "SURNAME"
student_id = "MATRICULATION NUMBER"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To check the error stack trace, you can uncomment the dedicated line in
# testlib.py (see the comment in the body of function runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #
'''Ex. 1: 7 points

We want to compute the final standings of a football league championship.
  The input is in a text file. In this text file, every line contains the
  following fields separated by blank spaces (' '):
    - the club name of the home team
    - the amount of goals against the home team (i.e., scored by the away team)
    - the club name of the away team
    - the amount of goals against the away team (i.e., scored by the home team).
  The winning team gets 3 points. The losing team gets no points. In case of a
  draw, both teams get 1 point.

Design and implement a function ex1(matches_file, standings_file) such that:
  - it takes as arguments:
    - matches_file: the path of the .txt file with matches data
      (as described above);
    - standings_file: the filename of the .txt file in which the standings
      should be saved;
  - it returns the number of clubs that took part in the championship.
  
The output file sould contain the final standings. The ranking is computed
  according to the rules below, presented in order of priority (if two or more
  clubs stand in the same position – a tie – by applying rule (1), apply also
  rule (2), and so on):
  1) Total points gained at the end of the championship (descending)
  2) In case of a tie, the teams who scored more away goals prevail
  3) In case of a tie, the teams who scored more home goals prevail
  4) In case of a tie, the teams who received less away goals prevail
  5) In case of a tie, the teams who received less home goals prevail
  6) In case of a tie, the alphabetical order of the club names (ascending)
     applies.

In the output file, every line consists of the following fields, separated by a
  blank space (' '):
  - club name;
  - total points;
  - goals for (i.e., scored by the team);
  - goals against (i.e., received by team);
  - away goals for;
  - away goals against;
  - home goals for;
  - home goals against.

Example: if the games file contains only the lines (apart for the indentation):
    one 3 two 2
    two 2 one 0
It means that the clubs are only 2 ('one' and 'two') and that in the two games:
    one vs two: two won for 3 to 2 and thus one gets 0 points and two gets 3
    two vs one: one won for 2 to 0 and thus one gets 3 points and two gets 0
The final standings to write in the file are:
    two 3 3 4 3 2 0 2   (made more goals away)
    one 3 4 3 2 0 2 3
and the function shoud return the value 2 (numer of clubs)
'''

def ex1(matches_file, standings_file):
    # Enter your code here
    pass


# ----------------------------------- EX.2 ----------------------------------- #
'''Ex. 2: 8 points

Given a PNG image, we want to compute and draw the histogram of its colours.
Design and implement a function (input_file, output_file) such that:
  - it receives as arguments
    - input_file: the path to a PNG file;
    - output_file: the path to the file in which the histogram should be saved;
  - it returns:
    - the number of different colours in the input image.

The image of the histogram to be produced should be as follows.
  - The background is black (0, 0, 0).
  - Bars are:
    - horizontal;
    - left-aligned leaving 2 pixels from the left border
    - 2 pixels beneath the bar above (if any);
    - as wide as the number of pixels of that colour;
    - 3 pixels high;
    - of the same colour as that of the related pixels in the original file.
    - and there are at least 2 black pixels on the right
  - The top-most bar is 2 pixels beneath the upper border of the histogram.
  - The bottom-most bar is 2 pixels above the lower border of the histogram.
  - The colour bars should occur sorted by the decreasing count of related
    pixels, from top to bottom. In case two or more colours are associated to
    the same amount of pixels, bars are sorted as their associated colour-triple
    (in descending order).

  E.g. if the file is 5-5-10.png then the output histogram contains 9 bars
  (see expected_histogram_5-5-10.png) and the functions should return the value 9.

  To load and save PNG images you should use the load and save functions of the
  images.py library.
'''
import images

def ex2(fimage, n):
    # Enter your code here
    pass


# ----------------------------------- EX.3 ----------------------------------- #

'''Ex. 3: 9 points

Design and implement a function ex3(root) such that:
    - it is recursive or uses recursive function(s)/method(s);
    - it receives the root node ('root') of a tree, namely a tree.BinaryTree
      object;
    - it returns a list of integers.
    
The list of integers to be returned should be generated by visting the tree in
  post-order. The list should contain all and only the values of the nodes such
  that a child has a value that is a multiple of the other child's value.

We recall that a post-order visit requires to visit the left child first, then 
  the right child, and finally the root node.
  For example, given the root of the following tree:
                        6
                    /       \
                 5             1
              /     \       /     \
             2       4     6       8
                    / \           / \
                  15   3         2   10

  the function should return [4,5,8,6].
'''
from tree import BinaryTree

def ex3(root):
    # Enter your code here
    pass


# ----------------------------------- EX.4 ----------------------------------- #

'''Ex. 4: 8 points

Design and implement a function ex4(n) such that:
    - it is recursive or uses recursive function(s)/method(s);
    - it receives an integer ('n') as argument;
    - it returns all the numbers that can be encoded in base-3 on n positions,
      in ascending order.

  Notice that the enumeration has to be obtained * * * recursively * * *.
  In no case iterative approaches are acceptable for this exercise.
  
The function should return the enumeration of generated numbers as a list.
  Every element of the list is a tuple. The tuple consists of the following
  three elements:
    1) A string that expresses the base-3 encoding of the number;
    2) An integer that expresses the base-10 conversion of the number;
    3) The minimum number of bits that are necessary to represent the number in
       base 2.
       
    If the argument n is less than or equal to zero, the function should return
    [('', None, None)] without entering the recursion.
    
    Notice that the int() function can be used.
    
    Given, e.g., n=2, we show below a possible recursion tree for convenience
    (although it is unnecessary to create additional data structures to solve
    this exercise):
                                                     
            ______________|_______________              
           |              |              |             
           0              1              2            
        ___|___        ___|___        ___|___
       |   |   |      |   |   |      |   |   |                           
       0   1   2      0   1   2      0   1   2                      

Example: ex4(n=2) should return:
  [('00', 0, 1),
   ('01', 1, 1),
   ('02', 2, 2),
   ('10', 3, 2),
   ('11', 4, 3),
   ('12', 5, 3),
   ('20', 6, 3),
   ('21', 7, 3),
   ('22', 8, 4)]

  (notice the mapping between decimal and base-3 numbers).
'''
from tree import BinaryTree

def ex4(root):
    # Enter your code here
    pass



################################################################################
if __name__ == '__main__':
    # Insert your own tests here
    pass

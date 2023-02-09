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
'''Ex1: 7 points
    Design and implement a function ex1(file_rows, file_cols, file_values)
    that takes 3 file paths as input and returns a matrix as output.
    The output matrix should be represented as a list of lists.
    The aim of the exercise is to write the output matrix (henceforth named as
    "out"), computed on the basis of three matrices ("rows", "cols" and
    "values") stored in the three text files provided as an input to the
    function (file_rows, file_cols, file_values, respectively).

    The files keep integer numbers on their lines separated by blank spaces.
    Every file line is a matrix row. The c-th space-separated number in a line
    is the element in the c-th column. Therefore, the c-th number in the r-th
    line of the file is the element at position (r,c) in the matrix.
    For example, if the file content is as follows:

    0    1
    1 0

    the corresponding matrix, represented as a list of lists, is the following:

    [[0, 1],
    [1, 0]].

    The "out" matrix should bear at position (r,c) the element of the "values"
    matrix specified at position (r',c') where r' is the value of "rows" at
    (r,c) and c' is the value of "cols" at (r,c). 
    If (r',c') is not a suitable index for "values" (for example, because r' or
    c' are negative numbers, r' exceeds the number of rows or c' is beyond the
    number of elements in the line), then the "out" matrix should contain None
    at the corrisponding position.

    For example: given three input files encoding the following matrices:
          "rows"              "cols"                     "vals"
     0         1        |   1              5    |     3     4      1
     0         1        |   0              2    |     10     -1    5

    the function should return:

      "out"
    [[4, None],
     [3, 5]]

    Notice that:
    - "out" contains 5 at position (1,1) as 5 is in "vals" at
      row 1, as specified by the "rows" matrix at position (1,1), and
      column 2, as specified by the "cols" matrix at position (1,1);
    - "out" contains None at position (0,1) because the "values" matrix is not
      accessible at position (1,5).

    Note: "out", "rows" and "cols" have the same size, whereas the size of
          "values" can be different.
'''

def ex1(file_rows, file_cols, file_values):
    pass
    # Insert your code here


# ----------------------------------- EX.2 ----------------------------------- #

'''Ex2: 8 points
    
    Given a PNG image with white rectangles on a black background, we want to
    sum up the perimeters of all rectangles that have the same width in pixels.
    Rectangles do not touch nor overlap.
    
    Design and implement a function ex2(input_file) such that it takes a file
    with a PNG image as input (the content of which is as described above) and
    returns a dictionary.
    
    The output dictionary is such that:
    - the keys represent the widths of the rectangle;
    - the values represent the sum of the perimeters of the rectangles whose
      width is equal to the key.

   For example, as the image in ex2p1.png contains two rectangles whose width is
      of 20 pixels and height of 10 pixels, and one rectangle of size 3x3, the
      function should return the following dictionary:
      {20: 120, 3:12} 
'''

import images
def ex2(input_file):
    pass
    # Insert your code here


# ----------------------------------- EX.3 ----------------------------------- #

'''Ex3: 9 points
    Design and implement a function ex3(charstring) such that:
    - it is recursive or uses recursive function(s)/method(s);
    - it receives a string (charstring) as input;
    - it returns the leaves of a game tree obtained by applying the following
      move:
      - remove from charstring a pair of consecutive different characters
        in a case-insensitive fashion (i.e., consider uppercase and lowercase
        characters as equal).
    The leaves are strings to which the move can no longer be applied.
    
    The function should return the leaves in a list, with no repetitions and 
    in a decending order determined by the string length (from the longest to
    the shortest). In case of equal length, the ascending alphabetical order
    applies.
    
    For example, if charstring is 'aBbACc' the (indented) game tree is as
    follows:

aBbACc
    bACc            # removed: 'aB'
        Cc          # removed: 'bA' (leaf)
        bc          # removed: 'AC'
           ''       # removed: 'bc' (leaf)
    aBCc            # removed: 'bA'
        Cc          # removed: 'aB' (leaf)
        ac          # removed: 'BC'
           ''       # removed: 'ac' (leaf)
    aBbc            # removed: 'AC'
        bc          # removed: 'aB'
           ''       # removed: 'bc' (leaf)
        aB          # removed: 'bc'
           ''       # removed: 'aB' (leaf)
    
    The result is the following list: [ 'Cc', '' ]

'''

def ex3(charstring):
    pass
    # Insert your code here


# ----------------------------------- EX.4 ----------------------------------- #

'''Ex4: 8 points

    Design and implement a function ex4(dir1, ext) such that:
    - it is recursive or uses recursive function(s)/method(s);
    - it takes the following parameters as input:
      - a path to a directory (dir1) and
      - a string (ext);
    - it returns a dictionary computed as follows.
    
    The function explores the directory tree starting from dir1 and return a
    dictionary such that:
    
    - every key is the path of a sub-directory of dir1 that contains at least
      one file such that its name begins with an uppercase letter and its
      exention is ext;
      
    - values are lists of strings, wherein each string is the name of a file 
      in the key's sub-directory such that its name begins with an uppercase
      letter and its extension is ext; lists are ordered by the length of the
      string (ascending, i.e., from the shortest to the longest) and, in case of 
      equal length, by the alphabetical order (ascending).

    Example: function ex4('ex4/a0','.txt') should return the following
    dictionary:
      {
       'ex4/a0': ['Roar.txt', 'Miaao.txt', 'Muuuu.txt'],
       'ex4/a0/b1': ['Bau.txt', 'Ciao.txt', 'Miao.txt']
      }

    Hint: The usage of function os.listdir and of the functions in the os.path
    library is recommended.
    
    Warning: Function os.path.join may not work on a Windows machine. Thus, the
    concatenation of sub-directory names with the '/' character is recommended.

    NOTE: You can not use the function os.walk
'''
import os

def ex4(dir1, ext):
    pass
    # Insert your code here

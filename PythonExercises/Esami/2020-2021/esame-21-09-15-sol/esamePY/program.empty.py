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

''' Ex1: 6 points

    Design and implement a function ex1(pts, indexes) that takes two lists of
    lists as input: pts and indexes. Those two lists of lists represent 
    matrices. The size of the pts matrix is Nx3 and the size of the 
    indexes matrix is Mx3, where N is different from M.
    The ex1 function should return a third matrix of size Mx3x3, built as
    follows:
    - for every row in the indexes matrix, a row occurs in the output matrix;
    - in particular, every row of the indexes matrix serves as a selector for
      a row in the pts matrix;
    - the three lines selected in the pts matrix are included as a new row in
      the output matrix.  
   
    For example, given the following input data:

    pts    =  [ [1,2,3],    # 0
                [50,20,30], # 1
                [0,12,13],  # 2
                [3,1,0]     # 3
              ]

    indexes = [ [0,1,3],
                [0,0,0],
                [3,2,1],
              ]
   
    the following matrix should be returned by ex1(pts, indexes):

    [
      [[1, 2, 3], [50, 20, 30], [3, 1, 0]], 
      [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
      [[3, 1, 0], [0, 12, 13], [50, 20, 30]]
    ]
'''

def ex1(pts, indexes):
    pass
    # insert your code here / inserisci qui le tue istruzioni

# ----------------------------------- EX.2 ----------------------------------- #

''' Ex2: 8 points

    The objective of this exercise is to draw a sequence of coloured rectangles
    along the secondary diagonal of a picture. We recall that the secondary
    diagonal connects the bottom-left corner to the top-right corner.
    The rectangles should be drawn on a black background.
   
    To this end, design and implement a function
      ex2(rectangles, width, height, png_file)
    which takes the following arguments as input:
    - rectangles: a list of triples (r_w, r_h, r_colour), which indicate
      width (r_w), height (r_h) and colour (r_colour, as an RGB triple) of
      every rectangle to be drawn;
      we assume this list is of length 2 or more;
    - width and height: the size of the picture to be created;
    - png_file: the name of the PNG file in which the image should be saved.
   
    The rectangles should be positioned along the secondary diagonal so that
    their centres are equally distanced both horizontally and vertically.
    In other words:
    - first off, the first and the last rectangle should lie on the bottom-left
      and top-right corners, respectively;
    - then, the distance among the centres of the other rectangles should be
      computed considering the horizontal and vertical distance from the
      centres of the already laid rectangles (that is, of the first and the
      last one in the list; NOTICE that the horizontal and vertical distances
      may differ!);
    - the computed coordinates of the rectangles should be rounded to the
      closest integer.
   
    As rectangles may overlap, they should be drawn in the same order
    as they occur in the input list.
   
    The function should return the number of black pixels in the picture.
   
    HINT: We recommend to implement an auxiliary function that draws a
    rectangle of given colour and size, given its centre.
    We recall that (0, 0) indicate the pixel on the top-left corner,
    as the values on the y coordinate increase from top to bottom.
    
    Example:
    assuming that width is set to 500 and height is set to 400 (i.e., the
    picture's size is 500x400), let the rectangles list be as follows:
    [   (316, 260, (171, 155, 135)),     
        (304, 328, (77, 176, 176)),
        (172, 180, (193, 76, 56))]
    Then, the image to be built should be like the one in
    "rectangles/example.png".
    The function should return 42336 as the number of black pixels.
    
    Notice, indeed, the following:
    - the coordinates of the first rectangle's centre are (158, 270), that is
      0+316/2=158 (horizontally) and 400-260/2 = 270 (vertically); it gets
      painted on the picture's area from (0,140) to (315,399);
    - the coordinates of the last rectangle's centre are (414, 90), that is
      500-172/2=414 (horizontally) and 0+180/2 = 90 (vertically); it gets
      painted on the picture's area from (328,0) to (499,179);
    - only one rectangle is left, thus the distance between centres can be
      divided by two, both horizontally and vertically, thereby yielding
      (414-158)/2 = 256/2 = 128 and (270-90)/2 = 180/2 = 90,
      respectively: those are the horizontal and vertical distance of the
      centre of the rectangle in the middle from the other two rectangles'
      centres; therefore, the rectangle in the middle of the picture has its
      centre at (286, 180), as
      158+128 = 414-128 = 286 (horizontally) and
      270-90 = 90+90 = 180 (vertically); the rectangle in the middle occupies
      the region starting from its centre, (286,180), and then expanding for
      half its width (304/2 = 152) and half its height (328/2 = 164);
      as a result, it gets painted on the picture's area from (134,16) to
      (437,343).
    
    As a final remark, NOTICE that, because of rounding numbers, the area of 
    the drawn rectangles could exceed the boundaries of the picture.
    Please handle the error (or find a way to avoid it) and paint only the 
    part inside the image.
'''
import images
def ex2(rectangles, width, height, png_file):
    pass
    # insert your code here / inserisci qui le tue istruzioni

# ----------------------------------- EX.3 ----------------------------------- #

''' Ex3: 9 points

    Design and implement a function ex3(dir_path, words, extensions) such
    that
    - it is recursive or uses recursive function(s)/method(s);
    - it looks for files in a directory tree such that they have one of the
      given extensions and contain at least one of the provided words; the files
      contain words that are separated by one or more non-alphabetic characters.
    
    In particular, the function takes the following arguments as input:
    - dir_path: a path to the base directory to be explored;
    - words: a list of words to be looked for inside the files;
    - extensions: a list of extensions for the searched files;
    and returns a dictionary such that:
    - every key is a path to a file matching the search criteria;
    - the value associated to every key is the FIRST word in the searched
      list that can be found inside the key's file.
    
    Notice that:
    - files and directory starting with '.' must be ignored, and
    - the usage of functions such as os.walk and the like is forbidden.
    Hint:
    - define the recursive function at the outermost level so that the
      automated recursion test works. 
    
    Example:
    assume that the "test/d1" directory contains a file named "check.txt"
    containing the following string: 'sky-dog...home!!! nail'. The
    invocation of
      ex3('test',['rabbit','home','dog'],'txt')
    should return
      {'test/d1/check.txt':'home'}
'''
import os

def ex3(dir_path, words, extensions):
    pass
    # insert your code here / inserisci qui le tue istruzioni

# ----------------------------------- EX.4 ----------------------------------- #

'''Ex4: 8 points

    Design and implement a function ex4(alphabet, k) such that
    - it is recursive or uses recursive function(s)/method(s)
    - it takes as input a string (alphabet) and an integer (k)
    - it recursively generates all palindrome words of length k
      that are composed by characters in the alphabet string
    - it returns a set containing all the generated words.
   
    Examples:
    ex4('abc', 4)
    returns
    {'aaaa', 'abba', 'baab', 'bbbb', 'acca', 'caac', 'cccc', 'bccb', 'cbbc'}

    ex4('abc', 3)
    returns
    {'aaa', 'aba', 'bab', 'bbb', 'aca', 'cac', 'ccc', 'bcb', 'cbc'}

'''


def ex4(alphabet, k):
    pass
    # insert your code here / inserisci qui le tue istruzioni

################################################################################
if __name__ == '__main__':
    # Insert your own tests here
    pass

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
from pkg_resources import non_empty_lines

name = "NAM"
surname = "SUNAME"
student_id = "MTRICULATION NUMBER"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 4 points
Define the function func1(D1: dict[str, int], D2: dict[int, str]) -> str,
which receives as arguments two dictionaries D1 and D2: D1 has strings as keys
and integers as values, while D2 has integers as keys and strings as values.
The function must find all the values of D1 that are keys of D2 and return
a list obtained concatenating the corresponding keys of D1 with the corresponding
value of D2. The list must be sorted in decreasing order of length and, in case
of a tie, in ascending alphabetical order.

Example:
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
D2 = {4:'bb', 1:'ff', 2:'ggg'}

Result: ['bbggg', 'aaff', 'ccff', 'ebb']
'''

def func1(D1,  D2):
    pass
    def criterio(s):
        return (-len(s), s)
    stringhe = [k + D2[v] for k, v in D1.items() if v in D2]
    return sorted(stringhe, key=criterio)

## Tests
# D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
# D2 = {4:'bb', 1:'ff', 2:'ggg'}
# print(func1(D1, D2))  # ['bbggg', 'aaff', 'ccff', 'ebb']

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Define a function func2(l) that takes a list of int l as input and modifies
the list so that the element in position i is the sum of all the elements
from position 0 to i. The function returns the value of the last element
of the modified list.

Example: if l = [3, -3, 6, -1, 10], the call func2(l) returns the value 15
    and modifies l in [3, 0, 6, 5, 15].
'''
def func2(l : list[int] ) -> int :
    pass
    for i in range(1, len(l)):
        l[i] += l[i-1]
    return l[-1]


# l = [3, -3, 6, -1, 10]
# print(func2(l) ) # [3, 0, 6, 5, 15]
# print(l)
# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Define a function func3(words, l) that that takes as input:
    - a set of strings 
    - an int
and returns a new set with all the strings of length at least l in the set
words that are a substring of another string in words.

Example: if words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
the call func3(words, 3) should return the set
{'cat', 'bert'}
'''

def func3(words :  set[str], l : int) -> set[str]:
    pass
    return {w   for w in words
                if  any(w in x for x in words if w!=x)
                    and len(w) >= l}

# print(func3({'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}, 3))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 points
Define a function func4(file_in, file_out, length, chars) that takes as input:
    -two strings representing the paths of two text files
    -an integer length,
    -a string chars.
The function must return the list of all the words found in the file pointed
by file_in with a length at least length and containing at least one of the
characters in the string chars.
The list must be sorted by decreasing length and, in case of a tie, in
alphabetical order.
Moreover, the function must write the words of the list in output in the
file pointed by file_out separated by a whitespace.

Example: func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd')
     should return the list ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
     and write the string 'hippopotamus elephant cobra horse panda snake' in func4/out_01.txt.
"""

def func4(file_in : str, file_out: str, length:int, chars:str) -> list[str]:
    pass
    with open(file_in) as f:
        words = f.read().split()
    words = [w for w in words if len(w) >= length and any(c in w for c in chars)]
    words.sort(key=lambda x: (-len(x), x))
    with open(file_out, 'w') as f:
        f.write(' '.join(words))
    return words

# print(func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd')) # ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Define a function func5(input_png, output_png, m, M) which takes as inputs
    - the path to an image stored in a .png file named input_png,
    - the path to an output png file output_png
    - two ints m and M.
The input image contains several colored horizontal lines on a black background. 
The function has to find the lines with a length included in the range [m, M]
and create a new image with only those found lines.

The function returns the difference between the number of lines found in
the input and those in the output image.
"""
import images

def func5(input_png:str, output_png:str, m:int, M:int) -> int:
    pass
    img   = images.load(input_png)
    W, H  = len(img[0]), len(img)
    lines = trova_linee(img)
    lines2 = [l for l in lines if m <= l[2] <= M]
    img2  = crea_immagine(lines2, W, H)
    images.save(img2, output_png)
    return len(lines) - len(lines2)

def trova_linee(img):
    return [ line   for y, row in enumerate(img)
                    for line in trova_linee_X(row, y) ]

def trova_linee_X(row, y):
    ''' Trova le linee di una singola riga della immagine '''
    linee = []
    b = 0,0,0
    last_color  = None
    last_x      = None
    last_length = 0
    for x,pixel in enumerate(row):
        if pixel == b:
            if last_color is not None:
                linee.append((last_x, y, last_length, last_color))
                last_color = None
                last_length = 0
                last_x = None
        else:
            if pixel != last_color:
                if last_color is not None:
                    linee.append((last_x, y, last_length, last_color))
                last_color = pixel
                last_length = 1
                last_x = x
            else:
                last_length += 1
    if last_color is not None: # se c'è una linea alla fine appoggiata al bordo destro
        linee.append((last_x, y, last_length, last_color))
    return linee

def crea_immagine(lines, W, H):
    img2  = [[(0,0,0)]*W for _ in range(H)]
    for x,y,l,c in lines:
        for i in range(l):
            img2[y][x+i] = c
    return img2


def gen_image(fname, h, w, N):
    from random import randint
    img = [[(0,0,0)]*w for _ in range(h)]
    while N:
        color = (randint(0,255), randint(0,255), randint(0,255))
        row = randint(0,h-1)
        col = randint(0, w-randint(0,w//2))
        
        length = randint(1,w-col)
        print(w, col, length, col+length)
        if any(x!=(0,0,0) for x in img[row][col:col+length]):
            continue
        img[row][col:col+length] = [color]*length
        N-=1
    images.save(img, fname)

# print(func5('test.png', 'test_out.png', 1, 80))
# print(func5('func5/func5_test1.png', 'func5/func5_out1.png', 1, 20)) # 6
# print(func5('func5/func5_test2.png', 'func5/func5_out2.png', 20, 40)) # 14
# print(func5('func5/func5_test3.png', 'func5/func5_out3.png', 40, 100)) # 28
# print(func5('func5/func5_test4.png', 'func5/func5_out4.png', 10, 40)) # 37

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(chars, l), recursive or using recursive functions
or methods, that takes as input a set of characters (strings of length one)
and an int l and outputs the set of all the possible palindrome strings of
length l made of characters taken from chars.
Ex:
    ex1({'a', 'b', 'c'}, 3) must return the set {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}

"""
def ex1(chars, l):
    ## Write your code here
    pass
    if l == 1:
        return chars
    if l == 0:
        return {''}
    # altrimenti aggiungo lo stesso carattere ai due estremi
    return {c + s + c for c in chars for s in ex1(chars, l-2)}


# print(ex1(set('abc'), 3))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

Define a function ex2(root), recursive or using recursive functions
or methods, that takes as argument 'root', an instance of a BinaryTree as defined
in the tree module, representing the root of a binary tree with int values.
The function must return a pair (v, l) with the value and the level of the
node of the tree with the max product v*l.
Assume that the root is at level 1.
Assume that the MAX product is unique.

For example, if input is the root of following tree:

               6             |
              / \            |
             5   3           |
            /   / \          |
           4   10  6         |
              /   / \        |
             7   8  1        |
             
the function should return the pair (8, 4).
"""
import tree

def ex2(root, level=1):
    pass
    coppie = trova_coppie(root, level)
    def criterio(x):
        return x[0]*x[1], -x[1]
    return max(coppie, key=criterio)

def trova_coppie(root, level):
    if root is None:
        return []
    coppie1 = trova_coppie(root.left,  level+1)
    coppie2 = trova_coppie(root.right, level+1)
    return coppie1 + coppie2 + [(root.value, level)]

T = tree.BinaryTree.fromList([6, [5, [4, None, None], None ], [3, [10, [7, None, None], None],
                                                                [6, [8, None, None], [1, None, None]]]])
# print(T)
print(ex2(T))
# print(T)    


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

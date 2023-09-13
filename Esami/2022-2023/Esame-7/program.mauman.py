



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Steps to do FIRST:
 1) save this file as program.py
 2) assign the variables below with your
    FIRST NAME, LAST NAME, STUDENT ID (Sapienza matriculation number)

To pass the exam it is necessary to:
    - !!!fill in your personal information in the variables below!!!
    - AND solve at least 1 ex-type exercise (recursive problem)
    - AND solve at least 3 func-type exercises
    - AND obtain a score greater than or equal to 18

The final score is the sum of the scores of the solved problems.
"""
nome       = "nome"
cognome    = "cognome"
matricola  = "matricola"

name       = 'name'
surname    = 'surname'
student_id = 'student_id'    # your Sapienza registration number

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

# ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 2 points

Define the function func1(dict1, dict2) that receives as arguments two dictionaries that have
integer keys and string list values.
The function must return the dictionary that contains the keys in common to both dictionaries.
The values associated with each key are those that appear in only one of the two lists
associated with that key in the two dictionaries.
These values, without repetition, should be sorted in order of decreasing length 
and in case of equality in ascending alphabetical order.

Example:
dict1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
dict2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
the result is  { 1: ['bc', 'cd', 'f'], 3: ['qrt', 'bn', 'st', 'c'] }
'''

def func1(dict, dict):
    pass
    def criterio(s):  return -len(s), s
    return {
        k : sorted(set(v1).symmetric_difference(set(diz2[k])), key=criterio)
        for k,v1 in diz1.items()
        if k in diz2
    }

#diz1 = { 1: ['a', 'bc', 'a'], 2: ['b', 'cr', 'e'], 3: ['a', 'qrt', 'st'] }
#diz2 = { 1: ['a', 'cd', 'f'], 5: ['b', 'cr', 'e'], 3: ['a', 'bn', 'c'] }
#print(func1(diz1,diz2))

# ---------------------------- FUNC 2 ---------------------------- #

'''
Func 2: 2 punti

Define the function func2(text) which receives as an argument:
  - text: a string consisting of words separated by spaces
and which returns a dictionary that has:
  - as keys the initial letters of the words, lower case
  - as values the number of words that contain that letter,
  ignoring the difference between lower and upper case
  
Example:
text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
expected   = { 's':2, 'l':4, 'p':6, 'c':6}
'''

def func2(text):
    pass
    lower = text.lower().split()
    diz = { parola[0]: 0 for parola in lower }
    for parola in lower:
        for carattere in diz:
            if carattere in parola:
                diz[carattere] += 1
    return diz

# ---------------------------- FUNC 3 ---------------------------- #
'''
Func 3: 4 punti
Define the function func3(textfile_in, textfile_out) which receives as argument:
- textfile_in: the path to a text file to read
- textfile_out: the path to a text file to create

The file at the path textfile_in contains either 
floats or integers, positive or negative, separated by spaces.

The function must read the numbers, sort them in descending order,
based on the number of significant digits, 
and in case of equality in ascending value.
(significant digits are those remaining ignoring dot and sign.)

Then it must write these sorted numbers into the textfile_out file,
separated by comma and space.
Finally, the function returns the number of numbers read from textfile_in.

Example:
if the file textfile_in contains the line
-23.5 17 -141 +322.7 -3227
In the textfile_out file, the function should write the line
-3227, +322.7, -141, -23.5, 17
and return the value 5
'''

def func3(textfile_in, textfile_out):
    def criterio(elemento):
        cifre = elemento.replace('.','')
        cifre = cifre.replace('-', '')
        cifre = cifre.replace('+', '')
        return -len(cifre), float(elemento)
    with open(textfile_in) as FIN:
        numeri = FIN.read().split()
    numeri.sort(key = criterio)
    with open(textfile_out, mode='w') as FOUT:
        print(*numeri, sep=', ', file=FOUT)
    return len(numeri)


# ---------------------------- FUNC 4 ---------------------------- #

'''
Func 4: 4 points
Define the function func5(filein) that receives as argument
- filein: a text file containing a matrix of NxM integers separated by spaces

and which returns the matrix transposed with respect to its secondary diagonal 
(i.e., the one going from the top right element to the bottom left element)
represented as a list of lists.

Example:
if filein contains the matrix:
1 2 3 4
5 6 7 8
9 10 11 12
the function should return the matrix reflected with respect to the diagonal 4-9, as a list of lists:
[[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
'''
def func4(input_filename):
    pass
    with open(input_filename) as FIN:
        M = [ list(map(int, riga.split())) for riga in FIN ]
    W = len(M[0])
    H = len(M)
    return [ [  M[H-1-y][W-1-x]
                for y in range(H)]
                for x in range(W)]

# ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 8 points

Define the function func5(txt_input, width, height, png_output) that receives as arguments:
- txt_input: the path to a file containing a list of figures to be drawn
- width: width in pixels of the image to be created
- height: height in pixels of the image to be created
- png_output: the path to a PNG image you need to create, containing the figures

The function should create a black background image and draw all the figures
indicated in the 'txt_input' file, in the order they appear in the file.

The txt_file contains, one per line, separated by spaces: 
- a word indicating the type of figure to be drawn
- the three R G B components of the color to be used
- the coordinates and other parameters needed to define the figure
There can be 2 types of figure:
- descending diagonal of a square (-45° direction):
    diagonalDOWN R G B x y L
    The diagonal begins at the point (x,y), heads LOW-right, and is L pixels long
- Ascending diagonal of a square (+45° direction):
    diagonalUP R G B x y L
    The diagonal starts at the point (x,y), heads UP-right, and is L pixels long

Then it must save the obtained image in the file 'png_output' using the images.save function.
It must also return the number of diagonals drawn of the two types 
as a tuple of the two values (DIAGUP, DIAGDOWN).

NOTE: the points of the figures outside the image must be handled correctly, 
in fact, negative coordinates are also allowed, 
and dimensions or parameter L such that parts of the figure are outside the image.

Example: if the file func5/in_1.txt contains the 3 figures:
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

running the function func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
will produce the figure in the file 'func5/expected_1.png'
and will return the pair (2, 1)
'''

from math import dist
import images
def func5(txt_input, width, height, png_output):
    pass
    def draw_diagonalDown(img, W, H, x, y, L, color):
        for i in range(L):
            X,Y = x+i, y+i
            if 0 <= X < W and 0 <= Y < H:
                img[Y][X] = color
    def draw_diagonalUp(img, W, H, x, y, L, color):
        for i in range(L):
            X,Y = x+i, y-i
            if 0 <= X < W and 0 <= Y < H:
                img[Y][X] = color
    img = [ [(0,0,0)]*width for _ in range(height) ] # immagine vuota, nera
    diagUP = diagDOWN = 0
    with open(txt_input) as F:
        for line in F:
            tipo, *data= line.split()
            R, G, B, x, y, L = list(map(int, data))
            if tipo == 'diagonalDOWN':
                draw_diagonalDown(img, width, height, x, y, L, (R, G, B))
                diagDOWN += 1
            elif tipo == 'diagonalUP':
                draw_diagonalUp(  img, width, height, x, y, L, (R, G, B))
                diagUP += 1
    images.save(img, png_output)
    return diagUP, diagDOWN

# print(func5('func5/in_1.txt', 50, 100, 'func5/out_1.png'))


# ---------------------------- EX 1 ---------------------------- #

'''
Ex1: recursive, 6 points 

Let us define the function ex1(root, values), recursive or using recursive functions,
which receives as input 
- the root 'root' of an n-ary tree defined by nodes nary_tree.NaryTree
- a list of integers 'values' 
which destructively modifies the 'root' tree by adding all nodes that are at depth P 
(assuming the root is at depth 0) to the value that in the 'values' list is
at index P (if it exists, otherwise they remain as they are).

The function must return the sum 'total' of all the nodes in the resulting tree.

IMPORTANT: the recursive function must be define at the outmost level, 
that is, with the keyword 'def' located at the beginning of the line.

Example:
    values: [-42, -80, 68, 2, 81, 75, 54, 48, -4, 5]        to be added up:
    root:                        -7                         | -42
                    /      |      |      |    \             |
                  -10      -3     -8    -10    -5           | -80
                /   \      |       |     |                  |
               6    -2     9       7     -9                 | +68

    expected:                    -49                         |
                    /      |       |      |     \            |
                  -90     -83     -88    -90    -85          |
                /   \      |       |      |                  |
               74    66   77       75     59                 |
    total = -134


'''

from nary_tree import NaryTree

def ex1(root : NaryTree, valori : list[int]):
    return _ex1(root, valori, 0)

def _ex1(root : NaryTree, valori : list[int], depth : int):
    if depth < len(valori):
        root.value += valori[depth]
    total = root.value
    for son in root.sons:
        total += _ex1(son, valori, depth + 1)
    return total


# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: recursive, 4 + 2 points
    Define the function ex2(dirin, words), recursive or using functions
    or recursive functions, having as arguments:
    - dirin: the path to a directory
    - words: a list of words
    The function will examine dirin and all its subdirectories (at any level),
    and will count the occurrences of words in the words list in all text files
    (i.e., those having the extension .txt) in any folder.
    A word is present in a file if and only if it is separated from the preceding word
    or the next word, if any, by a space, tab, or newline character.

    (5 points) The function returns a list of tuples (word, occurrences),
    where the first value of each tuple is one of the words in the words list
    and the second is the number of occurrences of that word in all the text files that
    have been found.
    (+ 3 points) The list is sorted by the number of occurrences of the words
    (in descending order); if two or more words have the same number of occurrences,
    they are sorted alphabetically (in ascending order).
    If a word in the words list never occurs, it must still be returned by the function.

    NOTICE 1: useful functions could be os.listdir,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTICE 2: it is forbidden to use the os.walk function.

    For example, given folder = "ex2" and words = ["cat", "dog"]
    the function returns: [("dog", 11), ("cat", 6)]

'''

import os


def RecScan(dir, words):
    D = {}
    items = os.listdir(dir)
    for item in items:
        if os.path.isfile(dir + "/" + item):
            if item[-4:].lower() == ".txt":
                fileRef = open(dir + "/" + item, "r", encoding="utf-8")
                for line in fileRef:
                    tokens = line.strip().replace("\t", " ").split(" ")
                    for token in tokens:
                        if token in words:
                            if token not in D:
                                D[token] = 1
                            else:
                                D[token] += 1
                fileRef.close()
        else:
            resD = RecScan(dir + "/" + item, words)
            for k in resD:
                if k not in D:
                    D[k] = resD[k]
                else:
                    D[k] += resD[k]
    return D


def ex2(dirin, words):
    D = RecScan(dirin, words)
    result = []
    for k in D:
        result.append((k, D[k]))
    return sorted(result, key=lambda x: x[1], reverse=True)

######################################################################################

if __name__ == '__main__':
    pass
    from random import randint, choice
    def creadiagonale(maxxy):
        UD = choice(['diagonalUP', 'diagonalDOWN'])
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
        x = randint(-50, maxxy)
        y = randint(-50, maxxy)
        L = randint(100, maxxy)
        return UD, R, G, B, x, y, L
    ID = 4
    N = 55
    FN = f'func5/in_{ID}.txt'
    with open(FN, mode='w') as F:
        for _ in range(N):
           print(*creadiagonale(500), sep=' ', file=F)



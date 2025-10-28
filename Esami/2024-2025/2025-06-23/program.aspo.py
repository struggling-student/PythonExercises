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

name = "c"
surname = "URNAME"
student_id = "ATRICULATION NUMBER"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 marks
Define the function func1(D) that receives as a parameter a dictionary
D, in which each key is a positive integer N and the corresponding value
is a list of characters L.
The function returns a list in which each item is a string obtained by repeating
N times each of the characters in L. The list is sorted alphabetically,
in descending order.
For example, if D = {2 : ['s', 'u', 'e'], 3 : ['q', 'a'],
the function will return:
L = ['uu', 'ss', 'qqq', 'ee', 'aaa']
'''
def func1(D):
    l = []
    for k in D:
        l.extend([k*v for v in D[k]])
    return sorted(l, reverse=True)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 marks
Define the function func2(L) that gets as parameter a list L of N lists.
Each list in L can be empty or contain a single list, defined the same way.
The function returns a list of N integers, in which the i-th value
is the number of lists nested in the list at the i-th position in L.
For example, if L = [ [[]], [], [[[]], [[]], [[[[]]]], [], [[[]] ]
the function will return: [1, 0, 2, 1, 3, 0, 2]
'''
def func2(L):
    ret = []
    for l in L:
        count = 0
        while l != []:
            l = l[0]
            count+=1
        ret.append(count)
    return ret

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 marks
Define the function func3(S) that receives as input a string containing
words separated by commas and, optionally, also by spaces.
The function should extract the words from S, considering only those that
begin with a vowel, and insert them into another list, sorted
alphabetically without considering the difference between uppercase and lowercase.
For example, if S = “Brad,ALIce, keVin, oscar, Dana, UMA,ian, Zoe”
the function will return: ['ALIce', 'ian', 'oscar', 'UMA']
'''

def func3(S):
    l = [w.strip() for w in S.split(',') if w.strip()[0].lower() in 'aeiou']
    return sorted(l, key = lambda x: x.lower())


#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 marks
Define the function `func4(input_filepath, output_filepath)` that reads a file
located at `input_filepath` and writes the identified words to a new file at
`output_filepath`. Words in the input file are separated by various delimiters,
including newlines, spaces, tabs, commas, or semicolons. 

The task is to group these words by their last letter without distinguishing
between uppercase and lowercase letters. Words are considered identical if
they are the same when case is ignored, meaning each word should only be
counted once. 

For each group of words, the output file should include a line formatted as
follows:

`<lowercase letter>: <word count>`

In this format, the initial letter is in lowercase, followed by a colon and a
space. After the colon and space, the number of words ending with that letter
is provided, regardless of the case of the letters in the words. The lines in
the output file should be ordered in descending alphabetical order based on
the letter before the colon.

Please note that there should be no space at the end of each line in the
output file, but each line should end with a carriage return.

The function should return the total number of words in the input file,
including duplicates.
For example:

contents of func4/func4_in1.txt:
GE
wOa;II,see ua;PAO,oA;wOA
pao iu;jJa,kE

By calling the function as:
n = func4(“func4/func4_in1.txt”, “func4/func4_out1.txt”)

the expected contents of func4/func4_out1.txt is:
u: 1
o: 1
i: 1
e: 3
a: 4

and the value of n will be 12
"""

def func4(input_filepath, output_filepath):
    with open(input_filepath) as f:
        text = f.read()
    d = {}
    words = text.replace(',', ' ').replace(';', ' ').split()
    for w in map(str.lower, words):
        ending_letter = w[-1]
        if ending_letter not in d:
            d[ending_letter] = [w]
        else:
            if w not in d[ending_letter]:
                d[ending_letter].append(w)
    with open(output_filepath, 'w') as f:
        for k in sorted(d, reverse=True):
            print(f'{k}: {len(d[k])}', file = f)
    return len(words)
        

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 marks
Define the function func5(file_in, file_out) that uses images.load to
load the image stored into file_in. The loaded image is a list of lists
and each internal item is a pixel represented as a tuple (r, g, b).
The background is completely black, i.e. all background pixels are (0, 0, 0).

Only the following groups of non-black pixels can appear in the image,
all of uniform color:
- 1x1, 1x2 or 2x1 groups
- 2x2 groups

There are no groups larger than 2x2, and two or more distinct but neighboring groups
are always separated by black pixels.

The function must:
1. locate all 2x2 groups of non-black pixels;
2. replace the four pixels in the group with black pixels, leaving the rest
   of the image unchanged;
3. save the result in file_out using images.save;
4. return the number of 2x2 groups found and blacked out.
"""
import images

def is_suqare(im, x, y):
    pixels = ((x, y), (x+1, y), (x, y+1), (x+1, y+1))
    try:
        colors = {im[x][y] for x,y in pixels}
        if len(colors) == 1:
            for x,y in pixels:
                im[x][y] = (0,0,0)
            return True
        else:
            return 0
    except IndexError:
        return False

def func5(file_in, file_out):
    image = images.load(file_in)
    count = 0
    for x, row in enumerate(image):
        for y, col in enumerate(row):
            if col != (0,0,0):
                count += is_suqare(image, x, y)
    images.save(image, file_out)
    return count

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks
Write a function ex1(T), recursive or using one or more recursive functions,
that gets as parameter the root of a BinaryTree, as defined in tree.py file.
Each node of the tree is a node with empty strings.
The function must traverse the entire tree and modify it in-place,
so that at the end each node contains a string of N stars (*), where
N is the level of that node. The root is at level 0, so
at the end of the execution of ex1 it will still contain an empty string.
The function returns the height of the tree (a tree with only the
root has height 0).
For example, if T is the following tree:

          ""                level 0
       --------
       |      |
      ""      ""            level 1
  ---------    --
  |       |      |
  ""     ""     ""          level 2
  
After executing the function, the function will return the
value 2 and T will contain:
          ""                level 0
       --------
       |      |
      "*"    "*"            level 1
  ---------    --
  |       |      |
 "**"    "**"   "**"        level 2
"""
import tree

def ex1(T):
    return ex1_(T, 0)
    pass

def ex1_(T, lev):
    if T is None:
        return lev-1
    T.value = lev*'*'
    return max(ex1_(T.left, lev+1), ex1_(T.right, lev+1))
    
# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 marks
Write a recursive function called `ex2(L, k)` that takes the
following parameters:
- `L`: a list of N non-empty sublists of characters (strings containing 1 
            lowercase letter each)
- `k`: an integer between 0 and N

The function should construct and return a list of strings of length N, where:

- Each string is formed by choosing one character from the first sublist, one
  from the second sublist, and so on.
- Every string contains exactly k vowels (the letters 'a', 'e', 'i', 'o', 'u').
- No strings are repeated (even if characters from `L` are repeated, the
    output must contain no duplicates; each string should appear only once).
- The resulting list is sorted in ascending alphabetical order.


Example:
L = [['c', 'q', 'a', 'a'], ['w', 'e', 'y']]
k = 1

Expected output:
['aw', 'ay', 'ce', 'qe']
"""

def ex2(L, k):
    return sorted(filter(lambda x: sum(x.count(c) for c in 'aeiou') == k, ex2_(L, k)))
    
def ex2_(L, k):
    if len (L) == 1:
        return set(L[0])
    partial = ex2_(L[1:], k)
    return {c+w for c in L[0] for w in partial}    


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)

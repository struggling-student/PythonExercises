#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal tu 18

The final score is the sum of the solved problems.
"""
name       = "Maurizio"
surname    = "Mancini"
student_id = "12345678"

#########################################

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

# %%  ---- FUNC1 ----
''' func1: 2 points

A dictionary D is provided as input. D has integer keys and its values are
lists of strings with repetitions.

D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}

Write the function func1(D) that builds and returns the
list W that contains the values obtained by taking, for each key K in D,
the corresponding item from the list L associated to K;
before picking an item, the function sorts L in reversed order.

Given the D as defined above, the function returns:

    W = ["c", "b", "b"]
    
as the first list sorted in reversed order is ["h", "g", "f", "e", "c"],
and its 4th item is "c"; the second list is ["z", "w", "b", "a"], and its
2nd item is "b"; the third list is ["b", "a", "a"] and its 0th item is "b".

'''

def func1(D):
    W = []
    for key in D:
        S = sorted(D[key], reverse=True)
        W.append(S[key])
    return W


# %%  ---- FUNC2 ----
''' func2: 2 points

Implement the func2(list_all, list_rm) function to destructively delete
from list_all all the integers that are not contained in list_rm.
The function does not considers the repetitions in list_all,
so the resulting list will not contain repetitions.

Example: if  list_all = [2, 4, 3, 4, 4, 3, 4, 5, 2, 6]
         and list_rm = [5, 3, 2, 7]
         list_all must be destructively changed to [2, 3, 5]

'''

def func2(list_all, list_rm):
    i = 0
    while i < len(list_all):
        item = list_all[i]
        if item not in list_rm:
            list_all.pop(i)
        elif item in list_all[0:i]:
            list_all.pop(i)
        else:
            i += 1


# %%  ---- FUNC3 ----
'''  func3: 2 points

Implement the func3(strList) that:
- takes as input a list of strings
- computes the sum of the ascii codes of the characters of each string,
obtaining an integer value for each string, and adding all the obtained
values to a list;
- returns the list of integers sorted, based on the initial string values
in the list strList, in ascending order.

For example, if strList = ["monkey", "cat", "panda", "alligator"]
the corresponding ascii values are: [659, 312, 516, 959]
that, based on the alphabetical ordering of the initial list, are returned as:
[959, 312, 659, 516]
'''

def func3(strList):
    result = []
    for item in strList:
        value = sum(map(ord, list(item)))
        result.append((item, value))
    result.sort(key=lambda y: y[0])
    result = [x[1] for x in result]
    return result


# %%  ---- FUNC4 ----
''' func4: 4 points

    Implement the function  func4(M) that takes as arguments:
    - M: a 2 dimensional matrix of integers represented as lists of lists
    
    The function returns the result of R + C, where R is the product
    of the values obtained by summing each row of M, and C is the
    product of the values obtained by summing each column of M.

    Example:
        Suppose M is:
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
        then, the sums computed on its rows are 10, 26, 12, and their product is 3120;
        the sums computed on its columns are 15, 8, 11, 14, and their product is 18480;
        so, the function returns 21600.

'''

def func4(M):
    rows = []
    for row in M:
        rows.append(sum(row))
    cols = []
    for col in range(len(M[0])):
        column = []
        for row in M:
            column.append(row[col])
        cols.append(sum(column))
    prodRows = rows[0]
    for item in rows[1:]:
        prodRows *= item
    prodCols = cols[0]
    for item in cols[1:]:
        prodCols *= item
    return prodRows + prodCols



# %%  ---- FUNC5 ----
''' func5: 6 points

Write a function func5(points) that takes a list of (x,y) coordinates
of N points in the Cartesian plane (N >= 3). Each point is a pair of integers.
For each point, we consider its distance from the center fhe plane (0,0).

The function must return the barycenter (X, Y) of the 3 points that are closer to
the center of the plane.
All values should be reported to an accuracy of 3 decimal places (you can use
the round function to do that).

  - NOTE: The distance between 2 points (x1, y1) and (x2, y2)
    is the Euclidean distance: sqrt[(x1-x2)² + (y1-y2)²]
  - NOTE: The barycenter of N points is the point (X', Y'),
    where X' is the mean of the x coordinates and Y' is the mean
    of the y coordinates of the N points.
    
For example, if points = [(2, 2), (-1, 1), (3, 0), (3, 2), (2, -1)]
the corresponding (unsorted) distances are: 2.828, 1.414, 3.0, 3.606, 2.236
and, after sorting them, the resulting barycenter of the 3 points
closest to (0, 0) is: (1.0, 0.667)
'''

def func5(points):
    distances = []
    for i, point in enumerate(points):
        distances.append((round((point[0]**2 + point[1]**2)**0.5, 3), i))
    distances.sort(key=lambda x : x[0])
    bar_x = round((points[distances[0][1]][0] + points[distances[1][1]][0] + points[distances[2][1]][0]) / 3, 3)
    bar_y = round((points[distances[0][1]][1] + points[distances[1][1]][1] + points[distances[2][1]][1]) / 3, 3)
    return bar_x, bar_y



# %% ----------------------------------- EX.1 ----------------------------------- #
'''
Ex1: 6 points
    Implement the ex1(root, result) function, recursive or using
    recursive functions, with 2 arguments:
    - root:  the root of a binary tree;
    - result: an empty list, that will be populated with the result (see below).
    
    The tree is made of instances of the BinaryTree class defined in tree.py.
    The function should build and return a list in the parameter "result",
    in which each i-th item contains the sum of all the nodes at depth i
    (the root of the tree is at depth 0).

    Example:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    If the tree is the left one, result = [5, 10, 13]
    If the tree is the right one, result = [2, 12, 12, 24]
'''

from tree import BinaryTree

def GetNodesAtDepth(root, depth):
    if depth == 0:
        return [root.value]
    if depth > 0:
        if root.left is not None:
            left = GetNodesAtDepth(root.left, depth - 1)
        else:
            left = []
        if root.right is not None:
            right = GetNodesAtDepth(root.right, depth - 1)
        else:
            right = []
        return left + right

def ex1(root, result):
    depth = 0
    R = GetNodesAtDepth(root, depth)
    while R != []:
        result.append(sum(R))
        depth += 1
        R = GetNodesAtDepth(root, depth)

# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 6 + 3 points
    Implement the ex2(dirin, words) function, recursive or using recursive
    functions or methods, having the argument:
    - dirin: the path of an existing directory
    - words: a list of words
    The function will go through dirin and all its subfolders (at any level),
    and count the occurrences of the words in the input list in all the
    text files (i.e., files having the .txt extension) found in any folder.
    A word occurs in a file, if and only if it is separated from the preceding
    or following word, if there are, by a space, a tab, or a newline character.
    
    (6 points) The function returns a list of pairs (word, occ), in which the first
    value of each pair is one of the words in the input list and the second
    value of the pair is the number of occurrences of that word in the text files.
    (+ 3 points) The list is sorted on the number of occurrences of the words
    (in descending order); if two or more words have the same number of occurrences,
    they are sorted alphabetically (in ascending order).
    If a word in the input list never occurs, it still has to be returned
    by the function.

    NOTICE 1: you could find useful the functions: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTICE 2: it is forbidden to use the os.walk function
    
    For example, given the folder "ex2" and if words = ["cat", "dog"]
    the function returns: [('dog', 11), ('cat', 6)]
        
'''

import os

def RecScan(dir, words):
    D = {}
    items = os.listdir(dir)
    for item in items:
        if os.path.isfile(os.path.join(dir, item)):
            if item[-4:].lower() == ".txt":
                fileRef = open(os.path.join(dir, item), "r", encoding="utf-8")
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
            resD = RecScan(os.path.join(dir, item), words)
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
    return sorted(result, key=lambda x : x[1], reverse=True)

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    '''D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}
    print(func1(D))
    D = {1: ["c", "h", "f", "g", "e"], 0: ["a", "z", "b", "w"], 2: ["a", "b", "a"]}
    print(func1(D))
    D = {0: ["ball", "bike", "blue"], 1: ["bike", "ball", "blue"], 2: ["blue", "bike", "ball"]}
    print(func1(D))
    D = {0: ["ball", "bike", "blue"], 1: ["cat", "cube", "coat"], 2: ["dog", "day", "data"]}
    print(func1(D))'''


    '''list_all = [2, 4, 3, 4, 4, 3, 4, 5, 2, 6]
    list_rm = [5, 3, 2, 7]
    func2(list_all, list_rm)
    print(list_all)

    list_all = list(range(100))
    list_rm = list(range(-100, 99))
    func2(list_all, list_rm)
    print(list_all)

    list_all = list(range(100))
    list_rm = list(range(-100, 100, 2))
    func2(list_all, list_rm)
    print(list_all)'''

    '''strList = ["monkey", "cat", "panda", "alligator"]
    print(func3(strList))

    strList = [
        "Aardvark",
        "Albatross",
        "Alligator",
        "Alpaca",
        "Ant",
        "Anteater",
        "Antelope",
        "Ape",
        "Armadillo",
        "Donkey",
        "Baboon",
        "Badger",
        "Barracuda",
        "Bat",
        "Bear",
        "Beaver",
        "Bee",
        "Bison",
        "Boar",
        "Buffalo",
        "Butterfly",
        "Camel",
        "Capybara",
        "Caribou",
        "Cassowary",
        "Cat",
        "Caterpillar",
        "Cattle",
        "Chamois",
        "Cheetah",
        "Chicken",
        "Chimpanzee",
        "Chinchilla",
        "Chough",
        "Clam",
        "Cobra",
        "Cockroach",
        "Cod",
        "Cormorant",
        "Coyote",
        "Crab",
        "Crane",
        "Crocodile",
        "Crow",
        "Curlew",
        "Deer",
        "Dinosaur",
        "Dog",
        "Dogfish",
        "Dolphin",
        "Dotterel",
        "Dove",
        "Dragonfly",
        "Duck",
        "Dugong",
        "Dunlin",
        "Eagle",
        "Echidna",
        "Eel",
        "Eland",
        "Elephant",
        "Elk",
        "Emu",
        "Falcon",
        "Ferret",
        "Finch",
        "Fish",
        "Flamingo",
        "Fly",
        "Fox",
        "Frog",
        "Gaur",
        "Gazelle",
        "Gerbil",
        "Giraffe",
        "Gnat",
        "Gnu",
        "Goat",
        "Goldfinch",
        "Goldfish",
        "Goose",
        "Gorilla",
        "Goshawk",
        "Grasshopper",
        "Grouse",
        "Guanaco",
        "Gull",
        "Hamster",
        "Hare",
        "Hawk",
        "Hedgehog",
        "Heron",
        "Herring",
        "Hippopotamus",
        "Hornet",
        "Horse",
        "Human",
        "Hummingbird",
        "Hyena",
        "Ibex",
        "Ibis",
        "Jackal",
        "Jaguar",
        "Jay",
        "Jellyfish",
        "Kangaroo",
        "Kingfisher",
        "Koala",
        "Kookabura",
        "Kouprey",
        "Kudu",
        "Lapwing",
        "Lark",
        "Lemur",
        "Leopard",
        "Lion",
        "Llama",
        "Lobster",
        "Locust",
        "Loris",
        "Louse",
        "Lyrebird",
        "Magpie",
        "Mallard",
        "Manatee",
        "Mandrill",
        "Mantis",
        "Marten",
        "Meerkat",
        "Mink",
        "Mole",
        "Mongoose",
        "Monkey",
        "Moose",
        "Mosquito",
        "Mouse",
        "Mule",
        "Narwhal",
        "Newt",
        "Nightingale",
        "Octopus",
        "Okapi",
        "Opossum",
        "Oryx",
        "Ostrich",
        "Otter",
        "Owl",
        "Oyster",
        "Panther",
        "Parrot",
        "Partridge",
        "Peafowl",
        "Pelican",
        "Penguin",
        "Pheasant",
        "Pig",
        "Pigeon",
        "Pony",
        "Porcupine",
        "Porpoise",
        "Quail",
        "Quelea",
        "Quetzal",
        "Rabbit",
        "Raccoon",
        "Rail",
        "Ram",
        "Rat",
        "Raven",
        "Red deer",
        "Red panda",
        "Reindeer",
        "Rhinoceros",
        "Rook",
        "Salamander",
        "Salmon",
        "Sand Dollar",
        "Sandpiper",
        "Sardine",
        "Scorpion",
        "Seahorse",
        "Seal",
        "Shark",
        "Sheep",
        "Shrew",
        "Skunk",
        "Snail",
        "Snake",
        "Sparrow",
        "Spider",
        "Spoonbill",
        "Squid",
        "Squirrel",
        "Starling",
        "Stingray",
        "Stinkbug",
        "Stork",
        "Swallow",
        "Swan",
        "Tapir",
        "Tarsier",
        "Termite",
        "Tiger",
        "Toad",
        "Trout",
        "Turkey",
        "Turtle",
        "Viper",
        "Vulture",
        "Wallaby",
        "Walrus",
        "Wasp",
        "Weasel",
        "Whale",
        "Wildcat",
        "Wolf",
        "Wolverine",
        "Wombat",
        "Woodcock",
        "Woodpecker",
        "Worm",
        "Wren",
        "Yak",
        "Zebra"
    ]
    print(func3(strList))

    strList = list("lorem ipsum dolor sit amet")
    print(func3(strList))

    strList = map(str, list(range(1, 100)))
    print(func3(strList))'''


    M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
    print(func4(M))

    M = [[1, 2, 3, 4] for x in range(10)]
    print(func4(M))

    M = [[x for x in range(10)] for x in range(2)]
    print(func4(M))

    M = [[1 for x in range(5)] for x in range(2)]
    print(func4(M))

    '''points = [(2, 2), (-1, 1), (3, 0), (3, 2), (2, -1)]
    print(func5(points))

    points = [(0, 2), (2, 0), (2, 2), (-2, 0), (0, -2), (-2, -2)]
    print(func5(points))

    points = [(x, x) for x in range(1, 10)]
    print(func5(points))

    points = [(x, -x) for x in range(1, 10)]
    print(func5(points))'''


    '''tree = BinaryTree.fromList([5, [8, None, [3, None, None]], [2, [9, None, None],[1, None, None]]])
    res = []
    ex1(tree, res)
    print(res)

    tree = BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]], [5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    res = []
    ex1(tree, res)
    print(res)

    tree = BinaryTree.fromList([-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]] )
    res = []
    ex1(tree, res)
    print(res)'''

    print(ex2("ex2", ["cat", "dog"]))
    print(ex2("ex2/A", ["gnu", "cat", "fish"]))
    print(ex2("ex2", ["bird", "dog", "gnu", "tuna"][::-1]))

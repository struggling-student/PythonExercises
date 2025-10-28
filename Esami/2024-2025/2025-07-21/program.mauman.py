#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" PREREQUISITES:
 1) Save the file as program.py
 2) Assign the variables below with your
    NAME, SURNAME, STUDENT_ID

To pass the exam, it is necessary to obtain a score greater than or equal to 18 (15 for DSA students)

The final grade is the sum of the scores of the solved problems.

Attention! DEBUG=True in grade.py to improve debugging.
However, to properly test recursion, DEBUG=False is necessary.

"""
name       = "Maurizio"
surname    = "Mancini"
student_id = "12345678"



################################################################################
# ---------------------------- DEBUGGING SUGGESTIONS --------------------- #
# To run only some of the tests, you can comment out the entries
# corresponding to the tests you do not want to run within the `test` list
# at the END of `grade.py`.
#
# To debug recursive functions, you can disable the recursion test by
# setting `DEBUG=True` inside the `grade.py` file.
#
# Setting DEBUG=True also activates the terminal printout of the STACK
# TRACE of errors, which allows you to know the line number in `program.py`
# that generated an error.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 4 points
Define the function func1(embedding_list1, embedding_list2) that takes as arguments
two lists of tuples. Each tuple represents a word and its vector embedding: `(word_str, [float1, float2, ...])`.
The function should find the pair of words that are most similar. Similarity is computed using the helper function `cosine_similarity` on the corresponding 
embeddings. The function should return a tuple `(word1, word2, similarity_score)`, where `word1` is from `embedding_list1`,
`word2` is from `embedding_list2`, and `similarity_score` is the calculated cosine similarity. 
If multiple pairs have the same highest similarity, return the one where `word1`
is alphabetically smallest, then `word2` is alphabetically smallest.

Example:
  embeddings1 = [('king', [0.1, 0.2]), ('queen', [0.3, 0.4])]
  embeddings2 = [('man', [0.05, 0.15]), ('woman', [0.25, 0.35])]
  # For simplicity, if (queen, woman) has highest similarity.
  func1(embeddings1, embeddings2) might return ('queen', 'woman', 0.9997)
'''
import math
def func1(embedding_list1, embedding_list2):
    # Helper for cosine similarity
    def cosine_similarity(vec1, vec2):
        dot_product = sum(a*b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a**2 for a in vec1))
        magnitude2 = math.sqrt(sum(b**2 for b in vec2))
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        return round(dot_product / (magnitude1 * magnitude2), 4)
    # Complete the code here
    L = []
    for word1 in embedding_list1:
        for word2 in embedding_list2:
            L.append((word1[0], word2[0], cosine_similarity(word1[1], word2[1])))
    L.sort(key=lambda x:x[2], reverse=True)
    return L[0]

# embeddings1 = [('king', [0.1, 0.2]), ('queen', [0.3, 0.4])]
# embeddings2 = [('man', [0.05, 0.15]), ('woman', [0.25, 0.35])]
# print(func1(embeddings1, embeddings2))

# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 4 points
Define the function func2(text_corpus, sentiment_lexicon, top_k_sentences) that takes:
  - `text_corpus`: a list of strings, where each string is a sentence.
  - `sentiment_lexicon`: a dictionary, mapping words (strings, lowercase) to their sentiment scores (floats, e.g., -1.0 to 1.0).
  - `top_k_sentences`: an integer, the number of top positive sentences to report.

Divide each sentence in `text_corpus` into words (lowercase tokens) using the helper function `tokenize_alphabetic`.   
Calculate the sentence sentiment score by summing the scores of all its words found in the lexicon. 
Words not in the lexicon contribute 0 to the score. Round all sentiment values to 2 decimal places.

The function should return a dictionary with the following structure:
  - `overall_sentiment`: float, the average sentiment score of all sentences.
  - `top_positive_sentences`: a list of tuples `(score, sentence_string)` for the top K positive sentences (i.e., with sentiment > 0),
    ordered by score descending. If fewer than `top_k_sentences` with positive sentiment exist, include all available. 
    In case of ties, include the ones with the largest sentence in lexicographical order.
  - `total_sentences_analyzed`: integer, the total number of sentences processed.

Example:
  text_corpus = ["This is a great movie!", "It was terrible.", "What a lovely day."]
  sentiment_lexicon =  {'great': 0.8, 'terrible': -0.9, 'lovely': 0.7}
  func2(text_corpus, sentiment_lexicon, 1) should return (order of sentences might vary for same score):
  {
      'overall_sentiment': 0.20,
      'top_positive_sentences': [(0.80, 'This is a great movie!')],
      'total_sentences_analyzed': 3
  }
'''
import re

def tokenize_alphabetic(text):
    """
    Tokenizes the input text into a list of alphabetic words.
    Ignores punctuation and non-alphabetic characters.

    Args:
        text (str): The input string to be tokenized.

    Returns:
        list: A list of alphabetic words.
    """
    return re.findall(r'[a-z]+', text.lower())


def func2(text_corpus, sentiment_lexicon, top_k_sentences):
    count_sentences = 0
    overall_sentiment = 0
    top_positive = []
    for sentence in text_corpus:
        sentiment = 0
        tokens = tokenize_alphabetic(sentence)
        for T in tokens:
            if T in sentiment_lexicon:
                sentiment += sentiment_lexicon[T]
        if sentiment > 0:
            top_positive.append((sentiment, sentence))
        overall_sentiment += sentiment
        count_sentences += 1
    top_positive.sort(key=lambda x:(x[0], x[1]), reverse=True)
    top_positive = top_positive[0:top_k_sentences]
    return {"overall_sentiment" : round(overall_sentiment/count_sentences, 2),
            "top_positive_sentences" : top_positive,
            "total_sentences_analyzed" : count_sentences}

# text_corpus = ["This is a great movie!", "It was terrible.", "What a lovely day."]
# sentiment_lexicon =  {'great': 0.8, 'terrible': -0.9, 'lovely': 0.7}
# print(func2(text_corpus, sentiment_lexicon, 1))

# %% -------------------------------- FUNC.3 -------------------------------- #
''' func3: 4 points
Define the function func3(sentence_list, forbidden_words) that takes as arguments
a list of strings `sentence_list` (representing sentences) and a set of `forbidden_words` (strings).
The function should identify and remove any sentence from `sentence_list` (modifying it in-place)
that contains at least one word from the `forbidden_words` set (case-insensitive).
Words in sentences are defined as sequences of alphabetic characters (you may use the helper function 
`tokenize_alphabetic` to tokenize sentences).
The function should return the total count of sentences removed.

Example:
    sentence_list = ["This is a test sentence.", "Bad words here.", "Another one for good measure."]
    forbidden_words = {"bad", "terrible", "forbidden"}
    after calling func3(sentence_list, forbidden_words),
    sentence_list should be ["This is a test sentence.", "Another one for good measure."]
    and the function should return 1.

IMPORTANT: the list `sentence_list` must be changed at the end of the function execution.
'''

def func3(sentence_list, forbidden_words):
    toremove = []
    for sentence in sentence_list:
        for w in tokenize_alphabetic(sentence):
            if w.lower() in forbidden_words:
                toremove.append(sentence)
                break
    for sentence in toremove:
        sentence_list.remove(sentence)
    return len(toremove)

# sentence_list = ["This is a test sentence.", "Bad words here.", "Another one for good measure."]
# forbidden_words = {"bad", "terrible", "forbidden"}
# print(func3(sentence_list, forbidden_words))
# print(sentence_list)

# %% -------------------------------- FUNC.4 -------------------------------- #
''' func4: 4 points
Define the function func4(text, n) that takes a string `text` and an integer `n`.
The function should tokenize the text into alphabetic words (using `tokenize_alphabetic`),
count the frequency of each word, and return a list of the `n` most frequent words
along with their counts. The list should be sorted by count descending, then alphabetically
by word for ties.

Example:
  text = "The quick brown fox jumps over the lazy dog. The fox is quick."
  func4_a(text, 2) should return [('the', 3), ('fox', 2)] 
  func4_a(text, 3) should return [('the', 3), ('fox', 2), ('quick', 2)]
'''
def func4(text, n):
    words = {}
    for t in tokenize_alphabetic(text):
        if t not in words:
            words[t] = 1
        else:
            words[t] += 1
    words = sorted(words.items(), key=lambda x:(-x[1], x[0]))
    return words[0:n]

# text = "The quick brown fox jumps over the lazy dog. The fox is quick."
# print(func4(text, 3))

# %% -------------------------------- FUNC.5 -------------------------------- #
''' func5: 4 points
Define the function func5(word_list) that takes a list of strings `word_list`.
The function should find all groups of anagrams within the `word_list`.
Two words are anagrams if they contain the same characters, regardless of order or case.
The function should return a dictionary where keys are the "canonical form" of an anagram group
(i.e., the lowercase word with its letters sorted alphabetically), and values are
sets of unique words from `word_list` that belong to that anagram group (original casing preserved).

Example:
  word_list = ["listen", "silent", "Enlist", "apple", "Banana", "apPLe"]
  func5(word_list) should return (order of keys might vary):
  {
      'eilnst': {'listen', 'silent', 'Enlist'},
      'aelpp': {'apple', 'apPLe'},
      'aaabnn': {'Banana'}
  }
'''
def func5(word_list):
    D = {}
    for w in word_list:
        c = list(w.lower())
        c.sort()
        c = ''.join(c)
        if c not in D:
            D[c] = {w}
        else:
            D[c].add(w)
    return D

# word_list = ["listen", "silent", "Enlist", "apple", "Banana", "apPLe"]
# print(func5(word_list))

# %% --------------------------------- EX.1 --------------------------------- #
""" Ex1: 6 points
**This function must be solved using a recursive approach.**
**The recursive function must be at the top level of this file (i.e., not defined inside of another function).**

Implement the ex1(root, result, target_value) function, which takes three arguments:
- root: The root of a binary tree.
- result: An empty list, must be populated in-place with the path to the target node.
- target_value: The value of the node to find.

Record the path from the root to the deepest occurrence of the target_value in the list `result`.
If there are multiple occurrences of the target_value at the same maximum depth, choose the leftmost.
The function should not return a value. Instead, it must populate the result list in-place with the list 
of node values representing the path from the root to the chosen target node. If the target_value is not found in 
the tree, the result list should remain empty.

Example:
  Tree:
       1
     /   \ 
    2     3
   / \   / \ 
  4   5 4   9
 / \ 
8   9
If target_value is 5, result will be [1, 2, 5].
If target_value is 9, result will be [1, 2, 4, 9] (deepest).
If target_value is 4, result will be [1, 2, 4] (leftmost).

You can use the BinaryTree class from the tree.py module.
"""

from tree import BinaryTree

def tree_scan(root, nodes_list, all_paths):
    nodes_list.append(root.value)
    if root.left is not None:
        L = tree_scan(root.left, nodes_list.copy(), all_paths)
        all_paths.append(nodes_list)
    if root.right is not None:
        L = tree_scan(root.right, nodes_list.copy(), all_paths)
        all_paths.append(nodes_list)
    if root.left is None and root.right is None:
        all_paths.append(nodes_list)


def ex1(root, result, target_value):
    nodes_list = []
    all_paths = []
    tree_scan(root, nodes_list, all_paths)
    res = []
    for P in all_paths:
        if P[-1] == target_value:
            res.append(P)
    res.sort(key=len, reverse=True)
    if len(res) > 0:
        for i in res[0]:
            result.append(i)


# root = BinaryTree(1,
#                           BinaryTree(2,
#                                      BinaryTree(4,
#                                                 BinaryTree(8),
#                                                 BinaryTree(9)),
#                                      BinaryTree(5)),
#                           BinaryTree(3,
#                                      BinaryTree(4),
#                                      BinaryTree(9)))
# result = []
# ex1(root, result, 5)
# print(result)



# %% --------------------------------- EX.2 --------------------------------- #
import images
''' Ex2: 6 points 
**This function must be solved using a recursive approach.**
**The recursive function must be at the top level of this file (i.e., not defined inside of another function).**

Implement the ex2(in_path, out_fpath, x, y, replacement_color) function, which takes the following arguments:
- in_path, out_fpath: the paths to the input and output PNG images. 
- x, y (int): The starting x and y coordinate.
- replacement_color (3-tuple of ints): The new color to fill with.
Starting from the pixel at coordinates (x, y) of color c, paint it with `replacement_color`. Recursively, fill the 
region of neighboring pixels of color c with the new color. Consider the pixels to the left, right, top, and bottom 
of the current pixel as neighbors.
'''

def fill_color(image, startx, starty, oldcol, newcol):
    if startx > 0:
        if image[starty][startx - 1] == oldcol:
            image[starty][startx - 1] = newcol
            fill_color(image, startx - 1, starty, oldcol, newcol)
    if startx < len(image[0]) - 1:
        if image[starty][startx + 1] == oldcol:
            image[starty][startx + 1] = newcol
            fill_color(image, startx + 1, starty, oldcol, newcol)
    if starty > 0:
        if image[starty - 1][startx] == oldcol:
            image[starty - 1][startx] = newcol
            fill_color(image, startx, starty - 1, oldcol, newcol)
    if starty < len(image) - 1:
        if image[starty + 1][startx] == oldcol:
            image[starty + 1][startx] = newcol
            fill_color(image, startx, starty + 1, oldcol, newcol)

from images import load, save

def ex2(in_path, out_fpath, x, y, replacement_color):
    img = load(in_path)
    oldcol = img[y][x]
    img[y][x] = replacement_color
    fill_color(img, x, y, oldcol, replacement_color)
    save(img, out_fpath)

# ex2("ex2_test_data/input_images/complex_shape_fill.png", "ex2_test_data/output_images/output_complex_shape_fill.png", x=7, y=8, replacement_color=(255, 0, 0))

###################################################################################
if __name__ == '__main__':
    print('*' * 50)
    print('Run grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)

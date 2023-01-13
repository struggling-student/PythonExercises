
import copy
import random

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


    @classmethod
    def fromList(cls, a_list):
        """
        Build the tree from a list in the following form:
          [value, left, right]
        wherein left and right are other trees or None
        :param a_list: a list [value, left, right]
        :return: a tree
        """
        value, left, right = a_list
        if left: left = cls.fromList(left)
        if right: right = cls.fromList(right)
        return cls(value, left, right)

    def toList(self):
        """
        Convert this tree into a list in the following form:
          [value, left, right].
        :return: a list [value, left, right]
        """
        left = None if not self.left else self.left.toList()
        right = None if not self.right else self.right.toList()
        return [self.value, left, right]

    def __eq__(self, other):
        """
        Compare two trees
        :param other: a tree
        :return: True if trees are equal; False otherwise
        """
        return other != None and \
               type(self) == type(other) and \
               self.value == other.value and \
               self.left == other.left and \
               self.right == other.right

    def __repr__(self, level=0):
        """
        Print a tree with a given indentation level
        :param level: indentation level
        :return: a string-representation of the tree
        """
        indent = "|  " * level
        res = "{0}Node_{1}: {2.value}".format(indent, id(self), self)
        indent = "|  " * (level + 1)
        if self.left:
            res += "\n{}".format(self.left.__repr__(level + 1))
        else:
            res += "\n{}{}".format(indent, self.left)
        if self.right:
            res += "\n{}".format(self.right.__repr__(level + 1))
        else:
            res += "\n{}{}".format(indent, self.right)
        return res

    @classmethod
    def randomTree(cls, level):
        """
        Generate a random tree of at most N levels
        :param level: N, the maximum height of the tree
        :return: a tree of at most N levels
        """
        if random.randint(0,
                          100) < 10 or level < 0:  # in 10% of the cases, it is None
            return None
        V = random.randint(1, 1000000)
        left = cls.randomTree(level -
                              random.randint(1, 3))  # shorten the height of the left subtree by 1, 2 or 3
        right = cls.randomTree(level -
                               random.randint(1, 3))  # shorten the height of the right subtree by 1, 2 or 3
        return cls(V, left, right)

if __name__ == '__main__':
    a_list = [1, [2, None, None],
             [3, [4, None, None],
                 [5, None, None],],
             ]
    tree = BinaryTree.fromList(a_list)
    tree2 = copy.deepcopy(tree)
    tree3 = BinaryTree.randomTree(10)

    print('A =', tree, sep='\n')
    print('B =', tree2, sep='\n')
    print('A =', tree.toList())
    print('C =', tree3)
    print('C =', tree3.toList())

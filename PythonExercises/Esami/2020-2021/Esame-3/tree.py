
class BinaryTree:
    def __init__(self, ID, left=None, right=None):
        self.ID    = ID
        self.left  = left
        self.right = right

class NaryTree:
    def __init__(self, ID, sons):
        self.value = ID
        self.sons  = sons


import albero


def es48(tree):
    if tree == None:
        return 0
    count = es48(tree.sx) + es48(tree.dx)
    if tree.sx != None and tree.dx != None:
        count += 1
    return count

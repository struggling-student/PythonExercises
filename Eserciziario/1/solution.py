import albero

def es1(tree1,tree2):
    t3 = albero.AlberoBinario(somma_sottoalbero(tree1)+somma_sottoalbero(tree2))
    if tree1.sx:
      t3.sx = es1(tree1.sx, tree2.sx)
    if tree2.dx:
      t3.dx = es1(tree1.dx, tree2.dx)
    return t3

def somma_sottoalbero(tree):
    somma = tree.valore
    if tree.sx:
      somma += somma_sottoalbero(tree.sx)
    if tree.dx:
      somma += somma_sottoalbero(tree.dx)
    return somma
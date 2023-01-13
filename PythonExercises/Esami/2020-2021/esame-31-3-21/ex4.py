'''Progettare e implementare una funzione ex4(root), ricorsiva o che
   fa uso di funzioni/metodi ricorsivi, tale che:
   - riceva come argomenti un albero root di tipo tree.BinaryTree
   - restituisca in output una lista di interi.
   La lista di interi da restituire deve essere costruita visitando
   l'albero in post-order e deve contenere soltanto i valori di quei
   nodi interni per i quali i figli sono uno multiplo dell'altro.

  Si ricorda che la visita in post-order prevede che si visiti prima
  il figlio sinistro, poi il figlio destro e infine la radice.

Es: dato l'albero root di seguito definito
                    6
                /       \
             5             1
          /     \       /     \
         2       4     6       8
                / \           / \
              15   3         2   10
   la funzione deve ritornare la lista [4,5,8,6]
'''
from tree import BinaryTree

def ex4(root):
    if not root.left and not root.right:
        return []
    l = []
    if root.left:
        l += ex4(root.left)
    if root.right:
        l += ex4(root.right)
    if root.left and root.right:
        if root.left.value % root.right.value == 0 or root.right.value % root.left.value == 0:
            l += [root.value]
    return l


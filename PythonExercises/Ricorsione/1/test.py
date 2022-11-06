import testlib
import isrecursive
import albero
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, lista1, lista2, expected):
        '''Implementazione del test:
            - lista1: lista nodi albero 1 in input
            - lista2: lista nodi albero 2 in input
            - expected: lista nodi albero output
        '''
        #controllo la ricorsione

        tree1 = albero.AlberoBinario.fromList(lista1)
        tree2 = albero.AlberoBinario.fromList(lista2)
        try:
            isrecursive.decorate_module(program)
            program.es1(tree1, tree2)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es1(tree1, tree2)
        
        self.assertEqual(lista1, tree1.toList(), "tree1 è stato modificato")
        self.assertEqual(lista2, tree2.toList(), "tree2 è stato modificato")
        self.assertEqual(result.toList(), expected, "L'albero tree3 restituito non e' corretto")

    def test_1(self):
        '''
        Prova con in input i due alberi:
        
                    9                          4                                     145           
                /  \                       /  \                                   /  \          
                /    \                     /    \                                 /    \         
                /      \                   /      \                               /      \        
                /        \                 /        \                             /        \       
            /          \               /          \                           /          \      
            2            4             4            4     il risultato e'     63          69     
            /   \        /   \         /   \        /   \                     /   \        /   \   
        6     6      6     6       5     6      7     8                  28    29     30    31  
        / \   / \    / \   / \     / \   / \    / \   / \                 / \   / \    / \   / \ 
        5   5 5   5  5   5 5   5   1   6 6   1  1   6 6   1               6  11 11  6  6  11 11  6
        '''
        lista1 = [9,[2,[6,[5, None, None],[5, None, None]],[6,[5, None, None],[5, None, None]]],
        [4,[6,[5, None, None],[5, None, None]],[6,[5, None, None],[5, None, None]]]]
        lista2 = [4,[4,[5,[1, None, None],[6, None, None]],[6,[6, None, None],[1, None, None]]],
            [4,[7,[1, None, None],[6, None, None]],[8,[6, None, None],[1, None, None]]]]
        lista3 =[145, [63, [28, [6, None, None], [11, None, None]], [29, [11, None, None], [6, None, None]]], 
        [69, [30, [6, None, None], [11, None, None]], [31, [11, None, None], [6, None, None]]]]
        return self.do_test(lista1, lista2, lista3)

    def test_2(self):
        '''Prova con in input i due alberi:
            
            5              1                                             30      
            \              \                                             \     
            1              5                                            24    
            /              /                                             /     
            5               1          il risultato deve essere           18      
            \              \                                              \     
            1              5                                             12    
            /             /                                              /     
            5              1                                             6      
        '''
        lista1 = [5,None,[1,[5,None,[1,[5,None,None],None]],None]]
        lista2 = [1,None,[5,[1,None,[5,[1,None,None],None]],None]]
        lista3 = [30, None, [24, [18, None, [12, [6, None, None], None]], None]]
        return self.do_test(lista1, lista2, lista3)
    
    def test_3(self):
        '''Prova con in input i due alberi:
            
                1              7                                    90   
                /\             /\                                    /\   
            2  3           1  3                                  76 6  
            / \            / \                                   / \    
            4    5          4   6     il risultato e'            36  37   
        /    /          /   /                                 /   /    
        6    7          5   2                                 28 26     
        /     \         /    \                                /    \     
        8      9       9      8                              17    17    
        

        '''
        lista1 = [1, [2, [4, [6, [8, None, None], None], None], [5, [7, None, [9, None, None]], None]], [3, None, None]]
        lista2 = [7, [1, [4, [5, [9, None, None], None], None], [6, [2, None, [8, None, None]], None]], [3, None, None]]
        lista3 = [90, [76, [36, [28, [17, None, None], None], None], [37, [26, None, [17, None, None]], None]], [6, None, None]]
        return self.do_test(lista1, lista2, lista3)

if __name__ == "__main__":
    Test.main()

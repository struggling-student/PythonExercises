
# Esempio di test

# IMPORT NECESSARI
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive
import albero

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, x, expected):
        '''Implementazione del test
            - lista         : lista dei nodi dell'albero binario
            - x             : numero intero 
            - expected      : numero di nodi con valore divisibile per x
        '''
        tree = albero.AlberoBinario.fromList(lista)
        try:
            isrecursive.decorate_module(program)
            program.es14(tree, x)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        tree = albero.AlberoBinario.fromList(lista)
        # poi controlliamo che faccia quello che deve fare
        # - ignoraando la presenza di stampe
        # - proibendo l'uso della funzione os.walk
        # - con un timeout di 2 secondi
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es14(tree, x)
        self.assertEqual(type(result), int, "Il risultato non è un intero")
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(  
            ([7, [1, [4, [5, [9, None, None], None], None], [6, [2, None, [8, None, None]], None]], [3, None, None]], 2, 3),
            ([9, [2, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]], [4, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]]], 1, 7),
            ([5,None,[2,[5,None,[1,[5,None,None],None]],None]], 1, 3)
        )
    @unpack
    def test(self, lista, x, expected):
        return self.do_test(lista, x, expected)

# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()

